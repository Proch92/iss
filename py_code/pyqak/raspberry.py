import pyqak
from pyqak import *
from transitions import *
from context import Context
import motors
import sensors
from generator_utils import drop_outliers, avg_window

ctx = Context('ctx-raspberry', '192.168.1.2', 8030)

sonar = sensors.Sensor(17, 27)
ctx.emitter('sonar', avg_window(drop_outliers(sonar.read())))


ctx.actor_scope('robot')


@initial
@state
async def init(self, t):
    print('robot | init')
    self.motorsx = motors.Motor(6, 13, 5)
    self.motordx = motors.Motor(19, 26, 20)
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
        self.motorsx.backward()
        self.motordx.forward()
    elif cmd == 'd':
        self.motorsx.forward()
        self.motordx.backward()
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
