# -*- coding: utf-8 -*-
"""
Created on Thu Jan 16 20:22:09 2020
@author: Katinder
description: driver code for TOPSIS for MCDM problems

"""


import csv
import sys
import numpy as np
import pandas as pd
import argparse
 

#step:1 normalize the matrix and multiply with weights
def normalize(y,m,n,weights):
    
    rms = np.zeros((n,1))
    
    for i in range(n):
        
        for j in range(m):
            
            rms[i] += ((y[j,i])**2)
            
        rms[i] = (rms[i])**(0.5)
            
    for i in range(n):
        
        for j in range(m):
            
            y[j,i] = (y[j,i]/rms[i])*(weights[i])
            
    return y


#step:2 find ideal values
def idealvals(x,m,n,impacts):
    
    v_best = np.zeros((n,1))
    v_worst = np.zeros((n,1))
    
    for i in range(n):
        
        if impacts[i] == '+':
            v_best[i] = max(x[:,i])
            v_worst[i] = min(x[:,i])
            
        elif impacts[i] == '-':
            v_worst[i] = max(x[:,i])
            v_best[i] = min(x[:,i])
            
        else:
            print("Invalid symbol(s) in Impacts vector")
            sys.exit(0)
            
    return v_best,v_worst


#step:3 find euclidean distance and performance score
def performance(x,m,n,v_best,v_worst):
    
    s_best = np.zeros((m,1))
    s_worst = np.zeros((m,1))
    
    p = np.zeros((m,1))
    
    for j in range(m):
        
        for i in range(n):
            
            s_best[j] += (x[j,i] - v_best[i]) ** 2
            s_worst[j] += (x[j,i] - v_worst[i]) ** 2
            
        s_best[j] = (s_best[j]) ** (0.5)
        s_worst[j] = (s_worst[j]) ** (0.5)
        
        p[j] = s_worst[j] / (s_worst[j] + s_best[j])
        
    return p
  
    
#step:4 assign ranks to datapoints
def rank_df(p,m):
    
    index = list( range(1, m+1) )
    df=pd.DataFrame(p,index=index,columns=['P-Score'])
    
    df['Rank'] = df['P-Score'].rank(ascending=False).astype(int)
    
    return df



#step:5 print results
def print_df(df):
   
    print('''
        TOPSIS RESULTS
---------------------------------
          ''')
    
    print(df)
    
    
    
    
def main():
   
    # parse command line arguments 
    parser = argparse.ArgumentParser(prog ='topsis')
    parser.add_argument("InputDataFile", help="Enter the name of CSV file with .csv extention",type=str)
    parser.add_argument("Weights", nargs=1, help="Enter the weight vector comma separated" ,type=str)
    parser.add_argument("Impacts", nargs=1, help="Enter the impact vector comma separated",type=str)
    args = parser.parse_args()
    
    args=vars(args)
    
    filename = args['InputDataFile'] 
  
    try:
        f = open(filename, 'r')
       
    except IOError:
       print ("There was an error reading", filename)
       sys.exit()
   
    file = csv.reader(f)
    data = list(file)
    data=np.array(data)
    data=np.array(data[1:,1:],dtype=float)
    
    
    x=data
    n=np.size(x,1)
    m=np.size(x,0)
    
    try:
        weights = np.array(args['Weights'][0].split(','),dtype=float)
  
    except ValueError:
        print ("Incorrect value(s) in Weight vector")
        sys.exit()
    
    if(len(weights) != n):
        print("Incorrect input size for Weights vector")
        sys.exit(0)
    
    
    try:
        impacts = args['Impacts'][0].split(',')
    
    except ValueError:
        print ("Incorrect value(s) in Impacts vector")
        sys.exit()
    
    if(len(impacts) != n):
        print("Incorrect input size for Impacts vector")
        sys.exit(0)    
    
    
    x=normalize(x,m,n,weights)
    v_best,v_worst=idealvals(x,m,n,impacts)
    p_score=performance(x,m,n,v_best,v_worst)
       
    ranked_df=rank_df(p_score,m)
    
    print_df(ranked_df)
    

    
# driver code    
if __name__ == "__main__":
    main()
    
    

    
    
    
    

