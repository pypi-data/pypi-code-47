# (C) British Crown Copyright 2014 - 2019, Met Office
#
# This file is part of Iris.
#
# Iris is free software: you can redistribute it and/or modify it under
# the terms of the GNU Lesser General Public License as published by the
# Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Iris is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with Iris.  If not, see <http://www.gnu.org/licenses/>.
"""
Test some key usages of :func:`iris.plot.quiver`.

"""

from __future__ import (absolute_import, division, print_function)
from six.moves import (filter, input, map, range, zip)  # noqa

# import iris tests first so that some things can be initialised before
# importing anything else
import iris.tests as tests

import numpy as np

import cartopy.crs as ccrs
from iris.coords import AuxCoord, DimCoord
from iris.coord_systems import Mercator
from iris.cube import Cube
from iris.tests.stock import sample_2d_latlons

# Run tests in no graphics mode if matplotlib is not available.
if tests.MPL_AVAILABLE:
    import matplotlib.pyplot as plt
    from iris.plot import quiver


@tests.skip_plot
class MixinVectorPlotCases(object):
    """
    Test examples mixin, used by separate quiver + streamplot classes.

    NOTE: at present for quiver only, as streamplot does not support arbitrary
    coordinates.

    """

    def plot(self, plotname, *args, **kwargs):
        plot_function = self.plot_function_to_test()
        plot_function(*args, **kwargs)
        plt.suptitle(plotname)

    @staticmethod
    def _nonlatlon_xyuv():
        # Create common x, y, u, v arrays for quiver/streamplot testing.
        x = np.array([0., 2, 3, 5])
        y = np.array([0., 2.5, 4])
        uv = np.array([[(0., 0), (0, 1), (0, -1), (2, 1)],
                       [(-1, 0), (-1, -1), (-1, 1), (-2, 1)],
                       [(1., 0), (1, -1), (1, 1), (-2, 2)]])
        uv = np.array(uv)
        u, v = uv[..., 0], uv[..., 1]
        return x, y, u, v

    @staticmethod
    def _nonlatlon_uv_cubes(x, y, u, v):
        # Create u and v test cubes from x, y, u, v arrays.
        coord_cls = DimCoord if x.ndim == 1 else AuxCoord
        x_coord = coord_cls(x, long_name='x')
        y_coord = coord_cls(y, long_name='y')
        u_cube = Cube(u, long_name='u', units='ms-1')
        if x.ndim == 1:
            u_cube.add_dim_coord(y_coord, 0)
            u_cube.add_dim_coord(x_coord, 1)
        else:
            u_cube.add_aux_coord(y_coord, (0, 1))
            u_cube.add_aux_coord(x_coord, (0, 1))
        v_cube = u_cube.copy()
        v_cube.rename('v')
        v_cube.data = v
        return u_cube, v_cube

    def test_non_latlon_1d_coords(self):
        # Plot against simple 1D x and y coords.
        x, y, u, v = self._nonlatlon_xyuv()
        u_cube, v_cube = self._nonlatlon_uv_cubes(x, y, u, v)
        self.plot('nonlatlon, 1-d coords', u_cube, v_cube)
        plt.xlim(x.min() - 1, x.max() + 2)
        plt.ylim(y.min() - 1, y.max() + 2)
        self.check_graphic()

    def test_non_latlon_2d_coords(self):
        # Plot against expanded 2D x and y coords.
        x, y, u, v = self._nonlatlon_xyuv()
        x, y = np.meshgrid(x, y)
        u_cube, v_cube = self._nonlatlon_uv_cubes(x, y, u, v)
        # Call plot : N.B. default gives wrong coords order.
        self.plot('nonlatlon_2d', u_cube, v_cube, coords=('x', 'y'))
        plt.xlim(x.min() - 1, x.max() + 2)
        plt.ylim(y.min() - 1, y.max() + 2)
        self.check_graphic()

    @staticmethod
    def _latlon_uv_cubes(grid_cube):
        # Make a sample grid into u and v data for quiver/streamplot testing.
        u_cube = grid_cube.copy()
        u_cube.rename('dx')
        u_cube.units = 'ms-1'
        v_cube = u_cube.copy()
        v_cube.rename('dy')
        ny, nx = u_cube.shape
        nn = nx * ny
        angles = np.arange(nn).reshape((ny, nx))
        angles = (angles * 360.0 / 5.5) % 360.
        scale = np.arange(nn) % 5
        scale = (scale + 4) / 4
        scale = scale.reshape((ny, nx))
        u_cube.data = scale * np.cos(np.deg2rad(angles))
        v_cube.data = scale * np.sin(np.deg2rad(angles))
        return u_cube, v_cube

    def test_2d_plain_latlon(self):
        # Test 2d vector plotting with implicit (PlateCarree) coord system.
        u_cube, v_cube = self._latlon_uv_cubes(sample_2d_latlons())
        ax = plt.axes(projection=ccrs.PlateCarree(central_longitude=180))
        self.plot('latlon_2d', u_cube, v_cube,
                  coords=('longitude', 'latitude'))
        ax.coastlines(color='red')
        ax.set_global()
        self.check_graphic()

    def test_2d_plain_latlon_on_polar_map(self):
        # Test 2d vector plotting onto a different projection.
        u_cube, v_cube = self._latlon_uv_cubes(sample_2d_latlons())
        ax = plt.axes(projection=ccrs.NorthPolarStereo())
        self.plot('latlon_2d_polar', u_cube, v_cube,
                  coords=('longitude', 'latitude'))
        ax.coastlines(color='red')
        self.check_graphic()

    def test_2d_rotated_latlon(self):
        # Test plotting vectors in a rotated latlon coord system.
        u_cube, v_cube = self._latlon_uv_cubes(
            sample_2d_latlons(rotated=True))
        ax = plt.axes(projection=ccrs.PlateCarree(central_longitude=180))
        self.plot('2d_rotated', u_cube, v_cube,
                  coords=('longitude', 'latitude'))
        ax.coastlines(color='red')
        ax.set_global()
        self.check_graphic()

    def test_fail_unsupported_coord_system(self):
        # Test plotting vectors in a rotated latlon coord system.
        u_cube, v_cube = self._latlon_uv_cubes(sample_2d_latlons())
        patch_coord_system = Mercator()
        for cube in u_cube, v_cube:
            for coord in cube.coords():
                coord.coord_system = patch_coord_system
        re_msg = ('Can only plot .* lat-lon projection, .* '
                  'This .* translates as Cartopy.*Mercator')
        with self.assertRaisesRegexp(ValueError, re_msg):
            self.plot('2d_rotated', u_cube, v_cube,
                      coords=('longitude', 'latitude'))

    def test_circular_longitude(self):
        # Test circular longitude does not cause a crash.
        res = 5
        lat = DimCoord(np.arange(-90, 91, res), 'latitude',
                       units='degrees_north')
        lon = DimCoord(np.arange(0, 360, res), 'longitude',
                       units='degrees_east', circular=True)
        nlat = len(lat.points)
        nlon = len(lon.points)
        u_arr = np.ones((nlat, nlon))
        v_arr = np.ones((nlat, nlon))
        u_cube = Cube(u_arr, dim_coords_and_dims=[(lat, 0), (lon, 1)],
                      standard_name='eastward_wind')
        v_cube = Cube(v_arr, dim_coords_and_dims=[(lat, 0), (lon, 1)],
                      standard_name='northward_wind')

        self.plot('circular', u_cube, v_cube,
                  coords=('longitude', 'latitude'))


class TestQuiver(MixinVectorPlotCases, tests.GraphicsTest):
    def setUp(self):
        super(TestQuiver, self).setUp()

    def plot_function_to_test(self):
        return quiver


if __name__ == "__main__":
    tests.main()
