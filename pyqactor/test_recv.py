import pyqak
from pyqak import *
from transitions import *
from context import Context, ExternalContext

ctx = Context('ctx-robot', 'localhost', 8019)
ctx.actor_scope('robot')


@initial
@state
async def init(self, t):
    print('robot | init')
    await self.transition('work', Epsilon)


@state
async def work(self, t):
    print('robot | work')
    await self.transition('handle', WhenMsg, 'cmd')


@state
async def handle(self, t):
    print('robot | handle_response')
    print(t.msg)
    await self.transition('work', Epsilon)


pyqak.run()
