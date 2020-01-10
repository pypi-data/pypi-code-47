from osgeo import gdal, ogr, osr
from gdalhelpers.helpers import datasource_helpers, layer_helpers
from gdalhelpers.checks import datasource_checks, layer_checks
from losanalyst.functions import checks, helpers
import losanalyst.functions.los_field_names as field_names
from losanalyst.classes.los_without_target import LoSWithoutTarget


def extract_horizon_line(los_ds: ogr.DataSource,
                         identifier_field_name: str,
                         order_field_name: str,
                         use_curvature_corrections: bool = True,
                         refraction_coefficient: float = 0.13) -> ogr.DataSource:
    """
    Extract horizon line from set of LoS. The field `identifier_field_name` specifies which LoSs should be used to
    construct one horizon line. `order_field_name` specifies field that should be used to order LoSs so that the
    horizon line is created correctly, this should be usually horizontal angle of the LoS.

    Parameters
    ----------
    los_ds : ogr.DataSource
        Data source containing layer with LoS without target to analyze.

    identifier_field_name : str
        Name of field from `los_ds` that specifies which lines of sight should be considered together, generally field
        specifying observed id.

    order_field_name : str
        Name of field from `los_ds` that specifies order in which lines of sight should be considered, generally field
        specifying horizontal angle or something very similar.

    use_curvature_corrections : bool, optional
        Calculate Earth curvature corrections while analyzing LoS. Default value is `True`.

    refraction_coefficient : float, optional
        Refraction coefficient. Default value is `0.13`.

    Returns
    -------
     ogr.DataSource
        Virtual `ogr.DataSource` in memory with one layer (named `horizon_line`) containing the lines.
    """

    datasource_checks.check_is_ogr_datasource(los_ds, "los_ds")

    los_layer = los_ds.GetLayer()

    checks.check_los_layer(los_layer)

    if not checks.is_los_without_target(los_layer):
        raise TypeError("Cannot extract horizon line for global or local lines of sight.")

    if identifier_field_name is None:
        raise ValueError("`identifier_field_name` can not be `None`. It must be field name that links "
                         "lines of sight to specific observer.")

    if not layer_checks.does_field_exist(los_layer, identifier_field_name):
        raise ValueError("Field `{0}` does not exist in `los_ds`. It must be existing field."
                         .format(identifier_field_name))

    if not layer_checks.is_field_of_type(los_layer, identifier_field_name, ogr.OFTInteger):
        raise ValueError("Field `{0}` in `los_ds` is not of `ogr.OFTInteger` type. Cannot use it as identifier."
                         .format(identifier_field_name))

    if order_field_name is None:
        raise ValueError("`order_field_name` can not be `None`. It must be field name that links "
                         "specifies order of line of sights.")

    if not layer_checks.does_field_exist(los_layer, order_field_name):
        raise ValueError("Field `{0}` does not exist in `los_ds`. It must be existing field.")

    horizon_line_ds = datasource_helpers.create_temp_gpkg_datasource()

    layer_helpers.create_layer_lines_25d(horizon_line_ds, los_layer.GetSpatialRef(), "horizon_line")

    horizon_line_layer = horizon_line_ds.GetLayer()

    fields_definition = {field_names.observer_id_field_name: ogr.OFTInteger}
    layer_helpers.add_fields_from_dict(horizon_line_layer, fields_definition)
    horizon_line_feature_def = horizon_line_layer.GetLayerDefn()

    unique_field_values = layer_helpers.get_unique_field_values(los_layer, identifier_field_name)

    for value in unique_field_values:

        sql = "SELECT * FROM {0} WHERE {1}='{2}' ORDER BY {3}".format(los_layer.GetName(),
                                                                      identifier_field_name,
                                                                      value,
                                                                      order_field_name)
        temp_layer = los_ds.ExecuteSQL(sql)

        if temp_layer.GetFeatureCount() > 1:

            h_line = ogr.Geometry(ogr.wkbLineString25D)

            for feature in temp_layer:
                geom = feature.GetGeometryRef()
                points = helpers.wkt_to_list(geom.ExportToWkt())

                o_offset = feature.GetField(field_names.observer_offset_field_name)

                los = LoSWithoutTarget(points,
                                       observer_offset=o_offset,
                                       use_curvature_corrections=use_curvature_corrections,
                                       refraction_coefficient=refraction_coefficient)

                horizon_point = los.get_global_horizon()
                h_line.AddPoint(horizon_point.GetX(), horizon_point.GetY(), horizon_point.GetZ())

            horizon_line_feature = ogr.Feature(horizon_line_feature_def)
            horizon_line_feature.SetGeometry(h_line)

            field_values = {field_names.observer_id_field_name: value}
            layer_helpers.add_values_from_dict(horizon_line_feature, field_values)

            horizon_line_layer.CreateFeature(horizon_line_feature)
            horizon_line_feature = None

    return horizon_line_ds
