from ..config import *

def line(data, size, ls):
    """
    """
    df0 = check_data_type(data)
    
    fig, ax = plt.subplots(figsize=size)
    for label, df in df0.groupby(amu):
        c    = df[col].iloc[1]
        m    = df[mar].iloc[1]
        yerr = df[std].iloc[1]
        df.plot(x=ev, y=sem, linestyle=ls, marker=m,
                c=c, yerr=std, ax=ax, label=label)

    return fig,ax
