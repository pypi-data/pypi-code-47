import pandas as pd
import numpy as np

def preprocessData(InputDataFile):
    df = pd.read_csv(InputDataFile)
    df = df.fillna(df.mode().iloc[0])
    df = df.apply(lambda x: pd.factorize(x)[0])
    return df

def vectorNormalize(df):
    denominator = []
    
    for feature in range(df.shape[1]):
        denominator.append((df.iloc[:,feature]**2).sum())

    denominator = np.array(denominator)
    denominator = denominator**0.5
    #print(denominator)
    
    for feature in range(df.shape[1]):
        df.iloc[:,feature] = df.iloc[:,feature]/denominator[feature]
    #print(df.head())
    return df

def weightMultiplication(weights,df):
    weights = weights.split(",")
    weights = [int(i) for i in weights]
    
    for feature in range(df.shape[1]):
        df.iloc[:,feature] = df.iloc[:,feature]*weights[feature]
        
    return df

def idealValues(impacts,df):
    impacts = impacts.split(",")
    v_best = []
    v_worst = []
    
    for feature in range(df.shape[1]):
        if impacts[feature]=="+":
            v_best.append(df.iloc[:,feature].max())
            v_worst.append(df.iloc[:,feature].min())
        else:
            v_best.append(df.iloc[:,feature].min())
            v_worst.append(df.iloc[:,feature].max())
        
    return v_best,v_worst

def calculateEuclideanDistance(df,v_best,v_worst):
    s_best = []
    s_worst = []
    
    a=0
    b=0
    
    for row in range(df.shape[0]):
        for feature in range(df.shape[1]):
            a += (df.iloc[row,feature]-v_best[feature])**2
            b += (df.iloc[row,feature]-v_worst[feature])**2
        s_best.append(a**0.5)
        s_worst.append(b**0.5)
        
    return s_best,s_worst

def calculatePerformance(s_best,s_worst):
    p = np.empty([len(s_best)])
    s_best = np.array(s_best)
    s_worst = np.array(s_worst)
    
    p = s_worst/(s_best+s_worst)
    return p

def allocateRanks(p):
    
    order = p.argsort()
    ranks = order.argsort()
    return ranks

def topsis(InputDataFile,weights,Impacts):
    df = preprocessData(InputDataFile)
    df = vectorNormalize(df)
    df = weightMultiplication(weights,df)
    v_best,v_worst = idealValues(Impacts,df)
    s_best,s_worst = calculateEuclideanDistance(df,v_best,v_worst)
    p = calculatePerformance(s_best,s_worst)
    r = allocateRanks(p)
    
    best_label = None
    for label in range(df.shape[0]):
        print("Label",label+1,"has rank:",r[label])
        if r[label]==0:
            best_label = label
    
    print()
    print("Best Label is:",best_label)
