#
# Copyright (c) 2019 Mobikit, Inc.
#
# This source code is licensed under the MIT license found in the
# LICENSE file in the root directory of this source tree.
#

import pandas as pd
import numpy as np
import warnings
import os
from mobikit import feeds
from ..config import config
from sklearn.cluster import KMeans
import datetime


def standardize(df):
    returnDF = pd.DataFrame()
    cols = list(df)
    colID = None
    match = False
    for i in cols:
        for index, row in config.col_ref.iterrows():
            if i in row["Permutations"]:
                colID = row["ID"]
                match = True
                break
        if match:
            returnDF[colID] = df[i]
        else:
            returnDF[i.upper()] = df[i]
        match = False
    return returnDF


def generate_meta_feed(api_token=None, dataset_id=None):
    config.api_token = api_token
    dataframes = feeds.load(dataset_id)

    # produce metadata for each source
    meta_data = [config.meta_base for _ in range(len(dataframes))]

    # right now, the policy is that all source files must be pandas readable. If not, entire feed gets flagged. Eventually this should be fixed
    if isinstance(dataframes[0], pd.DataFrame):
        for i in range(len(meta_data)):
            meta_data[i]["pandas_readable"] = 1
            df_standard = standardize(dataframes[i])
            if "LONGITUDE" in df_standard and "LATITUDE" in df_standard:
                meta_data[i]["viz_readable"] = 1
            if (
                "TIME" in df_standard
                or "TIME_START" in df_standard
                or "TIME_FINISH" in df_standard
            ):
                meta_data[i]["temporal"] = 1
            meta_data[i]["stats"] = df_standard.describe().to_dict()
    return meta_data


def generate_meta_source(api_token=None, source_id=None):
    config.api_token = api_token
    dataframes = feeds.load(source_id, source=True)

    # produce metadata for each source
    meta_data = config.meta_base

    # right now, the policy is that all source files must be pandas readable. If not, entire feed gets flagged. Eventually this should be fixed
    if isinstance(dataframes, pd.DataFrame):
        meta_data["pandas_readable"] = 1
        df_standard = standardize(dataframes)
        if "LONGITUDE" in df_standard and "LATITUDE" in df_standard:
            meta_data["viz_readable"] = 1
        if "TIME" in df_standard:
            meta_data["temporal"] = 1
        meta_data["stats"] = df_standard.describe().to_dict()

    return meta_data


def augment(df):
    print("augmenting...")
    augmented_df = df.copy()
    augmented_df = augmented_df.reset_index(drop=True)
    augmented_df = add_turn_flags(augmented_df)
    augmented_df = add_hard_braking_flags(augmented_df)
    # augmented_df = self.add_spatial_coordinates(augmented_df)
    augmented_df = augmented_df.reset_index(drop=True)
    print("done!")
    return augmented_df


def add_turn_flags(df):
    # the plan is to use runge kutta method to model the path and then predict turns
    if "STEER_ANGLE" in df.columns:
        # turn ratio is 1:16 -> if ths wheels 45 degrees, it's a turn
        df["LEFT_TURN_FLAG"] = df["STEER_ANGLE"] > 100
        df["RIGHT_TURN_FLAG"] = df["STEER_ANGLE"] < -100
        df["TURN_FLAG"] = df["LEFT_TURN_FLAG"] + df["RIGHT_TURN_FLAG"]
        df["TURN_FLAG"] = df["TURN_FLAG"] > 0
        return df

    elif ("BEARING" in df.columns) & ("GPS SPEED" in df.columns):
        turn_rate = (
            0.001
        )  # if bearing is changing XX% per record, then the user is turning. THIS IS THE METRIC THAT NEEDS TO BE TUNED
        sampling = (
            1
        )  # this is the rate at which we compare bearing changes, aka every x samples
        left_turn = [0]
        right_turn = [0]
        col_size = df["BEARING"].size
        for i in range(0, col_size - sampling, sampling):
            bearing_i = df.loc[[i]]["BEARING"].values.squeeze()
            bearing_i_sample = df.loc[[i + sampling]]["BEARING"].values.squeeze()
            speed_i = df.loc[[i]]["GPS SPEED"].values.squeeze()
            change = 0
            if speed_i > 0:
                change = (bearing_i - bearing_i_sample) * 1.0 / bearing_i / speed_i
            if (change < 0) & (abs(change) > turn_rate):
                left_turn = [1 for j in range(sampling)]
            else:
                left_turn = [0 for j in range(sampling)]
            if (change > 0) & (abs(change) > turn_rate):
                right_turn = [1 for j in range(sampling)]
            else:
                right_turn = [0 for j in range(sampling)]
        df["LEFT_TURN_FLAG"] = left_turn
        df["RIGHT_TURN_FLAG"] = right_turn
        df["TURN_FLAG"] = left_turn + right_turn
        df["TURN_FLAG"] = df["TURN_FLAG"] > 0
        return df
    else:
        return df


def add_hard_braking_flags(df):
    # hard braking occurs at -0.55g's, or -5.39 m/s^2, or 21.9mph/s
    # https://copradar.com/chapts/references/acceleration.html
    # threshold = -3.3936575
    threshold = -3.0
    try:
        df["HARD_BRAKING_FLAG"] = df["ACCEL"] < threshold
        if "SPEED" in df.columns:
            df["BRAKESTATUS_MOVING"] = (df["SPEED"] > 1) & (df["BRAKESTATUS"] == 1)
    except:
        pass
    return df


def add_spatial_coordinates(df):
    try:
        lats = df["LATITUDE"]
        longs = df["LONGITUDE"]
        df["X"] = np.cos(lats) * np.cos(longs)
        df["Y"] = np.cos(lats) * np.sin(longs)
        df["Z"] = np.sin(lats)
    except:
        pass
    return df


def summarize(df, level="overall", statistic="mean"):
    if level == "overall":
        return overall_summary(df)
    elif level == "device":
        return device_summary(df)
    elif level == "device-trip":
        return device_trip_summary(df)
    else:
        print(
            "error! incorrect level input. please select between overall, device, or device-trip"
        )


def overall_summary(df):
    sub_df = df[
        [
            "ACCEL",
            "SPEED",
            "TURN_FLAG",
            "HARD_BRAKING_FLAG",
            "TURNSIGNAL",
            "LEFT_TURN_FLAG",
            "RIGHT_TURN_FLAG",
            "ABSSTATUS",
            "BRAKESTATUS",
            "LATITUDE",
            "LONGITUDE",
        ]
    ]
    return_df = sub_df.describe()
    return return_df.drop("count")


def device_summary(df):
    devices = list(set(df["DEVICE_ID"]))
    means_list = []
    try:
        for i in devices:
            sub_df = df[df["DEVICE_ID"] == i].mean(axis=0, numeric_only=True)
            sub_df["BRAKESTATUS_MOVING"] = df[
                (df["DEVICE_ID"] == i) & (df["SPEED"] > 0)
            ]["BRAKESTATUS"].mean()
            sub_df["ACCEL_ABS"] = df[df["DEVICE_ID"] == i]["ACCEL"].abs().mean()
            means_list.append(sub_df)

        summarized_df = pd.DataFrame(means_list).reset_index(drop=True)
        summarized_df_trim = summarized_df[
            [
                "DEVICE_ID",
                "ACCEL",
                "SPEED",
                "TURN_FLAG",
                "HARD_BRAKING_FLAG",
                "TURNSIGNAL",
                "LEFT_TURN_FLAG",
                "RIGHT_TURN_FLAG",
                "ABSSTATUS",
                "BRAKESTATUS",
                "LATITUDE",
                "LONGITUDE",
            ]
        ]
        return summarized_df_trim
    except:
        print("sorry! there's been an error")


def device_trip_summary(df):
    if "TRIP" in df:
        devices = list(set(df["DEVICE_ID"]))
        summarized_trips = []
        for i in devices:
            trips = list(set(df[df["DEVICE_ID"] == i]["TRIP"]))
            summarized_trips += [
                df[(df["TRIP"] == trip_id) & (df["DEVICE_ID"] == i)].mean(axis=0)
                for trip_id in trips
            ]
        # convert trip data to a dataframe
        summarized_df = pd.DataFrame(summarized_trips)
        return summarized_df
    else:
        print("sorry! this is not trip-level data")


def remove_anomalies(df):
    # TODO design remove anomalies algorthm at the device and trip levels
    return 0


def normalize(df, technique):
    # will accomodate min-max, z-score
    normalized_ranking = df.copy()
    if technique == "min-max":
        for i in list(df):
            if not (i == "DEVICE_ID"):
                normalized_ranking[i] = (df[i] - df[i].min()) / (
                    df[i].max() - df[i].min()
                )
    elif technique == "z-score":
        for i in list(df):
            if not (i == "DEVICE_ID"):
                normalized_ranking[i] = (
                    normalized_ranking[i] - normalized_ranking[i].mean()
                ) / normalized_ranking[i].std(ddof=0)

    normalized_ranking = normalized_ranking.reset_index(drop=True)
    return normalized_ranking


def describe(df, sample=300):
    print("scanning data...")

    # time
    end_time = datetime.datetime.strptime(df["DATE_TIME"].max(), "%Y/%m/%d %H:%M")
    start_time = datetime.datetime.strptime(df["DATE_TIME"].min(), "%Y/%m/%d %H:%M")
    time_diff = abs((end_time - start_time).days)

    # locations
    locations = geocode_sample(df, sample)
    states = list(set(locations["USPS"]))
    locations_str = ", ".join(states)

    # centroids
    centroid = geocode_row(df["LATITUDE"].mean(), df["LONGITUDE"].mean())

    # devices
    devices = list(set(df["DEVICE_ID"]))

    # results
    print(
        "this dataset spans over %s days and across %d vehicles"
        % (str(time_diff), len(devices))
    )
    print("the data spans across these sampled locations: %s" % locations_str)
    print(
        "the centroid of the dataset is in: %s, %s"
        % (str(centroid["NAME"].item()), str(centroid["USPS"].item()))
    )

    if sample < df.index.size:
        print("for a full geocoding, use learn().geocode_all(df)")
    return_file = {
        "days": time_diff,
        "devices": devices,
        "locations": locations,
        "centroid": centroid[["USPS", "NAME"]],
    }
    return return_file


def geocode_sample(df, sample):
    locations = []
    county_table = config.counties_ref.copy()
    county_table["FLAG"] = 0
    for i in range(sample):
        row = df.sample(1)
        longitude = row["LONGITUDE"].values.squeeze()
        latitude = row["LATITUDE"].values.squeeze()
        dist_x = (county_table["INTPTLONG"] * 1.0 - longitude * 1.0) ** 2
        dist_y = (county_table["INTPTLAT"] * 1.0 - latitude * 1.0) ** 2
        county_table["DIST"] = dist_x + dist_y
        locations.append(
            county_table[county_table["DIST"] == county_table["DIST"].min()][
                "GEOID"
            ].item()
        )
    return county_table[county_table["GEOID"].isin(locations)]


def geocode_row(latitude, longitude):
    county_table = config.counties_ref.copy()
    dist_x = (county_table["INTPTLONG"] * 1.0 - longitude * 1.0) ** 2
    dist_y = (county_table["INTPTLAT"] * 1.0 - latitude * 1.0) ** 2
    county_table["DIST"] = dist_x + dist_y
    return county_table[county_table["DIST"] == county_table["DIST"].min()]


def geocode_county(lat_field, lon_field, df):
    df["county"] = df.apply(geocode_row)
    return df


def cluster(model_type, df, n=3, remove_anomolies=False):
    if remove_anomolies:
        df = remove_anomalies(df)
    devices = list(set(df["DEVICE_ID"]))
    summary_list = []
    for i in devices:
        sub_df = df[df["DEVICE_ID"] == i]
        summary_list.append(generate_cluster_stats(sub_df))
    summary_df = pd.concat(summary_list)
    summary_df_normalized = normalize(summary_df, technique="min-max")
    summary_df_normalized = summary_df_normalized.drop("DEVICE_ID", axis=1)
    if model_type == "k-means":
        kmeans = KMeans(n_clusters=n, random_state=0).fit(summary_df_normalized)
        summary_df["GROUP"] = kmeans.labels_
        print(
            "clustered devices into %d groups. drivers with lower ranks exhibit more risky behavior"
            % (n)
        )
        # reorder the columns
        summary_df = summary_df[
            [
                "DEVICE_ID",
                "GROUP",
                "ACCEL_AVG",
                "SPEED_AVG",
                "TURN_SIGNAL_RATIO",
                "BRAKESTATUS_MOVING",
                "HARD_BRAKING_AVG",
            ]
        ]
        summary_df = summary_df.reset_index(drop=True)
        return summary_df
    else:
        print("that model type is unrecognized or unsupported")


def generate_cluster_stats(df):
    df["ACCEL_ABS"] = df["ACCEL"].abs()
    moving_df = df[df["SPEED"] > 0]
    summary_stats = {
        "DEVICE_ID": [int(df["DEVICE_ID"].mean())],
        "SPEED_AVG": [df["SPEED"].mean()],
        "ACCEL_AVG": [df["ACCEL_ABS"].mean()],
        "HARD_BRAKING_AVG": [
            df["HARD_BRAKING_FLAG"].sum() * 1.0 / len(set(df["TRIP"]))
        ],
        "TURN_SIGNAL_RATIO": [
            df["TURN_FLAG"].sum() * 1.0 / ((df["TURNSIGNAL"] > 0) * 1.0).sum()
        ],
        "BRAKESTATUS_MOVING": [moving_df["BRAKESTATUS"].mean()],
    }
    return pd.DataFrame(summary_stats)
