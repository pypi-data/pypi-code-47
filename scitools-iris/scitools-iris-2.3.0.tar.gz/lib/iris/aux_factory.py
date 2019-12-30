# (C) British Crown Copyright 2010 - 2019, Met Office
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
Definitions of derived coordinates.

"""

from __future__ import (absolute_import, division, print_function)
from six.moves import (filter, input, map, range, zip)  # noqa
import six

from abc import ABCMeta, abstractmethod, abstractproperty
import warnings

import dask.array as da
import numpy as np

from iris._cube_coord_common import CFVariableMixin
import iris.coords


class AuxCoordFactory(six.with_metaclass(ABCMeta, CFVariableMixin)):
    """
    Represents a "factory" which can manufacture an additional auxiliary
    coordinate on demand, by combining the values of other coordinates.

    Each concrete subclass represents a specific formula for deriving
    values from other coordinates.

    The `standard_name`, `long_name`, `var_name`, `units`, `attributes` and
    `coord_system` of the factory are used to set the corresponding
    properties of the resulting auxiliary coordinates.

    """

    def __init__(self):
        #: Descriptive name of the coordinate made by the factory
        self.long_name = None

        #: netCDF variable name for the coordinate made by the factory
        self.var_name = None

        #: Coordinate system (if any) of the coordinate made by the factory
        self.coord_system = None

    @abstractproperty
    def dependencies(self):
        """
        Returns a dictionary mapping from constructor argument names to
        the corresponding coordinates.

        """

    def _as_defn(self):
        defn = iris.coords.CoordDefn(
            self.standard_name, self.long_name,
            self.var_name, self.units,
            self.attributes,
            self.coord_system,
            # Slot for Coord 'climatological' property, which this
            # doesn't have.
            False,)
        return defn

    @abstractmethod
    def make_coord(self, coord_dims_func):
        """
        Returns a new :class:`iris.coords.AuxCoord` as defined by this
        factory.

        Args:

        * coord_dims_func:
            A callable which can return the list of dimensions relevant
            to a given coordinate.
            See :meth:`iris.cube.Cube.coord_dims()`.

        """

    @abstractmethod
    def update(self, old_coord, new_coord=None):
        """
        Notifies the factory of a removal/replacement of a dependency.

        Args:

        * old_coord:
            The dependency coordinate to be removed/replaced.
        * new_coord:
            If None, the dependency using old_coord is removed, otherwise
            the dependency is updated to use new_coord.

        """

    def __repr__(self):
        def arg_text(item):
            key, coord = item
            return '{}={}'.format(key, str(coord and repr(coord.name())))
        items = sorted(self.dependencies.items(), key=lambda item: item[0])
        args = map(arg_text, items)
        return '<{}({})>'.format(type(self).__name__, ', '.join(args))

    def derived_dims(self, coord_dims_func):
        """
        Returns the cube dimensions for the derived coordinate.

        Args:

        * coord_dims_func:
            A callable which can return the list of dimensions relevant
            to a given coordinate.
            See :meth:`iris.cube.Cube.coord_dims()`.

        Returns:

            A sorted list of cube dimension numbers.

        """
        # Which dimensions are relevant?
        # e.g. If sigma -> [1] and orog -> [2, 3] then result = [1, 2, 3]
        derived_dims = set()
        for coord in six.itervalues(self.dependencies):
            if coord:
                derived_dims.update(coord_dims_func(coord))

        # Apply a fixed order so we know how to map dependency dims to
        # our own dims (and so the Cube can map them to Cube dims).
        derived_dims = tuple(sorted(derived_dims))
        return derived_dims

    def updated(self, new_coord_mapping):
        """
        Creates a new instance of this factory where the dependencies
        are replaced according to the given mapping.

        Args:

        * new_coord_mapping:
            A dictionary mapping from the object IDs potentially used
            by this factory, to the coordinate objects that should be
            used instead.

        """
        new_dependencies = {}
        for key, coord in six.iteritems(self.dependencies):
            if coord:
                coord = new_coord_mapping[id(coord)]
            new_dependencies[key] = coord
        return type(self)(**new_dependencies)

    def xml_element(self, doc):
        """
        Returns a DOM element describing this coordinate factory.

        """
        element = doc.createElement('coordFactory')
        for key, coord in six.iteritems(self.dependencies):
            element.setAttribute(key, coord._xml_id())
        element.appendChild(self.make_coord().xml_element(doc))
        return element

    def _dependency_dims(self, coord_dims_func):
        dependency_dims = {}
        for key, coord in six.iteritems(self.dependencies):
            if coord:
                dependency_dims[key] = coord_dims_func(coord)
        return dependency_dims

    @staticmethod
    def _nd_bounds(coord, dims, ndim):
        """
        Return a lazy bounds array for a dependency coordinate, 'coord'.

        The result is aligned to the first 'ndim' cube dimensions, and
        expanded to the full ('ndim'+1)-dimensional shape.

        The value of 'ndim' must be >= the highest cube dimension of the
        dependency coordinate.

        The extra final result dimension ('ndim'-th) is the bounds dimension.

        Example:
            coord.shape == (70,)
            coord.nbounds = 2
            dims == [3]
            ndim == 5
        results in:
            nd_bounds.shape == (1, 1, 1, 70, 1, 2)

        """
        # Transpose to be consistent with the Cube.
        sorted_pairs = sorted(enumerate(dims), key=lambda pair: pair[1])
        transpose_order = [pair[0] for pair in sorted_pairs] + [len(dims)]
        bounds = coord.lazy_bounds()
        if dims and transpose_order != list(range(len(dims))):
            bounds = bounds.transpose(transpose_order)

        # Figure out the n-dimensional shape.
        nd_shape = [1] * ndim + [coord.nbounds]
        for dim, size in zip(dims, coord.shape):
            nd_shape[dim] = size
        bounds = bounds.reshape(nd_shape)
        return bounds

    @staticmethod
    def _nd_points(coord, dims, ndim):
        """
        Return a lazy points array for a dependency coordinate, 'coord'.

        The result is aligned to the first 'ndim' cube dimensions, and
        expanded to the full 'ndim'-dimensional shape.

        The value of 'ndim' must be >= the highest cube dimension of the
        dependency coordinate.

        Example:
            coord.shape == (4, 3)
            dims == [3, 2]
            ndim == 5
        results in:
            nd_points.shape == (1, 1, 3, 4, 1)

        """
        # Transpose to be consistent with the Cube.
        sorted_pairs = sorted(enumerate(dims), key=lambda pair: pair[1])
        transpose_order = [pair[0] for pair in sorted_pairs]
        points = coord.lazy_points()
        if dims and transpose_order != list(range(len(dims))):
            points = points.transpose(transpose_order)

        # Expand dimensionality to be consistent with the Cube.
        if dims:
            keys = [None] * ndim
            for dim, size in zip(dims, coord.shape):
                keys[dim] = slice(None)
            points = points[tuple(keys)]
        else:
            # Scalar coordinates have one dimensional points despite
            # mapping to zero dimensions, so we only need to add N-1
            # new dimensions.
            keys = (None,) * (ndim - 1)
            points = points[keys]
        return points

    def _remap(self, dependency_dims, derived_dims):
        """
        Return a mapping from dependency names to coordinate points arrays.

        For dependencies that are present, the values are all expanded and
        aligned to the same dimensions, which is the full set of all the
        dependency dimensions.
        These non-missing values are all lazy arrays.
        Missing dependencies, however, are assigned a scalar value of 0.0.

        """
        if derived_dims:
            ndim = max(derived_dims) + 1
        else:
            ndim = 1

        nd_points_by_key = {}
        for key, coord in six.iteritems(self.dependencies):
            if coord:
                # Get the points as consistent with the Cube.
                nd_points = self._nd_points(coord, dependency_dims[key], ndim)

                # Restrict to just the dimensions relevant to the
                # derived coord. NB. These are always in Cube-order, so
                # no transpose is needed.
                if derived_dims:
                    keys = tuple(slice(None) if dim in derived_dims else 0 for
                                 dim in range(ndim))
                    nd_points = nd_points[keys]
            else:
                # If no coord, treat value as zero.
                # Use a float16 to provide `shape` attribute and avoid
                # promoting other arguments to a higher precision.
                nd_points = np.float16(0)

            nd_points_by_key[key] = nd_points
        return nd_points_by_key

    def _remap_with_bounds(self, dependency_dims, derived_dims):
        """
        Return a mapping from dependency names to coordinate bounds arrays.

        For dependencies that are present, the values are all expanded and
        aligned to the same dimensions, which is the full set of all the
        dependency dimensions, plus an extra bounds dimension.
        These non-missing values are all lazy arrays.
        Missing dependencies, however, are assigned a scalar value of 0.0.

        Where a dependency coordinate has no bounds, then the associated value
        is taken from its points array, but reshaped to have an extra bounds
        dimension of length 1.

        """
        if derived_dims:
            ndim = max(derived_dims) + 1
        else:
            ndim = 1

        nd_values_by_key = {}
        for key, coord in six.iteritems(self.dependencies):
            if coord:
                # Get the bounds or points as consistent with the Cube.
                if coord.nbounds:
                    nd_values = self._nd_bounds(coord, dependency_dims[key],
                                                ndim)
                else:
                    nd_values = self._nd_points(coord, dependency_dims[key],
                                                ndim)

                # Restrict to just the dimensions relevant to the
                # derived coord. NB. These are always in Cube-order, so
                # no transpose is needed.
                shape = []
                for dim in derived_dims:
                    shape.append(nd_values.shape[dim])
                # Ensure the array always has at least one dimension to be
                # compatible with normal coordinates.
                if not derived_dims:
                    shape.append(1)
                # Add on the N-bounds dimension
                if coord.nbounds:
                    shape.append(nd_values.shape[-1])
                else:
                    # NB. For a non-bounded coordinate we still need an
                    # extra dimension to make the shape compatible, so
                    # we just add an extra 1.
                    shape.append(1)
                nd_values = nd_values.reshape(shape)
            else:
                # If no coord, treat value as zero.
                # Use a float16 to provide `shape` attribute and avoid
                # promoting other arguments to a higher precision.
                nd_values = np.float16(0)

            nd_values_by_key[key] = nd_values
        return nd_values_by_key


class HybridHeightFactory(AuxCoordFactory):
    """
    Defines a hybrid-height coordinate factory with the formula:
        z = a + b * orog

    """
    def __init__(self, delta=None, sigma=None, orography=None):
        """
        Creates a hybrid-height coordinate factory with the formula:
            z = a + b * orog

        At least one of `delta` or `orography` must be provided.

        Args:

        * delta: Coord
            The coordinate providing the `a` term.
        * sigma: Coord
            The coordinate providing the `b` term.
        * orography: Coord
            The coordinate providing the `orog` term.

        """
        super(HybridHeightFactory, self).__init__()

        if delta and delta.nbounds not in (0, 2):
            raise ValueError('Invalid delta coordinate: must have either 0 or'
                             ' 2 bounds.')
        if sigma and sigma.nbounds not in (0, 2):
            raise ValueError('Invalid sigma coordinate: must have either 0 or'
                             ' 2 bounds.')
        if orography and orography.nbounds:
            msg = 'Orography coordinate {!r} has bounds.' \
                  ' These will be disregarded.'.format(orography.name())
            warnings.warn(msg, UserWarning, stacklevel=2)

        self.delta = delta
        self.sigma = sigma
        self.orography = orography

        self.standard_name = 'altitude'
        if delta is None and orography is None:
            raise ValueError('Unable to determine units: no delta or orography'
                             ' available.')
        if delta and orography and delta.units != orography.units:
            raise ValueError('Incompatible units: delta and orography must'
                             ' have the same units.')
        self.units = (delta and delta.units) or orography.units
        if not self.units.is_convertible('m'):
            raise ValueError('Invalid units: delta and/or orography'
                             ' must be expressed in length units.')
        self.attributes = {'positive': 'up'}

    @property
    def dependencies(self):
        """
        Returns a dictionary mapping from constructor argument names to
        the corresponding coordinates.

        """
        return {'delta': self.delta, 'sigma': self.sigma,
                'orography': self.orography}

    def _derive(self, delta, sigma, orography):
        return delta + sigma * orography

    def make_coord(self, coord_dims_func):
        """
        Returns a new :class:`iris.coords.AuxCoord` as defined by this
        factory.

        Args:

        * coord_dims_func:
            A callable which can return the list of dimensions relevant
            to a given coordinate.
            See :meth:`iris.cube.Cube.coord_dims()`.

        """
        # Which dimensions are relevant?
        derived_dims = self.derived_dims(coord_dims_func)
        dependency_dims = self._dependency_dims(coord_dims_func)

        # Build the points array.
        nd_points_by_key = self._remap(dependency_dims, derived_dims)
        points = self._derive(nd_points_by_key['delta'],
                              nd_points_by_key['sigma'],
                              nd_points_by_key['orography'])

        bounds = None
        if ((self.delta and self.delta.nbounds) or
                (self.sigma and self.sigma.nbounds)):
            # Build the bounds array.
            nd_values_by_key = self._remap_with_bounds(dependency_dims,
                                                       derived_dims)
            delta = nd_values_by_key['delta']
            sigma = nd_values_by_key['sigma']
            orography = nd_values_by_key['orography']
            ok_bound_shapes = [(), (1,), (2,)]
            if delta.shape[-1:] not in ok_bound_shapes:
                raise ValueError('Invalid delta coordinate bounds.')
            if sigma.shape[-1:] not in ok_bound_shapes:
                raise ValueError('Invalid sigma coordinate bounds.')
            if orography.shape[-1:] not in [(), (1,)]:
                warnings.warn('Orography coordinate has bounds. '
                              'These are being disregarded.',
                              UserWarning, stacklevel=2)
                orography_pts = nd_points_by_key['orography']
                bds_shape = list(orography_pts.shape) + [1]
                orography = orography_pts.reshape(bds_shape)

            bounds = self._derive(delta, sigma, orography)

        hybrid_height = iris.coords.AuxCoord(points,
                                             standard_name=self.standard_name,
                                             long_name=self.long_name,
                                             var_name=self.var_name,
                                             units=self.units,
                                             bounds=bounds,
                                             attributes=self.attributes,
                                             coord_system=self.coord_system)
        return hybrid_height

    def update(self, old_coord, new_coord=None):
        """
        Notifies the factory of the removal/replacement of a coordinate
        which might be a dependency.

        Args:

        * old_coord:
            The coordinate to be removed/replaced.
        * new_coord:
            If None, any dependency using old_coord is removed, otherwise
            any dependency using old_coord is updated to use new_coord.

        """
        if self.delta is old_coord:
            if new_coord and new_coord.nbounds not in (0, 2):
                raise ValueError('Invalid delta coordinate:'
                                 ' must have either 0 or 2 bounds.')
            self.delta = new_coord
        elif self.sigma is old_coord:
            if new_coord and new_coord.nbounds not in (0, 2):
                raise ValueError('Invalid sigma coordinate:'
                                 ' must have either 0 or 2 bounds.')
            self.sigma = new_coord
        elif self.orography is old_coord:
            if new_coord and new_coord.nbounds:
                msg = 'Orography coordinate {!r} has bounds.' \
                      ' These will be disregarded.'.format(new_coord.name())
                warnings.warn(msg, UserWarning, stacklevel=2)
            self.orography = new_coord


class HybridPressureFactory(AuxCoordFactory):
    """
    Defines a hybrid-pressure coordinate factory with the formula:
        p = ap + b * ps

    """
    def __init__(self, delta=None, sigma=None, surface_air_pressure=None):
        """
        Creates a hybrid-height coordinate factory with the formula:
            p = ap + b * ps

        At least one of `delta` or `surface_air_pressure` must be provided.

        Args:

        * delta: Coord
            The coordinate providing the `ap` term.
        * sigma: Coord
            The coordinate providing the `b` term.
        * surface_air_pressure: Coord
            The coordinate providing the `ps` term.

        """
        super(HybridPressureFactory, self).__init__()

        # Check that provided coords meet necessary conditions.
        self._check_dependencies(delta, sigma, surface_air_pressure)

        self.delta = delta
        self.sigma = sigma
        self.surface_air_pressure = surface_air_pressure

        self.standard_name = 'air_pressure'
        self.attributes = {}

    @property
    def units(self):
        if self.delta is not None:
            units = self.delta.units
        else:
            units = self.surface_air_pressure.units
        return units

    @staticmethod
    def _check_dependencies(delta, sigma,
                            surface_air_pressure):
        # Check for sufficient coordinates.
        if (delta is None and (sigma is None or
                               surface_air_pressure is None)):
            msg = 'Unable to contruct hybrid pressure coordinate factory ' \
                  'due to insufficient source coordinates.'
            raise ValueError(msg)

        # Check bounds.
        if delta and delta.nbounds not in (0, 2):
            raise ValueError('Invalid delta coordinate: must have either 0 or'
                             ' 2 bounds.')
        if sigma and sigma.nbounds not in (0, 2):
            raise ValueError('Invalid sigma coordinate: must have either 0 or'
                             ' 2 bounds.')
        if surface_air_pressure and surface_air_pressure.nbounds:
            msg = 'Surface pressure coordinate {!r} has bounds. These will' \
                  ' be disregarded.'.format(surface_air_pressure.name())
            warnings.warn(msg, UserWarning, stacklevel=2)

        # Check units.
        if sigma is not None and not sigma.units.is_dimensionless():
            raise ValueError('Invalid units: sigma must be dimensionless.')
        if delta is not None and surface_air_pressure is not None and \
                delta.units != surface_air_pressure.units:
            msg = 'Incompatible units: delta and ' \
                  'surface_air_pressure must have the same units.'
            raise ValueError(msg)

        if delta is not None:
            units = delta.units
        else:
            units = surface_air_pressure.units

        if not units.is_convertible('Pa'):
            msg = 'Invalid units: delta and ' \
                'surface_air_pressure must have units of pressure.'
            raise ValueError(msg)

    @property
    def dependencies(self):
        """
        Returns a dictionary mapping from constructor argument names to
        the corresponding coordinates.

        """
        return {'delta': self.delta, 'sigma': self.sigma,
                'surface_air_pressure': self.surface_air_pressure}

    def _derive(self, delta, sigma, surface_air_pressure):
        return delta + sigma * surface_air_pressure

    def make_coord(self, coord_dims_func):
        """
        Returns a new :class:`iris.coords.AuxCoord` as defined by this
        factory.

        Args:

        * coord_dims_func:
            A callable which can return the list of dimensions relevant
            to a given coordinate.
            See :meth:`iris.cube.Cube.coord_dims()`.

        """
        # Which dimensions are relevant?
        derived_dims = self.derived_dims(coord_dims_func)
        dependency_dims = self._dependency_dims(coord_dims_func)

        # Build the points array.
        nd_points_by_key = self._remap(dependency_dims, derived_dims)
        points = self._derive(nd_points_by_key['delta'],
                              nd_points_by_key['sigma'],
                              nd_points_by_key['surface_air_pressure'])

        bounds = None
        if ((self.delta and self.delta.nbounds) or
                (self.sigma and self.sigma.nbounds)):
            # Build the bounds array.
            nd_values_by_key = self._remap_with_bounds(dependency_dims,
                                                       derived_dims)
            delta = nd_values_by_key['delta']
            sigma = nd_values_by_key['sigma']
            surface_air_pressure = nd_values_by_key['surface_air_pressure']
            ok_bound_shapes = [(), (1,), (2,)]
            if delta.shape[-1:] not in ok_bound_shapes:
                raise ValueError('Invalid delta coordinate bounds.')
            if sigma.shape[-1:] not in ok_bound_shapes:
                raise ValueError('Invalid sigma coordinate bounds.')
            if surface_air_pressure.shape[-1:] not in [(), (1,)]:
                warnings.warn('Surface pressure coordinate has bounds. '
                              'These are being disregarded.')
                surface_air_pressure_pts = nd_points_by_key[
                    'surface_air_pressure']
                bds_shape = list(surface_air_pressure_pts.shape) + [1]
                surface_air_pressure = surface_air_pressure_pts.reshape(
                    bds_shape)

            bounds = self._derive(delta, sigma, surface_air_pressure)

        hybrid_pressure = iris.coords.AuxCoord(
            points, standard_name=self.standard_name, long_name=self.long_name,
            var_name=self.var_name, units=self.units, bounds=bounds,
            attributes=self.attributes, coord_system=self.coord_system)
        return hybrid_pressure

    def update(self, old_coord, new_coord=None):
        """
        Notifies the factory of the removal/replacement of a coordinate
        which might be a dependency.

        Args:

        * old_coord:
            The coordinate to be removed/replaced.
        * new_coord:
            If None, any dependency using old_coord is removed, otherwise
            any dependency using old_coord is updated to use new_coord.

        """
        new_dependencies = self.dependencies
        for name, coord in self.dependencies.items():
            if old_coord is coord:
                new_dependencies[name] = new_coord
                try:
                    self._check_dependencies(**new_dependencies)
                except ValueError as e:
                    msg = 'Failed to update dependencies. ' + str(e)
                    raise ValueError(msg)
                else:
                    setattr(self, name, new_coord)
                break


class OceanSigmaZFactory(AuxCoordFactory):
    """Defines an ocean sigma over z coordinate factory."""

    def __init__(self, sigma=None, eta=None, depth=None,
                 depth_c=None, nsigma=None, zlev=None):
        """
        Creates a ocean sigma over z coordinate factory with the formula:

        if k < nsigma:
            z(n, k, j, i) = eta(n, j, i) + sigma(k) *
                             (min(depth_c, depth(j, i)) + eta(n, j, i))

        if k >= nsigma:
            z(n, k, j, i) = zlev(k)

        The `zlev` and 'nsigma' coordinates must be provided, and at least
        either `eta`, or 'sigma' and `depth` and `depth_c` coordinates.

        """
        super(OceanSigmaZFactory, self).__init__()

        # Check that provided coordinates meet necessary conditions.
        self._check_dependencies(sigma, eta, depth, depth_c, nsigma, zlev)

        self.sigma = sigma
        self.eta = eta
        self.depth = depth
        self.depth_c = depth_c
        self.nsigma = nsigma
        self.zlev = zlev

        self.standard_name = 'sea_surface_height_above_reference_ellipsoid'
        self.attributes = {'positive': 'up'}

    @property
    def units(self):
        return self.zlev.units

    @staticmethod
    def _check_dependencies(sigma, eta, depth, depth_c, nsigma, zlev):
        # Check for sufficient factory coordinates.
        if zlev is None:
            raise ValueError('Unable to determine units: '
                             'no zlev coordinate available.')
        if nsigma is None:
            raise ValueError('Missing nsigma coordinate.')

        if eta is None and (sigma is None or depth_c is None or
                            depth is None):
            msg = 'Unable to construct ocean sigma over z coordinate ' \
                'factory due to insufficient source coordinates.'
            raise ValueError(msg)

        # Check bounds and shape.
        for coord, term in ((sigma, 'sigma'), (zlev, 'zlev')):
            if coord is not None and coord.nbounds not in (0, 2):
                msg = 'Invalid {} coordinate {!r}: must have either ' \
                    '0 or 2 bounds.'.format(term, coord.name())
                raise ValueError(msg)

        if sigma and sigma.nbounds != zlev.nbounds:
            msg = 'The sigma coordinate {!r} and zlev coordinate {!r} ' \
                'must be equally bounded.'.format(sigma.name(), zlev.name())
            raise ValueError(msg)

        coords = ((eta, 'eta'), (depth, 'depth'),
                  (depth_c, 'depth_c'), (nsigma, 'nsigma'))
        for coord, term in coords:
            if coord is not None and coord.nbounds:
                msg = 'The {} coordinate {!r} has bounds. ' \
                    'These are being disregarded.'.format(term, coord.name())
                warnings.warn(msg, UserWarning, stacklevel=2)

        for coord, term in ((depth_c, 'depth_c'), (nsigma, 'nsigma')):
            if coord is not None and coord.shape != (1,):
                msg = 'Expected scalar {} coordinate {!r}: ' \
                    'got shape {!r}.'.format(term, coord.name(), coord.shape)
                raise ValueError(msg)

        # Check units.
        if not zlev.units.is_convertible('m'):
            msg = 'Invalid units: zlev coordinate {!r} ' \
                'must have units of distance.'.format(zlev.name())
            raise ValueError(msg)

        if sigma is not None and not sigma.units.is_dimensionless():
            msg = 'Invalid units: sigma coordinate {!r} ' \
                'must be dimensionless.'.format(sigma.name())
            raise ValueError(msg)

        coords = ((eta, 'eta'), (depth_c, 'depth_c'), (depth, 'depth'))
        for coord, term in coords:
            if coord is not None and coord.units != zlev.units:
                msg = 'Incompatible units: {} coordinate {!r} and zlev ' \
                    'coordinate {!r} must have ' \
                    'the same units.'.format(term, coord.name(), zlev.name())
                raise ValueError(msg)

    @property
    def dependencies(self):
        """
        Returns a dictionary mapping from constructor argument names to
        the corresponding coordinates.

        """
        return dict(sigma=self.sigma, eta=self.eta, depth=self.depth,
                    depth_c=self.depth_c, nsigma=self.nsigma, zlev=self.zlev)

    def _derive(self, sigma, eta, depth, depth_c,
                zlev, nsigma, coord_dims_func):
        # Calculate the index of the 'z' dimension in the input arrays.
        # First find the cube 'z' dimension ...
        [cube_z_dim] = coord_dims_func(self.dependencies['zlev'])
        # ... then calculate the corresponding dependency dimension.
        derived_cubedims = self.derived_dims(coord_dims_func)
        z_dim = derived_cubedims.index(cube_z_dim)

        # Calculate the result shape as a combination of all the inputs.
        # Note: all the inputs have the same number of dimensions >= 1, except
        # for any missing dependencies, which have scalar values.
        allshapes = np.array(
            [el.shape
             for el in (sigma, eta, depth, depth_c, zlev)
             if el.ndim > 0])
        result_shape = list(np.max(allshapes, axis=0))
        ndims = len(result_shape)

        # Make a slice tuple to index the first nsigma z-levels.
        z_slices_nsigma = [slice(None)] * ndims
        z_slices_nsigma[z_dim] = slice(0, int(nsigma))
        z_slices_nsigma = tuple(z_slices_nsigma)
        # Make a slice tuple to index the remaining z-levels.
        z_slices_rest = [slice(None)] * ndims
        z_slices_rest[z_dim] = slice(int(nsigma), None)
        z_slices_rest = tuple(z_slices_rest)

        # Perform the ocean sigma over z coordinate nsigma slice.
        if eta.ndim:
            eta = eta[z_slices_nsigma]
        if sigma.ndim:
            sigma = sigma[z_slices_nsigma]
        if depth.ndim:
            depth = depth[z_slices_nsigma]
        # Note that, this performs a point-wise minimum.
        nsigma_levs = eta + sigma * (da.minimum(depth_c, depth) + eta)

        # Make a result-shaped lazy "ones" array for expanding partial results.
        # Note: for the 'chunks' arg, we try to use [1, 1, ... ny, nx].
        # This calculation could be assuming too much in some cases, as we
        # don't actually check the dimensions of our dependencies anywhere.
        result_chunks = result_shape
        if len(result_shape) > 1:
            result_chunks = [1] * len(result_shape)
            result_chunks[-2:] = result_shape[-2:]
        ones_full_result = da.ones(result_shape, chunks=result_chunks,
                                   dtype=zlev.dtype)

        # Expand nsigma_levs to its full required shape : needed as the
        # calculated result may have a fixed size of 1 in some dimensions.
        result_nsigma_levs = nsigma_levs * ones_full_result[z_slices_nsigma]

        # Likewise, expand zlev to its full required shape.
        result_rest_levs = (zlev[z_slices_rest] *
                            ones_full_result[z_slices_rest])

        # Combine nsigma and 'rest' levels for the final result.
        result = da.concatenate([result_nsigma_levs, result_rest_levs],
                                axis=z_dim)
        return result

    def make_coord(self, coord_dims_func):
        """
        Returns a new :class:`iris.coords.AuxCoord` as defined by this factory.

        Args:

        * coord_dims_func:
            A callable which can return the list of dimesions relevant
            to a given coordinate. See :meth:`iris.cube.Cube.coord_dims()`.

        """
        # Determine the relevant dimensions.
        derived_dims = self.derived_dims(coord_dims_func)
        dependency_dims = self._dependency_dims(coord_dims_func)

        # Build the points array.
        nd_points_by_key = self._remap(dependency_dims, derived_dims)

        [nsigma] = nd_points_by_key['nsigma']
        points = self._derive(nd_points_by_key['sigma'],
                              nd_points_by_key['eta'],
                              nd_points_by_key['depth'],
                              nd_points_by_key['depth_c'],
                              nd_points_by_key['zlev'],
                              nsigma,
                              coord_dims_func)

        bounds = None
        if self.zlev.nbounds or (self.sigma and self.sigma.nbounds):
            # Build the bounds array.
            nd_values_by_key = self._remap_with_bounds(dependency_dims,
                                                       derived_dims)
            valid_shapes = [(), (1,), (2,)]
            for key in ('sigma', 'zlev'):
                if nd_values_by_key[key].shape[-1:] not in valid_shapes:
                    name = self.dependencies[key].name()
                    msg = 'Invalid bounds for {} ' \
                        'coordinate {!r}.'.format(key, name)
                    raise ValueError(msg)
            valid_shapes.pop()
            for key in ('eta', 'depth', 'depth_c', 'nsigma'):
                if nd_values_by_key[key].shape[-1:] not in valid_shapes:
                    name = self.dependencies[key].name()
                    msg = 'The {} coordinate {!r} has bounds. ' \
                        'These are being disregarded.'.format(key, name)
                    warnings.warn(msg, UserWarning, stacklevel=2)
                    # Swap bounds with points.
                    bds_shape = list(nd_points_by_key[key].shape) + [1]
                    bounds = nd_points_by_key[key].reshape(bds_shape)
                    nd_values_by_key[key] = bounds

            bounds = self._derive(nd_values_by_key['sigma'],
                                  nd_values_by_key['eta'],
                                  nd_values_by_key['depth'],
                                  nd_values_by_key['depth_c'],
                                  nd_values_by_key['zlev'],
                                  nsigma,
                                  coord_dims_func)

        coord = iris.coords.AuxCoord(points,
                                     standard_name=self.standard_name,
                                     long_name=self.long_name,
                                     var_name=self.var_name,
                                     units=self.units,
                                     bounds=bounds,
                                     attributes=self.attributes,
                                     coord_system=self.coord_system)
        return coord

    def update(self, old_coord, new_coord=None):
        """
        Notifies the factory of the removal/replacement of a coordinate
        which might be a dependency.

        Args:

        * old_coord:
            The coordinate to be removed/replaced.
        * new_coord:
            If None, any dependency using old_coord is removed, otherwise
            any dependency using old_coord is updated to use new_coord.

        """
        new_dependencies = self.dependencies
        for name, coord in self.dependencies.items():
            if old_coord is coord:
                new_dependencies[name] = new_coord
                try:
                    self._check_dependencies(**new_dependencies)
                except ValueError as e:
                    msg = 'Failed to update dependencies. ' + str(e)
                    raise ValueError(msg)
                else:
                    setattr(self, name, new_coord)
                break


class OceanSigmaFactory(AuxCoordFactory):
    """Defines an ocean sigma coordinate factory."""

    def __init__(self, sigma=None, eta=None, depth=None):
        """
        Creates an ocean sigma coordinate factory with the formula:

        z(n, k, j, i) = eta(n, j, i) + sigma(k) *
                        (depth(j, i) + eta(n, j, i))

        """
        super(OceanSigmaFactory, self).__init__()

        # Check that provided coordinates meet necessary conditions.
        self._check_dependencies(sigma, eta, depth)

        self.sigma = sigma
        self.eta = eta
        self.depth = depth

        self.standard_name = 'sea_surface_height_above_reference_ellipsoid'
        self.attributes = {'positive': 'up'}

    @property
    def units(self):
        return self.depth.units

    @staticmethod
    def _check_dependencies(sigma, eta, depth):
        # Check for sufficient factory coordinates.
        if eta is None or sigma is None or depth is None:
            msg = 'Unable to construct ocean sigma coordinate ' \
                'factory due to insufficient source coordinates.'
            raise ValueError(msg)

        # Check bounds and shape.
        coord, term = (sigma, 'sigma')
        if coord is not None and coord.nbounds not in (0, 2):
            msg = 'Invalid {} coordinate {!r}: must have either ' \
                  '0 or 2 bounds.'.format(term, coord.name())
            raise ValueError(msg)

        coords = ((eta, 'eta'), (depth, 'depth'))
        for coord, term in coords:
            if coord is not None and coord.nbounds:
                msg = 'The {} coordinate {!r} has bounds. ' \
                    'These are being disregarded.'.format(term, coord.name())
                warnings.warn(msg, UserWarning, stacklevel=2)

        # Check units.
        if sigma is not None and not sigma.units.is_dimensionless():
            msg = 'Invalid units: sigma coordinate {!r} ' \
                'must be dimensionless.'.format(sigma.name())
            raise ValueError(msg)

        coords = ((eta, 'eta'), (depth, 'depth'))
        for coord, term in coords:
            if coord is not None and coord.units != depth.units:
                msg = 'Incompatible units: {} coordinate {!r} and depth ' \
                    'coordinate {!r} must have ' \
                    'the same units.'.format(term, coord.name(), depth.name())
                raise ValueError(msg)

    @property
    def dependencies(self):
        """
        Returns a dictionary mapping from constructor argument names to
        the corresponding coordinates.

        """
        return dict(sigma=self.sigma, eta=self.eta, depth=self.depth)

    def _derive(self, sigma, eta, depth):
        return eta + sigma * (depth + eta)

    def make_coord(self, coord_dims_func):
        """
        Returns a new :class:`iris.coords.AuxCoord` as defined by this factory.

        Args:

        * coord_dims_func:
            A callable which can return the list of dimensions relevant
            to a given coordinate. See :meth:`iris.cube.Cube.coord_dims()`.

        """
        # Determine the relevant dimensions.
        derived_dims = self.derived_dims(coord_dims_func)
        dependency_dims = self._dependency_dims(coord_dims_func)

        # Build the points array.
        nd_points_by_key = self._remap(dependency_dims, derived_dims)
        points = self._derive(nd_points_by_key['sigma'],
                              nd_points_by_key['eta'],
                              nd_points_by_key['depth'])

        bounds = None
        if self.sigma and self.sigma.nbounds:
            # Build the bounds array.
            nd_values_by_key = self._remap_with_bounds(dependency_dims,
                                                       derived_dims)
            valid_shapes = [(), (1,), (2,)]
            key = 'sigma'
            if nd_values_by_key[key].shape[-1:] not in valid_shapes:
                name = self.dependencies[key].name()
                msg = 'Invalid bounds for {} ' \
                    'coordinate {!r}.'.format(key, name)
                raise ValueError(msg)
            valid_shapes.pop()
            for key in ('eta', 'depth'):
                if nd_values_by_key[key].shape[-1:] not in valid_shapes:
                    name = self.dependencies[key].name()
                    msg = 'The {} coordinate {!r} has bounds. ' \
                        'These are being disregarded.'.format(key, name)
                    warnings.warn(msg, UserWarning, stacklevel=2)
                    # Swap bounds with points.
                    bds_shape = list(nd_points_by_key[key].shape) + [1]
                    bounds = nd_points_by_key[key].reshape(bds_shape)
                    nd_values_by_key[key] = bounds

            bounds = self._derive(nd_values_by_key['sigma'],
                                  nd_values_by_key['eta'],
                                  nd_values_by_key['depth'])

        coord = iris.coords.AuxCoord(points,
                                     standard_name=self.standard_name,
                                     long_name=self.long_name,
                                     var_name=self.var_name,
                                     units=self.units,
                                     bounds=bounds,
                                     attributes=self.attributes,
                                     coord_system=self.coord_system)
        return coord

    def update(self, old_coord, new_coord=None):
        """
        Notifies the factory of the removal/replacement of a coordinate
        which might be a dependency.

        Args:

        * old_coord:
            The coordinate to be removed/replaced.
        * new_coord:
            If None, any dependency using old_coord is removed, otherwise
            any dependency using old_coord is updated to use new_coord.

        """
        new_dependencies = self.dependencies
        for name, coord in self.dependencies.items():
            if old_coord is coord:
                new_dependencies[name] = new_coord
                try:
                    self._check_dependencies(**new_dependencies)
                except ValueError as e:
                    msg = 'Failed to update dependencies. ' + str(e)
                    raise ValueError(msg)
                else:
                    setattr(self, name, new_coord)
                break


class OceanSg1Factory(AuxCoordFactory):
    """Defines an Ocean s-coordinate, generic form 1 factory."""

    def __init__(self, s=None, c=None, eta=None, depth=None, depth_c=None):
        """
        Creates an Ocean s-coordinate, generic form 1 factory with the formula:

        z(n,k,j,i) = S(k,j,i) + eta(n,j,i) * (1 + S(k,j,i) / depth(j,i))

        where:
            S(k,j,i) = depth_c * s(k) + (depth(j,i) - depth_c) * C(k)

        """
        super(OceanSg1Factory, self).__init__()

        # Check that provided coordinates meet necessary conditions.
        self._check_dependencies(s, c, eta, depth, depth_c)

        self.s = s
        self.c = c
        self.eta = eta
        self.depth = depth
        self.depth_c = depth_c

        self.standard_name = 'sea_surface_height_above_reference_ellipsoid'
        self.attributes = {'positive': 'up'}

    @property
    def units(self):
        return self.depth.units

    @staticmethod
    def _check_dependencies(s, c, eta, depth, depth_c):
        # Check for sufficient factory coordinates.
        if (eta is None or s is None or c is None or
           depth is None or depth_c is None):
            msg = 'Unable to construct Ocean s-coordinate, generic form 1 ' \
                'factory due to insufficient source coordinates.'
            raise ValueError(msg)

        # Check bounds and shape.
        coords = ((s, 's'), (c, 'c'))
        for coord, term in coords:
            if coord is not None and coord.nbounds not in (0, 2):
                msg = 'Invalid {} coordinate {!r}: must have either ' \
                    '0 or 2 bounds.'.format(term, coord.name())
                raise ValueError(msg)

        if s and s.nbounds != c.nbounds:
            msg = 'The s coordinate {!r} and c coordinate {!r} ' \
                'must be equally bounded.'.format(s.name(), c.name())
            raise ValueError(msg)

        coords = ((eta, 'eta'), (depth, 'depth'))
        for coord, term in coords:
            if coord is not None and coord.nbounds:
                msg = 'The {} coordinate {!r} has bounds. ' \
                    'These are being disregarded.'.format(term, coord.name())
                warnings.warn(msg, UserWarning, stacklevel=2)

        if depth_c is not None and depth_c.shape != (1,):
            msg = 'Expected scalar {} coordinate {!r}: ' \
                'got shape {!r}.'.format(term, coord.name(), coord.shape)
            raise ValueError(msg)

        # Check units.
        coords = ((s, 's'), (c, 'c'))
        for coord, term in coords:
            if coord is not None and not coord.units.is_dimensionless():
                msg = 'Invalid units: {} coordinate {!r} ' \
                    'must be dimensionless.'.format(term, coord.name())
                raise ValueError(msg)

        coords = ((eta, 'eta'), (depth, 'depth'), (depth_c, 'depth_c'))
        for coord, term in coords:
            if coord is not None and coord.units != depth.units:
                msg = 'Incompatible units: {} coordinate {!r} and depth ' \
                    'coordinate {!r} must have ' \
                    'the same units.'.format(term, coord.name(), depth.name())
                raise ValueError(msg)

    @property
    def dependencies(self):
        """
        Returns a dictionary mapping from constructor argument names to
        the corresponding coordinates.

        """
        return dict(s=self.s, c=self.c, eta=self.eta, depth=self.depth,
                    depth_c=self.depth_c)

    def _derive(self, s, c, eta, depth, depth_c):
        S = depth_c * s + (depth - depth_c) * c
        return S + eta * (1 + S / depth)

    def make_coord(self, coord_dims_func):
        """
        Returns a new :class:`iris.coords.AuxCoord` as defined by this factory.

        Args:

        * coord_dims_func:
            A callable which can return the list of dimensions relevant
            to a given coordinate. See :meth:`iris.cube.Cube.coord_dims()`.

        """
        # Determine the relevant dimensions.
        derived_dims = self.derived_dims(coord_dims_func)
        dependency_dims = self._dependency_dims(coord_dims_func)

        # Build the points array.
        nd_points_by_key = self._remap(dependency_dims, derived_dims)
        points = self._derive(nd_points_by_key['s'],
                              nd_points_by_key['c'],
                              nd_points_by_key['eta'],
                              nd_points_by_key['depth'],
                              nd_points_by_key['depth_c'])

        bounds = None
        if self.s.nbounds or (self.c and self.c.nbounds):
            # Build the bounds array.
            nd_values_by_key = self._remap_with_bounds(dependency_dims,
                                                       derived_dims)
            valid_shapes = [(), (1,), (2,)]
            key = 's'
            if nd_values_by_key[key].shape[-1:] not in valid_shapes:
                name = self.dependencies[key].name()
                msg = 'Invalid bounds for {} ' \
                    'coordinate {!r}.'.format(key, name)
                raise ValueError(msg)
            valid_shapes.pop()
            for key in ('eta', 'depth', 'depth_c'):
                if nd_values_by_key[key].shape[-1:] not in valid_shapes:
                    name = self.dependencies[key].name()
                    msg = 'The {} coordinate {!r} has bounds. ' \
                        'These are being disregarded.'.format(key, name)
                    warnings.warn(msg, UserWarning, stacklevel=2)
                    # Swap bounds with points.
                    bds_shape = list(nd_points_by_key[key].shape) + [1]
                    bounds = nd_points_by_key[key].reshape(bds_shape)
                    nd_values_by_key[key] = bounds

            bounds = self._derive(nd_values_by_key['s'],
                                  nd_values_by_key['c'],
                                  nd_values_by_key['eta'],
                                  nd_values_by_key['depth'],
                                  nd_values_by_key['depth_c'])

        coord = iris.coords.AuxCoord(points,
                                     standard_name=self.standard_name,
                                     long_name=self.long_name,
                                     var_name=self.var_name,
                                     units=self.units,
                                     bounds=bounds,
                                     attributes=self.attributes,
                                     coord_system=self.coord_system)
        return coord

    def update(self, old_coord, new_coord=None):
        """
        Notifies the factory of the removal/replacement of a coordinate
        which might be a dependency.

        Args:

        * old_coord:
            The coordinate to be removed/replaced.
        * new_coord:
            If None, any dependency using old_coord is removed, otherwise
            any dependency using old_coord is updated to use new_coord.

        """
        new_dependencies = self.dependencies
        for name, coord in self.dependencies.items():
            if old_coord is coord:
                new_dependencies[name] = new_coord
                try:
                    self._check_dependencies(**new_dependencies)
                except ValueError as e:
                    msg = 'Failed to update dependencies. ' + str(e)
                    raise ValueError(msg)
                else:
                    setattr(self, name, new_coord)
                break


class OceanSFactory(AuxCoordFactory):
    """Defines an Ocean s-coordinate factory."""

    def __init__(self, s=None, eta=None, depth=None, a=None, b=None,
                 depth_c=None):
        """
        Creates an Ocean s-coordinate factory with the formula:

        z(n,k,j,i) = eta(n,j,i)*(1+s(k)) + depth_c*s(k) +
                     (depth(j,i)-depth_c)*C(k)

        where:
            C(k) = (1-b) * sinh(a*s(k)) / sinh(a) +
                   b * [tanh(a * (s(k) + 0.5)) / (2 * tanh(0.5*a)) - 0.5]

        """
        super(OceanSFactory, self).__init__()

        # Check that provided coordinates meet necessary conditions.
        self._check_dependencies(s, eta, depth, a, b, depth_c)

        self.s = s
        self.eta = eta
        self.depth = depth
        self.a = a
        self.b = b
        self.depth_c = depth_c

        self.standard_name = 'sea_surface_height_above_reference_ellipsoid'
        self.attributes = {'positive': 'up'}

    @property
    def units(self):
        return self.depth.units

    @staticmethod
    def _check_dependencies(s, eta, depth, a, b, depth_c):
        # Check for sufficient factory coordinates.
        if (eta is None or s is None or depth is None or
           a is None or b is None or depth_c is None):
            msg = 'Unable to construct Ocean s-coordinate ' \
                'factory due to insufficient source coordinates.'
            raise ValueError(msg)

        # Check bounds and shape.
        if s is not None and s.nbounds not in (0, 2):
            msg = 'Invalid s coordinate {!r}: must have either ' \
                '0 or 2 bounds.'.format(s.name())
            raise ValueError(msg)

        coords = ((eta, 'eta'), (depth, 'depth'))
        for coord, term in coords:
            if coord is not None and coord.nbounds:
                msg = 'The {} coordinate {!r} has bounds. ' \
                    'These are being disregarded.'.format(term, coord.name())
                warnings.warn(msg, UserWarning, stacklevel=2)

        coords = ((a, 'a'), (b, 'b'), (depth_c, 'depth_c'))
        for coord, term in coords:
            if coord is not None and coord.shape != (1,):
                msg = 'Expected scalar {} coordinate {!r}: ' \
                    'got shape {!r}.'.format(term, coord.name(), coord.shape)
                raise ValueError(msg)

        # Check units.
        if s is not None and not s.units.is_dimensionless():
            msg = 'Invalid units: s coordinate {!r} ' \
                'must be dimensionless.'.format(s.name())
            raise ValueError(msg)

        coords = ((eta, 'eta'), (depth, 'depth'), (depth_c, 'depth_c'))
        for coord, term in coords:
            if coord is not None and coord.units != depth.units:
                msg = 'Incompatible units: {} coordinate {!r} and depth ' \
                    'coordinate {!r} must have ' \
                    'the same units.'.format(term, coord.name(), depth.name())
                raise ValueError(msg)

    @property
    def dependencies(self):
        """
        Returns a dictionary mapping from constructor argument names to
        the corresponding coordinates.

        """
        return dict(s=self.s, eta=self.eta, depth=self.depth, a=self.a,
                    b=self.b, depth_c=self.depth_c)

    def _derive(self, s, eta, depth, a, b, depth_c):
        c = ((1 - b) * da.sinh(a * s) / da.sinh(a) + b *
             (da.tanh(a * (s + 0.5)) / (2 * da.tanh(0.5 * a)) - 0.5))
        return eta * (1 + s) + depth_c * s + (depth - depth_c) * c

    def make_coord(self, coord_dims_func):
        """
        Returns a new :class:`iris.coords.AuxCoord` as defined by this factory.

        Args:

        * coord_dims_func:
            A callable which can return the list of dimensions relevant
            to a given coordinate. See :meth:`iris.cube.Cube.coord_dims()`.

        """
        # Determine the relevant dimensions.
        derived_dims = self.derived_dims(coord_dims_func)
        dependency_dims = self._dependency_dims(coord_dims_func)

        # Build the points array.
        nd_points_by_key = self._remap(dependency_dims, derived_dims)
        points = self._derive(nd_points_by_key['s'],
                              nd_points_by_key['eta'],
                              nd_points_by_key['depth'],
                              nd_points_by_key['a'],
                              nd_points_by_key['b'],
                              nd_points_by_key['depth_c'])

        bounds = None
        if self.s.nbounds:
            # Build the bounds array.
            nd_values_by_key = self._remap_with_bounds(dependency_dims,
                                                       derived_dims)
            valid_shapes = [(), (1,), (2,)]
            key = 's'
            if nd_values_by_key[key].shape[-1:] not in valid_shapes:
                name = self.dependencies[key].name()
                msg = 'Invalid bounds for {} ' \
                    'coordinate {!r}.'.format(key, name)
                raise ValueError(msg)
            valid_shapes.pop()
            for key in ('eta', 'depth', 'a', 'b', 'depth_c'):
                if nd_values_by_key[key].shape[-1:] not in valid_shapes:
                    name = self.dependencies[key].name()
                    msg = 'The {} coordinate {!r} has bounds. ' \
                        'These are being disregarded.'.format(key, name)
                    warnings.warn(msg, UserWarning, stacklevel=2)
                    # Swap bounds with points.
                    bds_shape = list(nd_points_by_key[key].shape) + [1]
                    bounds = nd_points_by_key[key].reshape(bds_shape)
                    nd_values_by_key[key] = bounds

            bounds = self._derive(nd_values_by_key['s'],
                                  nd_values_by_key['eta'],
                                  nd_values_by_key['depth'],
                                  nd_values_by_key['a'],
                                  nd_values_by_key['b'],
                                  nd_values_by_key['depth_c'])

        coord = iris.coords.AuxCoord(points,
                                     standard_name=self.standard_name,
                                     long_name=self.long_name,
                                     var_name=self.var_name,
                                     units=self.units,
                                     bounds=bounds,
                                     attributes=self.attributes,
                                     coord_system=self.coord_system)
        return coord

    def update(self, old_coord, new_coord=None):
        """
        Notifies the factory of the removal/replacement of a coordinate
        which might be a dependency.

        Args:

        * old_coord:
            The coordinate to be removed/replaced.
        * new_coord:
            If None, any dependency using old_coord is removed, otherwise
            any dependency using old_coord is updated to use new_coord.

        """
        new_dependencies = self.dependencies
        for name, coord in self.dependencies.items():
            if old_coord is coord:
                new_dependencies[name] = new_coord
                try:
                    self._check_dependencies(**new_dependencies)
                except ValueError as e:
                    msg = 'Failed to update dependencies. ' + str(e)
                    raise ValueError(msg)
                else:
                    setattr(self, name, new_coord)
                break


class OceanSg2Factory(AuxCoordFactory):
    """Defines an Ocean s-coordinate, generic form 2 factory."""

    def __init__(self, s=None, c=None, eta=None, depth=None, depth_c=None):
        """
        Creates an Ocean s-coordinate, generic form 2 factory with the formula:

        z(n,k,j,i) = eta(n,j,i) + (eta(n,j,i) + depth(j,i)) * S(k,j,i)

        where:
            S(k,j,i) = (depth_c * s(k) + depth(j,i) * C(k)) /
                       (depth_c + depth(j,i))

        """
        super(OceanSg2Factory, self).__init__()

        # Check that provided coordinates meet necessary conditions.
        self._check_dependencies(s, c, eta, depth, depth_c)

        self.s = s
        self.c = c
        self.eta = eta
        self.depth = depth
        self.depth_c = depth_c

        self.standard_name = 'sea_surface_height_above_reference_ellipsoid'
        self.attributes = {'positive': 'up'}

    @property
    def units(self):
        return self.depth.units

    @staticmethod
    def _check_dependencies(s, c, eta, depth, depth_c):
        # Check for sufficient factory coordinates.
        if (eta is None or s is None or c is None or
           depth is None or depth_c is None):
            msg = 'Unable to construct Ocean s-coordinate, generic form 2 ' \
                'factory due to insufficient source coordinates.'
            raise ValueError(msg)

        # Check bounds and shape.
        coords = ((s, 's'), (c, 'c'))
        for coord, term in coords:
            if coord is not None and coord.nbounds not in (0, 2):
                msg = 'Invalid {} coordinate {!r}: must have either ' \
                    '0 or 2 bounds.'.format(term, coord.name())
                raise ValueError(msg)

        if s and s.nbounds != c.nbounds:
            msg = 'The s coordinate {!r} and c coordinate {!r} ' \
                'must be equally bounded.'.format(s.name(), c.name())
            raise ValueError(msg)

        coords = ((eta, 'eta'), (depth, 'depth'))
        for coord, term in coords:
            if coord is not None and coord.nbounds:
                msg = 'The {} coordinate {!r} has bounds. ' \
                    'These are being disregarded.'.format(term, coord.name())
                warnings.warn(msg, UserWarning, stacklevel=2)

        if depth_c is not None and depth_c.shape != (1,):
            msg = 'Expected scalar depth_c coordinate {!r}: ' \
                'got shape {!r}.'.format(depth_c.name(), depth_c.shape)
            raise ValueError(msg)

        # Check units.
        coords = ((s, 's'), (c, 'c'))
        for coord, term in coords:
            if coord is not None and not coord.units.is_dimensionless():
                msg = 'Invalid units: {} coordinate {!r} ' \
                    'must be dimensionless.'.format(term, coord.name())
                raise ValueError(msg)

        coords = ((eta, 'eta'), (depth, 'depth'), (depth_c, 'depth_c'))
        for coord, term in coords:
            if coord is not None and coord.units != depth.units:
                msg = 'Incompatible units: {} coordinate {!r} and depth ' \
                    'coordinate {!r} must have ' \
                    'the same units.'.format(term, coord.name(), depth.name())
                raise ValueError(msg)

    @property
    def dependencies(self):
        """
        Returns a dictionary mapping from constructor argument names to
        the corresponding coordinates.

        """
        return dict(s=self.s, c=self.c, eta=self.eta, depth=self.depth,
                    depth_c=self.depth_c)

    def _derive(self, s, c, eta, depth, depth_c):
        S = (depth_c * s + depth * c) / (depth_c + depth)
        return eta + (eta + depth) * S

    def make_coord(self, coord_dims_func):
        """
        Returns a new :class:`iris.coords.AuxCoord` as defined by this factory.

        Args:

        * coord_dims_func:
            A callable which can return the list of dimensions relevant
            to a given coordinate. See :meth:`iris.cube.Cube.coord_dims()`.

        """
        # Determine the relevant dimensions.
        derived_dims = self.derived_dims(coord_dims_func)
        dependency_dims = self._dependency_dims(coord_dims_func)

        # Build the points array.
        nd_points_by_key = self._remap(dependency_dims, derived_dims)
        points = self._derive(nd_points_by_key['s'],
                              nd_points_by_key['c'],
                              nd_points_by_key['eta'],
                              nd_points_by_key['depth'],
                              nd_points_by_key['depth_c'])

        bounds = None
        if self.s.nbounds or (self.c and self.c.nbounds):
            # Build the bounds array.
            nd_values_by_key = self._remap_with_bounds(dependency_dims,
                                                       derived_dims)
            valid_shapes = [(), (1,), (2,)]
            key = 's'
            if nd_values_by_key[key].shape[-1:] not in valid_shapes:
                name = self.dependencies[key].name()
                msg = 'Invalid bounds for {} ' \
                    'coordinate {!r}.'.format(key, name)
                raise ValueError(msg)
            valid_shapes.pop()
            for key in ('eta', 'depth', 'depth_c'):
                if nd_values_by_key[key].shape[-1:] not in valid_shapes:
                    name = self.dependencies[key].name()
                    msg = 'The {} coordinate {!r} has bounds. ' \
                        'These are being disregarded.'.format(key, name)
                    warnings.warn(msg, UserWarning, stacklevel=2)
                    # Swap bounds with points.
                    bds_shape = list(nd_points_by_key[key].shape) + [1]
                    bounds = nd_points_by_key[key].reshape(bds_shape)
                    nd_values_by_key[key] = bounds

            bounds = self._derive(nd_values_by_key['s'],
                                  nd_values_by_key['c'],
                                  nd_values_by_key['eta'],
                                  nd_values_by_key['depth'],
                                  nd_values_by_key['depth_c'])

        coord = iris.coords.AuxCoord(points,
                                     standard_name=self.standard_name,
                                     long_name=self.long_name,
                                     var_name=self.var_name,
                                     units=self.units,
                                     bounds=bounds,
                                     attributes=self.attributes,
                                     coord_system=self.coord_system)
        return coord

    def update(self, old_coord, new_coord=None):
        """
        Notifies the factory of the removal/replacement of a coordinate
        which might be a dependency.

        Args:

        * old_coord:
            The coordinate to be removed/replaced.
        * new_coord:
            If None, any dependency using old_coord is removed, otherwise
            any dependency using old_coord is updated to use new_coord.

        """
        new_dependencies = self.dependencies
        for name, coord in self.dependencies.items():
            if old_coord is coord:
                new_dependencies[name] = new_coord
                try:
                    self._check_dependencies(**new_dependencies)
                except ValueError as e:
                    msg = 'Failed to update dependencies. ' + str(e)
                    raise ValueError(msg)
                else:
                    setattr(self, name, new_coord)
                break
