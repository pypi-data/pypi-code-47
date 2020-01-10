from osgeo import ogr
from typing import Union, List
from gdalhelpers.checks import srs_checks


def check_is_layer(variable: ogr.Layer, variable_name: str) -> None:
    """
    Check if `variable` is `ogr.Layer`, raises `TypeError` otherwise.

    Parameters
    ----------
    variable : ogr.Layer
        Variable to check.

    variable_name : str
        Variable name for error message.

    Returns
    -------
    None

    Raises
    ------
    TypeError
        If `variable` is not `ogr.Layer`.
    """

    if not isinstance(variable, ogr.Layer):
        raise TypeError("`{0}` must be of class `ogr.Layer`. `{0}` is of type `{1}`."
                        .format(variable_name, type(variable).__name__))


# https://gis.stackexchange.com/questions/239289/gdal-ogr-python-getgeomtype-method-returns-integer-what-is-the-matching-geo
def check_is_layer_geometry_type(variable: ogr.Layer,
                                 variable_name: str,
                                 expected_geom_type: Union[int, List[int]]) -> None:
    """
    Checks if `variable` (`ogr.Layer`) is of expected type or types, raises `TypeError` if not.

    Parameters
    ----------
    variable : ogr.Layer
        Variable to check.

    variable_name : str
        Variable name for error message.

    expected_geom_type : int or list of int
        Only values provided by ogr.wkbPoint etc. makes sense.
        Can be constructed as `expected_geometry_type=ogr.wkbPoint` or
        `expected_geometry_type=[ogr.wkbPoint, ogr.wkbPoint25D, ogr.wkbPointZM ]`.

    Returns
    -------
    None

    Raises
    ------
    ValueError
        If `variable` is not of `expected_geometry_type`.
    """

    check_is_layer(variable, variable_name)

    geometry_name = ogr.GeometryTypeToName(variable.GetGeomType())

    check: bool = False
    expected_geometry_name: str

    if isinstance(expected_geom_type, list):

        for egt in expected_geom_type:
            if variable.GetGeomType() == egt:
                check = True

        expected_geometry_name = [ogr.GeometryTypeToName(x) for x in expected_geom_type]
        expected_geometry_name = ", ".join(expected_geometry_name)
    else:
        expected_geometry_name = ogr.GeometryTypeToName(expected_geom_type)
        check = (variable.GetGeomType() == expected_geom_type)

    if not check:
        raise ValueError("`{0}` must be of geometry type/types `{1}`, but it is `{2}`.".
                         format(variable_name, expected_geometry_name, geometry_name))


def does_field_exist(layer: ogr.Layer, field_name: Union[str, None]) -> bool:
    """
    Verify if field with `field_name` exists in layer.

    Parameters
    ----------
    layer : ogr.Layer
        `ogr.Layer` to look for field.

    field_name : str or None
        Name of the field.

    Returns
    -------
    bool
        `True` if field exists in the given `ogr.Layer`, `False` otherwise.
    """

    if field_name is None:
        return False

    field_index = layer.GetLayerDefn().GetFieldIndex(field_name)

    if field_index < 0:
        return False
    else:
        return True


def is_field_of_type(layer: ogr.Layer, field_name: str, field_type: int) -> bool:
    """
    Verify that field in layer is of given type.

    Parameters
    ----------
    layer : ogr.Layer
        `ogr.Layer` to look for field.

    field_name : str
        Name of the field.

    field_type : int
        Idetification of field type. It can be created as `ogr.OFTReal`, `ogr.OFTString` etc.

    Returns
    -------
    bool
        `True` if the field is of given type, `False` otherwise.
    """

    if field_type == get_field_type(layer, field_name):
        return True
    else:
        return False


def get_field_type(layer: ogr.Layer, field_name: str) -> str:
    """
    Get type of field in `layer` as string.

    Parameters
    ----------
    layer : ogr.Layer
        `ogr.Layer` to look for field type.

    field_name : str
        Name of the field to get the type.

    Returns
    -------
    str
        Type of the field as `string`.

    """
    field_index = layer.GetLayerDefn().GetFieldIndex(field_name)

    return layer.GetLayerDefn().GetFieldDefn(field_index).GetType()


def check_number_of_features(layer: ogr.Layer,
                             variable_name: str,
                             number: int):
    """
    Check if `layer` has specified (`number`) number of features.

    Parameters
    ----------
    layer : ogr.Layer
        `ogr.Layer`

    variable_name : str
        Variable name for error message.

    number : int
        Number of features the `layer` is expected to have.

    Returns
    -------
    None

    Raises
    ------
    AttributeError
        If the number of features in `layer` does not equal to `number`.
    """

    if not layer.GetFeatureCount() == number:
        raise AttributeError("Layer `{0}` must contain only `{1}` feature/s. Currently there are `{2}` features.".
                             format(variable_name, number, layer.GetFeatureCount()))


def check_is_projected(layer: ogr.Layer, variable_name: str,) -> None:
    """
    Check that layer is projected.

    Parameters
    ----------
    layer : ogr.Layer
        `ogr.Layer`

    variable_name : str
        Variable name for error message.

    Returns
    -------
    None

    Raises
    ------
    ValueError
        If the Spatial Reference System of the `layer` is not specified or if it is not projected.
    """

    if layer.GetSpatialRef() is None:
        raise ValueError("`{0}` layer does not have Spatial Reference specified.")
    else:
        srs_checks.check_srs_projected(layer.GetSpatialRef(), variable_name)


def check_layers_sr_are_same(layer1: ogr.Layer, layer1_name: str,
                             layer2: ogr.Layer, layer2_name: str) -> None:
    """
    Check that Spatial Reference Systems of two layers are the same.

    Parameters
    ----------
    layer1, layer2 : ogr.Layer
        `ogr.Layer` to compare.

    layer1_name, layer2_name : str
        Names of the variables for error message.

    Returns
    -------
    None

    """
    srs_checks.check_srs_are_same(layer1.GetSpatialRef(), layer1_name,
                                  layer2.GetSpatialRef(), layer2_name)