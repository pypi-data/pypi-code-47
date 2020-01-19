
#@author: manjot

import sys
import numpy as np
import pandas as pd
import math as m


def main():
    script=sys.argv[0]
    filename=sys.argv[1]
    # w=sys.argv[3]
    wt=sys.argv[2]
    wt=wt.split(",") 
    wt=[float(i) for i in wt]
         
    c1=sys.argv[3]
    data=pd.read_csv(filename)


    #data=pd.read_csv('data.csv');
    #take useful columns
    x=data.iloc[:,1:].values
    #w=[0.2,0.4,0.2,0.2]
    #c1=['+','+','-','+']
    a=[0]*10000
    (r,c)=x.shape
    sum=0
    for i in range(0,c):
        sum+=wt[i]
        
    for i in range(0,c):
        wt[i]=float(wt[i]/sum)

        
    for i in range(0,r):
      for j in range(0,c):
            a[j]=a[j]+x[i][j]**2
            
            
    for i in range(0,c):
        a[i]=m.sqrt(a[i])
        ##denominator done
    for i in range(0,r):
        for j in range(0,c):
            x[i][j]=x[i][j]/a[j]
            #normalized deci matrix
    for j in range(0,c):
        for i in range(0,r):
            x[i][j]=x[i][j]*wt[j]
            #weighted normalized vector
     
    vjp=[]
    vjm=[]
    
    
    for i in range(0,c):
        if(c1[i]=='+'):
            vjp.append([max(s) for s in zip(*x)][i])
            vjm.append([min(s) for s in zip(*x)][i])
        else:
            vjp.append([min(s) for s in zip(*x)][i])
            vjm.append([max(s) for s in zip(*x)][i])
    
    sp=[0]*10000
    sm=[0]*10000
    #euclidean distance find
    for i in range(0,r):
        for j in range (0,c):
            sp[i] = sp[i]+(x[i][j]-vjp[j])**2
            sm[i] = sm[i]+(x[i][j]-vjm[j])**2    
    
    
    for i in range(0,r):
        sp[i]=np.sqrt(sp[i]);        
        sm[i]=np.sqrt(sm[i]);    
            
    #evaluate performance
    sum1=[0]*10000    
    for i in range(0,r):
        sum1[i]=sp[i]+sm[i]     
           
    
    myans=[0]*10000
    for i in range(0,r):
        myans[i]=sm[i]/sum1[i]
        print(myans[i])
        
        
        
main()
