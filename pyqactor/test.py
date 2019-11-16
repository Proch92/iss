import pyqak
from pyqak import *
from transitions import *
from context import Context


ctx = Context()
act0 = ctx.actor_scope('actor0')


@initial
@state
def s0(self):
    print('actor0 | s0')
    self.dispatch('actor1', 'ciao')
    self.transition('s1', WhenMsg)


@state
def s1(self):
    print('actor0 | s1')


act1 = ctx.actor_scope('actor1')


@initial
@state
def s01(self):
    print('actor1 | s0')
    self.dispatch('actor0', 'ciao')
    self.transition('s11', WhenMsg)


@state
def s11(self):
    print('actor1 | s1')


pyqak.run(ctx)
