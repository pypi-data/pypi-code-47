#!/usr/bin/env/python
import unittest
from . import Box, Point, Shape
import copy
from .warnings import ReducedDimensionalityWarning


class BoxTestCase(unittest.TestCase):
    def setUp(self):
        self.box = Box(x_min=0, x_max=1,
                       y_min=2, y_max=3)

    def test_base_properties(self):
        self.assertEqual(self.box.x_min, 0)
        self.assertEqual(self.box.x_max, 1)
        self.assertEqual(self.box.y_min, 2)
        self.assertEqual(self.box.y_max, 3)

    def test_box_css_properties(self):
        self.assertEqual(self.box.left, 0)
        self.assertEqual(self.box.right, 1)
        self.assertEqual(self.box.top, 2)
        self.assertEqual(self.box.bottom, 3)

    def test_box_coordinates(self):
        self.assertEqual(self.box.bottom_left, (0, 3))
        self.assertEqual(self.box.bottom_right, (1, 3))
        self.assertEqual(self.box.top_left, (0, 2))
        self.assertEqual(self.box.top_right, (1, 2))
        self.assertEqual(self.box.bl, (0, 3))
        self.assertEqual(self.box.br, (1, 3))
        self.assertEqual(self.box.tl, (0, 2))
        self.assertEqual(self.box.tr, (1, 2))
        self.assertEqual(self.box.center, Point(0.5, 2.5))

    def test_to_tuple(self):
        box = Box(1, 2, 3, 4)
        self.assertEqual(box.to_tuple(), (1, 2, 3, 4))

    def test_box_width_height(self):
        self.assertEqual(self.box.width, 1)
        self.assertEqual(self.box.height, 1)

    def test_to_int(self):
        box = Box(1.2, 1.0, 2.1, 2.2)
        box_int = box.to_int()
        self.assertEqual(box_int.x_min, 1)
        self.assertEqual(box_int.y_min, 1)
        self.assertEqual(box_int.x_max, 2)
        self.assertEqual(box_int.y_max, 2)

    def test_coordinate_from_char(self):
        self.assertEqual(self.box.left,
                         self.box.coordinate_from_char('l'))
        self.assertEqual(self.box.right,
                         self.box.coordinate_from_char('r'))
        self.assertEqual(self.box.bottom,
                         self.box.coordinate_from_char('b'))
        self.assertEqual(self.box.top,
                         self.box.coordinate_from_char('t'))

    def test_css(self):
        self.assertEqual(self.box.css,
                         (self.box.top,
                          self.box.right,
                          self.box.bottom,
                          self.box.left))

    def test_set_x_min(self):
        self.box.x_min = -1
        self.assertEqual(self.box.x_min, -1)

    def test_set_y_min(self):
        self.box.y_min = 1
        self.assertEqual(self.box.y_min, 1)

    def test_set_x_max(self):
        self.box.x_max = 2
        self.assertEqual(self.box.x_max, 2)

    def test_set_y_max(self):
        self.box.y_max = 4
        self.assertEqual(self.box.y_max, 4)

    def test_x_min_changes_x_max_error(self):
        with self.assertRaises(ValueError):
            self.box.x_min = 2

    def test_y_min_changes_y_max_error(self):
        with self.assertRaises(ValueError):
            self.box.y_min = 4

    def test_x_max_changes_x_min_error(self):
        with self.assertRaises(ValueError):
            self.box.x_max = -1

    def test_y_max_changes_y_min_error(self):
        with self.assertRaises(ValueError):
            self.box.y_max = 1

    def test_add_tuple(self):
        box1 = Box(0, 0, 1, 1)
        box2 = box1 + (1, 1)
        self.assertEqual(box2,
                         Box(1, 1, 2, 2))

    def test_add_point(self):
        box1 = Box(0, 0, 1, 1)
        box2 = box1 + Point(1, 1)
        self.assertEqual(box2,
                         Box(1, 1, 2, 2))

    def test_sub_tuple(self):
        box1 = Box(0, 0, 1, 1)
        box2 = box1 - (-1, 2)
        self.assertEqual(box2,
                         Box(1, -2, 2, -1))

    def test_sub_point(self):
        box1 = Box(0, 0, 1, 1)
        box2 = box1 - Point(1, 1)
        self.assertEqual(box2,
                         Box(-1, -1, 0, 0))

    def test_mul_tuple(self):
        box1 = Box(-2, -1, 0, 1)
        box2 = box1 * (2, 3)
        self.assertEqual(box2,
                         Box(-3, -3, 1, 3))

    def test_mul_number(self):
        box1 = Box(-2, -1, 0, 1)
        box2 = box1 * 2
        self.assertEqual(box2,
                         Box(-3, -2, 1, 2))

    def test_div_tuple(self):
        box1 = Box(-3, -3, 1, 3)
        box2 = box1 / (2, 3)
        self.assertEqual(box2,
                         Box(-2, -1, 0, 1))

    def test_div_number(self):
        box1 = Box(-3, -2, 1, 2)
        box2 = box1 / 2
        self.assertEqual(box2,
                         Box(-2, -1, 0, 1))

    def test_and(self):
        box1 = Box(0, 0, 2, 1)
        box2 = Box(1, 0, 3, 1)
        self.assertEqual(box1 & box2,
                         1)

    def test_or(self):
        box1 = Box(0, 0, 2, 1)
        box2 = Box(1, 0, 3, 1)
        self.assertEqual(box1 | box2,
                         3)

    def test_contains_box(self):
        box1 = Box(-2, -2, 2, 2)
        box2 = Box(-1, -1, 1, 1)
        self.assertTrue(box2 in box1)

    def test_contains_point(self):
        box1 = Box(-2, -2, 2, 2)
        self.assertTrue(Point(-1, 0) in box1)

    def test_contains_tuple(self):
        box1 = Box(-2, -2, 2, 2)
        self.assertTrue((-1, 0) in box1)

    def test_from_wh_c(self):
        box = Box.from_width_height(width=3,
                                    height=2,
                                    center=Point(0, 1))
        self.assertEqual(box,
                         Box(-1.5, 0, 1.5, 2))

    def test_from_wh_c_tup(self):
        box = Box.from_width_height(width=3,
                                    height=2,
                                    center=(0, 1))
        self.assertEqual(box,
                         Box(-1.5, 0, 1.5, 2))

    def test_from_wh_tl(self):
        box = Box.from_width_height(width=3,
                                    height=2,
                                    top_left=Point(0, 1))
        self.assertEqual(box,
                         Box(0, 1, 3, 3))

    def test_from_wh_tl_tup(self):
        box = Box.from_width_height(width=3,
                                    height=2,
                                    top_left=(0, 1))
        self.assertEqual(box,
                         Box(0, 1, 3, 3))

    def test_scale_xy(self):
        box1 = Box(-1, -1, 1, 1)
        box2 = box1.scale_xy(x_factor=2, y_factor=3)
        self.assertEqual(box2,
                         Box(-2, -3, 2, 3))

    def test_scale_xy_clip(self):
        box1 = Box(-1, -1, 1, 1)
        box2 = box1.scale_xy(x_factor=2, y_factor=3,
                             min_x=-1, min_y=-2,
                             max_x=1, max_y=2)
        self.assertEqual(box2,
                         Box(-1, -2, 1, 2))

    def test_scale(self):
        box1 = Box(-1, -1, 1, 1)
        box2 = box1.scale(2)
        self.assertEqual(box2,
                         Box(-2, -2, 2, 2))

    def test_scale_factor_less_than_one(self):
        box1 = Box(-1, -0.5, 3, 1.5)
        box2 = box1.scale(0.5)
        self.assertEqual(box2,
                         Box(0, 0, 2, 1))

    def test_scale_clip(self):
        box1 = Box(-1, -1, 1, 1)
        box2 = box1.scale(2,
                          min_x=-1, min_y=-2,
                          max_x=1, max_y=2)
        self.assertEqual(box2,
                         Box(-1, -2, 1, 2))

    def test_shift_max_x_less_than_min_x_error(self):
        with self.assertRaises(ValueError):
            self.box.shift(1, 1, min_x=10, max_x=0)

    def test_shift_max_y_less_than_min_y_error(self):
        with self.assertRaises(ValueError):
            self.box.shift(1, 1, min_y=10, max_y=0)

    def test_shift(self):
        box1 = Box(-1, -1, 1, 1)
        box2 = box1.shift(delta_x=2, delta_y=3)
        self.assertEqual(box2,
                         Box(1, 2, 3, 4))

    def test_shift_clip(self):
        box1 = Box(-1, -1, 1, 1)
        box2 = box1.shift(delta_x=2, delta_y=3,
                          min_x=2, min_y=2,
                          max_x=3, max_y=3)
        self.assertEqual(box2,
                         Box(2, 2, 3, 3))

    def test_reduced_dimensionality_warning_x_min(self):
        with self.assertWarns(ReducedDimensionalityWarning):
            self.box.x_min = 1

    def test_reduced_dimensionality_warning_x_max(self):
        with self.assertWarns(ReducedDimensionalityWarning):
            self.box.x_max = 0

    def test_reduced_dimensionality_warning_y_min(self):
        with self.assertWarns(ReducedDimensionalityWarning):
            self.box.y_min = 3

    def test_reduced_dimensionality_warning_y_max(self):
        with self.assertWarns(ReducedDimensionalityWarning):
            self.box.y_max = 2

    def setup_align(self):
        self.box1 = Box(-4, -2, 0, 2)
        self.box2 = Box(0, 0, 1, 1)

    def test_align_center_x(self):
        self.setup_align()
        box2 = self.box2.align(self.box1, 'center_x')

        exp_box = Box(-2.5, 0, -1.5, 1)
        self.assertEqual(box2, exp_box)
        self.assertEqual(self.box2, exp_box)

    def test_align_center_y(self):
        self.setup_align()
        box2 = self.box2.align(self.box1, 'center_y')

        exp_box = Box(0, -.5, 1, .5)
        self.assertEqual(box2, exp_box)
        self.assertEqual(self.box2, exp_box)

    def test_align_left(self):
        self.setup_align()
        box2 = self.box2.align(self.box1, 'left')

        exp_box = Box(-4, 0, -3, 1)
        self.assertEqual(box2, exp_box)
        self.assertEqual(self.box2, exp_box)

    def test_align_right(self):
        self.setup_align()
        box2 = self.box2.align(self.box1, 'right')

        exp_box = Box(-1, 0, 0, 1)
        self.assertEqual(box2, exp_box)
        self.assertEqual(self.box2, exp_box)

    def test_align_bottom(self):
        self.setup_align()
        box2 = self.box2.align(self.box1, 'bottom')

        exp_box = Box(0, 1, 1, 2)
        self.assertEqual(box2, exp_box)
        self.assertEqual(self.box2, exp_box)

    def test_align_top(self):
        self.setup_align()
        box2 = self.box2.align(self.box1, 'top')

        exp_box = Box(0, -2, 1, -1)
        self.assertEqual(box2, exp_box)
        self.assertEqual(self.box2, exp_box)


class PointTestCase(unittest.TestCase):
    def test_props(self):
        point = Point(0, 1)
        self.assertEqual(point.x, 0)
        self.assertEqual(point.y, 1)

    def test_eq(self):
        self.assertEqual(Point(0, 1),
                         Point(0, 1))

    def test_add_tuple(self):
        point1 = Point(0, 1)
        point2 = point1 + (1, 2)
        self.assertEqual(point2,
                         Point(1, 3))

    def test_add_point(self):
        point1 = Point(0, 1)
        point2 = point1 + Point(1, 2)
        self.assertEqual(point2,
                         Point(1, 3))

    def test_add_number(self):
        point1 = Point(0, 1)
        point2 = point1 + 2
        self.assertEqual(point2,
                         Point(2, 3))

    def test_sub_tuple(self):
        point1 = Point(0, 1)
        point2 = point1 - (1, 2)
        self.assertEqual(point2,
                         Point(-1, -1))

    def test_sub_point(self):
        point1 = Point(0, 1)
        point2 = point1 - Point(1, 2)
        self.assertEqual(point2,
                         Point(-1, -1))

    def test_sub_number(self):
        point1 = Point(0, 1)
        point2 = point1 - 2
        self.assertEqual(point2,
                         Point(-2, -1))

    def test_mul_number(self):
        point1 = Point(-1, 1)
        point2 = point1 * 2
        self.assertEqual(point2,
                         Point(-2, 2))

    def test_div_number(self):
        point1 = Point(-1, 1)
        point2 = point1 / 2
        self.assertEqual(point2,
                         Point(-0.5, 0.5))

    def test_iter(self):
        point = Point(0, 1)
        self.assertEqual([*point],
                         [0, 1])

    def test_dist_to_point(self):
        point1 = Point(1, -1)
        point2 = Point(4, 3)

        self.assertEqual(point1.dist(to=point2),
                         5)


class ShapeTestCase(unittest.TestCase):
    def test_props_get(self):
        points = [Point(-1, -1),
                  Point(0, 1),
                  Point(1, -1)]

        shape = Shape(points)
        self.assertEqual(shape.points, points)
        self.assertEqual(shape.x_min, -1)
        self.assertEqual(shape.y_min, -1)
        self.assertEqual(shape.x_max, 1)
        self.assertEqual(shape.y_max, 1)

    def test_eq(self):
        points = [Point(-1, -1),
                  Point(0, 1),
                  Point(1, -1)]

        shape1 = Shape(points)
        shape2 = copy.deepcopy(Shape(points))
        self.assertEqual(shape1, shape2)

    def test_set_x_min(self):
        points = [Point(-1, -1),
                  Point(-2, 1),
                  Point(-3, -1)]

        shape = Shape(points)
        shape.x_min = -5

        self.assertEqual(shape,
                         Shape([Point(-1, -1),
                                Point(-3, 1),
                                Point(-5, -1)]))

    def test_set_y_min(self):
        points = [Point(-1, -1),
                  Point(0, 1),
                  Point(1, -1)]

        shape = Shape(points)
        shape.y_min = 0
        self.assertEqual(shape,
                         Shape([Point(-1, 0),
                                Point(0, 1),
                                Point(1, 0)]))

    def test_set_x_max(self):
        points = [Point(-1, -1),
                  Point(0, 1),
                  Point(1, -1)]

        shape = Shape(points)
        shape.x_max = 0
        self.assertEqual(shape,
                         Shape([Point(-1, -1),
                                Point(-.5, 1),
                                Point(0, -1)]))

    def test_set_y_max(self):
        points = [Point(-1, -1),
                  Point(0, 1),
                  Point(1, -1)]

        shape = Shape(points)
        shape.y_max = 0
        self.assertEqual(shape,
                         Shape([Point(-1, -1),
                                Point(0, 0),
                                Point(1, -1)]))

    def test_reduced_dimensionality_warning_x(self):
        points = [Point(-1, -1),
                  Point(0, 1),
                  Point(-1, 1)]

        # x_min
        shape = Shape(points)
        with self.assertWarns(Warning):
            shape.x_min = 0

        # x_max
        shape = Shape(points)
        with self.assertWarns(Warning):
            shape.x_max = -1

    def test_reduced_dimensionality_warning_y(self):
        points = [Point(-1, -1),
                  Point(0, 1),
                  Point(1, -1)]

        # y_min
        shape = Shape(points)
        with self.assertWarns(Warning):
            shape.y_min = 1

        # y_max
        shape = Shape(points)
        with self.assertWarns(Warning):
            shape.y_max = -1

    def test_set_x_min_zero_width(self):
        points = [Point(-1, -1),
                  Point(-1, 1)]

        shape = Shape(points)
        shape.x_min = -5

        self.assertEqual(shape,
                         Shape([Point(-5, -1),
                                Point(-5, 1)]))

    def test_set_y_min_zero_height(self):
        points = [Point(-1, -1),
                  Point(1, -1)]

        shape = Shape(points)
        shape.y_min = 0
        self.assertEqual(shape,
                         Shape([Point(-1, 0),
                                Point(1, 0)]))

    def test_set_x_max_zero_width(self):
        points = [Point(-1, -1),
                  Point(-1, 1)]

        shape = Shape(points)
        shape.x_max = 0
        self.assertEqual(shape,
                         Shape([Point(0, -1),
                                Point(0, 1)]))

    def test_set_y_max_zero_height(self):
        points = [Point(-1, -1),
                  Point(1, -1)]

        shape = Shape(points)
        shape.y_max = 0
        self.assertEqual(shape,
                         Shape([Point(-1, 0),
                                Point(1, 0)]))

    def test_center(self):
        points = [Point(-1, 0),
                  Point(1, 0)]

        shape = Shape(points)
        self.assertEqual(shape.center,
                         Point(0, 0))

    def test_set_center(self):
        points = [Point(-1, 0),
                  Point(1, 2)]

        shape = Shape(points)
        shape.center = Point(1, 1)
        self.assertEqual(shape,
                         Shape([Point(0, 0),
                                Point(2, 2)]))

    def test_envelope(self):
        points = [Point(-1, -1),
                  Point(0, 1),
                  Point(1, -1)]

        shape = Shape(points)
        self.assertEqual(shape.envelope,
                         Box(-1, -1, 1, 1))

    def test_add_point(self):
        shape = Shape([Point(-1, 0),
                       Point(1, 0)])

        shape2 = shape + Point(1, 2)

        self.assertEqual(shape2,
                         Shape([Point(0, 2),
                                Point(2, 2)]))

    def test_add_tuple(self):
        shape = Shape([Point(-1, 0),
                       Point(1, 0)])

        shape2 = shape + (1, 2)

        self.assertEqual(shape2,
                         Shape([Point(0, 2),
                                Point(2, 2)]))

    def test_add_number(self):
        shape = Shape([Point(-1, 0),
                       Point(1, 0)])

        shape2 = shape + 2

        self.assertEqual(shape2,
                         Shape([Point(1, 2),
                                Point(3, 2)]))

    def test_sub_point(self):
        shape = Shape([Point(-1, 0),
                       Point(1, 0)])

        shape2 = shape - Point(1, 2)

        self.assertEqual(shape2,
                         Shape([Point(-2, -2),
                                Point(0, -2)]))

    def test_sub_tuple(self):
        shape = Shape([Point(-1, 0),
                       Point(1, 0)])

        shape2 = shape - (1, 2)

        self.assertEqual(shape2,
                         Shape([Point(-2, -2),
                                Point(0, -2)]))

    def test_sub_number(self):
        shape = Shape([Point(-1, 0),
                       Point(1, 0)])

        shape2 = shape - 2

        self.assertEqual(shape2,
                         Shape([Point(-3, -2),
                                Point(-1, -2)]))

    def test_truediv(self):
        shape = Shape([Point(-1, 0),
                       Point(1, 0)])

        shape2 = shape / 2

        self.assertEqual(shape2,
                         Shape([Point(-0.5, 0),
                                Point(0.5, 0)]))

    def test_mul(self):
        shape = Shape([Point(-1, 0),
                       Point(1, 0)])

        shape2 = shape * 2

        self.assertEqual(shape2,
                         Shape([Point(-2, 0),
                                Point(2, 0)]))

    def test_iter(self):
        points = [Point(-1, 0),
                  Point(1, 0)]
        shape = Shape(points)
        self.assertEqual([*shape],
                         points)


if __name__ == '__main__':
    unittest.main()
