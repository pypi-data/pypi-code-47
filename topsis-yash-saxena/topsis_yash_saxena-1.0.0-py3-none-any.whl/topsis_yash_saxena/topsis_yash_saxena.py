# -*- coding: utf-8 -*-
"""
Created on Sun Jan 19 17:36:48 2020

@author: dell
"""

import numpy as np

def main():
    import sys
    import pandas as pd
    if len(sys.argv) != 4:
        print("ERROR! WRONG NUMBER OF PARAMETERS")
        print("USAGES: $python <programName> <dataset> <weights array> <impacts array>")
        print("EXAMPLE: $python programName.py data.csv '1,1,1,1' '+,+,-,+' ")
        exit(1)
    dataset = pd.read_csv(sys.argv[1]).values               #importing the dataset
    decisionMatrix = dataset[:,1:]                          #dropping first column
    weights = [int(i) for i in sys.argv[2].split(',')]      #initalizing weights array                   
    impacts = sys.argv[3].split(',')                        #initalizing impacts array
    topsis(decisionMatrix, weights, impacts)

def topsis(decisionMatrix, weights, impacts):
    
    # getting the number of rows and columns
    r = len(dm)
    c = len(dm[0])
    
    # getting the normalization factor
    normFactor = []
    for j in range(numCols):
        sum = 0
        for i in range(c):
            sum = 0
            for i in range(r):
                sum = sum + (decisionMatrix[i][j] ** 2)
            value = sum ** 0.5
            normFactor.append(value)
             
    # dividing each value by corresponding normalization factor
    for i in range(r):
        for j in range(c):
            decisionMatrix[i][j] = decisionMatrix[i][j] / normFactor[j]
            
    # multiplying each value by corresponding weight
    for j in range(c):
        for i in range(r):
            decisionMatrix[i][j] = decisionMatrix[i][j] * float(weights[j])
    
    # calculating the ideal best and ideal worst from each column
    maxElement = np.amax(decisionMatrix, axis=0)
    minElement = np.amin(decisionMatrix, axis=0)
    vbest = []
    vworst = []
    for i in range(c):
        if impacts[i] == '+':
            vbest.append(maxElement[i])
            vworst.append(minElement[i])
        elif impacts[i] == '-':
            vbest.append(minElement[i])
            vworst.append(maxElement[i])
            
    
    # calculating the eucledian distance of each value from ideal best 
    dbest = []
    for i in range(r):
        sum1 = 0
        for j in range(c):
            sum1 = sum1 + ((decisionMatrix[i][j] - vbest[j]) ** 2)
        dist1 = sum1 ** 0.5
        dbest.append(dist1)  
        
    # calculating the eucledian distance of each value from ideal worst 
    dworst = []
    for i in range(r):
        sum2 = 0
        for j in range(c):
            sum2 = sum2 + ((decisionMatrix[i][j] - vworst[j]) ** 2)
        dist2 = sum2 ** 0.5
        dworst.append(dist2)       
        
    # calculating the performance score
    perf = []
    for i in range(r):
        ps = dworst[i] / (dworst[i] + dbest[i])
        perf.append(round(ps,7))

    # displaying the rank based on decreasing order of performance score
    rank = perf.copy()
    rank.sort(reverse=True)

    print("Index        Score       Rank")
    for i in range(r):
        print(str(i+1) + "        " + str(perf[i]) + "        " + str(rank.index(perf[i]) + 1))       
            
if __name__ == "__main__":
    main()
              
                    
                   