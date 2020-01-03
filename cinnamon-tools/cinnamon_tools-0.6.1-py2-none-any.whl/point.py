from enum import Enum
from functools import total_ordering
from numbers import Number


@total_ordering
class Point:
    def __init__(self, *args):
        ints = list(map(lambda v: isinstance(v, Number), args))
        if not all(ints):
            raise TypeError("{} is not an integer".format(args[ints.index(False)]))
        self.values = args

    def distance_to(self, other):
        return sum([abs(a - b) for a, b in zip(self.values, other.values)])

    def zero_distance(self):
        return self.distance_to(self.zero_point())

    def __repr__(self):
        return "Point{}".format(str(self))

    def __str__(self):
        return "({})".format(",".join(map(str, self.values)))

    def __add__(self, other):
        return Point(*[a + b for a, b in zip(self.values, other.values)])

    def __sub__(self, other):
        return Point(*[a - b for a, b in zip(self.values, other.values)])

    def __mul__(self, other):
        return Point(*map(lambda x: x * other, self))

    def __rmul__(self, other):
        return self.__mul__(other)

    def __eq__(self, other):
        return all(a == b for a, b in zip(self.values, other.values))

    def __hash__(self):
        return hash(repr(self))

    def __iter__(self):
        yield from self.values

    def __bool__(self):
        return True

    def __lt__(self, other):
        # return self < other
        return all(a < b for a, b in zip(self.values, other.values))

    def __len__(self):
        return len(self.values)

    def __getitem__(self, item):
        return self.values[item]

    def zero_point(self):
        return zero_point(len(self))

    @property
    def adjacent(self):
        return [
            self + p for p in [Point(-1, 0), Point(1, 0), Point(0, -1), Point(0, 1)]
        ]

    @property
    def x(self):
        return self.values[0]

    @property
    def y(self):
        return self.values[1]

    @property
    def z(self):
        return self.values[2]


def zero_point(order):
    return Point(*([0] * order))


class WrappedEnum(Enum):
    def next(self):
        cls = self.__class__
        members = list(cls)
        index = (members.index(self) + 1) % len(members)

        return members[index]

    def prev(self):
        cls = self.__class__
        members = list(cls)
        index = (members.index(self) - 1) % len(members)
        return members[index]


class Direction(WrappedEnum):
    UP = Point(0, 1)
    RIGHT = Point(1, 0)
    DOWN = Point(0, -1)
    LEFT = Point(-1, 0)


class FileDirection(WrappedEnum):
    UP = Point(-1, 0)
    RIGHT = Point(0, 1)
    DOWN = Point(1, 0)
    LEFT = Point(0, -1)
