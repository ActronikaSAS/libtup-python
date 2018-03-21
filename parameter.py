import numpy


class Parameter(object):
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
            if id >= numpy.iinfo(numpy.uint8).min and \
               id <= numpy.iinfo(numpy.uint8).max:
                self._id = id

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        if isinstance(value, int):
            if value >= numpy.iinfo(numpy.uint32).min and \
               value <= numpy.iinfo(numpy.uint32).max:
                self._value = value
