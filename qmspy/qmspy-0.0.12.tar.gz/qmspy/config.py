import sys
import numpy as np
import pandas as pd
import seaborn as sb
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.colors import LogNorm
import matplotlib.pyplot as plt

#A standard size for graphs
size = (10,10)

#Error Header and Tail
error_head = "\n*****uh oh spaghettios*****\n"
error_tail = "\n*****Ponder this, then return to me*****\n"

#Data Frame Columns
amu       =  'mass amu'
sem       =  'SEM Amps'
ev        =  'electron-energy V'
cyc       =  'Cycle'
col       =  'Color'
mar       =  'Marker'
std       =  'Standard Deviation'
pks       =  'Peaks'
gfs       =  'G-Fit Sums'

def gaussian(x, mu, sig, height):
    return  np.exp(-(x-mu)**2 / (2.*sig**2)) * height

def gaussian_fit(x, *params):
    y = np.zeros_like(x).astype(np.float64)
    for i in range(0, len(params), 3):
        mu     = params[i]
        sig    = params[i+1]
        height = params[i+2]
        y     += gaussian(x, mu, sig, height)
    return y

def p_law(x, AE, p, a):
    y = np.piecewise(x, [x < AE, x >= AE],
                    [lambda x: 0, lambda x: a*(x - AE)**p])
    return y

def p_law2(x, AE1, AE2, p1, p2, a, b):
    y = np.piecewise(x, [x < AE1, (AE1 < x) & (x < AE2), AE2 <= x],
                    [lambda x: 0, lambda x: a*(x - AE1)**p1,
                     lambda x: a*(x-AE1)**p1 + b*(x-AE2)**p2])
    return y

def check_data_type(data):
    #Check if data is in CSV format
    if '.csv' in data:
        df = pd.read_csv(data)

    #Terminates function with error message if data format not acceptable
    elif type(data) is not type(pd.DataFrame()):
        print(error_head)
        print("Your data is not in CSV or Pandas DataFrame Format")
        print(error_tail)
        sys.exit()

    #If data already DataFrame format, changes its name to df
    else:
        df = data

    return df

def species_of_interest(data):
    #Grabs only rows with 1 in peaks column
    temp = data.loc[data[pks] == 1]

    #Returns a list of uniques species of interest (species with data peaks)
    return temp[amu].unique()
