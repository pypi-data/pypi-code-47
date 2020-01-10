from osgeo import ogr
import numpy as np
import math
from typing import List
import gdalhelpers.checks.geometry_checks as geometry_checks
import gdalhelpers.checks.values_checks as values_checks
import gdalhelpers.helpers.math_helpers as math_helpers
from gdalhelpers.classes.DEM import DEM


def line_segmentize(line: ogr.Geometry,
                    segment_length: float = None,
                    allowed_input_types: List[int] = None) -> ogr.Geometry:
    """
    Segmetize line into parts of regular length.

    Parameters
    ----------
    line: ogr.Geometry
        Line to segmentize.

    segment_length : float
        Length of individual line segment.

    allowed_input_types: list of int
        Allowed geometry types for line. Default value is `None` which means any type of line. The default value
        is equal to definition `allowed_input_types=[ogr.wkbLineString, ogr.wkbLineString25D, ogr.wkbLineStringM,
        ogr.wkbLineStringZM]`.

    Returns
    -------
    ogr.Geometry
        `ogr.Geometry` with the same definition as input `line`.
    """

    if allowed_input_types is None:
        allowed_input_types = [ogr.wkbLineString, ogr.wkbLineString25D, ogr.wkbLineStringM, ogr.wkbLineStringZM]

    geometry_checks.check_variable_expected_geometry(line, "line", allowed_input_types)

    values_checks.check_value_is_zero_or_positive(segment_length, "segment_length")

    if segment_length is not None:
        values_checks.check_value_is_zero_or_positive(segment_length, "segment_length")
        # offset distance by the smallest possible value change towards higher value,
        # otherwise Segmetize tries to use smaller value and not the actual distance as limit
        segment_length = np.nextafter(float(segment_length), np.Inf)

        line.Segmentize(segment_length)

    return line


def line_create_3_points(point1: ogr.Geometry,
                         point2: ogr.Geometry,
                         point3: ogr.Geometry,
                         segment_length: float = None,
                         allowed_input_types: List[int] = None) -> ogr.Geometry:
    """
    Create line defined by three points. The line can be segmentized. The resulting line does not have to be
    straight, the points are always put in order - starting point `point1`, mid point `point2`, end point `point3`.

    Parameters
    ----------
    point1, point2, point3: ogr.Geometry
        `ogr.Geometry` that defines starting and ending point of line. Allowed types are checked against
        `allowed_input_types`.

    segment_length : float, optional
        Length of individual segments of the line. Default value is `None` which means no segmentization of the line.

    allowed_input_types : list of int, optional
        Allowed geometry types for points. Default value is `None` which means any type of point. The default value
        is equal to definition `allowed_input_types=[ogr.wkbPoint, ogr.wkbPoint25D, ogr.wkbPointM, ogr.wkbPointZM]`.

    Returns
    -------
    ogr.Geometry
        `ogr.Geometry` with definition `wkbLineString`.
        """

    if allowed_input_types is None:
        allowed_input_types = [ogr.wkbPoint, ogr.wkbPoint25D, ogr.wkbPointM, ogr.wkbPointZM]

    geometry_checks.check_variable_expected_geometry(point1, "point1", allowed_input_types)
    geometry_checks.check_variable_expected_geometry(point2, "point2", allowed_input_types)
    geometry_checks.check_variable_expected_geometry(point3, "point3", allowed_input_types)

    values_checks.check_value_is_zero_or_positive(segment_length, "segment_length")

    line = ogr.Geometry(ogr.wkbLineString)

    line.SetPoint(0, point1.GetX(), point1.GetY())
    line.SetPoint(1, point2.GetX(), point2.GetY())
    line.SetPoint(2, point3.GetX(), point3.GetY())

    line = line_segmentize(line, segment_length)

    return line


def line_create_2_points(point1: ogr.Geometry,
                         point2: ogr.Geometry,
                         segment_length: float = None,
                         allowed_input_types: List[int] = None) -> ogr.Geometry:
    """
    Create line between two points. The line can be segmentized.

    Parameters
    ----------
    point1, point2: ogr.Geometry
        `ogr.Geometry` that defines starting and ending point of line. Allowed types are checked against
        `allowed_input_types`.

    segment_length : float, optional
        Length of individual segments of the line. Default value is `None` which means no segmentization of the line.

    allowed_input_types : list of int, optional
        Allowed geometry types for points. Default value is `None` which means any type of point. The default values is
        equal to definition `allowed_input_types=[ogr.wkbPoint, ogr.wkbPoint25D, ogr.wkbPointM, ogr.wkbPointZM]`.

    Returns
    -------
    ogr.Geometry
        `ogr.Geometry` with definition `wkbLineString`.
    """

    if allowed_input_types is None:
        allowed_input_types = [ogr.wkbPoint, ogr.wkbPoint25D, ogr.wkbPointM, ogr.wkbPointZM]

    geometry_checks.check_variable_expected_geometry(point1, "point1", allowed_input_types)
    geometry_checks.check_variable_expected_geometry(point2, "point2", allowed_input_types)

    values_checks.check_value_is_zero_or_positive(segment_length, "segment_length")

    line = ogr.Geometry(ogr.wkbLineString)

    line.SetPoint(0, point1.GetX(), point1.GetY())
    line.SetPoint(1, point2.GetX(), point2.GetY())

    line = line_segmentize(line, segment_length)

    return line


def line_assign_z_to_vertexes(line_2d: ogr.Geometry,
                              dem: DEM,
                              allowed_input_types: List[int] = None) -> ogr.Geometry:
    """
    Assign Z dimension to vertices of line based on raster value of `dem`. The values from `dem` are interpolated using
    bilinear interpolation to provide smooth surface.

    Parameters
    ----------
    line_2d : ogr.Geometry
        `ogr.Geometry` containing lines. Allowed types are checked against `allowed_input_types`.

    dem : DEM
        Raster data source in specific format `DEM` (`gdalhepers` class).

    allowed_input_types : list of int, optional
        Allowed geometry types for `line_2d`. Default value is `None` which means any type of line. The default values
        is equal to definition `allowed_input_types=[ogr.wkbLineString, ogr.wkbLineString25D,
        ogr.wkbLineStringM, ogr.wkbLineStringZM]]`.

    Returns
    -------
    ogr.Geometry
        `ogr.Geometry` with definition `ogr.wkbLineStringZ`.
    """

    if allowed_input_types is None:
        allowed_input_types = [ogr.wkbLineString, ogr.wkbLineString25D, ogr.wkbLineStringM, ogr.wkbLineStringZM]

    geometry_checks.check_variable_expected_geometry(line_2d, "line_2d", allowed_input_types)

    line_3d = ogr.Geometry(ogr.wkbLineString25D)

    for i in range(0, line_2d.GetPointCount()):
        pt = line_2d.GetPoint(i)
        z_value = dem.get_value_bilinear(pt[0], pt[1])

        if z_value != dem.get_nodata_value():
            line_3d.AddPoint(pt[0], pt[1], z_value)

    return line_3d


def angle_points(point1: ogr.Geometry,
                 point2: ogr.Geometry,
                 allowed_input_types: List[int] = None) -> float:
    """
    Calculate angle from `point1` to `point2`. The function is not symetrical, so
    `angle_points(p_a, p_b) != angle_points(p_b, p_a)`.

    Parameters
    ----------
    point1, point2: ogr.Geometry
        `ogr.Geometry` representing points. Allowed types are checked against `allowed_input_types`.

    allowed_input_types : list of int, optional
        Allowed geometry types for points. Default value is `None` which means any type of point. The default values is
        equal to definition `allowed_input_types=[ogr.wkbPoint, ogr.wkbPoint25D, ogr.wkbPointM, ogr.wkbPointZM]`.

    Returns
    -------
    float
        Angle between `point1` and `point2`.

    """

    if allowed_input_types is None:
        allowed_input_types = [ogr.wkbPoint, ogr.wkbPoint25D, ogr.wkbPointM, ogr.wkbPointZM]

    geometry_checks.check_variable_expected_geometry(point1, "point1", allowed_input_types)
    geometry_checks.check_variable_expected_geometry(point2, "point2", allowed_input_types)

    return math_helpers.horizontal_angle(point1.GetX(), point1.GetY(), point2.GetX(), point2.GetY())


def point_at_angle_distance(point: ogr.Geometry,
                            distance: float,
                            theta: float,
                            allowed_input_types: List[int] = None) -> ogr.Geometry:
    """
    Create a point based on position of another point, angle and distance.

    Parameters
    ----------
    point: ogr.Geometry
        Origin point from which the position is created. Allowed types are checked against `allowed_input_types`.

    distance: float
        Distance at which the new point should be created.

    theta : float
        Angle in radians ([-pi, pi]) at which the new point should be create.

    allowed_input_types : list of int, optional
        Allowed geometry types for `point`. Default value is `None` which means any type of point. The default values is
        equal to definition `allowed_input_types=[ogr.wkbPoint, ogr.wkbPoint25D, ogr.wkbPointM, ogr.wkbPointZM]`.

    Returns
    -------
    ogr.Geometry
        `ogr.Geometry` representing `ogr.wkbPoint`.
    """

    if allowed_input_types is None:
        allowed_input_types = [ogr.wkbPoint, ogr.wkbPoint25D, ogr.wkbPointM, ogr.wkbPointZM]

    geometry_checks.check_variable_expected_geometry(point, "point", allowed_input_types)
    values_checks.check_value_is_zero_or_positive(distance, "distance")
    values_checks.check_return_value_is_angle(theta, "theta")

    point_new = ogr.Geometry(ogr.wkbPoint)

    point_new.AddPoint_2D(point.GetX() - distance * math.cos(theta),
                      point.GetY() - distance * math.sin(theta))

    return point_new
