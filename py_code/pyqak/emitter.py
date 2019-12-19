from messages import Message
import asyncio


class Emitter():
    def __init__(self, msg_id, stream, hz, context, from_name):
        self.msg_id = msg_id
        self.stream = stream
        self.hz = hz
        self.context = context
        self.from_name = from_name

    async def start(self):
        for val in self.stream:
            msg = Message(self.msg_id, 'event', self.from_name, 'nan', val)
            await self.context.emit(msg)
            await asyncio.sleep(1 / self.hz)
