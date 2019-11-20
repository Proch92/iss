import pyqak
from pyqak import *
from transitions import *
from context import Context


ctx = Context()
ctx.actor_scope('actor0')


@initial
@state
def s0(self):
    print('actor0 | s0')
    self.dispatch('actor1', 'saluto', 'ciao')
    self.transition('s1', WhenMsg, 'saluto')


@state
def s1(self):
    print('actor0 | s1')


ctx.actor_scope('actor1')


@initial
@state
def s01(self):
    print('actor1 | s0')
    self.dispatch('actor0', 'saluto', 'ciao')
    self.transition('s11', WhenMsg)


@state
def s11(self):
    print('actor1 | s1')


pyqak.run(ctx)
