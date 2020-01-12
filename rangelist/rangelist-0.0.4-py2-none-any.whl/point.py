from __future__ import absolute_import, unicode_literals
import sys


class Point(object):
    def __init__(self, value):
        if sys.version_info >= (3, 0):
            if isinstance(value, str):
                assert value in ['inf', '-inf']
        else:
            if isinstance(value, (str, unicode)):  # noqa
                assert value in ['inf', '-inf']
        self._value = value

    @property
    def value(self):
        return self._value

    def __eq__(self, other):
        if not isinstance(other, Point):
            other = Point(other)
        return self.value == other.value

    def __ne__(self, other):
        return not self == other

    def __lt__(self, other):
        if not isinstance(other, Point):
            other = Point(other)
        if other.value == '-inf':
            return False
        if other.value == 'inf':
            if self.value == 'inf':
                return False
            return True
        if self.value == 'inf':
            return False
        if self.value == '-inf':
            return True
        return self.value < other.value

    def __gt__(self, other):
        if not isinstance(other, Point):
            other = Point(other)
        if other.value == 'inf':
            return False
        if other.value == '-inf':
            if self.value == '-inf':
                return False
            return True
        if self.value == '-inf':
            return False
        if self.value == 'inf':
            return True
        return self.value > other.value

    def __le__(self, other):
        return self == other or self < other

    def __ge__(self, other):
        return self == other or self > other

    def __str__(self):
        return str(self.value)

    def __repr__(self):
        return self.__str__()


INF = Point('inf')
NEG_INF = Point('-inf')
