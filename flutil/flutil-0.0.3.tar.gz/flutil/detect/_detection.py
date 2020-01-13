from ..shape import Point, Box, Shape
from typing import List
from matplotlib.patches import Circle
from matplotlib.patches import Patch
import warnings
from ..shape.warnings import ReducedDimensionalityWarning


class Detection(Box):
    def __init__(self,
                 x_min: float, y_min: float,
                 x_max: float, y_max: float,
                 confidence: float = None):
        super().__init__(int(x_min), int(y_min),
                         int(x_max), int(y_max))
        self.confidence = confidence

    @property
    def confidence(self) -> float:
        """Confidence score of the detection."""
        return self._confidence

    @confidence.setter
    def confidence(self, value):
        self._confidence = value

    @property
    def x_min(self):
        return int(super().x_min)

    @x_min.setter
    def x_min(self, value):
        Box.x_min.fset(self, int(value))

    @property
    def y_min(self):
        return int(super().y_min)

    @y_min.setter
    def y_min(self, value):
        Box.y_min.fset(self, int(value))

    @property
    def x_max(self):
        return int(super().x_max)

    @x_max.setter
    def x_max(self, value):
        Box.x_max.fset(self, int(value))

    @property
    def y_max(self):
        return int(super().y_max)

    @y_max.setter
    def y_max(self, value):
        Box.y_max.fset(self, int(value))

    def to_patches(self, *args, **kwargs) -> List[Patch]:
        return [self.to_patch(*args, **kwargs)]

    def coordinate_from_char(self, coor_char: str):
        """Return the detection's coordinate that corresponds to the given
        char.

        :param str coor_char: character describing the desired coordinate. 't'
        for top, 'r' for right, 'b' for bottom, 'l' for left and 'c' for
        confidence score.
        """
        if coor_char == 'c':
            return self.confidence
        else:
            return super().coordinate_from_char(coor_char)

    def to_tuple(self, order: str = 'ltrbc'):
        """Return the detection as a tuple with its coordinates in certain
        order.

        :param str order: Optional, string describing the desired order of the
        tuple.  't' for top, 'r' for right, 'b' for bottom, 'l' for left and
        'c' for confidence score.
        """
        return super().to_tuple(order)

    def __eq__(self, other):
        if not super().__eq__(other):
            return False
        if not isinstance(other, Detection):
            return False
        return self.confidence == other.confidence

    def __hash__(self):
        return hash(tuple(self))


class ObjectDetection(Detection):
    def __init__(self,
                 x_min: float, y_min: float,
                 x_max: float, y_max: float,
                 label: str, confidence: float = None):
        super().__init__(x_min, y_min,
                         x_max, y_max,
                         confidence)
        self.label = label

    def coordinate_from_char(self, coor_char: str):
        """Return the detection's coordinate that corresponds to the given
        char.

        :param str coor_char: character describing the desired coordinate. 't'
        for top, 'r' for right, 'b' for bottom, 'l' for left, 'c' for
        confidence score and 'L' for label.
        """
        if coor_char == 'L':
            return self.label
        else:
            return super().coordinate_from_char(coor_char)

    def to_tuple(self, order: str = 'ltrbLc'):
        """Return the detection as a tuple with its coordinates in certain
        order.

        :param str order: Optional, string describing the desired order of the
        tuple.  't' for top, 'r' for right, 'b' for bottom, 'l' for left,
        'c' for confidence score and 'L' for label.
        """
        return super().to_tuple(order)

    def __eq__(self, other):
        if not super().__eq__(other):
            return False
        if not isinstance(other, Detection):
            return False
        return self.label == other.label

    def __hash__(self):
        return hash(tuple(self))


class PointDetection(Point, Detection):
    def __init__(self, x: float, y: float, confidence: float = None):
        Detection.__init__(self, x, y, x, y, confidence)
        Point.__init__(self, x, y)

    @property
    def x(self):
        assert self.x_min == self.x_max
        return self.x_min

    @x.setter
    def x(self, value):
        with warnings.catch_warnings():
            warnings.filterwarnings('ignore',
                                    category=ReducedDimensionalityWarning)
            self.x_min = value
            self.x_max = value

    @property
    def y(self):
        assert self.y_min == self.y_max
        return self.y_min

    @y.setter
    def y(self, value):
        with warnings.catch_warnings():
            warnings.filterwarnings('ignore',
                                    category=ReducedDimensionalityWarning)
            self.y_min = value
            self.y_max = value

    def to_patches(self, **kwargs) -> List[Patch]:
        if 'alpha' in kwargs:
            alpha = kwargs['alpha']
            del kwargs['alpha']
        elif self.confidence is not None:
            alpha = self.confidence
        else:
            alpha = 0.3

        if 'radius' in kwargs:
            radius = kwargs['radius']
            del kwargs['radius']
        else:
            radius = 5

        if 'color' in kwargs:
            color = kwargs['color']
            del kwargs['color']
        else:
            color = 'white'

        return [Circle(tuple(self.center),
                       alpha=alpha,
                       radius=radius,
                       color=color,
                       **kwargs)]


class ShapeDetection(Shape, Detection):
    """A detection consisting of a set of points."""
    def __init__(self, xs, ys, confidences: List[float] = None):

        if len(xs) != len(ys):
            raise ValueError('xs and ys must be of the same length.')

        if confidences is not None and len(xs) != len(confidences):
            raise ValueError('not enough confidence values for the given '
                             'points')

        if confidences is not None:
            points = [PointDetection(x, y, c)
                      for x, y, c in zip(xs, ys, confidences)]
        else:
            points = [PointDetection(x, y)
                      for x, y in zip(xs, ys)]

        super().__init__(points)

    def to_patches(self, **kwargs) -> List[Patch]:
        return [patch
                for p in self.points
                for patch in p.to_patches(**kwargs)]


class BoxShapeDetection(Detection):
    """A detection consisting of a box and a shape."""
    def __init__(self,
                 box_x_min, box_y_min,
                 box_x_max, box_y_max,
                 points_x, points_y,
                 box_confidence: List[float] = None,
                 points_confidence: List[float] = None):
        if len(points_x) != len(points_y):
            raise ValueError('points_x and points_y must be '
                             'of the same length.')

        self.shape = ShapeDetection(points_x, points_y, points_confidence)
        self.box = Detection(box_x_min, box_y_min,
                             box_x_max, box_y_max,
                             box_confidence)

        if not (self.shape in self.box or self.box in self.shape):
            warnings.warn('The given box and shape only partly overlap. '
                          'Currently, only "box in shape" and "shape in box" '
                          'are fully tested. Handle with care.')

        super().__init__(self.x_min, self.y_min, self.x_max, self.y_max)

    def to_patches(self, **kwargs) -> List[Patch]:
        """Return list of patches that represent the detection.

        The kwargs should be prefixed with "box_..." or "point_..." to indicate
        whether the kwarg is meant for the box patch or the point patches. If
        no prefix is given, the kwarg will be passed to both.
        """
        box_kwargs = {k.replace('box_', ''): v
                      for k, v in kwargs.items()
                      if not k.startswith('point_')}
        points_kwargs = {k.replace('point_', ''): v
                         for k, v in kwargs.items()
                         if not k.startswith('box_')}

        return [*self.box.to_patches(**box_kwargs),
                *self.shape.to_patches(**points_kwargs)]

    def prop_setter(self, attr, value):
        if 'min' in attr:
            ref_shape, adj_shape = ((self.box, self.shape)
                                    if (getattr(self.box, attr)
                                        < getattr(self.shape, attr))
                                    else (self.shape, self.box))
        else:
            ref_shape, adj_shape = ((self.box, self.shape)
                                    if (getattr(self.box, attr)
                                        > getattr(self.shape, attr))
                                    else (self.shape, self.box))

        size_attr = 'width' if 'x_' in attr else 'height'
        diff = getattr(adj_shape, attr) - getattr(ref_shape, attr)
        frac = diff / getattr(ref_shape, size_attr)

        # We need the complementary attribute of the given attribute
        # E.g. x_min if x_max is given
        # This is because that also needs to be set for the adj_shape
        compl_attr = (attr.replace('min', 'max')
                      if 'min' in attr
                      else attr.replace('max', 'min'))
        compl_diff = (getattr(adj_shape, compl_attr)
                      - getattr(ref_shape, compl_attr))
        compl_frac = compl_diff / getattr(ref_shape, size_attr)

        # Now set the attribute for the reference shape
        setattr(ref_shape, attr, value)

        # Adjust the other shape accordingly
        # Make sure to first stretch, then shrink
        # Otherwise e.g. the x_max changes when setting x_min
        new_attr_val = (getattr(ref_shape, attr)
                        + frac * getattr(ref_shape, size_attr))
        new_comp_attr_val = (getattr(ref_shape, compl_attr)
                             + compl_frac * getattr(ref_shape, size_attr))

        if 'min' in attr and new_attr_val > getattr(adj_shape, compl_attr):
            # First adjust the complementary attribute, i.e. the 'max'
            # Otherwise, our max will change
            setattr(adj_shape, compl_attr, new_comp_attr_val)
            setattr(adj_shape, attr, new_attr_val)
        elif 'max' in attr and new_attr_val < getattr(adj_shape, compl_attr):
            # First adjust the complementary attribute, i.e. the 'min'
            # Otherwise, our min will change
            setattr(adj_shape, compl_attr, new_comp_attr_val)
            setattr(adj_shape, attr, new_attr_val)
        else:
            # No worries, first setting the attribute will stretch the
            # adj_shape
            setattr(adj_shape, attr, new_attr_val)
            setattr(adj_shape, compl_attr, new_comp_attr_val)

    def prop_getter(self, attr):
        extremum_func = min if 'min' in attr else max
        return extremum_func(getattr(self.shape, attr),
                             getattr(self.box, attr))

    @property
    def x_min(self):
        return self.prop_getter('x_min')

    @x_min.setter
    def x_min(self, value):
        self.prop_setter('x_min', value)

    @property
    def y_min(self):
        return self.prop_getter('y_min')

    @y_min.setter
    def y_min(self, value):
        self.prop_setter('y_min', value)

    @property
    def x_max(self):
        return self.prop_getter('x_max')

    @x_max.setter
    def x_max(self, value):
        self.prop_setter('x_max', value)

    @property
    def y_max(self):
        return self.prop_getter('y_max')

    @y_max.setter
    def y_max(self, value):
        self.prop_setter('y_max', value)
