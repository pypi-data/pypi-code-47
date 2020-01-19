# -*- coding: utf-8 -*-
"""
Created on Sun Jan 17 19:41:38 2020

@author: Jasmanpreet
"""


import numpy as np
import sys
from sklearn.preprocessing import LabelEncoder
import math 
import pandas as pd
from scipy.stats import rankdata
from tabulate import tabulate    # if not installed already enter command ->pip install tabulate 


def main():
    if len(sys.argv)!=4:
        print("Wrong number of parameters. please input in the format:->python <programName> <dataset> <weights array> <impacts array>")
        exit(1)
    else:
        dataset = pd.read_csv(sys.argv[1]).values             #import the dataset
        decision_matrix = dataset[:,1:]                        #drop the first column that contains information about number of methods(m1,m2..)
        weights = [int(i) for i in sys.argv[2].split(',')]    #initalize the weights array entered by user
        '''for i in range(0,len(weights)):
            weights[i]=int(weights[i])'''
        impacts = sys.argv[3].split(',')                      #initalize impacts array entered by user
        y=decision_matrix[:,-1]
        le=LabelEncoder()                   #apply the label encoder in case of categorical values
        y=le.fit_transform(y)               
        decision_matrix[:,-1]=y                 # substitute the label encoded values back into the decision matrix.
        
       
        topsis(decision_matrix , weights , impacts)
        
        
def topsis(decision_matrix,weights,impacts):
    rows,cols = decision_matrix.shape
    if len(weights) != cols or len(impacts) != cols or not all(i > 0 for i in weights) or not all(i=="+"or i=="-" for i in impacts):
        return print("Please check the input arguments.")

    data = np.zeros([rows+2,cols+4])
    s=sum(weights)
    
    for i in range(cols):
        for j in range(rows):
            data[j,i] = (decision_matrix[j,i]/np.sqrt(sum(decision_matrix[:,i]**2)))*weights[i]/s
    
    for i in range(cols):
        data[rows,i] = max(data[:rows,i])
        data[rows+1,i] = min(data[:rows,i])
        if impacts[i] == "-":
            data[rows,i] , data[rows+1,i] = data[rows+1,i] , data[rows,i]
    
    for i in range(rows):
        data[i,cols] = np.sqrt(sum((data[rows,:cols] - data[i,:cols])**2))
        data[i,cols+1] = np.sqrt(sum((data[rows+1,:cols] - data[i,:cols])**2))
        data[i,cols+2] = data[i,cols+1]/(data[i,cols] + data[i,cols+1])
        
    data[:rows,cols+3] = len(data[:rows,cols+2]) - rankdata(data[:rows,cols+2]).astype(int) + 1
    print(tabulate({"Model": np.arange(1,rows+1), "Performance Score": data[:5,cols+2], "Rank (Rank1 is the best option) ": data[:5,cols+3]}, headers="keys"))
    

if __name__ == "__main__":
    main()
