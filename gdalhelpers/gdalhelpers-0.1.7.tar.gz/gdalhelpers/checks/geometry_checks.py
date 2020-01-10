from osgeo import ogr
from typing import Union, List


def check_variable_geometry(geometry: ogr.Geometry, variable_name: str) -> None:
    """
    Checks if `geometry` is `ogr.Geometry`, raises `TypeError` otherwise.

    Parameters
    ----------
    geometry : ogr.Geometry
        Variable to check.

    variable_name : str
        Variable name for error message.

    Returns
    -------
    None

    Raises
    ------
    TypeError
        If `variable` is not `ogr.Geometry`.
    """

    if not isinstance(geometry, ogr.Geometry):
        raise TypeError("`{0}` must be of class `ogr.Geometry`. `{0}` is of type `{1}`.".
                        format(variable_name, type(geometry).__name__))


# https://mypy.readthedocs.io/en/latest/cheat_sheet_py3.html
# TODO fix using names to codes
def check_variable_expected_geometry(geometry: ogr.Geometry,
                                     variable_name: str,
                                     expected_geometry_type: Union[int, List[int]]) -> None:
    """
    Checks if `geometry` (`ogr.Geometry`) is of expected type or types, raises `ValueError` if not.

    Parameters
    ----------
    geometry : ogr.Geometry
        Variable to check.

    variable_name : str
        Variable name for error message.

    expected_geometry_type: int or list of int
        Only values provided by ogr.wkbPoint etc. makes sense.
        Can be constructed as `expected_geometry_type=ogr.wkbPoint` or
        `expected_geometry_type=[ogr.wkbPoint, ogr.wkbPoint25D, ogr.wkbPointZM ]`

    Returns
    -------
    None

    Raises
    ------
    ValueError
        If `variable` is not of `expected_geometry_type`.
    """

    check_variable_geometry(geometry, variable_name)

    geometry_name = ogr.GeometryTypeToName(geometry.GetGeometryType())

    check: bool = False
    expected_geometry_name: str

    if isinstance(expected_geometry_type, list):

        for egt in expected_geometry_type:
            if ogr.GeometryTypeToName(geometry.GetGeometryType()) == ogr.GeometryTypeToName(egt):
                check = True

        expected_geometry_name = [ogr.GeometryTypeToName(x) for x in expected_geometry_type]
        expected_geometry_name = ", ".join(expected_geometry_name)
    else:
        expected_geometry_name = ogr.GeometryTypeToName(expected_geometry_type)
        check = (ogr.GeometryTypeToName(geometry.GetGeometryType()) in ogr.GeometryTypeToName(expected_geometry_type))

    if not check:
        raise ValueError("`{0}` must be of geometry type/types `{1}`, but it is `{2}`.".
                         format(variable_name, expected_geometry_name, geometry_name))


def check_is_wkt_geometry(string: str, variable_name: str) -> None:
    """
    Checks if the provided `string` is a valid WKT. Raises `TypeError` otherwise.

    Parameters
    ----------
    string : str
        String to check if it is WKT.

    variable_name : str
        Variable name for error message.

    Returns
    -------
    None

    Raises
    ------
    ValueError
        If `string` is not valid WKT.
    """

    if ogr.CreateGeometryFromWkt(string) is None:
        raise ValueError("`{0}` is not a valid WKT. `{1}` cannot be loaded as geometry.".format(variable_name, string))
