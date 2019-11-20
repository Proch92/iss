from fsmactor import FSMactor
import pyqak
import asyncio
import messages
import socket


class Context(object):
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.actors = {}
        pyqak.add_context(self)

    async def run(self):
        print('STARTING')

        for _, actor in self.actors.items():
            await actor.init()

        tasks = []
        for name, actor in self.actors.items():
            tasks.append(asyncio.create_task(actor.start()))

        await asyncio.wait(tasks)

    def actor_scope(self, name):
        newactor = FSMactor(name, self)
        self.actors[name] = newactor
        pyqak.current_actor_scope = newactor

    def send_message(self, msg):
        if msg._to in self.actors:
            self.actors[msg._to].send_message(msg)
        else:
            for ctx in pyqak.contexts:
                if msg._to in ctx.actors:
                    ctx.send_message(msg)

    def emit(self, msg):
        [ctx.send_event(msg) for ctx in pyqak.contexts]

    def send_event(self, msg):
        [actor.send_message(msg) for _, actor in self.actors.items()]


class ExternalContext(Context):
    def __init__(self, host, port):
        super().__init__(host, port)
        self.actors = []
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect((self.host, self.port))

    async def run(self):
        print('cannot run an external context')

    def actor_scope(self, name):
        print('cannot open an actor scope for an external context')

    def external_actor(self, name):
        self.actors.append(name)

    def send_message(self, msg):
        encoded = messages.natali_encode(msg)
        encoded = str(encoded) + '\n'
        encoded = encoded.encode()
        self.sock.send(encoded)

    def send_event(self, msg):
        encoded = messages.natali_encode(msg)
        encoded = str(encoded) + '\n'
        encoded = encoded.encode()
        self.sock.send(encoded)
