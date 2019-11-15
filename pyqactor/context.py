from fsmactor import FSMactor
import asyncio


async def start_actors(actors):
    tasks = [asyncio.create_task(actor.start()) for name, actor in actors.items()]
    await asyncio.wait(tasks)


class Context(object):
    def __init__(self):
        self.actors = {}

    def run(self):
        print('STARTING')
        asyncio.run(start_actors(self.actors))

    def add_actor(self, name):
        newactor = FSMactor(name)
        self.actors[name] = newactor
        return newactor
