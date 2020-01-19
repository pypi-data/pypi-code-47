# -*- coding: utf-8 -*-
"""
Created on Sat Jan 18 22:13:22 2020

@author: DELL
"""

def topsiss(data,mat,sign):
    import pandas as pd
    import numpy
    print("hello")
    print(data)
    #data=pd.read_csv("book1.csv")
    rows=data.shape[0]
    cols=data.shape[1]
    #mat=[1,1]
    #sign=['+','+']
    sum=0;
    k=len(mat)
    for i in range(k):
        sum+=mat[i]
        for i in range(len(mat)):
            mat[i]=(mat[i]/sum)
            sum1=[]
            for j in range(cols):
                sum1.append(0)
                for i in range(rows):
                    sum1[j]=sum1[j]+data.get_value(i,j, takeable = True)*data.get_value(i,j, takeable = True)
                    sum1[j]=numpy.sqrt(sum1[j])
            for j in range(cols):
                for i in range(rows):
                    numm=(data.get_value(i,j, takeable = True)/sum1[j])*mat[j]
                    data.set_value(i, data.columns[j], numm) 
            best=[]
            worst=[]
            for i in  range(cols):
                if sign[i]=='+':
                    best.append(data[data.columns[i]].max())
                    worst.append(data[data.columns[i]].min())
                elif sign[i]=='-':
                    best.append(data[data.columns[i]].min())
                    worst.append(data[data.columns[i]].max())
    
    s1=[]
    s2=[]
    for i in range(rows):
        s1.append(0)
        s2.append(0)
        for j in range(cols):
            s1[i]=s1[i]+(data.get_value(i,j, takeable = True)-best[j])*(data.get_value(i,j, takeable = True)-best[j])
            s2[i]=s2[i]+(data.get_value(i,j, takeable = True)-worst[j])*(data.get_value(i,j, takeable = True)-worst[j])
        s1[i]=numpy.sqrt(s1[i])
        s2[i]=numpy.sqrt(s2[i])
    for i in range(rows):
        s2[i]=(s2[i])/(s1[i]+s2[i])
    s2= pd.DataFrame(s2) 
    data['rank']=s2.rank()
    return(data)
