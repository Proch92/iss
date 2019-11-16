import asyncio


current_actor_scope = None


# DECORATORS

def initial(state_func):
    global current_actor_scope
    current_actor_scope.set_initial(state_func)
    return state_func


def state(foo):
    global current_actor_scope
    current_actor_scope.add_state(foo)
    return foo


# FUNCTIONS

def run(context):
    asyncio.run(context.run())
