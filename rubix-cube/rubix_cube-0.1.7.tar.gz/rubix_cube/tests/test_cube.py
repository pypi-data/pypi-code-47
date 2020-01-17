# -*- coding: utf-8 -*-
"""Rubix :class:`Cube <rubix_cube.cube.Cube` class :mod:`tests` Module

Module Description
==================


Module Contents
===============

.. moduleauthor:: David Grethlein <djg329@drexel.edu>

"""

import unittest
import copy

from ..cube_game import Cube_Game


class TestCubeGameMethods(unittest.TestCase):

    def test_up(self):
        cg = Cube_Game()
        seq = Cube_Game.get_scramble_sequence()
        for mv in seq:
            cg.manipulate_cube(mv)

        copy_cube = copy.deepcopy(cg.game_cube)
        cg.manipulate_cube('U')
        cg.manipulate_cube('Ui')
        self.assertEqual(copy_cube , cg.game_cube)


    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)

if __name__ == '__main__':
    unittest.main()