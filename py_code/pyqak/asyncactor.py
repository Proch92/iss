import asyncio


class Actor(object):
    def __init__(self):
        self.alive = False

    async def init(self):
        self.queue = asyncio.Queue()

    async def start(self):
        self.alive = True
        await self.on_start()
        while self.alive:
            message = await self.queue.get()
            await self.on_receive(message)

    async def send_message(self, message):
        self.queue.put_nowait(message)

    def die(self):
        self.alive = False

    async def on_start(self):
        pass

    async def on_receive(self, message):
        pass
