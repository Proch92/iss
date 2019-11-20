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
def init(self, t):
    print('robot | init')
    self.transition('work', Epsilon)


@state
def work(self, t):
    print('robot | work')
    print('w')  # fire motors
    self.transition('halt', WhenEvent, 'sonar', lambda s: int(s) < 10)
    self.transition('toradar', WhenEvent, 'sonar', lambda s: int(s) >= 10)


@state
def halt(self, t):
    print('robot | halt')
    print('h')  # stop motors


@state
def toradar(self, t):
    print('robot | toradar')
    self.request('radar', 'sonar_val_req', t['msg'].payload)
    self.transition('halt', WhenEvent, 'sonar', lambda s: int(s) < 10)
    self.transition('handle_response', WhenReply, 'sonar_val_req')


@state
def handle_response(self, t):
    print('robot | handle_response')
    self.transition('work', Epsilon)


ctx.actor_scope('sonar')


@initial
@state
def run(self, t):
    self.emit('sonar', 20)
    self.emit('sonar', 20)
    self.emit('sonar', 20)
    self.emit('sonar', 10)


pyqak.run(ctx)
