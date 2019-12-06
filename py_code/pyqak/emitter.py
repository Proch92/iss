from messages import Message
import asyncio


class Emitter():
    def __init__(self, msg_id, stream, hz, context):
        self.msg_id = msg_id
        self.stream = stream
        self.hz = hz
        self.context = context

    async def start(self):
        for val in self.stream:
            msg = Message(self.msg_id, 'event', self.msg_id, 'nan', val)
            await self.context.emit(msg)
            await asyncio.sleep(1 / self.hz)
