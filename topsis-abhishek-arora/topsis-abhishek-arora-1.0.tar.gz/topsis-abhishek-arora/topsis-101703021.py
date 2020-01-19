import pandas as pd

def topsis(file_name, weight, impact):
    
    # Implemented by Abhishek Arora
    #.....Roll No. 101703021
    #.....Group : 3CO1 (Coe-1)
    #.....Project - 1 UCS633...............
    
    data = pd.read_csv(file_name).iloc[:,1:].values.tolist()
    
    
    #..............Normalization............
    den = [0]*(len(data[0]))
    
    for j in range(len(data[0])):
        for i in range(len(data)):
            den[j] = den[j] + (data[i][j])**2
        den[j] = (den[j])**(1/2)
    
    x = list()
    for i in range(len(data)):
        l = list()
        for j in range(len(data[0])):
            l.append(data[i][j]/den[j])
        x.append(l)
    
    #.............Ideal...Best...And...Worst...Solution....
        
    W = list(map(int, weight.strip().split(',')))
    
    if len(W)!= len(data[0]):
        raise Exception("Length of weights must be equal to the no. of columns in the data.")
    
    for i in W:
        if i<0:
            raise Exception("Weights must be positive")
    
    
    w = list()
    
    for i in range(len(W)):
        w.append(W[i]/sum(W))
        
    imp = impact.strip().split(',')
    
    if len(W)!= len(data[0]):
        raise Exception("Length of impacts must be equal to the no. of columns in the data.")
        
    for i in imp:
        if i not in ['+','-']:
            raise Exception("Impacts must be only '+' or '-' signs")
    
    for j in range(len(data[0])):
        for i in range(len(data)):
            x[i][j] = x[i][j] * w[j]
    
    
    ib = list()
    iw = list()
    
    def transpose(x):
        t = list()
        for j in range(len(x[0])):
            l = list()
            for i in range(len(x)):
                l.append(x[i][j])
            t.append(l)
        return t
               
    tx = transpose(x)
    
    for i in range(len(tx)):
        if imp[i] == '+':
            ib.append(max(tx[i]))
            iw.append(min(tx[i]))
        if imp[i] == '-':
            iw.append(max(tx[i]))
            ib.append(min(tx[i]))
    
    p = list()
    
    #..............Calculating.......Performance...........
    for i in range(len(x)):
        sip = 0
        sim = 0
        for j in range(len(x[0])):
            sip = sip + (x[i][j] - ib[j])**2
            sim = sim + (x[i][j] - iw[j])**2
        sip = sip**0.5
        sim = sim**0.5
        pi = sim/(sim+sip)
        p.append(pi)
    #.............Ranking............................
    ranks = sorted(list(range(1,len(p)+1)))
    pt = sorted(p,reverse = True)
    
    perform = list()
    
    for i in p:
        perform.append([i,ranks[pt.index(i)]])
    
    d = {'row_no':['Score', 'Rank']}
    for i in range(len(perform)):
        d[i] = perform[i]
    for k,v in d.items():
        print(k,v)