"""Functions for visualization purposes in Data Science tasks.
"""

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def plotHeatmapBetweenColumns(
        dataframe: pd.DataFrame,
        size: tuple,
        savefig=False,
        pathAndFileName='heatmap') -> plt.axes:
    """Plot heatmap between values of multiple columns in a Pandas dataframe.

    Arguments:
        dataframe {pd.DataFrame} -- Pandas dataframe
        size {tuple} -- Size of output figure

    Keyword Arguments:
        savefig {bool} -- True to save figure (default: {False})
        pathAndFileName {str} -- Filepath (default: {'heatmap'})

    Returns:
        plt.axes -- Matplotlib axes object
    """
    plt.figure(figsize=size)

    axes = sns.heatmap(dataframe, vmin=-1, cmap='coolwarm', annot=True)

    if savefig:
        plt.savefig(pathAndFileName)

    return axes
