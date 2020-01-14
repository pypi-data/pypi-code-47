from ..config import *

def line3d(data, size):
    """
    """
    df = check_data_type(data)

    fig = plt.figure(figsize=size)
    ax  = fig.add_subplot(111, projection='3d')
    ax.plot(df[amu], df[ev], df[sem])
    return fig, ax
