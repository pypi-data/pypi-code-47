
import argparse
import sys
import pandas as pd
import numpy as np
from toposis import *

def main():
    parser=argparse.ArgumentParser(description='Find out the ranking table')
    parser.add_argument("filename",help='Name of the file to be extracted',type=str)
    parser.add_argument('-w',"--weights",help='Enter the weights of attributes'  ,nargs="+", type=int,default=[1,1,1,1])
    parser.add_argument('-i',"--impacts",help='Enter the impacts of attributes',nargs='+',type=str,default=['+','+','+','+'])
    args=parser.parse_args()

    file=args.filename
    data=pd.read_csv(file)
    
    
    X=data.iloc[:,1:].values
    
    
    impacts=args.impacts
    weights=args.weights
    if(len(impacts)!=np.shape(X)[1] or len(weights)!=np.shape(X)[1]):
        print("Values didnt match:")
        sys.exit(0)

    s=0
    for i  in weights:
        s=s+1
    
    for i,j in enumerate(weights):
        weights[i]=j/s
    
    if(top(X,weights,impacts)==None):
        print("Successfully executed")

if __name__=='__main__':
    
   main()