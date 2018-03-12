INT32_MAX = 2**31 - 1
INT32_MIN = -1 * 2**31


class Input(object):
    def __init__(self, id=0, value=0):
        self.id = id
        self.value = value

    def __str__(self):
        return "<id: {}, value: {}>".format(self._id, self._value)

    def __eq__(self, other):
        return self._id == other._id and self._value == other._value

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, id):
        if isinstance(id, int):
            if 0 <= id <= 255:
                self._id = id

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        if isinstance(value, int):
            if INT32_MIN <= value <= INT32_MAX:
                self._value = value
