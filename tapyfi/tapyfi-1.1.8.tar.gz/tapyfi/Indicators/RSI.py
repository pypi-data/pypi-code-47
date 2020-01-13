import pandas as pd
import numpy as np
from tapyfi.Helpers.MAs import *





def RSI(Series,Period=14,MAMethod=sma):

    Data=pd.DataFrame(Series)
    Data.columns=['Series']
    Data.loc[:,'Change']=Data['Series'].diff()
    Data=Data.iloc[1:]
    Data.loc[ Data['Change']>0   ,'Gain']= Data['Change']
    Data.loc[ Data['Change']<0   ,'Loss']= Data['Change']
    Data[np.isnan(Data)]=0
    Data.loc[:,'AvgGain']=MAMethod(Data['Gain'],Period)
    Data.loc[:,'AvgLoss']=MAMethod(Data['Loss'],Period).abs()
    Data.loc[:,'RS']=Data['AvgGain']/Data['AvgLoss']
    Data.loc[:,'RSI']=100-(100/(1+(Data['RS'])))
    return Data['RSI'].values





