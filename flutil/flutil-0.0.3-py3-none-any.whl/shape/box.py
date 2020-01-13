import copy
from typing import Union
from matplotlib.patches import Rectangle
from .point import Point
from .warnings import warn_reduced_dim_after_setting_attr


class Box:
    """An easy-to-use box.

    :param float x_min: the x-coordinate of the left side of the rectangle
    :param float y_min: the y-coordinate of the top side of the rectangle
    :param float x_max: the x-coordinate of the right side of the rectangle
    :param float y_max: the y-coordinate of the bottom side of the rectangle
    """
    def __init__(self,
                 x_min: float,
                 y_min: float,
                 x_max: float,
                 y_max: float):
        self._x_min = x_min
        self._y_min = y_min
        self._x_max = x_max
        self._y_max = y_max

    def __repr__(self):
        return f'{self.x_min, self.y_min, self.x_max, self.y_max}'

    def __iter__(self):
        return iter(self.to_tuple())

    def __iadd__(self, other):
        if isinstance(other, tuple):
            self.center = tuple([c + o for c, o in zip(self.center, other)])
        else:
            self.center += other
        return self

    def __isub__(self, other):
        if isinstance(other, (tuple, Point)):
            self.center += tuple(-o for o in other)
        else:
            self.center += -other
        return self

    def __imul__(self, other):
        """Rescale the box with factor `b`"""
        if isinstance(other, tuple):
            factor = other
        else:
            factor = (other, other)
        self.width *= factor[0]
        self.height *= factor[1]
        return self

    def __itruediv__(self, b):
        """Rescale the box with factor `1/b`"""
        if isinstance(b, tuple):
            self *= tuple(1/x for x in b)
        else:
            self *= 1/b
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

    def __and__(self, other):
        """The area of overlap of two boxes."""
        dx = min(self.x_max, other.x_max) - max(self.x_min, other.x_min)
        dy = min(self.y_max, other.y_max) - max(self.y_min, other.y_min)
        if dx >= 0 and dy >= 0:
            return dx * dy
        else:
            return 0

    def __or__(self, other):
        """The union area of two boxes."""
        overlap = self & other
        return self.area + other.area - overlap

    def __contains__(self, other):
        """Check if `other` is inside the `self` Box.

        `other` can be a Box, Point or tuple (x, y) instance.
        """
        if isinstance(other, Point):
            return (other.x >= self.x_min
                    and other.y >= self.y_min
                    and other.x <= self.x_max
                    and other.y <= self.y_max)
        elif isinstance(other, tuple):
            return (other[0] >= self.x_min
                    and other[1] >= self.y_min
                    and other[0] <= self.x_max
                    and other[1] <= self.y_max)
        elif isinstance(other, Box):
            return (other.x_min >= self.x_min
                    and other.y_min >= self.y_min
                    and other.x_max <= self.x_max
                    and other.y_max <= self.y_max)

    def __eq__(self, other):
        if not isinstance(other, Box):
            return False
        return (self.x_min == other.x_min
                and self.y_min == other.y_min
                and self.x_max == other.x_max
                and self.y_max == other.y_max)

    def __hash__(self):
        return hash(tuple(self))

    @staticmethod
    def from_width_height(width: float, height: float,
                          center: Union[Point, tuple] = None,
                          top_left: Union[Point, tuple] = None):
        """Return a new ``Box`` from a width and a height.

        :param float width: the width of the new ``Box``
        :param float height: the height of the new ``Box``
        :param Point,tuple center: (optional) the center coordinate of the box.
        If ``None``, the center will be put in the middle of ``width`` and
        ``height`` (i.e. the ``Box`` will have top left coordinates (0, 0) ).
        If a tuple is passed, the coordinates are considered the x and y
        coordinates of the center, respectively.
        :param Point,tuple top_left: (optional) the top left coordinate of the
        box. If ``None``, the ``Box`` will have top left coordinates (0, 0).
        """
        if center is not None and top_left is not None:
            raise ValueError('Either `center` or `top_left` should be '
                             'defined, not both.')

        if center is None and top_left is None:
            top_left = Point(0, 0)
        elif top_left is None:
            top_left = Point(x=tuple(center)[0] - width/2,
                             y=tuple(center)[1] - height/2)
        elif isinstance(top_left, tuple):
            top_left = Point(x=top_left[0], y=top_left[1])

        x_min = top_left.x
        y_min = top_left.y
        x_max = top_left.x + width
        y_max = top_left.y + height

        return Box(x_min=x_min, y_min=y_min,
                   x_max=x_max, y_max=y_max)

    @property
    def x_min(self):
        return self._x_min

    @x_min.setter
    def x_min(self, value):
        if self.width != 0 and self.x_max == value:
            warn_reduced_dim_after_setting_attr()
        if self.width != 0 and value > self.x_max:
            raise ValueError(f'Setting x_min changes x_max')
        self._x_min = value

    @property
    def y_min(self):
        return self._y_min

    @y_min.setter
    def y_min(self, value):
        if self.height != 0 and self.y_max == value:
            warn_reduced_dim_after_setting_attr()
        if self.height != 0 and value > self.y_max:
            raise ValueError(f'Setting y_min changes y_max')
        self._y_min = value

    @property
    def x_max(self):
        return self._x_max

    @x_max.setter
    def x_max(self, value):
        if self.width != 0 and self.x_min == value:
            warn_reduced_dim_after_setting_attr()
        if self.width != 0 and value < self.x_min:
            raise ValueError(f'Setting x_max changes x_min')
        self._x_max = value

    @property
    def y_max(self):
        return self._y_max

    @y_max.setter
    def y_max(self, value):
        if self.height != 0 and self.y_min == value:
            warn_reduced_dim_after_setting_attr()
        if self.height != 0 and value < self.y_min:
            raise ValueError(f'Setting y_max changes y_min')
        self._y_max = value

    @property
    def left(self):
        """The x-coordinate of the left boundary of the box."""
        return self.x_min

    @property
    def top(self):
        """The y-coordinate of the top boundary of the box."""
        return self.y_min

    @property
    def right(self):
        """The x-coordinate of the right boundary of the box."""
        return self.x_max

    @property
    def bottom(self):
        """The y-coordinate of the bottom boundary of the box."""
        return self.y_max

    @property
    def width(self):
        """The width of the box."""
        return self.x_max - self.x_min

    @width.setter
    def width(self, value):
        fac = value / self.width

        center_x = self.center.x
        new_x_min = int((self.x_min - center_x)*fac + center_x)
        new_x_max = int((self.x_max - center_x)*fac + center_x)

        self.x_min = new_x_min
        self.x_max = new_x_max

    @property
    def height(self):
        """The height of the box."""
        return self.y_max - self.y_min

    @height.setter
    def height(self, value):
        fac = value / self.height

        center_y = self.center.y
        new_y_min = int((self.y_min - center_y)*fac + center_y)
        new_y_max = int((self.y_max - center_y)*fac + center_y)

        self.y_min = new_y_min
        self.y_max = new_y_max

    @property
    def area(self):
        return self.width * self.height

    @property
    def size(self):
        return (self.width, self.height)

    @property
    def bottom_left(self):
        """The bottom left coordinates of the box."""
        return (self.left, self.bottom)

    @property
    def bl(self):
        """The bottom left coordinates of the box."""
        return self.bottom_left

    @property
    def bottom_right(self):
        """The bottom right coordinates of the box."""
        return (self.right, self.bottom)

    @property
    def br(self):
        """The bottom right coordinates of the box."""
        return self.bottom_right

    @property
    def top_left(self):
        """The top left coordinates of the box."""
        return (self.left, self.top)

    @property
    def tl(self):
        """The top left coordinates of the box."""
        return self.top_left

    @property
    def top_right(self):
        """The top right coordinates of the box."""
        return (self.right, self.top)

    @property
    def tr(self):
        """The top right coordinates of the box."""
        return self.top_right

    @property
    def center(self) -> Point:
        """The center coordinates of the box."""
        x_center = self.x_min + (self.x_max - self.x_min)/2
        y_center = self.y_min + (self.y_max - self.y_min)/2
        return Point(x_center, y_center)

    @center.setter
    def center(self, value):
        width = self.width
        height = self.height
        if isinstance(value, Point):
            x_min = value.x - width/2
            y_min = value.y - height/2
            x_max = value.x + width/2
            y_max = value.y + height/2
        elif isinstance(value, tuple):
            x_min = value[0] - width/2
            y_min = value[1] - height/2
            x_max = value[0] + width/2
            y_max = value[1] + height/2
        else:
            raise NotImplementedError('Setter not implemented for type '
                                      f'{type(value)}.')

        # Make sure not to flip min and max values
        if x_min >= self.x_max:
            self.x_max = x_max
            self.x_min = x_min
        else:
            self.x_min = x_min
            self.x_max = x_max

        if y_min >= self.y_max:
            self.y_max = y_max
            self.y_min = y_min
        else:
            self.y_min = y_min
            self.y_max = y_max

    def iou(self, other):
        """Return the intersection over union (IOU) of the two boxes."""
        return (self & other)/(self | other)

    def to_int(self):
        """Return copy with all the values converted to an int."""
        return Box(x_min=int(self.x_min),
                   y_min=int(self.y_min),
                   x_max=int(self.x_max),
                   y_max=int(self.y_max))

    def coordinate_from_char(self, coor_char: str):
        """Return the box's coordinate that corresponds to the given char.

        :param str coor_char: character describing the desired coordinate. 't'
        for top, 'r' for right, 'b' for bottom and 'l' for left.
        """
        if coor_char == 't':
            return self.top
        elif coor_char == 'r':
            return self.right
        elif coor_char == 'b':
            return self.bottom
        elif coor_char == 'l':
            return self.left

    def to_tuple(self, order: str='ltrb'):
        """Return the box as a tuple with its coordinates in certain order.

        :param str order: Optional, string describing the desired order of the
        tuple.  't' for top, 'r' for right, 'b' for bottom and 'l' for left.
        E.g.: 'trbl' will return a (top, right, bottom, left)-tuple, while
        'ltrb' will return a (left, top, right, bottom)-tuple. Default returns
        tuple with order ``x_min``, ``y_min``, ``x_max``, ``y_max``.
        """
        coordinates = []
        for char in order:
            coordinates.append(self.coordinate_from_char(char))
        return tuple(coordinates)

    @property
    def css(self):
        """The box as a (top, right, bottom, left)-tuple."""
        return self.to_tuple('trbl')

    def to_patch(self, *args, **kwargs):
        """Return the box as a matplotlib ``Patch``."""
        if 'fill' in kwargs:
            fill = kwargs['fill']
            del kwargs['fill']
        else:
            fill = False
        return Rectangle((self.left, self.top),
                         self.width,
                         self.height,
                         *args,
                         fill=fill,
                         **kwargs)

    def scale_xy(self, x_factor, y_factor,
                 min_x=-float('inf'), min_y=-float('inf'),
                 max_x=float('inf'), max_y=float('inf')):
        """Return an x- and y-scaled variant of this ``Box``.

        :param float x_factor: the factor to scale with in the x-direction
        :param float y_factor: the factor to scale with in the y-direction
        :param float min_x: the smallest allowed x-value, the box will clip to
        this value
        :param float min_y: the smallest allowed y-value, the box will clip to
        this value
        :param float max_x: the largest allowed x-value, the box will clip to
        this value
        :param float max_y: the largest allowed y-value, the box will clip to
        this value
        """
        scaled_box = self * (x_factor, y_factor)
        scaled_box.x_min = max(min_x, scaled_box.x_min)
        scaled_box.y_min = max(min_y, scaled_box.y_min)
        scaled_box.x_max = min(max_x, scaled_box.x_max)
        scaled_box.y_max = min(max_y, scaled_box.y_max)

        return scaled_box

    def scale(self, factor,
              min_x=-float('inf'), min_y=-float('inf'),
              max_x=float('inf'), max_y=float('inf')):
        """Return a uniformly scaled variant of this ``Box``.

        :param float factor: the factor to scale with
        :param float min_x: the smallest allowed x-value, the box will clip to
        this value
        :param float min_y: the smallest allowed y-value, the box will clip to
        this value
        :param float max_x: the largest allowed x-value, the box will clip to
        this value
        :param float max_y: the largest allowed y-value, the box will clip to
        this value
        """
        return self.scale_xy(x_factor=factor, y_factor=factor,
                             min_x=min_x, min_y=min_y,
                             max_x=max_x, max_y=max_y)

    def align(self, other, how):
        """Align the box with another box.

        :param Box other: another Box which is used as a reference / anchor
        :param str how: how to align the box, choose between 'center_x',
        'center_y', 'left', 'right', 'top' or 'bottom'
        :returns: the Box itself, which can be useful for performing multiple
        alignments successively
        """
        hows = ['center_x', 'center_y', 'left', 'right', 'top', 'bottom']
        if how not in hows:
            raise ValueError(f'how arg should be one of {hows}')

        if how == 'center_x':
            self.center = (other.center.x, self.center.y)
        elif how == 'center_y':
            self.center = (self.center.x, other.center.y)
        elif how == 'left':
            self.center = (other.center.x - other.width/2 + self.width/2,
                           self.center.y)
        elif how == 'right':
            self.center = (other.center.x + other.width/2 - self.width/2,
                           self.center.y)
        elif how == 'top':
            self.center = (self.center.x,
                           other.center.y - other.height/2 + self.height/2)
        elif how == 'bottom':
            self.center = (self.center.x,
                           other.center.y + other.height/2 - self.height/2)
        return self

    def shift(self, delta_x, delta_y,
              min_x=-float('inf'), min_y=-float('inf'),
              max_x=float('inf'), max_y=float('inf')):
        """Return a shifted version of this ``Box``.

        :param float delta_x: the horizontal shift
        :param float delta_y: the vertical shift
        :param float min_x: the smallest allowed x-value, the box will clip to
        this value
        :param float min_y: the smallest allowed y-value, the box will clip to
        this value
        :param float max_x: the largest allowed x-value, the box will clip to
        this value
        :param float max_y: the largest allowed y-value, the box will clip to
        this value
        """
        if max_x <= min_x:
            raise ValueError('max_x should be greater than min_x')
        if max_y <= min_y:
            raise ValueError('max_y should be greater than min_y')

        shifted_box = self + (delta_x, delta_y)

        x_min = max(min_x, shifted_box.x_min)
        x_max = min(max_x, shifted_box.x_max)
        y_min = max(min_y, shifted_box.y_min)
        y_max = min(max_y, shifted_box.y_max)

        # Make sure not to flip min and max values
        if x_min > shifted_box.x_max:
            shifted_box.x_max = x_max
            shifted_box.x_min = x_min
        else:
            shifted_box.x_min = x_min
            shifted_box.x_max = x_max

        if y_min > shifted_box.y_max:
            shifted_box.y_max = y_max
            shifted_box.y_min = y_min
        else:
            shifted_box.y_min = y_min
            shifted_box.y_max = y_max

        return shifted_box
