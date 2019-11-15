from pyqak import initial, state, actor_scope, transition
from transitions import Epsilon
from context import Context


ctx = Context()
actor_scope('actor0', ctx)


@initial
@state
def s0():
    print('actor0 | s0')


transition('s0', 's1', Epsilon)


@state
def s1():
    print('actor0 | s1')


ctx.run()
