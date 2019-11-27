import asyncio


current_actor_scope = None
contexts = []


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

def run():
    asyncio.run(fire_contexts())


async def fire_contexts():
    tasks = []
    for context in contexts:
        tasks.append(context.init())
    await asyncio.wait(tasks)

    tasks = []
    for context in contexts:
        tasks.append(context.run())
    await asyncio.wait(tasks)


def add_context(ctx):
    contexts.append(ctx)
