from osgeo import ogr
from typing import List, Union
import math
import os
import warnings
import numpy as np
from gdalhelpers.checks import values_checks, datasource_checks, layer_checks
from gdalhelpers.helpers import layer_helpers, datasource_helpers, geometry_helpers


def create_points_at_angles_distance_in_direction(start_points: ogr.DataSource,
                                                  main_direction_point: ogr.DataSource,
                                                  distance: Union[int, float] = 10,
                                                  angle_offset: Union[int, float] = 10,
                                                  angle_density: Union[int, float] = 1,
                                                  angles_specification_degrees: bool = True,
                                                  input_points_id_field: str = None) -> ogr.DataSource:
    """
    Function that generates for every `Feature` in `start_points` set of points at specified `distance` in direction of
    `main_direction_point`.

    Parameters
    ----------
    start_points : ogr.DataSource
        Points to generate new points around. Can be of geometrical types: `ogr.wkbPoint, ogr.wkbPoint25D,
        ogr.wkbPointM, ogr.wkbPointZM`.

    main_direction_point : ogr.DataSource
        Layer with single feature that specifies the direction in which the new points are generated.

    distance : float or int
        Distance at which the new points are generated. Default value is `10` and it is specified in units of layer
        `start_points`.

    angle_offset : float or int
        Specification of angle offset on each side from `main_direction_point`. The points are generated in interval
        `[main_angle - angle_offset, main_angle + angle_offset]`, where `main_angle` is angle between specific feature
        of `start_points` and `main_direction_point`. Default value is `10`, which gives over angle width of `20`.

    angle_density : float or int
        How often points are generated in inverval given by `angle_offset`. Default value is `1`.

    angles_specification_degrees : bool
        Are the angles specified in degrees? Default values is `True`, if `False` the values are in radians.

    input_points_id_field : str
        Name of ID (or other) field from `input_points_ds` that should be carried over the resulting DataSource.

    Returns
    -------
    ogr.DataSource
        Virtual `ogr.DataSource` in memory with one layer (named `points`) containing the points.

    Raises
    ------
    Various Errors can be raise while checking for validity of inputs.

    Warns
    -------
    UserWarning
        If the field of given name (`input_points_id_field`) is not present or if its not of type `ogr.OFTInteger`.
    """

    output_points_ds = datasource_helpers.create_temp_gpkg_datasource()

    datasource_checks.check_is_ogr_datasource(start_points, "start_points")
    datasource_checks.check_is_ogr_datasource(main_direction_point, "main_direction_point")

    values_checks.check_value_is_zero_or_positive(distance, "distance")
    values_checks.check_number(angle_offset, "angle_offset")
    values_checks.check_number(angle_density, "angle_density")

    if angles_specification_degrees:
        angle_offset = ((2*math.pi)/360)*angle_offset
        angle_density = ((2*math.pi)/360)*angle_density

    input_points_layer = start_points.GetLayer()
    layer_checks.check_is_layer_geometry_type(input_points_layer, "input_points_layer", [ogr.wkbPoint, ogr.wkbPoint25D,
                                                                                         ogr.wkbPointM, ogr.wkbPointZM])

    input_points_srs = input_points_layer.GetSpatialRef()

    main_point_layer = main_direction_point.GetLayer()
    layer_checks.check_is_layer_geometry_type(main_point_layer, "main_point_layer", [ogr.wkbPoint, ogr.wkbPoint25D,
                                                                                     ogr.wkbPointM, ogr.wkbPointZM])
    layer_checks.check_number_of_features(main_point_layer, "main_point_layer", 1)

    if input_points_id_field is not None:
        if not layer_checks.does_field_exist(input_points_layer, input_points_id_field):
            input_points_id_field = None
            warnings.warn(
                "Field {0} does not exist in {1}. Defaulting to FID.".format(input_points_id_field,
                                                                             os.path.basename(start_points.GetDescription()))
            )
        else:
            if not layer_checks.is_field_of_type(input_points_layer, input_points_id_field, ogr.OFTInteger):
                input_points_id_field = None
                warnings.warn(
                    "Field {0} in {1} is not `Integer`. Defaulting to FID.".format(input_points_id_field,
                                                                                   os.path.basename(start_points.GetDescription()))
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

    for main_feature in main_point_layer:

        main_geom = main_feature.GetGeometryRef()

        for feature in input_points_layer:
            geom = feature.GetGeometryRef()

            if input_points_id_field is None:
                f_id = feature.GetFID()
            else:
                f_id = feature.GetField(input_points_id_field)

            main_angle = geometry_helpers.angle_points(geom, main_geom)

            angles = np.arange(main_angle - angle_offset,
                               np.nextafter(main_angle + angle_offset, np.Inf),
                               step=angle_density)

            for angle in angles:
                p = geometry_helpers.point_at_angle_distance(geom, distance, angle)

                output_point_feature = ogr.Feature(output_points_def)
                output_point_feature.SetGeometry(p)

                values = {field_name_id: f_id,
                          field_name_angle: angle}

                layer_helpers.add_values_from_dict(output_point_feature, values)

                output_points_layer.CreateFeature(output_point_feature)

        return output_points_ds
