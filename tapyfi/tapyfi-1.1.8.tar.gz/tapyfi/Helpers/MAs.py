import numpy as np
import pandas as pd

def sma(data,period):
    if len(data) < period:
        return None
    else:
        sma=data.rolling(period+1).mean()
        return sma


def ema(data, period=21):
    weights = np.exp(np.linspace(-1., 0., period))
    weights /= weights.sum()
    a =  np.convolve(data, weights)[:len(data)]
    a[:period-1]=None
    a=pd.Series(a)
    a.index=data.index
    return a


def dema(data,period):
    dema=(2*ema(data,period)-ema(ema(data,period),period))
    return dema




def dema(data,period):
    dema=(2*ema(data,period)-ema(ema(data,period),period))
    return dema



def wma(data,period):

    WMAData=pd.DataFrame(data)
    Name=WMAData.columns[0]

    WMAList = list()
    for i in range(1,period+1):
        WMAData[Name + str(i)] = WMAData[WMAData.columns[0]].shift(int((i)))
        WMAList.append(Name + str(i))


    NumberList=list(range(2,period+1))
    NumberList.reverse()


    WMAData['Total']=WMAData[Name + str(10)]

    for i in range(1,period):
        print(i)

        print(NumberList[int(i-1)])
        print(Name+str(i))
        WMAData['Total']=WMAData['Total']+(WMAData[Name + str(i)]*NumberList[int(i-1)])


    WMAData['WMA']=WMAData['Total']/(sum(NumberList)+1)


    return WMAData['WMA']