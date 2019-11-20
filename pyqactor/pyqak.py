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
	asyncio.run(asyncrun())


async def asyncrun():
	tasks = []
	for context in contexts:
		tasks.append(asyncio.create_task(context.run()))

	await asyncio.wait(tasks)


def add_context(ctx):
    contexts.append(ctx)
