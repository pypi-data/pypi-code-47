from osgeo import osr
from typing import Any


def check_srs(srs: osr.SpatialReference, srs_name: str) -> None:
    """
    Checks if `srs` is `osr.SpatialReference`, raises `TypeError` otherwise.

    Parameters
    ----------
    srs : osr.SpatialReference
        Variable to check.

    srs_name : str
        Variable name for error message.

    Returns
    -------
    None

    Raises
    ------
    TypeError
        If `srs` is not `osr.SpatialReference`.
    """

    if not isinstance(srs, osr.SpatialReference):
        raise TypeError("`{0}` is not of type `osr.SpatialReference`. It is: `{1}`."
                        .format(srs_name, type(srs).__name__))


def check_srs_projected(srs: osr.SpatialReference, srs_name: str) -> None:
    """
    Checks if `srs` (`osr.SpatialReference`) is projected, raises `ValueError` otherwise.

    Parameters
    ----------
    srs : osr.SpatialReference
        osr.SpatialReference to check.
    srs_name : str
         Variable name for error message.

    Returns
    -------
    None

    Raises
    ------
    ValueError
        If `srs` is not projected.
    """

    check_srs(srs, srs_name)

    if srs.IsProjected() != 1:
        raise ValueError("`{0}` Spatial Reference needs to be projected. "
                         "The definition of current SRS is not projected: \n `{1}`"
                         .format(srs_name, srs.ExportToProj4()))


def check_srs_are_same(srs1: osr.SpatialReference, srs1_name: str,
                       srs2: osr.SpatialReference, srs2_name: str) -> None:
    """
    Checks if two provided `osr.SpatialReference` are the same.

    Parameters
    ----------
    srs1, srs2 : osr.SpatialReference
        osr.SpatialReference to compare.

    srs1_name, srs2_name : str
        Variable name for error message.

    Returns
    -------
    None

    Raises
    ------
    ValueError
        If `srs1` and `srs2` are not the same.
    """

    check_srs(srs1, srs1_name)
    check_srs(srs2, srs2_name)

    if srs1.IsSame(srs2) != 1:
        raise ValueError("Spatial Reference of both variables `{0}`, `{1}` needs to be equal."
                         .format(srs1_name, srs2_name))