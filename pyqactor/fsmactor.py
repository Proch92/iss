from transitions import *
from messages import *
from asyncactor import Actor


class FSMactor(Actor):
    def __init__(self, name, context):
        super().__init__()
        self.name = name
        self.context = context
        self.states = {}
        self.transitions = []
        self.current_state = None

    def __str__(self):
        return self.name

    def add_state(self, foo):
        self.states[foo.__name__] = foo

    def set_initial(self, foo):
        self.current_state = foo.__name__

    def goto(self, state_to):
        self.current_state = state_to
        self.execute_current_state()

    def execute_current_state(self):
        self.states[self.current_state](self)

    def dispatch(self, to, payload):
        msg = Message('dispatch', self.name, to, payload)
        self.context.send_message(msg)

    def transition(self, to, event):
        if event is Epsilon:
            self.goto(to)
        else:
            self.transitions.append((to, event))

    def on_start(self):
        self.execute_current_state()

    def on_receive(self, message):
        next_state = None
        for to, trans in self.transitions:
            if trans is WhenMsg:
                if message._type in ['dispatch', 'request']:
                    next_state = to
                    break
            elif trans is WhenEvent:
                if message._type == 'event':
                    next_state = to
                    break

        if next_state:
            self.transitions = []
            self.goto(next_state)
