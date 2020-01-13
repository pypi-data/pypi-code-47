import copy
from .box import Box
from .point import Point
from typing import Tuple, Union
from .warnings import warn_reduced_dim_after_setting_attr


class Shape:
    """A general representation of a geometric shape.

    The Shape is represented by a list of Point objects. The Shape object is
    iterable where an iterator will simply iterate through the points.
    """
    def __init__(self, points):
        """Initialize a Shape object.

        :param list points: a list of Point objects representing
        the geometric shape. The order of the points is of importance
        as it represents in which order lines should be drawn to create
        an enclosed shape.
        """
        self.points = points

    @property
    def envelope(self):
        """Get a Box that envelopes a list of Points."""
        min_x_point = min(map(lambda p: p.x, self.points))
        max_x_point = max(map(lambda p: p.x, self.points))
        min_y_point = min(map(lambda p: p.y, self.points))
        max_y_point = max(map(lambda p: p.y, self.points))
        return Box(min_x_point, min_y_point, max_x_point, max_y_point)

    def scale_with_origin(self, scale: Union[float, Tuple[float]],
                          origin: Point):
        """Scale the shape using the given origin.

        :param Union[float, Tuple[float]] scale: the x- and y-scale to use.
        When given as a single float, use this as a uniform scale factor.
        :param Point origin: the origin or anchor point of the scaling
        operation. This point will stay fixed.
        """
        if not isinstance(scale, tuple):
            scale = (scale, scale)

        self.points = [(p - origin)*scale + origin for p in self.points]

    @property
    def x_min(self):
        return min(p.x for p in self.points)

    @x_min.setter
    def x_min(self, value):
        if value == self.x_max:
            warn_reduced_dim_after_setting_attr()
        old_width = self.width
        if old_width == 0:
            self.points = [Point(value, p.y) for p in self.points]
            return

        new_width = self.x_max - value

        origin = Point(x=self.x_max, y=0)
        scale = (new_width/old_width, 1)
        self.scale_with_origin(scale, origin)

    @property
    def y_min(self):
        return min(p.y for p in self.points)

    @y_min.setter
    def y_min(self, value):
        if value == self.y_max:
            warn_reduced_dim_after_setting_attr()
        old_height = self.height
        if old_height == 0:
            self.points = [Point(p.x, value) for p in self.points]
            return

        new_height = self.y_max - value

        origin = Point(x=0, y=self.y_max)
        scale = (1, new_height/old_height)
        self.scale_with_origin(scale, origin)

    @property
    def x_max(self):
        return max(p.x for p in self.points)

    @x_max.setter
    def x_max(self, value):
        if value == self.x_min:
            warn_reduced_dim_after_setting_attr()
        old_width = self.width
        if old_width == 0:
            self.points = [Point(value, p.y) for p in self.points]
            return

        new_width = value - self.x_min

        origin = Point(x=self.x_min, y=0)
        scale = (new_width/old_width, 1)
        self.scale_with_origin(scale, origin)

    @property
    def y_max(self):
        return max(p.y for p in self.points)

    @y_max.setter
    def y_max(self, value):
        if value == self.y_min:
            warn_reduced_dim_after_setting_attr()
        old_height = self.height
        if old_height == 0:
            self.points = [Point(p.x, value) for p in self.points]
            return

        new_height = value - self.y_min

        origin = Point(x=0, y=self.y_min)
        scale = (1, new_height/old_height)
        self.scale_with_origin(scale, origin)

    @property
    def width(self):
        return self.x_max - self.x_min

    @property
    def height(self):
        return self.y_max - self.y_min

    @property
    def center(self):
        """The center of the (bounding box of the) shape."""
        return self.envelope.center

    @center.setter
    def center(self, value):
        width = self.width
        height = self.height

        # Make sure not to swap min and max values
        x_min = value.x - width / 2
        x_max = value.x + width / 2
        if x_min >= self.x_max:
            self.x_max = x_max
            self.x_min = x_min
        else:
            self.x_min = x_min
            self.x_max = x_max

        y_min = value.y - height / 2
        y_max = value.y + height / 2
        if y_min >= self.y_max:
            self.y_max = y_max
            self.y_min = y_min
        else:
            self.y_min = y_min
            self.y_max = y_max

    def __iadd__(self, other):
        self.points = [p + other for p in self.points]
        return self

    def __isub__(self, other):
        self.points = [p - other for p in self.points]
        return self

    def __imul__(self, other):
        self.points = [p * other for p in self.points]
        return self

    def __itruediv__(self, other):
        self.points = [p / other for p in self.points]
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

    def __iter__(self):
        return iter(self.points)

    def __eq__(self, other):
        if not isinstance(other, Shape):
            return False
        else:
            return all(p1 == p2 for p1, p2 in zip(self, other))
