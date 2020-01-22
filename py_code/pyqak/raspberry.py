import pyqak
from pyqak import *
from transitions import *
from context import Context, ExternalContext
import motors
import sensors
from generator_utils import clip, avg_window, discard_malformed
import numpy as np

OBSTACLE_THRESHOLD = 5.5

ctx = Context('ctx-raspberry', '192.168.1.119', 8030)
ctx_mind = ExternalContext('ctx-mind', '192.168.1.7', 8020)

sonar = sensors.Sonar(17, 27)
ctx.emitter('sonar', avg_window(clip(discard_malformed(sonar.stream()))), hertz=10, from_name='sonar')


ctx.actor_scope('robot')


@initial
@state
async def init(self, t):
    print('robot | init')
    self.motordx = motors.Motor(13, 6, 5, default_power=70)
    self.motorsx = motors.Motor(26, 19, 20, default_power=70)
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
        self.motorsx.forward(power=55)
        self.motordx.forward(power=65)
    elif cmd == 's':
        self.motorsx.backward(power=55)
        self.motordx.backward(power=65)
    elif cmd == 'a':
        steps = 10
        max_pow_sx = 60
        max_pow_dx = 70
        for r in np.linspace(0.0, 1.0, num=steps):
            self.motorsx.backward(power=max_pow_sx * r)
            self.motordx.forward(power=max_pow_dx * r)
            await self.sleep(0.2 / steps)
        await self.sleep(0.2)
        for r in np.linspace(1.0, 0.0, num=steps):
            self.motorsx.backward(power=max_pow_sx * r)
            self.motordx.forward(power=max_pow_dx * r)
            await self.sleep(0.2 / steps)
        self.motorsx.stop()
        self.motordx.stop()
    elif cmd == 'd':
        steps = 10
        max_pow_sx = 60
        max_pow_dx = 50
        for r in np.linspace(0.0, 1.0, num=steps):
            self.motorsx.forward(power=max_pow_sx * r)
            self.motordx.backward(power=max_pow_dx * r)
            await self.sleep(0.2 / steps)
        await self.sleep(0.2)
        for r in np.linspace(1.0, 0.0, num=steps):
            self.motorsx.forward(power=max_pow_sx * r)
            self.motordx.backward(power=max_pow_dx * r)
            await self.sleep(0.2 / steps)
        self.motorsx.stop()
        self.motordx.stop()
    elif cmd == 'h':
        self.motorsx.stop()
        self.motordx.stop()
    await self.transition('work', Epsilon)


@state
async def handle_sonar(self, t):
    print('robot | handle_sonar')
    sonar_value = t['msg'].payload
    print(sonar_value)
    if sonar_value < OBSTACLE_THRESHOLD:
        print(f'robot | emit | obstacle {sonar_value}')
        await self.emit('obstacle', sonar_value)
    await self.transition('work', Epsilon)


pyqak.run()
