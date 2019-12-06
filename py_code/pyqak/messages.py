import re
from copy import deepcopy


class Message(object):
    def __init__(self, _id, _type, _from, to, payload, msg_num=1):
        self._id = _id
        self._type = _type
        self._from = _from
        self._to = to
        self.payload = payload
        self.msg_num = msg_num

    def __str__(self):
        return "msg({0},{1},{2},{3},{4},{5})".format(self._id, self._type, self._from, self._to, self.payload, self.msg_num)


def parse_message(msg):
    terms = re.search('msg\((.*)\)', msg)
    if terms:
        terms = terms.group(1).split(',')
        if len(terms) == 6:
            terms[4] = natali_decode(terms[0], terms[4])
            return Message(terms[0], terms[1], terms[2], terms[3], terms[4], terms[5])
    print('messages.parse_message() | bad message | ', msg)
    return None


def natali_encode(msg):
    nat = deepcopy(msg)
    nat.payload = nat._id + '(' + str(nat.payload) + ')'
    return nat


# cmd(X) ---> [X]
def natali_decode(msgid, payload):
    terms = re.search(msgid + '\((.*)\)', payload)
    if terms:
        terms = terms.group(1).split(',')
        if len(terms) > 0:
            return terms
    return []
