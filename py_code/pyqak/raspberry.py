import pyqak
from pyqak import *
from transitions import *
from context import Context
import motors
import sensors
from generator_utils import clip, avg_window, discard_malformed

ctx = Context('ctx-raspberry', '192.168.1.7', 8030)

sonar = sensors.Sonar(17, 27)
ctx.emitter('sonar', avg_window(clip(discard_malformed(sonar.stream()))))


ctx.actor_scope('robot')


@initial
@state
async def init(self, t):
    print('robot | init')
    self.motordx = motors.Motor(13, 6, 5, default_power=50)
    self.motorsx = motors.Motor(26, 19, 20, default_power=50)
    await self.transition('work', Epsilon)


@state
async def work(self, t):
    print('robot | work')
    await self.transition('handle_cmd', WhenMsg, 'cmd')
    await self.transition('handle_sonar', WhenEvent, 'sonar')


@state
async def handle_cmd(self, t):
    print('robot | handle_cmd')
    cmd = t['msg'].payload[0]
    print(f'received command {cmd}')
    if cmd == 'w':
        self.motorsx.forward()
        self.motordx.forward()
    elif cmd == 's':
        self.motorsx.backward()
        self.motordx.backward()
    elif cmd == 'a':
        self.motorsx.backward(power=38)
        self.motordx.forward(power=52)
        await self.sleep(0.47)
        self.motorsx.stop()
        self.motordx.stop()
    elif cmd == 'd':
        self.motorsx.forward(power=52)
        self.motordx.backward(power=38)
        await self.sleep(0.47)
        self.motorsx.stop()
        self.motordx.stop()
    elif cmd == 'h':
        self.motorsx.stop()
        self.motordx.stop()
    await self.transition('work', Epsilon)


@state
async def handle_sonar(self, t):
    print('robot | handle_sonar')
    print(t['msg'])
    await self.transition('work', Epsilon)


pyqak.run()
