from osgeo import ogr, osr
from typing import List, Dict, Any, Set


def create_layer_points(ds: ogr.DataSource, srs: osr.SpatialReference, layer_name: str) -> None:
    """
    Creates layer within `ds` with `srs` Spatial Reference System and `layer_name` name with `ogr.wkbPoint`
    geometry type.

    Parameters
    ----------
    ds : ogr.DataSource
        `ogr.DataSource` to create the layer in.

    srs : osr.SpatialReference
        `osr.SpatialReference` for the layer.

    layer_name : str
        Layer name.

    Returns
    -------
    None
    """

    ds.CreateLayer(layer_name, srs, ogr.wkbPoint, ['OVERWRITE=YES'])


def create_layer_points_25d(ds: ogr.DataSource, srs: osr.SpatialReference, layer_name: str) -> None:
    """
    Creates layer within `ds` with `srs` Spatial Reference System and `layer_name` name with `ogr.wkbPoint25D`
    geometry type.

    Parameters
    ----------
    ds : ogr.DataSource
        `ogr.DataSource` to create the layer in.

    srs : osr.SpatialReference
        `osr.SpatialReference` for the layer.

    layer_name : str
        Layer name.

    Returns
    -------
    None
    """

    ds.CreateLayer(layer_name, srs, ogr.wkbPoint25D, ['OVERWRITE=YES'])


def create_layer_lines_25d(ds: ogr.DataSource, srs: osr.SpatialReference, layer_name: str):
    """
    Creates layer within `ds` with `srs` Spatial Reference System and `layer_name` name with `ogr.wkbLineString25D`
    geometry type.

    Parameters
    ----------
    ds : ogr.DataSource
        `ogr.DataSource` to create the layer in.

    srs : osr.SpatialReference
        `osr.SpatialReference` for the layer.

    layer_name : str
        Layer name.

    Returns
    -------
    None
    """

    ds.CreateLayer(layer_name, srs, ogr.wkbLineString25D, ['OVERWRITE=YES'])


def add_fields_from_dict(layer: ogr.Layer, fields_types: Dict[str, int]) -> None:
    """
    Add fields to `ogr.Layer` based on a dictionary. Keys of the dictionary are used as field names and values as
    field types.

    Parameters
    ----------
    layer : ogr.Layer
        `ogr.Layer` to add the fields to.

    fields_types : dict[str, int]
        Dictionary of field names and field types. Keys of the dictionary are used as field names and values as
        field types. It can be initialized as `fields_types = {"feature_id": ogr.OFTInteger, "value" : ogr.OFTReal}`.

    Returns
    -------
    None
    """

    for field, ftype in fields_types.items():
        field_def = ogr.FieldDefn(field, ftype)
        layer.CreateField(field_def)


def add_values_from_dict(feature: ogr.Feature, fields_values: Dict[str, Any]) -> None:
    """
    Sets field values for `feature` based on dictionary. Keys of the dictionary are used as field names and values as
    feature values.

    Parameters
    ----------
    feature : ogr.Feature
        `ogr.Feature` to add the values to.

    fields_values: dict[str, Any]
        Dictionary of field names and values. Keys of the dictionary are used as field names and values as
        values for the fields. It can be initialized as `fields_values = {"feature_id": 1, "value": 2.35}`.

    Returns
    -------
    None
    """
    for field, value in fields_values.items():
        feature.SetField(field, value)


def get_field_values(layer: ogr.Layer, field_name: str) -> List[Any]:
    """
    Extract values from a specific field into list.

    Parameters
    ----------
    layer : ogr.Layer
        Layer to get field the values from.

    field_name : str
        Field to extract values from.

    Returns
    -------
    list[Any]
        List containing the data from the field. The type of elements in list depends on field type of `field`
        in `layer`.
    """
    values = [None] * layer.GetFeatureCount()
    i = 0
    for feature in layer:
        values[i] = feature.GetField(field_name)
        i += 1
    return values


def get_unique_field_values(layer: ogr.Layer, field_name: str) -> Set[Any]:
    """
    Extract unique values from a specific field into set.

    Parameters
    ----------
    layer : ogr.Layer
        Layer to get field the values from.

    field_name : str
        Field to extract values from.

    Returns
    -------
    set[Any]
        Set containing the unique values from the field. The type of elements in set depends on field type of `field`
        in `layer`.
    """
    return set(get_field_values(layer, field_name))


def get_geometry_list(layer: ogr.Layer) -> List[ogr.Geometry]:
    """
    Extracts all geometry from a `layer` as a list of geometries.

    Parameters
    ----------
    layer : ogr.Layer
        Layer to get the geometry from.

    Returns
    -------
    list[ogr.Geometry]
        List of `ogr.Geometry` (geometries).

    """
    feature_list: list = [None] * layer.GetFeatureCount()
    i: int = 0

    for feature in layer:
        feature_list[i] = feature.GetGeometryRef().Clone()
        i += 1

    return feature_list
