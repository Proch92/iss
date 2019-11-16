from fsmactor import FSMactor
import pyqak
import asyncio


class Context(object):
    def __init__(self):
        self.actors = {}

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
        return newactor

    def send_message(self, msg):
        self.actors[msg._to].send_message(msg)
