import pyqak
from pyqak import *
from transitions import *
from context import Context, ExternalContext

ctx_radar = ExternalContext('localhost', 8020)
ctx_radar.external_actor('radar')

ctx = Context('localhost', 8030)
ctx.actor_scope('robot')


@initial
@state
async def init(self, t):
    print('robot | init')
    await self.transition('work', Epsilon)


@state
async def work(self, t):
    print('robot | work')
    print('w')  # fire motors
    await self.transition('halt', WhenEvent, 'sonar', lambda s: int(s) < 10)
    await self.transition('toradar', WhenEvent, 'sonar', lambda s: int(s) >= 10)


@state
async def halt(self, t):
    print('robot | halt')
    print('h')  # stop motors


@state
async def toradar(self, t):
    print('robot | toradar')
    # await self.dispatch('radar', 'polar', t['msg'].payload)
    await self.request('radar', 'polar', t['msg'].payload)
    await self.transition('halt', WhenEvent, 'sonar', lambda s: int(s) < 10)
    await self.transition('handle_response', WhenReply, 'polarReply')
    # await self.transition('work', Epsilon)


@state
async def handle_response(self, t):
    print('robot | handle_response')
    await self.transition('work', Epsilon)


ctx.actor_scope('sonar')


@initial
@state
async def run(self, t):
    await self.emit('sonar', 20)
    await self.sleep(2)
    await self.emit('sonar', 40)
    await self.sleep(2)
    await self.emit('sonar', 60)
    await self.sleep(2)
    await self.emit('sonar', 5)


pyqak.run()
