import numpy as np
import matplotlib.pyplot as plt


def plot_bland_altman(tp1, tp2, metric='', ylim=None):
    data_diff = tp1 - tp2
    data_mean = (tp1 + tp2) / 2

    ba_mean = np.mean(data_diff)
    ba_std  = np.std(data_diff)

    plt.close('all')
    plt.subplots(1,1, figsize=(10,10))
    plt.subplot(1,1,1)
    plt.plot(data_mean, data_diff, LineStyle = "", Marker="o", MarkerSize = 15)

    plt.axhline(ba_mean, color='gray', linestyle=':', Linewidth = 4)
    plt.axhline(ba_mean + 1.96*ba_std, color='gray', LineStyle='--', LineWidth = 4)
    plt.axhline(ba_mean - 1.96*ba_std, color='gray', LineStyle='--', LineWidth = 4)    

    plt.ylabel('%s Difference (%%)' % metric)                
    plt.xlabel('%s Mean (%%)' % metric)
    plt.title('%s Scan/Re-scan' % metric, fontweight='bold')
    plt.grid(which="Major")
    
    if ylim:
        plt.ylim(ylim)


def portfolio(ims, ims_overlays=None, cmap='hot', alpha=0.5, figsize=(30,30)):
    """
    Output portfolio of images as subplots
    param ims: 1D/2D list of RGB numpy arrays to display
    """
    is_1d = type(ims[0]) is not list
    nrows = len(ims) if not is_1d else 1
    ncols = len(ims[0]) if not is_1d else len(ims)
    
    fig, axs = plt.subplots(nrows=nrows, ncols=ncols, dpi=100, figsize=figsize)

    for r in range(nrows):
        for c in range(ncols):
            ax = axs[r, c] if not is_1d else axs[c]
            im = ims[r, c] if not is_1d else ims[c]
            ax.imshow(im)
            if ims_overlays is not None:
                imo = ims_overlays[r, c] if not is_1d else ims_overlays[c]
                ax.imshow(im, cmap=cmap, alpha=alpha)
                          
            ax.axis('equal')
    
    fig.tight_layout()
    plt.show()


def scale(x, ub=1):
    xo = x - np.min(x)
    xo = xo / np.max(xo)
    xo *= ub
    
    return xo
