import copy


class Point:
    """A point in space.

    :param float x: the x-coordinate of the point
    :param float y: the y-coordinate of the point
    """
    def __init__(self,
                 x: float,
                 y: float):
        self.x = x
        self.y = y

    def dist(self, to):
        """Return the distance to another Point.

        :param to: the other point, given as a Point instance or an iterable of
        two coordinates
        """
        return (sum((x1 - x2)**2 for x1, x2 in zip(self, to)))**(1/2)

    def __iadd__(self, other):
        if isinstance(other, Point):
            self.x += other.x
            self.y += other.y
        elif isinstance(other, tuple):
            self.x += other[0]
            self.y += other[1]
        else:
            self.x += other
            self.y += other
        return self

    def __isub__(self, other):
        if isinstance(other, Point):
            self.x -= other.x
            self.y -= other.y
        elif isinstance(other, tuple):
            self.x -= other[0]
            self.y -= other[1]
        else:
            self.x -= other
            self.y -= other
        return self

    def __imul__(self, other):
        if isinstance(other, tuple):
            self.x *= other[0]
            self.y *= other[1]
        elif isinstance(other, Point):
            self.x *= other.x
            self.y *= other.y
        else:
            self.x *= other
            self.y *= other
        return self

    def __itruediv__(self, other):
        if isinstance(other, tuple):
            self.x /= other[0]
            self.y /= other[1]
        elif isinstance(other, Point):
            self.x /= other.x
            self.y /= other.y
        else:
            self.x /= other
            self.y /= other
        return self

    def __add__(self, other):
        cp = copy.deepcopy(self)
        cp += other
        return cp

    def __sub__(self, other):
        cp = copy.deepcopy(self)
        cp -= other
        return cp

    def __mul__(self, other):
        cp = copy.deepcopy(self)
        cp *= other
        return cp

    def __truediv__(self, other):
        cp = copy.deepcopy(self)
        cp /= other
        return cp

    def __eq__(self, other):
        if not isinstance(other, Point):
            return False
        else:
            return (self.x == other.x
                    and self.y == other.y)

    def __iter__(self):
        return iter([self.x, self.y])

    def __repr__(self):
        return f'{self.x, self.y}'
