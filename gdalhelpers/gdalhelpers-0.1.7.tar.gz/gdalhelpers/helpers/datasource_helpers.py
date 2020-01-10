from osgeo import ogr
import tempfile
import os


def create_temp_gpkg_datasource() -> ogr.DataSource:
    """
    Creates temporary `ogr.DataSource` in memory.

    Returns
    -------
    ogr.DataSource
    """

    tf = tempfile.NamedTemporaryFile(suffix=".gpkg")
    file_name = os.path.basename(tf.name)
    tf.close()
    return ogr.GetDriverByName("GPKG").CreateDataSource("/vsimem/" + file_name)
