import asyncio


class Actor(object):
    def __init__(self):
        self.queue = asyncio.Queue()

    async def start(self):
        self.on_start()
        while True:
            message = await self.queue.get()
            self.on_receive(message)

    def send_message(self, message):
        self.queue.put_nowait(message)

    def on_start(self):
        pass

    def on_receive(self, message):
        pass
