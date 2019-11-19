from transitions import *
from messages import *
from asyncactor import Actor
import utils


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

    def goto(self, state_to, transition=None):
        self.current_state = state_to
        self.execute_current_state(transition)

    def execute_current_state(self, transition=None):
        self.states[self.current_state](self, transition)

    def dispatch(self, to, _id, payload):
        msg = Message(_id, 'dispatch', self.name, to, payload)
        self.context.send_message(msg)

    def request(self, to, _id, payload):
        msg = Message(_id, 'request', self.name, to, payload)
        self.context.send_message(msg)

    def emit(self, _id, payload):
        msg = Message(_id, 'event', self.name, 'nan', payload)
        self.context.emit(msg)

    def transition(self, to, event, msg_id=None, guard=utils.true):
        if event is Epsilon:
            self.goto(to)
        else:
            self.transitions.append((to, event, msg_id, guard))

    def on_start(self):
        self.execute_current_state()

    def on_receive(self, message):
        next_state = None
        for to, event, msg_id, guard in self.transitions:
            if message._type in event.accepted_messages:
                if msg_id:
                    if message._id == msg_id:
                        if guard(message.payload):
                            next_state = to
                            break
                else:
                    next_state = to
                    break

        if next_state:
            self.transitions = []
            self.goto(next_state, {'msg': message, 'type': event, 'msg_id': msg_id})
