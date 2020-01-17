# -*- coding: utf-8 -*-
"""Rubix :class:`Cube <rubix_cube.cube.Cube` class :mod:`tests` Module

Module Description
==================


Module Contents
===============

.. moduleauthor:: David Grethlein <djg329@drexel.edu>

"""

import unittest

from ..cube import Cube
from ..cube_game import Cube_Game


class TestCubeMethods(unittest.TestCase):

    def test_up(self):
        c = Cube()
        seq = Cube_Game.get_scramble_sequence()
        for mv in seq:
            c.manipulate_cube(mv)

        self.assertEqual('foo'.upper(), 'FOO')


    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)

if __name__ == '__main__':
    unittest.main()