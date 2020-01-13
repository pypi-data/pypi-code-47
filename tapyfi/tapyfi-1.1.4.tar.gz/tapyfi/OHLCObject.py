import pandas as pd
import numpy as np
from tapyfi.Helpers.MAs import *
from tapyfi.Indicators.RSI import RSI
class OHLCObject(object):
    def __init__(self,timeseries,open=None,high=None,low=None,close=None,volume=None):
        self.timeseries= pd.to_datetime(timeseries)
        self.open=np.array(open)
        self.high=np.array(high)
        self.low=np.array(low)
        self.close=np.array(close)
        self.volume=np.array(volume)

    def RSI(self,Period=14,MAType=sma,Series="close"):

        if Series=="open":
            self.RSI_values=RSI(self.open,Period=Period,MAMethod=MAType)

        if Series == "high":
            self.RSI_values = RSI(self.high, Period=Period, MAMethod=MAType)

        if Series == "low":
            self.RSI_values = RSI(self.low, Period=Period, MAMethod=MAType)

        if Series == "close":
            self.RSI_values = RSI(self.close, Period=Period, MAMethod=MAType)


        return self.RSI_values










