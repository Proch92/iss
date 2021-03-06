from fsmactor import FSMactor
import pyqak
import asyncio
import messages
from emitter import Emitter


class Context(object):
    def __init__(self, name, host, port):
        self.name = name
        self.host = host
        self.port = port
        self.actors = {}
        self.emitters = {}
        pyqak.add_context(self)

    async def init(self):
        self.server = await asyncio.start_server(self.handle_conn, self.host, self.port)
        await self.server.start_serving()

    async def handle_conn(self, reader, writer):
        while True:
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
        for _, actor in self.actors.items():
            tasks.append(actor.start())

        for _, emitter in self.emitters.items():
            tasks.append(emitter.start())

        await asyncio.wait(tasks)

    def actor_scope(self, name):
        newactor = FSMactor(name, self)
        self.actors[name] = newactor
        pyqak.current_actor_scope = newactor

    def emitter(self, msg_id, stream, hertz=10, from_name='None'):
        if from_name is None:
            from_name = msg_id
        self.emitters[msg_id] = Emitter(msg_id, stream, hertz, self, from_name)

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
        pass

    async def run(self):
        while(True):
            try:
                print(f"trying to connect to external context {self.name}")
                self.reader, self.writer = await asyncio.open_connection(self.host, self.port)

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
            except Exception as e:
                print(f"connection attempt failed to {self.name}. retrying in 1 second...")

            await asyncio.sleep(1)

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
        try:
            self.writer.write(encoded)
            await self.writer.drain()
        except Exception as e:
            print("tcp send failed. broken writer")
