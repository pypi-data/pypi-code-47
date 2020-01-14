from ..config import *

def scatter3d(data, size):
    """
    """
    df = check_data_type(data)

    fig = plt.figure(figsize=size)
    ax  = fig.add_subplot(111, projection='3d')
    ax.scatter(df[amu], df[ev], df[sem], c=df[col])
    ax.set_zscale('log')
    return fig, ax
