#!/usr/bin/env/python
import unittest
from color import Color


class ColorTestCase(unittest.TestCase):
    def test_rgb_init(self):
        color = Color((255, 255, 0))
        self.assertEquals(color._rgba, (1, 1, 0, 1))
