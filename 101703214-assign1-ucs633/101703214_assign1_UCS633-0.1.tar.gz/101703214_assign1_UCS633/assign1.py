# -*- coding: utf-8 -*-
"""
Created on Sun Jan 19 12:52:19 2020

@author: Harmeet Kaur
"""

"""n=int(input())
m=int(input())
a=[[int(input()) for x in range(m)] for y in range (n)] 
w=[float(input()) for x in range(m)]
need=[int(input()) for x in range(m)]"""
import numy as np
def normalized_matrix(a):
    sum1=[]
    attributes=len(a)
    models=len(a[0])
    for i in range(models):
        sum2=0
        for j in range(attributes):
            sum2+=a[j][i]*a[j][i]
        sum1.append(sum2)    
    for i in range(models):
        for j in range(attributes):
            a[j][i]=a[j][i]/sum1[j]
    return a        
def setting_weights(a,w):
    attributes=len(a)
    models=len(a[0])
    for i in range(attributes):
        for j in range(models):
            a[i][j]=a[i][j]*w[j]
    return a        
def cal_ideal_post(a,req_class):
    attributes=len(a)
    models=len(a[0])
    v_positive=[]
    maxi=0
    mini=1e9
    for i in range(models):
        for j in range(attributes):
            if(req_class[i]==1):
                maxi=max(maxi,a[j][i])
            else:
                mini=min(mini,a[j][i])
        if(req_class[i]==1):
            v_positive.append(maxi)
        else:
            v_positive.append(mini)
    return v_positive 
def cal_ideal_neg(a,req_class):
    attributes=len(a)
    models=len(a[0])
    v_neg=[]
    maxi=0
    mini=1e9
    for i in range(models):
        for j in range(attributes):
            if(req_class[i]==0):
                maxi=max(maxi,a[j][i])
            else:
                mini=min(mini,a[j][i])
        if(req_class[i]==1):
            v_neg.append(mini)
        else:
            v_neg.append(maxi)
    return v_neg
def separation_positive(a,vg):
    attributes=len(a)
    models=len(a[0])
    sg=[]
    for i in range(attributes):
        sum1=0
        for j in range(models):
            sum1+=(vg[i]-a[i][j])**2
        sg.append(sum1**0.5)    
    return sg        
            
def separation_negative(a,vb):
    attributes=len(a)
    models=len(a[0])
    sb=[]
    for i in range(attributes):
        sum1=0
        for j in range(models):
            sum1+=(vb[i]-a[i][j])**2
        sb.append(sum1**0.5)    
    return sb               

def relative_closeness(sg,sb):
    n1=len(sg)
    p=[]
    for i in range(n1):
        p.append(sb[i]/(sg[i]+sb[i]))
    return p    
def final_ranking(p):
    n1=len(p)
    k=p
    k.sort()
    dicti={}
    for i in range(0,n1):
        dicti[k[i]]=n1-i
    for j in range(n1):
        p[j]=dicti[p[j]]
    return p    
    
                
    
        
def topsis(a,w,req_class):
    a=normalized_matrix(a)
    a=setting_weights(a,w)
    vg=cal_ideal_post(a,req_class)
    vb=cal_ideal_neg(a,req_class)
    sg=separation_positive(a,vg)
    sb=separation_negative(a,vb)
    p=relative_closeness(sg,sb)
    ranking=final_ranking(p)
    return ranking
  
