from ..config import *

def barx3d(data, size):
    """
    """
    df = check_data_type(data)

    i = len(data[ev])
    z = np.zeros(i)
    fig = plt.figure(figsize=size)
    ax  = fig.add_subplot(111, projection='3d')
    ax.bar(df[amu], df[ev], zs=df[sem])
    return fig, ax
