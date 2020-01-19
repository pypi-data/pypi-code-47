# -*- coding: utf-8 -*-
"""
Created on Sat Jan 18 19:43:33 2020

@author: Home
"""
#import sys
import math
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
#arglist=sys.argv
#print(arglist[0])

dataset=pd.read_csv("topsis.csv")

weight=(input("enter"))
weight=np.fromstring(weight,dtype=np.float,sep=',')
weight=[1,1,1,1]
impact=['-','+','+','+']
impact=input("enter")
impact=list(impact.split(","))

print("hello")
x=dataset.iloc[:,1:].values
x=x.astype(float)

list1=[]
for column in range(len(x[0])):
    sum=0.0
    for row in range(len(x)):
        sum=sum+(x[row][column])**2
    list1.append(math.sqrt(sum))
        
     #normalize
    
for i in range(len(list1)):
    for j in range(len(x)):
        x[j][i]=x[j][i]/list1[i]

#weight=weight.astype(float)
for i in range(len(weight)):
    for j in range(len(x)):
        x[j][i]=x[j][i]*weight[i]
        
db=[]
dw=[]

for column in range(len(x[0])):
    min1=min(x[:,column])
    max1=max(x[:,column])
    if impact[column]=='-':
       db.append(min1)
       dw.append(max1)
    elif impact[column]=='+':
         db.append(max1)
         dw.append(min1)
   
    eb=[]
    ew=[]
    
for i in range(len(x)):
    sum2=0.0
    for j in range(len(x[0])):
        sum2=sum2+(x[i][j]-db[j])**2
    eb.append(math.sqrt(sum2))
    

for i in range(len(x)):
    sum2=0.0
    for j in range(len(x[0])):
        sum2=sum2+(x[i][j]-dw[j])**2
    ew.append(math.sqrt(sum2))
    
sd=[]
  
for i in range(len(x)):
    sd.append(eb[i]+ew[i])
        
        
pt=[]
for i in range(len(sd)):
    pt.append(ew[i]/sd[i])
    
    print(max(pt))
 #a={}
def calculate_rank(pt):
  a={}
  rank=len(x)
  for num in sorted(pt):
    if num not in a:
      a[num]=rank
      rank=rank-1
  return[a[i] for i in pt]    
out=calculate_rank(pt) 
print(out)   
    
    
    
    
    
    
    
    
    
    
    
    