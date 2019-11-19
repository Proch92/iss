import re
from copy import deepcopy


class Message(object):
    def __init__(self, _id, _type, _from, to, payload):
        self._id = _id
        self._type = _type
        self._from = _from
        self._to = to
        self.payload = payload
        self.msg_num = 1

    def __str__(self):
        return "msg({0},{1},{2},{3},{4},{5})".format(self._id, self._type, self._from, self._to, self.payload, self.msg_num)


def parse_message(msg):
    terms = re.search('msg\((.*)\)').group(1)
    terms = terms.split(',')
    return Message(terms[0], terms[1], terms[2], terms[3], terms[4], terms[5])


def natali_encode(msg):
    nat = deepcopy(msg)
    nat.payload = nat._id + '(' + str(nat.payload) + ')'
    return nat
