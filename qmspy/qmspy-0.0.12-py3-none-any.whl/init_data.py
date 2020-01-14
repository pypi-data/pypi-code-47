from .config import *

def init_data(filled, background, data_type, savename='./Data.csv', sub=False,
              drop=True):
    """
    This function reads in the QMS csv files and forms pandas DataFrames,
    it also preps the data.

    Parameters
    ----------
    filled: string
        This should be a string that points to the csv file of a
        gas-filled esweep. (FULL DIRECTORY STRING REQUIRED)
    background: string
        This should be a string that points to the csv file of a
        empty chamber esweep. (FULL DIRECTORY STRING REQUIRED)
    data_type: integer
        This should either be '21' for profile
                or            '22' for esweep.
        NO DEVIATIONS FROM THOSE TWO.
    savename: string [Optional, Default = './Data.csv']
        This should be a directory string that will be used to write
        the DataFrame csv to. (FULL DIRECTORY STRING REQUIRED)
    sub: True/False     Default==False
        This indicates if the background should be subtracted from
        the data.
    abs: True/False     Default==False
        This indicates if the absolute value of the SEM Amps data
        should be taken
    drop: True/False    Default==True
        This indicates if data collected after 1st Cycle should be kept


    Returns
    -------
    data: Pandas DataFrame
        This is the DataFrame of the Initialized experimental data

    Example
    -------
    >>> import qmspy as qp
    >>>
    >>> filled     = './SomeFile1.csv'
    >>> background = './SomeFile2.csv'
    >>> error      = qp.get_errs(filled, None)
    >>>
    >>> data = qp.init_data(filled, background, error)
    >>>
    """
    if (data_type is not 21) and (data_type is not 22):
        print('Check Data Type Parameter!!!')
        sys.exit()

    #Read in CSV files with Pandas
    data = pd.read_csv(filled,     header=data_type)
    back = pd.read_csv(background, header=data_type)

    #Get Standard Deviation and Mean of data and background
    if data_type is 21:
        data_error = data.groupby(amu).std()
        back_error = back.groupby(amu).std()

    if data_type is 22:
        data_error = data.groupby([ev, amu]).std()
        back_error = back.groupby([ev, amu]).std()

    #Add in Standard Deviation Column
    data_error = data_error.rename(index=str, columns={sem:std})
    data_error = data_error.reset_index()
    data[std]  = data_error[std]

    back_error = back_error.rename(index=str, columns={sem:std})
    back_error = back_error.reset_index()
    back[std]  = back_error[std]

    #Removes noise from Data and Background SEM Amps
    data.update(data[sem].where(data[sem] > 0).fillna(0))
    back.update(back[sem].where(back[sem] > 0).fillna(0))

    #Drops data outside of first cycle
    if drop is True:
        data = data.loc[data[cyc] == 1]
        back = back.loc[back[cyc] == 1]

    #subtract background from data
    if sub is True:
        data[sem] -= back[sem]

    #Write csv file of data
    data.to_csv(savename)

    return data
