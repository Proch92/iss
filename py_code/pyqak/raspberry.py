import pyqak
from pyqak import *
from transitions import *
from context import Context, ExternalContext
import motors
import sonar

ctx = Context('ctx-raspberry', '192.168.43.229', 8030)
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


ctx.actor_scope('sonar')


@initial
@state
async def init(self, t):
    print('robot | init')
    self.sonar = motors.Sonar(1,2,3)
    await self.transition('work', Epsilon)


@state
async def work(self, t):
    print('robot | work')
    distance = await self.sonar.read()
    await self.emit(distance)
    await self.transition('work', Espilon)


pyqak.run()
