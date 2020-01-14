from ..config import *

def scatter(data, size, hue=False):
    """
    """
    df = check_data_type(data)

    if hue is not False:
        hue = data[col]
    else:
        hue = None

    fig, ax = plt.subplots(figsize=size)
    sizes   = (20, 400)
    sb.scatterplot(df[ev], df[amu], size=df[sem],
                   hue=hue, sizes=sizes, legend=False, ax=ax)
    return fig, ax
