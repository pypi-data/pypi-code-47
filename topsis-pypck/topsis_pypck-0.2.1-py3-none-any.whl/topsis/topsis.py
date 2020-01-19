import numpy as np
import pandas as pd
import math
import sys
from scipy.stats import rankdata
from tabulate import tabulate

def fun1(a):
    sum1=[]
    for i in range(a.shape[1]):
        sum2=0
        for j in range(a.shape[0]):
            sum2+=a[j][i]*a[j][i]
        sum1.append(math.sqrt(sum2))  
        
    for i in range(a.shape[1]):
        for j in range(a.shape[0]):
            a[j][i]/=sum1[i]
    return a
            

def fun2(a,w):
    for i in range(a.shape[0]):
        for j in range(a.shape[1]):
            a[i][j]=a[i][j]*w[j]
    return a 

def fun3(a,im):
    best=[]
    for i in range(a.shape[1]):
        max_val=0
        min_val=1e9
        for j in range(a.shape[0]):
            if(im[i]=='+'):
                max_val=max(max_val,a[j][i])
            else:
                min_val=min(min_val,a[j][i])
        if(im[i]=='+'):
            best.append(max_val)
        else:
            best.append(min_val)

    worst=[]   
    for i in range(a.shape[1]):
        max_val=0
        min_val=1e9
        for j in range(a.shape[0]):
            if(im[i]=='-'):
                max_val=max(max_val,a[j][i])
            else:
                min_val=min(min_val,a[j][i])
        if(im[i]=='-'):
            worst.append(max_val)
        else:
            worst.append(min_val)
   
    return best,worst 
    


def fun4(a,idb,idw):
    s_pos=[]
    for i in range(a.shape[0]):
        sum1=0
        for j in range(a.shape[1]):
            sum1+=(a[i][j]-idb[j])*(a[i][j]-idb[j])
        sum1=math.sqrt(sum1)
        s_pos.append(sum1)
    
    
    s_neg=[]
    for i in range(a.shape[0]):
        sum1=0
        for j in range(a.shape[1]):
            sum1+=(a[i][j]-idw[j])*(a[i][j]-idw[j])
        sum1=math.sqrt(sum1)
        s_neg.append(sum1)
    
    return s_pos,s_neg
            

def fun5(sp,sn):
    sum1=[]
    p=[]
    for i in range(len(sp)):
        sum1.append(sp[i]+sn[i])
        
    for i in range(len(sp)):
        p.append(sn[i]/sum1[i])
    return p

def topsis(filename,w,im):
    data=pd.read_csv(filename)
    a=data.iloc[:,:].values
    a=a.astype("float64")
    a=fun1(a)
    a=fun2(a,w)
    ideal_best,ideal_worst=fun3(a,im)
    sp,sn=fun4(a,ideal_best,ideal_worst)
    pred=fun5(sp,sn)
    return pred

def main():
	data1 = list(sys.argv[2].strip('[]').split(','))
	data1=[float(i) for i in data1]
	data2 = list(sys.argv[3].strip('[]').split(','))
	pred=np.asarray(topsis(sys.argv[1],data1,data2))
	pred=np.reshape(pred,(pred.shape[0],1))
	rank=len(pred[:,0]) - rankdata(pred[:,0]).astype(int) + 1
	rank=np.reshape(rank,(rank.shape[0],1))
	print(tabulate({"Model": np.arange(1,pred.shape[0]+1), "Score": pred[:,0], "Rank": rank[:,0]}, headers="keys"))


if __name__ == "__main__":
    main()


