import pandas as pd

import matplotlib.pyplot as plt
import collections
import numpy as np
import os
import pandas as pd
import operator
from scipy.spatial import distance
from scipy.spatial.distance import euclidean
import locuspeerexplorer.params

dirname, filename = os.path.split(os.path.abspath(__file__))


def get_top_n_fms(
    df_data,
    area,
    year,
    n_fms=10,
    metric="PC_ESTAB",
    weight_metric="masking",
    filter_pop=False
):
    """
    Get peers using the top n_fms FMs ranked by the presence of the FMs in
    the area

    :param n_fms: Number of FMs to use
    :type n_fms: int
    :param n_peers: Number of peers to return
    :type n_peers: int
    :return: Peers based on most present FMs in the area
    :rtype: list
    """
    assert area in list(
        df_data["AREA"]), "Area code not present in the dataset"
    df_data = df_data[df_data["YEAR"] == year]

    if filter_pop:
        df_data = _filter_population(df_data, area)
    pc_fms = [c for c in df_data.columns if "-"
              + metric in c]
    df_area = df_data[pc_fms][df_data["AREA"] == area].T.reset_index()
    df_area.columns = ["FMs", "ESTAB"]
    df_area.sort_values("ESTAB", inplace=True, ascending=False)
    ranked_fms = list(df_area["FMs"])
    return ranked_fms


def show_ratio_closest_furthest(df_data, year):

    ratios = {}
    for area in df_data.sample(n=10)['AREA']:
        print(area)
        ratios[area] = []
        ranked_fms = get_top_n_fms(df_data, area, year)
        for i in range(5, 300, 10):
            cols = ranked_fms[:i]
            r = _ratio_euclidean_distance(
                df_data[df_data['YEAR'] == year], cols, area)
            ratios[area].append(r)
        print(ratios[area][-1])
        plt.plot(list(range(5, 300, 10)), ratios[area])
    plt.show()


def show_ratio_to_closest(df_data, year):

    ratios = {}
    for area in df_data.sample(n=1)['AREA']:
        print(area)

        ranked_fms = get_top_n_fms(df_data, area, year)
        for i in range(3, 50, 2):
            ratios[i] = []
            cols = ranked_fms[:i]
            r = _ratio_euclidean_distance(
                df_data[df_data['YEAR'] == year], cols, area, l=True)
            ratios[i] = r
            plt.plot(range(len(ratios[i])), ratios[i], label=i)
    plt.legend()
    plt.show()


def show_correlation(df_data, year):

    ratios = {}
    for area in df_data.sample(n=10)['AREA']:
        print(area)
        ranked_fms = get_top_n_fms(df_data, area, year)
        for i in range(2, 100, 2):
            ratios[i] = []
            cols = ranked_fms[:i]
            r = _ratio_euclidean_distance(
                df_data[df_data['YEAR'] == year], cols, area, l=True)
            ratios[i] = r

            # if i > 3:
            #     print(np.corrcoef(ratios[i-2], ratios[i]))

        correlations = [np.corrcoef(ratios[n], ratios[n-2])[0][1]
                        for n in range(4, 100, 2)]
        plt.plot(range(4, 100, 2), correlations)
        plt.axhline(y=0.99, color='r', linestyle='-')
        plt.xlabel('Number of FMs')
    plt.legend()
    plt.show()


def _ratio_euclidean_distance(df_data, cols, area, l=False):
    """
    Compute the euclidean distance to area for all rows (=all areas)
    on all columns in cols
    :param df: Data
    :type df: dataframe
    :param cols: Columns to use to compute the distance
    :type cols: list
    :param area: area to compute the distance to
    :type area: int
    :param n_peers: Number of peers to return
    :type n_peers: int
    :return: List of peers
    :rtype: list
    """

    # Weight distance outputs
    df = (df_data.copy()).dropna(subset=cols)[(["AREA"] + cols)]
    df.set_index("AREA", inplace=True)

    def standardize(c):
        return (c - c.mean()) / c.std()

    df = df.apply(standardize, axis=0)
    df_area = df.loc[area]
    df = df.drop(area)

    # Euclidean distance
    df_dist = (df - df_area).pow(2)
    df_dist = df_dist.sum(axis=1).pow(0.5)
    # df_dist = df.corrwith(df_area, axis=1)
    df_dist = df_dist.reset_index()
    df_dist.columns = ["AREA", "DIST"]
    dists = list(df_dist["DIST"])
    # dists = list(df_dist.sort_values("DIST", ascending=False)['DIST'])
    if l:
        return dists
    ratio = np.max(dists)/np.min(dists)
    # ratio = dists[2]/dists[1]
    return ratio


if __name__ == '__main__':

    df_data = pd.read_csv(os.path.join(
        dirname, "../data/processed/metrics_outcomes.csv"))
    df_county = pd.read_csv(os.path.join(
        dirname, "../data/processed/county_metrics_outcomes.csv"))
    df_msa_def = pd.read_csv(
        os.path.join(dirname, "../data/external/omb_msa_1990_2018.csv")
    )
    df_county_dist = pd.read_csv(
        os.path.join(
            dirname, "../data/processed/sf12010countydistance500miles.csv")
    )

    # show_ratio_closest_furthest(df_data, 2016)
    # show_ratio_to_closest(df_data, 2016)
    show_correlation(df_data, 2016)
