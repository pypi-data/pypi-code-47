# -*- coding: utf-8 -*-
"""
Created on Sun Jan 19 15:59:22 2020

@author: nipunn
"""

def calc_perfomance(input_file,weights_ratio,impacts):
    
    
    dataset=pd.read_csv(input_file)
    
    dataset=dataset.iloc[:,1:]
    
    m=dataset.shape
    
    coloumn_rms=[]
    
    for j in range(0,m[1]):
        sum=0
        for i in range(0,m[0]):
            sum=sum+((dataset.iloc[i,j])**2)
        coloumn_rms.append(sum**0.5)
        
     
    new_dataset=dataset    
       
    ideal_best=[]
    ideal_worst=[]
    
    
    weights=[]
    
    
    ind_per=1/m[1]    
        
    for j in range(0,m[1]):
        weights.append(ind_per*int(weights_ratio[j]))    
        
        
    
    
    
    for j in range(0,m[1]):
        for i in range(0,m[0]):
            new_dataset.iloc[i,j]=(new_dataset.iloc[i,j]/coloumn_rms[j])*weights[j]
    
    
    
    
    for j in range(0,m[1]):
        if impacts[j]=='+':
            ideal_best.append(max(new_dataset.iloc[j,:]))
            ideal_worst.append(min(new_dataset.iloc[j,:]))
        else:
            ideal_worst.append(max(new_dataset.iloc[j,:]))
            ideal_best.append(min(new_dataset.iloc[j,:]))
    
    best_ed=[]
    worst_ed=[]
    
    for i in range(0,m[0]):
        sum1=0
        sum2=0
        for j in range(0,m[1]):
            sum1=sum1+(new_dataset.iloc[i,j]-ideal_best[j])**2
            sum2=sum2+(new_dataset.iloc[i,j]-ideal_worst[j])**2
        best_ed.append(sum1**0.5)
        worst_ed.append(sum2**0.5)    
    
    
    new_dataset['best_ed']=best_ed
    new_dataset['worst_ed']=worst_ed
    
    perfomance_score=[]
    
    for i in range(0,m[0]):
        perfomance_score.append(worst_ed[i]/(worst_ed[i]+best_ed[i]))
    
    new_dataset['Perfomance Score']=perfomance_score
    
    new_dataset['Rank']=new_dataset['Perfomance Score'].rank(ascending=False)
    
    pd.set_option('display.max_columns', 1000)
    pd.set_option('display.width', 2000)
    
    result_data=new_dataset.iloc[:,(m[1]+2):(m[1]+4)]
    
    
    ID=[]
    for i in range(0,m[0]):
        ID.append(i+1)
    
    result_data['ID']=ID
    
    result_data=result_data[['ID','Perfomance Score','Rank']]
    
    print(result_data)
    

import sys
import pandas as pd
if len(sys.argv)>1:
    if len(sys.argv)==4:
        input_file=sys.argv[1]
        weights_ratio=sys.argv[2]
        impacts=sys.argv[3]
        calc_perfomance(input_file,weights_ratio,impacts)
    else:
        print("Enter three arguments: \n 1.INPUT FILE NAME \n 2. WEIGHTS RATIO \n 3.IMPACTS" )