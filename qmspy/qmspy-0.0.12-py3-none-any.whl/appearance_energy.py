from .config import *
from scipy.optimize import curve_fit

def appearance_energy(data, savedir=None):
    """
    This function finds the appearance energy of all amu species present in
    the data by means of linear fit.

    Parameters
    ----------
    data: string or Pandas DataFrame
        This should be a string that points to the csv DataFrame file
        or a Pandas DataFrame. (FULL DIRECTORY STRING REQUIRED)

    Returns
    -------
    energies: list
        This will be a list where each element is string with the amu
        energy in the following format 'amu: energy'


    Example
    -------

    """
    df   = check_data_type(data)

    #Grab species of interest
    soi = species_of_interest(df)

    #initialize a dictionary for appearance energies
    energies={}

    #iterate through each species of interest
    for specie in soi:

        #slice the DataFrame so that it only has rows with amu value
        #equal to the specie of interest
        temp = df.loc[df[amu] == specie]

        x    = temp[ev].values
        y    = temp[sem].values
        a,b  = x[y>0],y[y>0]

        if len(a) < 15:
            continue

        j    = np.where(x == a[0] + 3)[0][0]

        x    = x[0:j+1]
        y    = y[0:j+1]

        #Perform a levenberg marquet method power law
        #fitting to the data-set
        popt, pcov   = curve_fit(p_law, x, y, method='lm',
                                 maxfev=2000000000)
        p0           = (1, popt[0], 1, popt[1], popt[2], popt[2])
        popt2, pcov2 = curve_fit(p_law2, x, y, p0=p0, method='lm',
                                 maxfev=2000000000)

        #Fitted data
        fit  =  p_law(x, *popt)
        fit2 = p_law2(x, *popt2)

        if savedir is not None:
            ae = str(round(popt[0],2))
            p  = str(round(popt[1],2))
            s  = 'AE = ' + ae + '\np = ' + p
            plt.plot(x,y,'.', label='Data')
            plt.plot(x, fit, label='Wanier Fitting of Data')
            plt.text(12, 0.7*max(y), s)
            plt.title(specie)
            plt.savefig(savedir + str(specie) + '.png')
            plt.close()

            ae1 = str(round(popt2[0],2))
            ae2 = str(round(popt2[1],2))
            p1  = str(round(popt2[2],2))
            p2  = str(round(popt2[3],2))
            s  = ('AE1 = ' + ae1 + '\nAE2 = ' + ae2 +
                  '\np1 = ' + p1 + '\np2 = ' + p2)
            plt.plot(x,y,'.', label='Data')
            plt.plot(x, fit2, label='Wanier Fitting of Data')
            plt.text(12, 0.7*max(y), s)
            plt.title(specie)
            plt.savefig(savedir + str(specie) + '--fit2.png')
            plt.close()

        #interpolate the x-intercept and add it to the dictionary
        energies[specie] = popt[0:2]

    return energies
