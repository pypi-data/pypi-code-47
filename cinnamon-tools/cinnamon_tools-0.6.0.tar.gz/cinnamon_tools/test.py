import unittest

from cinnamon_tools.point import Point, Direction, zero_point


class TestPoint(unittest.TestCase):
    def test_addition(self):
        self.assertEqual(Point(1, 2, 3) + Point(1, 2, 3), Point(2, 4, 6))

    def test_subtraction(self):
        self.assertEqual(Point(1, 2, 3) - Point(1, 2, 3), Point(0, 0, 0))

    def test_multiplication(self):
        self.assertEqual(Point(1, 2, 3) * 2, Point(2, 4, 6))

    def test_reverse_multiplication(self):
        self.assertEqual(2 * Point(1, 2, 3), Point(2, 4, 6))

    def test_length(self):
        for size in range(10):
            with self.subTest(f'length of {size}'):
                self.assertEqual(size, len(zero_point(size)))


class TestDirection(unittest.TestCase):
    def test_simple_forwards(self):
        self.assertEqual(Direction.RIGHT, Direction.UP.next())

    def test_simple_backwards(self):
        self.assertEqual(Direction.UP, Direction.RIGHT.prev())

    def test_wrapped_forwards(self):
        self.assertEqual(Direction.UP, Direction.LEFT.next())

    def test_wrapped_backwards(self):
        self.assertEqual(Direction.LEFT, Direction.UP.prev())


if __name__ == '__main__':
    unittest.main()
