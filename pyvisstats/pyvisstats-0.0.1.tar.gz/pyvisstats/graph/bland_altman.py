import numpy as np
import pandas as pd

import matplotlib.pyplot as plt
from matplotlib import rcParams

import seaborn as sns
from copy import deepcopy

__all__ = ['bland_altman']


def bland_altman(d1, d2, ax=None, value_col=None, group_by=None, order=None, **kwargs):
    """Draw a Bland Altman (BA) plot between results of two experiments.

    Difference array is taken as :math:`d2-d1`.

    Args:
        d1: A 1D array-like or DataFrame.
        d2: A 1D array-like or DataFrame.
        ax (:obj:`plt.axis`, optional): If specified, plot on given axis. Otherwise, new figure will be created.
        value_col (:obj:`int` or :obj:`str`, optional): DataFrame column name/index that corresponds to values.
            Must be specified if inputs are DataFrames.
        group_by (:obj:`int` or :obj:`str`, optional): If specified, DataFrame column header to group scatter points by.
            Defaults to `None`. Can only be set if input is a `pd.DataFrame`.
        order (list[str]): The ordering of the groups specified by `group_by`. Defaults to `None`.

    Keyword Args:
        ax_label_format (str): A format string for the y and x labels. Defaults to `'%s'`.
        cpal (list): Colors for plotting scatter points. Defaults to `seaborn.color_palette("pastel")`.
        line_width (int): Line width for ba plot. Defaults to `matplotlib.rcParams['lines.linewidth']`.
        line_color: Line color for ba plot. Defaults to `'gray'`.
        marker (str): Marker for plotting scatter points. Defaults to `'o'`.
        marker_size (float): Marker size. Defaults to `matplotlib.rcParams['lines.markersize']`.

    Returns:
        tuple: Tuple containing:

            plt.axis: A matplotlib axis.
            float: Mean of `d2-d1`.
            float: Standard deviaition of `d2-d1`.
    """
    default_args = {'ax_label_format': '%s',
                    'cpal': sns.color_palette("pastel", 8),
                    'marker': 'o',
                    'marker_size': rcParams['lines.markersize'],
                    'line_color': 'gray',
                    'line_width': rcParams['lines.linewidth'],
                    }

    for k in default_args.keys():
        if k in kwargs:
            default_args[k] = kwargs.get(k)

    value_col = value_col
    group_by = group_by
    group_by_order = order
    if type(d1) != type(d2):
        raise TypeError('Type mismatch. `d1` and `d2` must be of the same type.')

    input_type = type(d1)
    if input_type is np.ndarray and group_by:
        raise ValueError('Cannot specify `group_by` argument with inputs of type np.ndarray')

    if input_type is pd.DataFrame:
        if value_col is None:
            raise ValueError('`value_col` must be specified with DataFrame input')

        d1_vals = np.array(d1[value_col])
        d2_vals = np.array(d2[value_col])
    else:
        value_col = 'value'
        d1_vals = np.array(d1)
        d2_vals = np.array(d2)

    if not ax:
        fig, ax = plt.subplots()

    diff_arr = (d2_vals - d1_vals).flatten()
    mean_arr = ((d1_vals + d2_vals) / 2).flatten()

    if input_type is pd.DataFrame:
        df_diff = deepcopy(d1)
        df_diff[value_col] = diff_arr

        df_mean = deepcopy(d2)
        df_mean[value_col] = mean_arr
    else:
        df_diff = pd.DataFrame(diff_arr, columns=[value_col])
        df_mean = pd.DataFrame(mean_arr, columns=[value_col])

    if not group_by:
        df_diff['_temp_group'] = pd.Series(['A'] * len(diff_arr), index=df_diff.index)
        df_mean['_temp_group'] = pd.Series(['A'] * len(mean_arr), index=df_mean.index)
        group_by = '_temp_group'

    # Calculate the mean and std of ALL values over all regions for the BA analysis
    ba_mean = np.mean(diff_arr)
    ba_std = np.std(diff_arr)

    unique_groups = sorted(list(df_diff[group_by].unique()))
    if group_by_order:
        if len(set(unique_groups).intersection(set(group_by_order))) != len(unique_groups):
            raise ValueError('`order` does not account for all unique values in column `%s`.' % group_by)
        unique_groups = group_by_order
    num_unique_groups = len(unique_groups)

    # color palette
    cpal = default_args['cpal']

    for num in range(num_unique_groups):
        group_val = unique_groups[num]

        diff_vals = df_diff[(df_diff[group_by] == group_val)]
        diff_vals = diff_vals[value_col]
        mean_vals = df_mean[(df_mean[group_by] == group_val)]
        mean_vals = mean_vals[value_col]

        ax.plot(mean_vals, diff_vals,
                label=group_val,
                color=cpal[num],
                LineStyle="",
                Marker=default_args['marker'],
                MarkerSize=default_args['marker_size'])

    line_color = default_args['line_color']
    line_width = default_args['line_width']
    ax.axhline(ba_mean, color=line_color, linestyle=':', Linewidth=line_width)
    ax.axhline(ba_mean + 1.96 * ba_std, color=line_color, LineStyle='--', LineWidth=line_width)
    ax.axhline(ba_mean - 1.96 * ba_std, color=line_color, LineStyle='--', LineWidth=line_width)

    ax.grid(which="Major")

    label = default_args['ax_label_format']
    ax.set_ylabel(label % 'Difference')
    ax.set_xlabel(label % 'Mean')

    return ax, ba_mean, ba_std
