import numpy as np
import pandas as pd
from scipy.stats import rankdata
import argparse

def topsis(filepath, W, Z):
    """
    Ranks the data set
    """
    data = pd.read_csv(filepath)
    X = data.iloc[:, 1:].values

    X = X.astype(float)
    m = len(X[0, :])

    for i in range(m):
        x = np.sqrt(np.sum(np.square(X[:, i])))
        X[:,i] = X[:, i]/x
    
    w = W/np.sum(W)

    for i in range(m):
        X[:,i] = X[:, i]*w[i]
    
    Aplus = np.zeros((m, 1), dtype = float)
    Aminus = np.zeros((m, 1), dtype = float)

    for i in range(m):
        if(Z[i] == '+'):
            Aplus[i] = np.max(X[:, i])
            Aminus[i] = np.min(X[:, i])
        if(Z[i] == '-'):
            Aplus[i] = np.min(X[:, i])
            Aminus[i] = np.max(X[:, i])

    Splus = np.zeros((len(X), 1), dtype = float)
    Sminus = np.zeros((len(X), 1), dtype = float)
        
    for j in range(m):
        Splus[:,0] += np.square(X[:, j] - Aplus[j])
        Sminus[:,0] += np.square(X[:, j] - Aminus[j])
    
    Splus[:] = np.sqrt(Splus[:])
    Sminus[:] = np.sqrt(Sminus[:])

    PerfM = np.zeros((len(X), 1), dtype = float)
    for i in range(len(X)):
        PerfM[i] = Sminus[i]/(Splus[i] + Sminus[i])
    
    rank = len(PerfM) - rankdata(PerfM, method = 'min').astype(int) + 1
    return rank

def main():
    """
    This function is called directly from command line and run the above code
    """
    ap = argparse.ArgumentParser(description='Calculate the TOPSIS')
    ap.add_argument('-f', '--Filepath', type=str, required=True, default = None, help='filepath of CSV file', dest='filepath')
    ap.add_argument('-w', '--Weights', nargs = '+', type=int, required=True, default = None, help='Weights of each column of the given dataset', dest='W')
    ap.add_argument('-z', '--Z', nargs = '+', type=str, required=True, default = None, help="Z('+', '-') of each column", dest='Z')
    args = ap.parse_args()
    rankz = topsis(args.filepath, args.W, args.Z)
    print(rankz)
    
if __name__ == '__main__':
    main()
    
#UCS633