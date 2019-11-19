class Transition(object):
    def __init__(self):
        pass


class Epsilon(Transition):
    def __init__(self):
        pass


class WhenMsg(Transition):
    accepted_messages = ['dispatch', 'request']

    def __init__(self):
        pass


class WhenReply(Transition):
    accepted_messages = ['reply']

    def __init__(self):
        pass


class WhenEvent(Transition):
    accepted_messages = ['event']

    def __init__(self):
        pass
