from transitions import *
from messages import *
from asyncactor import Actor


class FSMactor(Actor):
    def __init__(self, name):
        super().__init__()
        self.name = name
        self.states = {}
        self.transitions = {}
        self.current_state = None

    def add_state(self, foo):
        self.states[foo.__name__] = foo

    def set_initial(self, foo):
        self.current_state = foo.__name__

    def goto(self, state_to):
        self.current_state = state_to
        self.execute_current_state()

    def execute_current_state(self):
        self.states[self.current_state]()

    def add_transition(self, s_from, s_to, trans_type):
        if trans_type is Epsilon:
            def goto_wrapper(func):
                def wrapper():
                    func()
                    self.goto(s_to)
                return wrapper

            self.states[s_from] = goto_wrapper(self.states[s_from])
        else:
            if s_from in self.transitions:
                self.transitions[s_from].append({'state_to': s_to, 'trans_type': trans_type})

    def on_start(self):
        print('on_start')
        self.execute_current_state()

    def on_receive(self, message):
        trans = self.transitions[self.current_state]
        for t in trans:
            if t['trans_type'] is WhenMsg:
                if isinstance(message, Message):
                    self.goto(t['state_to'])
                    break
