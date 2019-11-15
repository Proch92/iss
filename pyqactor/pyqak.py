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


def transition(state_from, state_to, event):
    global current_actor_scope
    current_actor_scope.add_transition(state_from, state_to, event)


def actor_scope(actor_name, ctx):
    global current_actor_scope
    actor = ctx.add_actor(actor_name)
    current_actor_scope = actor
