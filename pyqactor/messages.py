import re


class Message(object):
    def __init__(self, _type, _from, to, payload):
        self._type = _type
        self._from = _from
        self._to = to
        self.payload = payload

    def __str__(self):
        return "msg({0},{1},{2},{3})".format(self._type, self._from, self._to, self.payload)


def parse_message(msg):
    terms = re.search('msg\((.*)\)').group(1)
    terms = terms.split(',')
    return Message(terms[0], terms[1], terms[2], terms[3])
