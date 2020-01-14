from ..config import *

def bar(data, size):
    """
    """
    df = check_data_type(data)

    fig, ax = plt.subplots(figsize=size)
    df.plot.bar(y=sem, ax=ax, legend=None)
    return fig, ax
