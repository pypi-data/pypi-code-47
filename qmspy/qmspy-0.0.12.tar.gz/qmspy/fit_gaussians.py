from .config      import *
from scipy.signal import find_peaks, peak_widths
from scipy.optimize import curve_fit
import matplotlib.animation as ani

def fit_gaussians(data, height, width, savedir='./', overplot=False,
                  savename='./Data-With-Gaussians.csv'):
    """
    Fits gaussians to the data peaks.

    Parameters
    ----------
    data: string or Pandas DataFrame
        This should be a string that points to the csv DataFrame file
        or a Pandas DataFrame. (FULL DIRECTORY STRING REQUIRED)
    height: float
        This should be the minimum value for data peak heights that will
        get a fitting.
    width: float
        This should be the minimum value for data peak widths that will
        get a fitting.
    savename: string [Optional, Default = './Data-With-Gaussians.csv']
        This should be a directory string that will be used to write
        the DataFrame csv to. (FULL DIRECTORY STRING REQUIRED)

    Returns
    -------


    Example
    -------

    """
    df = check_data_type(data)

    #Initialize new columns
    df[pks] = np.nan
    df[gfs] = np.nan

    for label, subDF in df.groupby(ev):
        subDF = subDF.reset_index()

        #find peaks and preperties(widths) in data
        peaks, properties = find_peaks(subDF[sem], height=height, width=width,
                                       distance=10)
        half_widths       = peak_widths(subDF[sem], peaks, rel_height=0.5)
        full_widths       = peak_widths(subDF[sem], peaks, rel_height=1)

        #Add peaks column to DataFrame
        temp        = np.zeros(len(subDF[sem]))
        temp[peaks] = 1
        subDF[pks]  = temp

        p0 = []
        for peak in peaks:
            p0.append(subDF[amu].iloc[peak])
            p0.append(1)
            p0.append(subDF[sem].iloc[peak])

        if not p0:
            continue

        x          = subDF[amu].values
        y          = subDF[sem].values
        popt, pcov = curve_fit(gaussian_fit, x, y, p0, maxfev=2000000000)
        gfit       = gaussian_fit(subDF[amu], *popt)

        for i in range(0, len(popt), 3):
            mu   = popt[i]
            sig  = popt[i+1]
            amp  = popt[i+2]
            area = amp * sig * np.sqrt(2.*np.pi)
            j    = int(i/3)
            temp[peaks[j]] = area

        if overplot is True:
            plt.plot(subDF[amu],subDF[sem], '.')
            plt.plot(subDF[amu],gfit,'--')
            plt.savefig(savedir+str(label)+'.png')
            plt.close()


        #Add Gaussian integrations into Dataframe
        subDF[gfs] = temp

        #Update main DataFrame with sub-DataFrame
        df[pks].update(subDF[pks])
        df[gfs].update(subDF[gfs])

    #Write csv file of data
    df.to_csv(savename)

    return df
