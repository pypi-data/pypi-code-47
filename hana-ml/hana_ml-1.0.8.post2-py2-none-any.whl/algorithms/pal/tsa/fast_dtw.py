"""
This module contains Python wrapper for PAL fast dtw algorithm.

The following function is available:

    * :func:`fast_dtw`
"""

# pylint:disable=line-too-long
import logging
import uuid

from hdbcli import dbapi

from hana_ml.algorithms.pal.pal_base import (
    ParameterTable,
    arg,
    try_drop,
    call_pal_auto
)

logger = logging.getLogger(__name__)#pylint: disable=invalid-name

def fast_dtw(conn_context, data, radius, thread_ratio=None, distance_method=None, minkowski_power=None):#pylint:disable=too-many-arguments, too-few-public-methods, unused-argument, too-many-locals
    """
    DTW is an abbreviation for Dynamic Time Warping. It is a method for calculating distance or similarity between two time series.

    Parameters
    ----------

    conn_context : ConnectionContext
        The connection to the SAP HANA system.

    data : DataFrame
        Input data.
            - ID for multiple time series
            - Timestamps
            - Attributes of time series

    radius : int
        Parameter used for fast DTW algorithm. It is for balancing DTW accuracy and runtime. The bigger, the more accuracy but slower. Must be positive.

    thread_ratio : float, optional
        Controls the proportion of available threads to use.
        The ratio of available threads.
            - 0: single thread.
            - 0~1: percentage.
            - Others: heuristically determined.

        Defaults to -1.

    distance_method : int, optional
        Specifies the method to compute the distance between two points.
            - 1: Manhattan
            - 2: Euclidean
            - 3: Minkowski
            - 4: Chebyshev
            - 6: Cosine

        Defaults to 2.

    minkowski_power : double, optional
        Specifies the power of the Minkowski method. Only valid when DISTANCE_METHOD is 3.

        Defaults to 3.

    Returns
    -------

    DataFrame
        result for fast dtw, structured as follows:
            - LEFT_<ID column name of input table>: ID of one time series.
            - RIGHT_<ID column name of input table>: ID of the other time series.
            - DISTANCE: DTW distance of two time series.

        Statistics for time series, structured as follows:
            - STAT_NAME: Statistics name.
            - STAT_VALUE: Statistics value.

    Examples
    --------
    >>> result, stats = fast_dtw(conn_context, data, 5)

    """

    radius = arg('radius', radius, int)
    thread_ratio = arg('thread_ratio', thread_ratio, float)
    distance_method = arg('distance_method', distance_method, int)
    minkowski_power = arg('minkowski_power', minkowski_power, float)

    unique_id = str(uuid.uuid1()).replace('-', '_').upper()
    outputs = ['RESULT', 'STATS',]
    outputs = ['#PAL_FAST_DTW_{}_TBL_{}_{}'.format(name, id, unique_id) for name in outputs]
    res_tbl, stats_tbl = outputs

    param_rows = [('RADIUS', radius, None, None),
                  ('THREAD_RATIO', None, thread_ratio, None),
                  ('DISTANCE_METHOD', distance_method, None, None),
                  ('MINKOWSKI_POWER', None, minkowski_power, None)]

    try:
        param_t = ParameterTable(name='#PARAM_TBL')
        call_pal_auto(conn_context,
                      'PAL_FAST_DTW',
                      data,
                      param_t.with_data(param_rows),
                      *outputs)

    except dbapi.Error as db_err:
        logger.exception(str(db_err))
        try_drop(conn_context, '#PARAM_TBL')
        try_drop(conn_context, res_tbl)
        try_drop(conn_context, stats_tbl)
        raise

    #pylint: disable=attribute-defined-outside-init, unused-variable
    return conn_context.table(res_tbl), conn_context.table(stats_tbl)
