from .config      import *
from scipy.signal import find_peaks, peak_widths
from scipy.optimize import curve_fit
import matplotlib.animation as ani

def get_peaks(data, height, width, savedir='./',
                  savename='./Data-With-Gaussians.csv'):
    """

    """
    df = check_data_type(data)

    #Initialize new columns
    df[pks] = np.nan

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

        #Update main DataFrame with sub-DataFrame
        df[pks].update(subDF[pks])

    #Write csv file of data
    df.to_csv(savename)

    return df
