from osgeo import ogr
import warnings


def check_is_ogr_datasource(variable: ogr.DataSource, variable_name: str) -> None:
    """
    Checks if `variable` is `ogr.DataSource` type, otherwise raises `TypeError`.

    Parameters
    ----------
    variable : ogr.DataSource
        Variable to check.

    variable_name : str
        Variable name for error message.

    Returns
    -------
    None

    Raises
    ------
    TypeError
        If `variable` is not `ogr.DataSource`.
    """

    if not isinstance(variable, ogr.DataSource):
        raise TypeError("`{0}` must be of class `ogr.DataSource`. `{0}` is of type `{1}`."
                        .format(variable_name, type(variable).__name__))


def warn_shapefile_output(ds: ogr.DataSource, ds_name: str) -> None:
    """
    Prints `warning` if provided `ogr.DataSource` (`ds`) has driver `ESRI Shapefile`.

    Parameters
    ----------
    ds : ogr.DataSource
        Variable to check.

    ds_name : str
        Variable name for error message.

    Returns
    -------
    None

    Warns
    -------
    UserWarning
        If driver of `ds` is `ESRI Shapefile`.

    """

    check_is_ogr_datasource(ds, ds_name)

    if ds.GetDriver().GetDescription() == "ESRI Shapefile":
        warnings.warn(
            "It is not recommended to use `ESRI Shapefile` as output type (for variable `{0}`). "
            "Geopackage (GPKG) is the recomended file output.".format(ds_name),
            UserWarning
        )
