import csv
import sys


def normalization(dataset):
    dividend=[0]*(len(dataset[0])-1)
    col=0
    for i in range(len(dataset)):
        for j in range(1,len(dataset[0])):
            dataset[i][j]=int(dataset[i][j])
    for i in dataset:
        for j in i[1:]:
            dividend[col]=dividend[col]+j*j
            col+=1
        col=0
    for i in range(len(dividend)):
        dividend[i]=dividend[i]**0.5
    num=0
    for i in range(len(dataset)):
        for j in range(1,len(dataset[0])):
            dataset[i][j]=dataset[i][j]/dividend[num]
            num+=1
        num=0
    return dataset

def weighted(dataset,weights):
    for i in range(len(dataset)):
        for j in range(1,len(dataset[0])):
            dataset[i][j]=dataset[i][j]*float(weights[j-1])
    return dataset

def best(dataset,impacts):
    x=-10000000;y=100000000
    ans=[]
    for i in range(1,len(dataset[0])):
        for j in range(len(dataset)):
            if(impacts[i-1]=='+'):
                x=max(x,dataset[j][i])
            else:
                y=min(y,dataset[j][i])
        if(impacts[i-1]=='+'):
            ans.append(x)
        else:
            ans.append(y)
        x=-10000000;y=10000000
    return ans

def worst(dataset,impacts):
    x=10000000;y=-100000000
    ans=[]
    for i in range(1,len(dataset[0])):
        for j in range(len(dataset)):
            if(impacts[i-1]=='+'):
                x=min(x,dataset[j][i])
            else:
                y=max(y,dataset[j][i])
        if(impacts[i-1]=='+'):
            ans.append(x)
        else:
            ans.append(y)
        x=10000000;y=-10000000
    return ans

def calc_eu(dataset,ideal):
    ans=[]
    x=0
    for i in range(len(dataset)):
        for j in range(1,len(dataset[0])):
            x=x+(dataset[i][j]-ideal[j-1])**2
        ans.append(x**0.5)
        x=0
    return ans

def performance(x,y):
    ans=[]
    z=0
    for i in range(len(x)):
        z=y[i]/(x[i]+y[i])
        ans.append(z)
    return ans

dataset=[]
with open(sys.argv[1],'r') as file:
    reader=csv.reader(file)
    for row in reader:
        dataset.append(row)

weights=sys.argv[2].split(",")
impacts=sys.argv[3].split(",")

if(len(dataset[0])-1<len(weights) or len(dataset[0])-1<len(impacts)):
    print("Dataset has less columns")
elif(len(dataset[0])-1>len(weights)):
    print("Less no. of weights are passed")
elif (len(dataset[0])-1>len(impacts)):
    print("Less no. of impacts are passed")
else:
    decision_matrix=normalization(dataset)
    weight_matrix=weighted(decision_matrix,weights)
    ideal_best=best(weight_matrix,impacts)
    ideal_worst=worst(weight_matrix,impacts)
    euclidean_best=calc_eu(weight_matrix,ideal_best)
    euclidean_worst=calc_eu(weight_matrix,ideal_worst)
    performance_score=performance(euclidean_best,euclidean_worst)
    dict={}
    num=0
    for i in dataset:
        dict[str(performance_score[num])]=i[0]
        num+=1
    performance_score.sort(reverse=True)
    for i in performance_score:
        print(dict[str(i)])


    