# -*- coding: utf-8 -*-
"""
Created on Tue Jan 14 23:37:46 2020

@author: agarw_ftjrwf3
"""
import numpy as np
def topsis(matrix,d,w):
    l=[]
    vjplus=[]
    vjminus=[]
    siplus=[]
    siminus=[]
    r=[]
    for j in range(len(matrix[0])):
        sqsum=0
        for i in range(len(matrix)):
            sqsum=sqsum+((matrix[i][j])**2)
        rms=sqsum**0.5
        l.append(rms)
    for j in range(len(matrix[0])):
        maxterm=0
        minterm=9999999999
        for i in range(len(matrix)):
            matrix[i][j]=matrix[i][j]/l[j]
            matrix[i][j]=matrix[i][j]*w[j]
            maxterm=max(matrix[i][j],maxterm)
            minterm=min(matrix[i][j],minterm)  
        if(d[j]=='+'):
            vjplus.append(maxterm)
            vjminus.append(minterm)
        else:
            vjplus.append(minterm)
            vjminus.append(maxterm)
    for i in range(len(matrix)):
        sum1=0
        sum2=0
        for j in range(len(matrix[0])):
            sum1=sum1+((matrix[i][j]-vjplus[j])**2)
            sum2=sum2+((matrix[i][j]-vjminus[j])**2)
        siplus.append(sum1**0.5) 
        siminus.append(sum2**0.5)
    for i in range(len(matrix)):
        r.append((siminus[i]/(siplus[i]+siminus[i])))  
    sortedr=sorted(r)    
    p=len(matrix)
    rank=np.zeros(len(matrix),dtype=int)
    for k in range(len(sortedr)):
        index=r.index(sortedr[k])
        rank[index]=p
        p=p-1
    return(rank)
    

