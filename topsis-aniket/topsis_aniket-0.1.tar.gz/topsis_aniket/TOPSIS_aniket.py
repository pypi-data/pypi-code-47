# -*- coding: utf-8 -*-

import numpy as np
import pandas as pd
import math

class Topsis:
    
    def __init__(self,filename):
        data = pd.read_csv(filename)
        self.d = data.iloc[:,1:].values
        self.d = self.d.astype("float64")
        self.features=len(self .d[0])
        self.samples=len(self.d)

    def evaluate(self,weights,impacts):
        data=self.d
        rows=self.samples
        cols=self.features
        if (weights==None):
            weights=[1]*weights
        if (impacts==None):
            impacts=["+"]*impacts
        
        divisor=[]
        for i in range(cols):
            temp=0
            for j in range(rows):
                temp = temp + (data[j,i]*data[j,i])
            temp = math.sqrt(temp)
            divisor.append(temp)
        
        for i in range(rows):
            for j in range(cols):
                data[i,j]=data[i,j]/divisor[j]
        
        for i in range(cols):
            for j in range(rows):
                data[j,i]=data[j,i]*float(weights[i])
        
        ideal_best=[]
        ideal_worst=[]
        
        maximum_val = np.amax(data, axis=0)
        minimum_val = np.amin(data, axis=0)
        for i in range(cols):
            if impacts[i] == '+':
                ideal_best.append(maximum_val[i])
                ideal_worst.append(minimum_val[i])
            elif impacts[i] == '-':
                ideal_best.append(minimum_val[i])
                ideal_worst.append(maximum_val[i])
                
        distbest = []
        for i in range(rows):
            sum1 = 0
            for j in range(cols):
                sum1 = sum1 + ((data[i][j] - ideal_best[j]) ** 2)
            temp1 = sum1 ** 0.5
            distbest.append(temp1)
        
        distworst = []
        for i in range(rows):
            sum2 = 0
            for j in range(cols):
                sum2 = sum2 + ((data[i][j] - ideal_worst[j]) ** 2)
            temp2 = sum2 ** 0.5
            distworst.append(temp2)
            
        p=[]
        
        for i in  range(rows):
            temp=distworst[i]/(distworst[i]+distbest[i])
            p.append(temp)
            
        return p
