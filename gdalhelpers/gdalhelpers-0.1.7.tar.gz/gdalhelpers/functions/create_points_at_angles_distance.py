from osgeo import ogr
from typing import List, Union
from itertools import repeat
import os
import math
import warnings
import numpy as np
from gdalhelpers.checks import geometry_checks, layer_checks, datasource_checks, values_checks
from gdalhelpers.helpers import layer_helpers, datasource_helpers, geometry_helpers


def create_points_at_angles_distance(input_points_ds: ogr.DataSource,
                                     angles: List[float] = None,
                                     distance: Union[float, int] = 1,
                                     angles_specification_degrees: bool = True,
                                     input_points_id_field: str = None) -> ogr.DataSource:
    """
    Function that generates for every `Feature` in `Layer` in `input_points_ds` set of points at specified `distance`
    and `angles`.

    Parameters
    ----------
    input_points_ds : ogr.DataSource
        Input points, geometry of the layer has to be `ogr.wkbPoint, ogr.wkbPoint25D, ogr.wkbLineStringM` or
        `ogr.wkbPointZM`.

    angles : list of float or None, optional
        Angles at which the resulting points should be created. Default value is `None`which creates list containg
        integer values from 0 to 360. Createad with coomand `np.arange(0, 360, step=1).tolist()`.

    distance : float or int, optional
        Distance at which the points should be created. Default value is `1`.

    angles_specification_degrees : bool, optional
        Are the angles specified in degrees? Default values is `True`, if `False` the values are in radians.

    input_points_id_field : str, optional
        Name of ID (or other) field from `input_points_ds` that should be carried over the resulting DataSource.

    Returns
    -------
    ogr.DataSource
        Virtual `ogr.DataSource` in memory with one layer (named `points`) containing the points.

    Example output
    -------
        Following image shows 

    .. image:: create_points_at_angles_distance.png

    Raises
    ------
    Various Errors can be raise while checking for validity of inputs.

    Warns
    -------
    UserWarning
        If the field of given name (`input_points_id_field`) is not present or if its not of type `ogr.OFTInteger`.
    """

    output_points_ds = datasource_helpers.create_temp_gpkg_datasource()

    datasource_checks.check_is_ogr_datasource(input_points_ds, "input_points_ds")

    input_points_layer = input_points_ds.GetLayer()

    layer_checks.check_is_layer_geometry_type(input_points_layer, "input_points_layer", [ogr.wkbPoint,
                                                                                         ogr.wkbPoint25D,
                                                                                         ogr.wkbLineStringM,
                                                                                         ogr.wkbPointZM])
    values_checks.check_value_is_zero_or_positive(distance, "distance")

    if angles is None:
        angles = np.arange(0, 360, step=1).tolist()

    if angles_specification_degrees:
        angles = [math.radians(x) - math.pi for x in angles]

    angles = list(map(values_checks.check_return_value_is_angle, angles, repeat("angles")))

    input_points_srs = input_points_layer.GetSpatialRef()

    if not layer_checks.does_field_exist(input_points_layer, input_points_id_field):
        input_points_id_field = None
        warnings.warn(
            "Field `{0}` does not exist in `{1}`. Defaulting to FID."
                .format(input_points_id_field,
                        os.path.basename(input_points_ds.GetDescription())),
            UserWarning
        )
    else:
        if not layer_checks.is_field_of_type(input_points_layer, input_points_id_field, ogr.OFTInteger):
            input_points_id_field = None
            warnings.warn(
                "Field `{0}` in `{1}` is not `Integer`. Defaulting to FID."
                    .format(input_points_id_field,
                            os.path.basename(input_points_ds.GetDescription())),
                UserWarning
            )

    if input_points_id_field is None:
        field_name_id = "input_point_FID"
    else:
        field_name_id = "input_point_ID"

    field_name_angle = "angle"

    layer_helpers.create_layer_points(output_points_ds, input_points_srs, "points")
    output_points_layer = output_points_ds.GetLayer()

    fields = {field_name_id: ogr.OFTInteger,
              field_name_angle: ogr.OFTReal}

    layer_helpers.add_fields_from_dict(output_points_layer, fields)

    output_points_def = output_points_layer.GetLayerDefn()

    for feature in input_points_layer:
        geom = feature.GetGeometryRef()

        if input_points_id_field is None:
            f_id = feature.GetFID()
        else:
            f_id = feature.GetField(input_points_id_field)

        for angle in angles:
            p = geometry_helpers.point_at_angle_distance(geom, distance, angle)

            output_point_feature = ogr.Feature(output_points_def)
            output_point_feature.SetGeometry(p)

            values = {field_name_id: f_id,
                      field_name_angle: angle}

            layer_helpers.add_values_from_dict(output_point_feature, values)

            output_points_layer.CreateFeature(output_point_feature)

    return output_points_ds