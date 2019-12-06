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

    def add_emitter(self, msg_id, stream, hertz=10):
        self.emitters[msg_id] = Emitter(msg_id, stream, hertz, self)

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
