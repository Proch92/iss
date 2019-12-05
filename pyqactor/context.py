from fsmactor import FSMactor
import pyqak
import asyncio
import messages
import paho.mqtt.client as mqtt


class Context(object):
    def __init__(self, name, host, port, mqtt=None, mqtt_port=1883):
        self.mqtt = mqtt
        self.mqtt_port = mqtt_port
        self.name = name
        self.host = host
        self.port = port
        self.actors = {}
        pyqak.add_context(self)

    def on_mqtt_connect(self, client, userdata, flags, rc):
        print(f"Connected with result code {rc}")
        client.subscribe("unibo/qak/events")
        for actor in self.actors:
            client.subscribe(f"unibo/qak/{actor}")

    def on_mqtt_message(self, client, userdata, msg):
        msg = messages.parse_message(msg.payload)
        for ctx in pyqak.contexts:
            if msg._to in ctx.actors:
                await ctx.send_message(msg)

    async def init(self):
        self.server = await asyncio.start_server(self.handle_conn, self.host, self.port)
        await self.server.start_serving()
        if self.mqtt:
            client = mqtt.Client()
            client.on_connect = self.on_mqtt_connect
            client.on_message = self.on_mqtt_message
            client.connect(self.mqtt, self.mqtt_port, 60)

    async def handle_conn(self, reader, writer):
        data = await reader.readline()
        data = data.decode()
        msg = messages.parse_message(data)
        if msg:
            if msg._type == 'event':
                await self.send_event(msg)
            elif msg._type in ['dispatch', 'request', 'reply']:
                await self.send_message(msg)

    async def run(self):
        for _, actor in self.actors.items():
            await actor.init()

        tasks = []
        for name, actor in self.actors.items():
            tasks.append(actor.start())

        await asyncio.wait(tasks)

    def actor_scope(self, name):
        newactor = FSMactor(name, self)
        self.actors[name] = newactor
        pyqak.current_actor_scope = newactor

    async def send_message(self, msg):
        if msg._to in self.actors:
            await self.actors[msg._to].send_message(msg)
        else:
            for ctx in pyqak.contexts:
                if msg._to in ctx.actors:
                    await ctx.send_message(msg)

    async def emit(self, msg):
        [await ctx.send_event(msg) for ctx in pyqak.contexts]

    async def send_event(self, msg):
        [await actor.send_message(msg) for _, actor in self.actors.items()]


class ExternalContext(Context):
    def __init__(self, name, host, port):
        super().__init__(name, host, port)
        self.actors = []

    async def init(self):
        self.reader, self.writer = await asyncio.open_connection(self.host, self.port)

    async def run(self):
        while(True):
            data = await self.reader.readline()
            data = data.decode()
            msg = messages.parse_message(data)
            if msg:
                print('received ', str(msg))
                if msg._type == 'reply':
                    for ctx in pyqak.contexts:
                        if msg._to in ctx.actors:
                            await ctx.send_message(msg)

        self.writer.close()
        await self.writer.wait_closed()

    def actor_scope(self, name):
        print('cannot open an actor scope for an external context')

    def external_actor(self, name):
        self.actors.append(name)

    async def send_message(self, msg):
        await self.tcp_send(msg)

    async def send_event(self, msg):
        await self.tcp_send(msg)

    async def tcp_send(self, msg):
        encoded = messages.natali_encode(msg)
        encoded = str(encoded) + '\n'
        encoded = encoded.encode()
        self.writer.write(encoded)
        await self.writer.drain()
