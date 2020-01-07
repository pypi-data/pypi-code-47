import numpy as np
import pandas as pd

import matplotlib.pyplot as plt
from matplotlib import rcParams

import seaborn as sns

from typing import List, Sequence, Union
import warnings

__all__ = ['bar', 'BarSigDrawer']


class BarCapSizer(object):
    def __init__(self, caps, size=1.0):
        self.size = size
        self.caps = caps
        self.ax = self.caps[0].axes
        self.resize()

    def resize(self):
        ppd = 72. / self.ax.figure.dpi
        trans = self.ax.transData.transform
        s = ((trans((self.size, 1)) - trans((0, 0))) * ppd)[0]
        for i, cap in enumerate(self.caps):
            cap.set_markersize(s)


class BarSigDrawer(object):
    """Container for drawing significance markers on bar graphs.

    Initialize class for drawing significance markers on graph of `N` _bars.

    Args:
        thresholds (:obj:`Sequence[float]`, optional): Decreasing thresholds for significance markers.
            Defaults to (0.05, 0.01, 0.001).
        use_hbar(:obj:`bool`, optional): If specified, horizontal lines (called hbars) are drawn between different
            _bars. Significance markers are drawn in between Defaults to `True`.
        on_bar (:obj:`str`, optional): Where marker should appear if `use_hbar=False`.
            Either `'min'` or `'max'`. Defaults to `'min'`.
        dy (float): Spacing between top of bar/errorbar and markers.

    Keyword Args:
        marker (str): The significance marker to use. Defaults to `'*'`.
        marker_size (int): The marker size. Defaults to `matplotlib.rcParams['lines.markersize']`.
        marker_color: The marker color. Defaults to `'black'`.
        marker_opacity (float): The marker opacity. Defaults to `1.0`.
        line_width (float): Width of hbar lines. Defaults to `matplotlib.rcParams['lines.linewidth']`.
        line_color: Line color for hbar lines. Defaults to `'black'`.
    """

    @classmethod
    def get_default_args(cls):
        return {
            'ax_dy': None,
            'marker': '*',
            'marker_size': rcParams['lines.markersize'],
            'marker_color': 'black',
            'marker_opacity': 1.0,
            'line_width': rcParams['lines.linewidth'],
            'line_color': 'black',
        }

    def __init__(self, thresholds: Sequence[float] = (0.05, 0.01, 0.001), use_hbar: bool = True, on_bar: str = 'min',
                 dy: float = None, **kwargs):
        default_args = self.get_default_args()
        for k in default_args.keys():
            if k in kwargs:
                default_args[k] = kwargs.get(k)

        self.thresholds = thresholds
        self.default_args = default_args
        self.use_hbar = use_hbar
        self.dy = dy

        self._on_bar = None
        self.on_bar = on_bar

        self.marker_bar_size = None

        # Updated whenever drawn.
        self._bars = None
        self._p_sig_matrix = None
        self._num_groups = None
        self._errs = None
        self._loc_matrix = None

    def draw(self, bars: Sequence[plt.Rectangle], p_sig_matrix: np.ndarray, errs: Sequence[float] = None,
             ax: plt.axis = None):
        """Draw significance markers.

        Args:
            bars (Sequence[plt.Rectangle]): A collection of rectangles specifying the _bars in the bar graph.
            p_sig_matrix (np.ndarray): A `N x N` symmetric matrix specifying p-values for combinations between _bars.
                If value is `np.nan`, no significance marker will be drawn.
            errs (:obj:`Sequence`, optional): A collection of errors corresponding to the errors on the bar.
                If specified, error _bars will be drawn. Defaults to `None`.
            ax (:obj:`plt.axis`, optional): If specified, plot on given axis. Otherwise, new figure will be created.

        Returns:
            plt.axis: A matplotlib axis.
        """
        if not ax:
            _, ax = plt.subplot(1, 1)

        if not isinstance(p_sig_matrix, np.ndarray):
            p_sig_matrix = np.asarray(p_sig_matrix)

        self._num_groups = p_sig_matrix.shape[0]
        self.__validate_p_matrix__(p_sig_matrix, self._num_groups)

        if not self.use_hbar and self._num_groups != 2:
            warnings.warn(
                '`use_hbar` option specified as False. will be difficult to differentiate multi-group significance.')

        loc_matrix = self.__compute_locs(bars, errs)
        if loc_matrix.ndim != 2 or loc_matrix.shape[0] != self._num_groups or loc_matrix.shape[1] != 2:
            raise ValueError(
                '_loc_matrix should be a nx2 matrix with columns 0 and 1 corresponding to x and y locations respectively')

        self._bars = bars
        self._p_sig_matrix = p_sig_matrix
        self._errs = errs
        self._loc_matrix = loc_matrix

        yticks = ax.get_yticks()
        dy = yticks[1] - yticks[0] if not self.default_args['ax_dy'] else self.default_args['ax_dy']
        self.marker_bar_size = 0.05 * dy

        self.__init_curr_height()

        if self.use_hbar:
            self.__draw_hbar_line(ax)
        else:
            self.__draw_only_marker(ax)

        return ax

    def __compute_locs(self, bars, errs):
        locs = []
        for ind, b in enumerate(bars):
            rect = bars[ind]
            x, height, width = rect.get_x(), rect.get_height(), rect.get_width()

            y = height + errs[ind] if errs is not None else height
            x = x + width / 2.0

            locs.append([x, y])

        return np.asarray(locs)

    def __init_curr_height(self):
        curr_heights = dict()
        for g in range(self._num_groups):
            curr_heights[g] = self.__get_yloc__(g)

        self.curr_heights = curr_heights

    def __get_marker_coords(self, g1, g2):
        on_bar = self.on_bar

        g1_bar_height = self._bars[g1].get_height()
        g2_bar_height = self._bars[g2].get_height()
        heights = [g1_bar_height, g2_bar_height]

        inds = [g1, g2]
        min_ind = np.argmin(heights)
        max_ind = np.argmax(heights)
        curr_ind = None

        dy = self.marker_bar_size * 10 if not self.dy else self.dy

        if on_bar == 'min':
            curr_ind = inds[min_ind]
        elif on_bar == 'max':
            curr_ind = inds[max_ind]

        return self.__get_xloc__(curr_ind), self.__get_yloc__(curr_ind) + dy

    def __draw_only_marker(self, ax: plt.axis):
        for g1 in range(self._num_groups):
            for g2 in range(g1 + 1, self._num_groups):
                p = self._p_sig_matrix[g1, g2]
                num_markers = self.__get_num_markers(p)

                if not num_markers:
                    continue

                x1, y1 = self.__get_marker_coords(g1, g2)

                marker = self.default_args['marker'] * num_markers

                ax.text(x1, y1, marker,
                        ha='center', va='baseline',
                        fontsize=self.default_args['marker_size'],
                        color=self.default_args['marker_color'],
                        alpha=self.default_args['marker_opacity'])

    def __draw_hbar_line(self, ax: plt.axis):
        # Draw vertical line up to the tallest point if that element has a signficant measure
        for g1 in range(self._num_groups):
            for g2 in range(g1 + 1, self._num_groups):
                p = self._p_sig_matrix[g1, g2]
                num_markers = self.__get_num_markers(p)

                if not num_markers:
                    continue

                x1, y1, x2, y2 = self.__get_hbar_coords__(g1, g2)
                ax.plot([x1, x2], [y1, y2],
                        color=self.default_args['line_color'],
                        linestyle='-',
                        Linewidth=self.default_args['line_width'])
                ax.plot([x1, x1], [y1 - self.marker_bar_size, y2],
                        color=self.default_args['line_color'],
                        linestyle='-',
                        Linewidth=self.default_args['line_width']
                        )
                ax.plot([x2, x2], [y1 - self.marker_bar_size, y2],
                        color=self.default_args['line_color'],
                        linestyle='-',
                        Linewidth=self.default_args['line_width']
                        )

                marker = self.default_args['marker'] * num_markers

                ax.text((x1 + x2) / 2, y1, marker,
                        ha='center', va='baseline',
                        fontsize=self.default_args['marker_size'],
                        color=self.default_args['marker_color'],
                        alpha=self.default_args['marker_opacity'])

    def __get_num_markers(self, p):
        thresholds = self.thresholds
        count = 0
        for t in thresholds:
            if p > t:
                break
            count += 1
        return count

    def __get_yloc__(self, i):
        return self._loc_matrix[i, 1]

    def __get_xloc__(self, i):
        return self._loc_matrix[i, 0]

    def __get_hbar_coords__(self, g1, g2):
        yloc_g1 = self.curr_heights[g1]
        yloc_g2 = self.curr_heights[g2]

        xloc_g1 = self.__get_xloc__(g1)
        xloc_g2 = self.__get_xloc__(g2)

        dy = self.marker_bar_size * 10
        hbar_height = max(yloc_g1, yloc_g2) + dy

        for i in range(g1 + 1, g2):
            yloc = self.curr_heights[i]
            if yloc > hbar_height:
                hbar_height = yloc + dy

        for i in range(g1, g2 + 1):
            self.curr_heights[i] = hbar_height

        return xloc_g1, hbar_height, xloc_g2, hbar_height

    def __validate_p_matrix__(self, p_matrix: np.ndarray, num_classes):
        if (p_matrix.ndim != 2) or not np.all(p_matrix == p_matrix.transpose([1, 0])):
            print(p_matrix)
            raise ValueError('_p_sig_matrix must be 2D symmetric matrix of shape (%d, %d) with diagonal of 1s' %
                             (num_classes,
                              num_classes))

        if p_matrix.shape[0] != num_classes or p_matrix.shape[1] != num_classes:
            raise ValueError('_p_sig_matrix must be 2D symmetric matrix of shape (%d, %d) with diagonal of 1s' %
                             (num_classes,
                              num_classes))

        if not (np.abs(np.diagonal(p_matrix)) > max(self.thresholds)).all():
            raise ValueError('_p_sig_matrix must be 2D symmetric matrix of shape (%d, %d) with diagonal of 1s' %
                             (num_classes,
                              num_classes))

    @property
    def on_bar(self):
        return self._on_bar

    @on_bar.setter
    def on_bar(self, loc):
        if loc not in ['min', 'max']:
            raise ValueError("`on_bar` must be one of the following options: {}".format(['min', 'max']))
        self._on_bar = loc


def bar(df_mean, df_error=None, p_matrices: Sequence[np.ndarray] = None, sig_drawer: BarSigDrawer = None, ax=None,
        bar_width: float = None, opacity: float = 0.9, capsize: int = 5, spacing: float = 0.0, **kwargs):
    """Draw bar graph.

    Args:
        df_mean: A DataFrame/ndarray with dimensions # experiments x # metrics (i.e. experiments span rows, samples
            span cols).
        df_error (optional): A DataFrame/ndarray with dimensions # experiments x # metrics (i.e. experiments span rows,
            samples span cols). If specified, error _bars will be drawn.
        p_matrices (:obj:`Sequence[np.ndarray]`, optional)
        sig_drawer (:obj:`BarSigDrawer`, optional): Initialized drawer for significance markers. If not specified, no
            significance markers will be drawn.
        ax (:obj:`plt.axis`, optional): If specified, plot on given axis. Otherwise, new figure will be created.
        bar_width (:obj:`float`, optional): Bar width. If not specified, automatically calculated. Defaults to `None`.
        opacity (:obj:`float`, optional): Bar opacity. Defaults to `0.9`.
        capsize (:obj:`int`, optional): Capsize of error bar. Defaults to `5`.
        spacing (:obj:`float`, optional): The spacing between groups (if multiple). Defaults to `0.`.

    Keyword Args:
        cpal (list): Colors for plotting scatter points. Defaults to `seaborn.color_palette("pastel")`.
        line_width (int): Line width for error _bars. Defaults to `matplotlib.rcParams['lines.linewidth']`.
        line_color: Line color for error _bars. Defaults to `'gray'`.
        x_label: The x_labels to print. Only specify if inputs are of type `np.ndarray`. If input is `pd.DataFrame`,
            defaults to unique values in group.
        labels: The labels of the different experiments.

    Returns:
        plt.axis: A matplotlib axis.
    """
    has_df_error = df_error is not None

    default_args = {'cpal': sns.color_palette("pastel", 8),
                    'line_color': 'gray',
                    'line_width': rcParams['lines.linewidth'],
                    'x_label': ['0'],
                    'labels': None,
                    }

    for k in default_args.keys():
        if k in kwargs:
            default_args[k] = kwargs.get(k)

    if has_df_error and type(df_mean) != type(df_error) or df_mean.shape != df_error.shape:
        raise TypeError('Type mismatch. `d1` and `d2` must be of the same type and shape.')

    # handle edge case of 1D
    if type(df_mean) in [pd.DataFrame, pd.Series] and df_mean.ndim == 1:
        default_args['labels'] = df_mean.index.tolist()
        df_mean = np.asarray(df_mean)
        df_error = np.asarray(df_error) if has_df_error else df_error

    names = default_args['labels'] if default_args['labels'] else None
    input_type = type(df_mean)
    if input_type is np.ndarray:
        df_mean = pd.DataFrame(df_mean, columns=default_args['x_label'], index=names).transpose()
        if has_df_error:
            df_error = pd.DataFrame(df_error, columns=default_args['x_label'], index=names).transpose()

    if type(p_matrices) is not list:
        p_matrices = [p_matrices]

    if has_df_error and df_mean.shape != df_error.shape:
        raise ValueError("Both dataframes must be same shape. df_mean: {}, df_error: {}".format(df_mean.shape,
                                                                                                df_error.shape))

    cpal = default_args['cpal']
    num_bars = df_mean.shape[1]
    if not bar_width:
        bar_width = (2 - spacing / 2) / num_bars

    if len(cpal) < num_bars:
        raise ValueError('cpal only has %d colors, but %d _bars' % (len(cpal), num_bars))

    x_labels = df_mean.index.tolist()
    n_groups = len(x_labels)
    x_index = np.arange(0, n_groups * 2, 2)

    columns = df_mean.columns.tolist()

    if not ax:
        fig, ax = plt.subplots()

    df_mean_arr = np.asarray(df_mean)
    df_error_arr = np.asarray(df_error) if has_df_error else None

    p = []
    e = []
    errs = []
    for ind in range(len(columns)):
        sub_means = df_mean_arr[..., ind]
        sub_errors = df_error_arr[..., ind] if has_df_error else None

        p.append(ax.bar(x_index + bar_width * ind, sub_means, bar_width,
                        alpha=opacity,
                        color=cpal[ind],
                        label=columns[ind],
                        edgecolor=default_args['line_color'],
                        linewidth=default_args['line_width'],
                        bottom=0))

        if has_df_error:
            e.append(ax.errorbar(x_index + bar_width * ind, sub_means,
                                 yerr=[np.zeros(sub_errors.shape), sub_errors],
                                 ecolor=default_args['line_color'],
                                 elinewidth=default_args['line_width'],
                                 capsize=capsize,
                                 capthick=default_args['line_width'],
                                 linewidth=0))
            errs.append(sub_errors)

    for eb in e:
        BarCapSizer(eb.lines[1], 0.8 * bar_width)

    delta = (len(columns) - 1) * bar_width / 2
    ax.set_xticks(x_index + delta)
    ax.set_xticklabels(x_labels)

    if not p_matrices:
        return ax

    if not sig_drawer:
        sig_drawer = BarSigDrawer()

    yticks = ax.get_yticks()
    dy = (yticks[1] - yticks[0]) * 1.2
    if sig_drawer.default_args['ax_dy'] is None:
        sig_drawer.default_args['ax_dy'] = dy

    for i in range(n_groups):
        bars_g = []
        errs_g = [] if has_df_error else None
        for j in range(len(p)):
            bars_g.append(p[j][i])
            if has_df_error is not None:
                errs_g.append(errs[j][i])

        if p_matrices[i] is not None:
            sig_drawer.draw(bars=bars_g, p_sig_matrix=p_matrices[i], errs=errs_g, ax=ax)
