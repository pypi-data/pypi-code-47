import unittest
from . import Detection, PointDetection
from . import ShapeDetection, BoxShapeDetection


class DetectionTestCase(unittest.TestCase):
    def test_init(self):
        det = Detection(x_min=-1, y_min=-2,
                        x_max=1, y_max=2,
                        confidence=0.5)
        self.assertEqual(det.x_min, -1)
        self.assertEqual(det.y_min, -2)
        self.assertEqual(det.x_max, 1)
        self.assertEqual(det.y_max, 2)
        self.assertEqual(det.confidence, 0.5)

    def test_ints(self):
        det = Detection(x_min=-1.1, y_min=-2.1,
                        x_max=1.1, y_max=2.1)
        self.assertEqual(det.x_min, -1)
        self.assertEqual(det.y_min, -2)
        self.assertEqual(det.x_max, 1)
        self.assertEqual(det.y_max, 2)

    def test_setters(self):
        det = Detection(x_min=-2, y_min=-3,
                        x_max=2, y_max=3,
                        confidence=0.5)

        det.x_min = -1
        det.y_min = -2
        det.x_max = 1
        det.y_max = 2
        det.confidence = 1.0
        self.assertEqual(det.x_min, -1)
        self.assertEqual(det.y_min, -2)
        self.assertEqual(det.x_max, 1)
        self.assertEqual(det.y_max, 2)
        self.assertEqual(det.confidence, 1.0)


class PointDetectionTestCase(unittest.TestCase):
    def test_init(self):
        det = PointDetection(x=-1, y=-2,
                             confidence=0.5)
        self.assertEqual(det.x, -1)
        self.assertEqual(det.y, -2)
        self.assertEqual(det.confidence, 0.5)

    def test_setters(self):
        det = PointDetection(x=-2, y=-3,
                             confidence=0.5)
        det.x = -1
        det.y = -4
        det.confidence = 1.0
        self.assertEqual(det.x, -1)
        self.assertEqual(det.y, -4)
        self.assertEqual(det.confidence, 1.0)


class ShapeDetectionTestCase(unittest.TestCase):
    def setUp(self):
        self.det = ShapeDetection(xs=[2, 1, 3],
                                  ys=[-2, -1, -3],
                                  confidences=[.6, .5, .7])

    def test_init(self):
        self.assertEqual(self.det.x_min, 1)
        self.assertEqual(self.det.y_min, -3)
        self.assertEqual(self.det.x_max, 3)
        self.assertEqual(self.det.y_max, -1)

        self.assertEqual(self.det.points[0].x, 2)
        self.assertEqual(self.det.points[0].y, -2)
        self.assertEqual(self.det.points[0].confidence, .6)

        self.assertEqual(self.det.points[1].x, 1)
        self.assertEqual(self.det.points[1].y, -1)
        self.assertEqual(self.det.points[1].confidence, .5)

        self.assertEqual(self.det.points[2].x, 3)
        self.assertEqual(self.det.points[2].y, -3)
        self.assertEqual(self.det.points[2].confidence, .7)

    def test_init_no_confidences(self):
        det = ShapeDetection(xs=[2, 1, 3], ys=[-2, -1, -3])
        self.assertEqual(det.x_min, 1)
        self.assertEqual(det.y_min, -3)
        self.assertEqual(det.x_max, 3)
        self.assertEqual(det.y_max, -1)

        self.assertEqual(det.points[0].x, 2)
        self.assertEqual(det.points[0].y, -2)

        self.assertEqual(det.points[1].x, 1)
        self.assertEqual(det.points[1].y, -1)

        self.assertEqual(det.points[2].x, 3)
        self.assertEqual(det.points[2].y, -3)

    def test_too_few_xs_error(self):
        with self.assertRaises(ValueError):
            ShapeDetection(xs=[2, 3],
                           ys=[0, -1, 2])

    def test_too_few_ys_error(self):
        with self.assertRaises(ValueError):
            ShapeDetection(xs=[2, 3, 1],
                           ys=[0, -1])

    def test_too_few_confidences_error(self):
        with self.assertRaises(ValueError):
            ShapeDetection(xs=[2, 3, 1],
                           ys=[0, -1, 4],
                           confidences=[1, 2])


class BoxShapeDetectionTestCase(unittest.TestCase):
    def test_init(self):
        det = BoxShapeDetection(box_x_min=-5, box_y_min=-2,
                                box_x_max=5, box_y_max=2,
                                box_confidence=.5,
                                points_x=[-6, 0, 2],
                                points_y=[1, -3, -1],
                                points_confidence=[.1, .2, .3])

        self.assertEqual(det.x_min, -6)
        self.assertEqual(det.y_min, -3)
        self.assertEqual(det.x_max, 5)
        self.assertEqual(det.y_max, 2)

        self.assertEqual(det.shape.points[0].x, -6)
        self.assertEqual(det.shape.points[0].y, 1)
        self.assertEqual(det.shape.points[0].confidence, .1)

        self.assertEqual(det.shape.points[1].x, 0)
        self.assertEqual(det.shape.points[1].y, -3)
        self.assertEqual(det.shape.points[1].confidence, .2)

        self.assertEqual(det.shape.points[2].x, 2)
        self.assertEqual(det.shape.points[2].y, -1)
        self.assertEqual(det.shape.points[2].confidence, .3)

        self.assertEqual(det.box.x_min, -5)
        self.assertEqual(det.box.y_min, -2)
        self.assertEqual(det.box.x_max, 5)
        self.assertEqual(det.box.y_max, 2)

    def points_in_box_setup(self):
        det = BoxShapeDetection(box_x_min=-4, box_y_min=-2,
                                box_x_max=0, box_y_max=2,
                                box_confidence=.5,
                                points_x=[-2, -1],
                                points_y=[-1, 1],
                                points_confidence=[.5, .5])
        return det

    def test_x_min_setter_points_in_box(self):
        det = self.points_in_box_setup()
        det.x_min = -8
        self.assertEqual(det.x_min, -8)
        self.assertEqual(det.y_min, -2)
        self.assertEqual(det.x_max, 0)
        self.assertEqual(det.y_max, 2)

        self.assertEqual(det.box.x_min, -8)
        self.assertEqual(det.box.y_min, -2)
        self.assertEqual(det.box.x_max, 0)
        self.assertEqual(det.box.y_max, 2)

        self.assertEqual(det.shape.points[0].x, -4)
        self.assertEqual(det.shape.points[0].y, -1)
        self.assertEqual(det.shape.points[1].x, -2)
        self.assertEqual(det.shape.points[1].y, 1)

    def test_y_min_setter_points_in_box(self):
        det = self.points_in_box_setup()

        det.y_min = -6
        self.assertEqual(det.x_min, -4)
        self.assertEqual(det.y_min, -6)
        self.assertEqual(det.x_max, 0)
        self.assertEqual(det.y_max, 2)

        self.assertEqual(det.box.x_min, -4)
        self.assertEqual(det.box.y_min, -6)
        self.assertEqual(det.box.x_max, 0)
        self.assertEqual(det.box.y_max, 2)

        self.assertEqual(det.shape.points[0].x, -2)
        self.assertEqual(det.shape.points[0].y, -4)
        self.assertEqual(det.shape.points[1].x, -1)
        self.assertEqual(det.shape.points[1].y, 0)

    def test_x_max_setter_points_in_box(self):
        det = self.points_in_box_setup()

        det.x_max = 4
        self.assertEqual(det.x_min, -4)
        self.assertEqual(det.y_min, -2)
        self.assertEqual(det.x_max, 4)
        self.assertEqual(det.y_max, 2)

        self.assertEqual(det.box.x_min, -4)
        self.assertEqual(det.box.y_min, -2)
        self.assertEqual(det.box.x_max, 4)
        self.assertEqual(det.box.y_max, 2)

        self.assertEqual(det.shape.points[0].x, 0)
        self.assertEqual(det.shape.points[0].y, -1)
        self.assertEqual(det.shape.points[1].x, 2)
        self.assertEqual(det.shape.points[1].y, 1)

    def test_y_max_setter_points_in_box(self):
        det = self.points_in_box_setup()

        det.y_max = 6
        self.assertEqual(det.x_min, -4)
        self.assertEqual(det.y_min, -2)
        self.assertEqual(det.x_max, 0)
        self.assertEqual(det.y_max, 6)

        self.assertEqual(det.box.x_min, -4)
        self.assertEqual(det.box.y_min, -2)
        self.assertEqual(det.box.x_max, 0)
        self.assertEqual(det.box.y_max, 6)

        self.assertEqual(det.shape.points[0].x, -2)
        self.assertEqual(det.shape.points[0].y, 0)
        self.assertEqual(det.shape.points[1].x, -1)
        self.assertEqual(det.shape.points[1].y, 4)

    def points_outside_box_setup(self):
        det = BoxShapeDetection(box_x_min=-2, box_y_min=-1,
                                box_x_max=-1, box_y_max=1,
                                box_confidence=.5,
                                points_x=[-4, 0],
                                points_y=[-2, 2],
                                points_confidence=[.5, .5])
        return det

    def test_x_min_setter_points_outside_box(self):
        det = self.points_outside_box_setup()

        det.x_min = -8
        self.assertEqual(det.x_min, -8)
        self.assertEqual(det.y_min, -2)
        self.assertEqual(det.x_max, 0)
        self.assertEqual(det.y_max, 2)

        self.assertEqual(det.box.x_min, -4)
        self.assertEqual(det.box.y_min, -1)
        self.assertEqual(det.box.x_max, -2)
        self.assertEqual(det.box.y_max, 1)

        self.assertEqual(det.shape.points[0].x, -8)
        self.assertEqual(det.shape.points[0].y, -2)
        self.assertEqual(det.shape.points[1].x, 0)
        self.assertEqual(det.shape.points[1].y, 2)

    def test_y_min_setter_points_outside_box(self):
        det = self.points_outside_box_setup()

        det.y_min = -6
        self.assertEqual(det.x_min, -4)
        self.assertEqual(det.y_min, -6)
        self.assertEqual(det.x_max, 0)
        self.assertEqual(det.y_max, 2)

        self.assertEqual(det.box.x_min, -2)
        self.assertEqual(det.box.y_min, -4)
        self.assertEqual(det.box.x_max, -1)
        self.assertEqual(det.box.y_max, 0)

        self.assertEqual(det.shape.points[0].x, -4)
        self.assertEqual(det.shape.points[0].y, -6)
        self.assertEqual(det.shape.points[1].x, 0)
        self.assertEqual(det.shape.points[1].y, 2)

    def test_x_max_setter_points_outside_box(self):
        det = self.points_outside_box_setup()

        det.x_max = 4
        self.assertEqual(det.x_min, -4)
        self.assertEqual(det.y_min, -2)
        self.assertEqual(det.x_max, 4)
        self.assertEqual(det.y_max, 2)

        self.assertEqual(det.box.x_min, 0)
        self.assertEqual(det.box.y_min, -1)
        self.assertEqual(det.box.x_max, 2)
        self.assertEqual(det.box.y_max, 1)

        self.assertEqual(det.shape.points[0].x, -4)
        self.assertEqual(det.shape.points[0].y, -2)
        self.assertEqual(det.shape.points[1].x, 4)
        self.assertEqual(det.shape.points[1].y, 2)

    def test_y_max_setter_points_outside_box(self):
        det = self.points_outside_box_setup()

        det.y_max = 6
        self.assertEqual(det.x_min, -4)
        self.assertEqual(det.y_min, -2)
        self.assertEqual(det.x_max, 0)
        self.assertEqual(det.y_max, 6)

        self.assertEqual(det.box.x_min, -2)
        self.assertEqual(det.box.y_min, 0)
        self.assertEqual(det.box.x_max, -1)
        self.assertEqual(det.box.y_max, 4)

        self.assertEqual(det.shape.points[0].x, -4)
        self.assertEqual(det.shape.points[0].y, -2)
        self.assertEqual(det.shape.points[1].x, 0)
        self.assertEqual(det.shape.points[1].y, 6)

    def test_get_shape_x_min(self):
        det = BoxShapeDetection(box_x_min=47, box_y_min=39,
                                box_x_max=136, box_y_max=165,
                                box_confidence=.5,
                                points_x=[83, 122, 103, 75, 110],
                                points_y=[84, 93, 115, 129, 138],
                                points_confidence=[.5, .5, .5, .5, .5])
        self.assertEqual(det.shape.x_min, 75)

    def test_set_center(self):
        det = BoxShapeDetection(box_x_min=47, box_y_min=39,
                                box_x_max=136, box_y_max=165,
                                box_confidence=.5,
                                points_x=[83, 122, 103, 75, 110],
                                points_y=[84, 93, 115, 129, 138],
                                points_confidence=[.5, .5, .5, .5, .5])
        det.center = (867, 127)

        self.assertEqual(tuple(det)[:-1], (822, 64, 911, 190))

    def test_add_tuple(self):
        det = BoxShapeDetection(box_x_min=47, box_y_min=39,
                                box_x_max=136, box_y_max=165,
                                box_confidence=.5,
                                points_x=[83, 122, 103, 75, 110],
                                points_y=[84, 93, 115, 129, 138],
                                points_confidence=[.5, .5, .5, .5, .5])
        det.__iadd__((775.0, 25.0))

        self.assertEqual(tuple(det)[:-1], (822, 64, 911, 190))


if __name__ == '__main__':
    unittest.main()
