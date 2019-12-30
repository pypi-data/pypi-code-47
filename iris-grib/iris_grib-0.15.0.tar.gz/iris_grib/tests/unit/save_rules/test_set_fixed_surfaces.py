# Copyright iris-grib contributors
#
# This file is part of iris-grib and is released under the LGPL license.
# See COPYING and COPYING.LESSER in the root of the repository for full
# licensing details.
"""
Unit tests for :func:`iris_grib._save_rules.set_fixed_surfaces`.

"""

# Import iris_grib.tests first so that some things can be initialised before
# importing anything else.
import iris_grib.tests as tests

import gribapi
import numpy as np

import iris.cube
import iris.coords

from iris_grib._save_rules import set_fixed_surfaces


class Test(tests.IrisGribTest):
    def test_bounded_altitude_feet(self):
        cube = iris.cube.Cube([0])
        cube.add_aux_coord(iris.coords.AuxCoord(
            1500.0, long_name='altitude', units='ft',
            bounds=np.array([1000.0, 2000.0])))
        grib = gribapi.grib_new_from_samples("GRIB2")
        set_fixed_surfaces(cube, grib)
        self.assertEqual(
            gribapi.grib_get_double(grib, "scaledValueOfFirstFixedSurface"),
            304.0)
        self.assertEqual(
            gribapi.grib_get_double(grib, "scaledValueOfSecondFixedSurface"),
            609.0)
        self.assertEqual(
            gribapi.grib_get_long(grib, "typeOfFirstFixedSurface"),
            102)
        self.assertEqual(
            gribapi.grib_get_long(grib, "typeOfSecondFixedSurface"),
            102)

    def test_theta_level(self):
        cube = iris.cube.Cube([0])
        cube.add_aux_coord(iris.coords.AuxCoord(
            230.0, standard_name='air_potential_temperature',
            units='K', attributes={'positive': 'up'},
            bounds=np.array([220.0, 240.0])))
        grib = gribapi.grib_new_from_samples("GRIB2")
        set_fixed_surfaces(cube, grib)
        self.assertEqual(
            gribapi.grib_get_double(grib, "scaledValueOfFirstFixedSurface"),
            220.0)
        self.assertEqual(
            gribapi.grib_get_double(grib, "scaledValueOfSecondFixedSurface"),
            240.0)
        self.assertEqual(
            gribapi.grib_get_long(grib, "typeOfFirstFixedSurface"),
            107)
        self.assertEqual(
            gribapi.grib_get_long(grib, "typeOfSecondFixedSurface"),
            107)

    def test_depth(self):
        cube = iris.cube.Cube([0])
        cube.add_aux_coord(iris.coords.AuxCoord(
            1, long_name='depth', units='m',
            bounds=np.array([0., 2]), attributes={'positive': 'down'}))
        grib = gribapi.grib_new_from_samples("GRIB2")
        set_fixed_surfaces(cube, grib)
        self.assertEqual(
            gribapi.grib_get_double(grib, "scaledValueOfFirstFixedSurface"),
            0.)
        self.assertEqual(
            gribapi.grib_get_double(grib, "scaledValueOfSecondFixedSurface"),
            2)
        self.assertEqual(
            gribapi.grib_get_long(grib, "typeOfFirstFixedSurface"),
            106)
        self.assertEqual(
            gribapi.grib_get_long(grib, "typeOfSecondFixedSurface"),
            106)


if __name__ == "__main__":
    tests.main()
