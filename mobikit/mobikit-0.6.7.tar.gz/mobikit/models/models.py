#
# Copyright (c) 2019 Mobikit, Inc.
#
# This source code is licensed under the MIT license found in the
# LICENSE file in the root directory of this source tree.
#

from math import ceil

import pandas as pd
import geopandas as gd
import mobikit_utils as mku
from mobikit_utils.schema.points import constants

from ..config import config


def to_trips(df, tm, lat, lng, speed, device=None):
    r"""
    Derives trip_ids from vehicle behavior data. Returns a DataFrame containing
    a new column labeled "trip_id_derived", applied to each row.

    Parameters
    ----------
    df : pandas.DataFrame
        Input DataFrame
    tm : str
        Name of time column
    lat : str
        Name of latitude column
    lng : str
        Name of longitude column
    speed : str
        Name of speed column
    device : str, optional
        Name of device column

    Returns
    -------
    df : pandas.DataFrame
        DataFrame containing trip ids

    Note
    ----
    The dataset will be sorted after being returned. How it is sorted is dependent
    on what is passed to the function. It sorts by device id and time or only time
    if device id is not given.
    """

    df[constants.primary_spatial] = _create_geom(df, lat, lng)
    return_df = mku.spatial.to_trips(
        df, tm, speed, point=constants.primary_spatial, device=device
    )

    return return_df.drop(constants.primary_spatial, axis=1)


def derive_speed(df, tm, lat, lng, device=None, trip=None, format="mph"):
    """ 
    Derives speed from vehicle data. Returns a DataFrame containing a new column
    labeled "speed_derived". Derives speed using great_circle distance. Format can
    be specified for the type of speed to be outputted. 

    Parameters
    ----------
    df : pandas.DataFrame
        Input DataFrame
    tm : str
        Name of time column
    lat : str
        Name of latitude column
    lng : str
        Name of longitude column
    device : str optional
        Name of device column
    trip : str, optional
        Name of trip column
    format : str, {mph, mps, kmh}
        Unit for speed output
    
    Returns
    -------
    df : pandas.DataFrame
        DataFrame containing derived speed
    """

    df[constants.primary_spatial] = _create_geom(df, lat, lng)

    return_df = mku.spatial.derive_speed(
        df,
        tm,
        coords=constants.primary_spatial,
        device=device,
        trip=trip,
        format=format,
    )

    return return_df.drop(constants.primary_spatial, axis=1)


def is_highway_like(
    df, tm, speed, trip_id, vehicle_id=None, smoothing_interval=10, threshold=50
):
    r"""
    Segments highway-like travel from city-like travel.
    Main use is for fuel consumption and does not classify physically being
    on a highway. Only uses driving behavior for determination.

    Parameters
    ----------
    df : pandas.DataFrame
        Input DataFrame
    tm : str
        Name of time column
    trip_id : str
        Name of trip id column
    vehicle_id : str, optional
        Name of vehicle id column
    smoothing_interval : int, optional
        Time length of interval for smoothing, in seconds. Defaults to 10
    threshold : int, optional
        Speed value for determining highway like behavior. Defaults to 50

    Returns
    -------
    df : pandas.DataFrame
        DataFrame containing boolean values in the is_highway_like column

    Note
    ----
    The dataset will be sorted after being returned. How it is sorted is dependent
    on what is passed to the function. It sorts by device id then trip id then time
    or trip id then time, if device id is not given.
    """

    extra_cols = []

    if not (set([tm, speed, trip_id]).issubset(df.columns)):
        raise KeyError(
            "One or more of the arguments you passed are not in the dataframe"
        )

    # Sort the df by vehicle_id and trip_id
    df = _sort(df, tm, trip_id, vehicle_id)

    if smoothing_interval != 0:
        # Smooth the df using a rolling window
        df = _smooth_data(
            df, tm, trip_id, speed, vehicle_id, smoothing_interval=smoothing_interval
        )

        # Reset the speed_column to sm_speed so that the remaining functions use the smoothed speed
        speed = "sm_speed"
        extra_cols = [speed]

    # Flag points of high speed using a aggregate and threshold value
    df = _flag_highway_like(df, speed, threshold=threshold)

    # Drop the 0th row since it gets mangled in the functions above
    # Extra columns used for indexing are also dropped
    df = df.drop(extra_cols, axis=1).drop(0).reset_index()

    return df


def _create_geom(df, lat, lng):
    """
    Creates a points geom column if there isn't one.
    """
    return gd.points_from_xy(df[lng], df[lat])


def _sort(df, tm, trip_id, vehicle_id):
    """
    Sorts the dataframe given certain input paramters
    """

    # If vehicle_id and trip are given sort by them,
    # else sort by just vehicle_id, and else that,
    # sort by just time

    if vehicle_id:
        cols = [vehicle_id, trip_id, tm]
    else:
        cols = [trip_id, tm]

    df = df.sort_values(cols).reset_index(drop=True)

    return df


def _smooth_data(df, tm, trip_id, speed, vehicle_id, smoothing_interval=10):
    """
    Smoothes the data points using a rolling average. Window size is
    calculated using the median of the time deltas in the dataset.
    """

    # Create a column with the dates as datetime
    df["datetime"] = pd.to_datetime(df[tm])

    # Create a time_delta column using panads datetime functions
    df["time_delta"] = (df["datetime"] - df["datetime"].shift(1)).dt.total_seconds()

    # Finds the most likely time delta between points
    median_time_delta = df["time_delta"].median()

    # Finds the size of the window by dividing the requested amount of time by
    # the most likely time delta, rounded up.
    window_size = ceil(smoothing_interval / median_time_delta)

    # Create the smoothed speed column by grouping by trip_id then creating a rolling mean
    if vehicle_id:
        cols = [vehicle_id, trip_id]
    else:
        cols = [trip_id]

    df["sm_speed"] = (
        df.groupby(cols)[speed]
        .rolling(window=window_size, min_window=1)
        .mean()
        .reset_index(drop=True)
    )

    df.drop(["time_delta", "datetime"], axis=1, inplace=True)

    return df


def _flag_highway_like(df, speed, threshold=50):
    """
    Flags highway like points by comparing to a threshold.
    """

    df["highway_like"] = df[speed] > threshold

    return df
