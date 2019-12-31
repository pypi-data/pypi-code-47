"""
    kline/candlestick module
"""

import numpy as np
import talib
from .marketdata import BarData
import  threading
from shinehope.eaaccess.constants import *

class Candlestick(object):
    """
    Series container of Bar: Open, High, Low, Close, Volume
    """

    def __init__(self, size=300):
        """Constructor"""
        self.count = 0
        self.start_candle = 10
        self.size = size
        self.inited = False
        self.lock = threading.Lock()

        # self.__timestamp = np.zeros(size+1, dtype=np.longlong)     # UTC milliseconds (UTC+8)
        # self.__open_price = np.zeros(size+1)
        # self.__high_price = np.zeros(size+1)
        # self.__low_price = np.zeros(size+1)
        # self.__close_price = np.zeros(size+1)
        # self.__volume = np.zeros(size+1)
        self.__timestamp = np.zeros(size, dtype=np.longlong)     # UTC milliseconds (UTC+8)
        self.__open_price = np.zeros(size)
        self.__high_price = np.zeros(size)
        self.__low_price = np.zeros(size)
        self.__close_price = np.zeros(size)
        self.__volume = np.zeros(size)
   
    def kline_refresh(self, kbars:[]) -> bool:
        isOK = False

        size = len(kbars)
        if size != self.size:
            return isOK

        try:
            if self.lock.acquire():
                # for idx, bar in enumerate(kbars, start=0):
                #     self.__timestamp[self.size - idx] = bar[0]
                #     self.__open_price[self.size - idx] = bar[1]
                #     self.__high_price[self.size - idx] = bar[2]
                #     self.__low_price[self.size - idx] = bar[3]
                #     self.__close_price[self.size - idx] = bar[4]
                #     self.__volume[self.size - idx] = bar[5]

                # self.__timestamp[0] = kbars[self.size - 1][0]
                # self.__open_price[0] = kbars[self.size - 1][1]
                # self.__high_price[0] = kbars[self.size - 1][2]
                # self.__low_price[0] = kbars[self.size - 1][3]
                # self.__close_price[0] = kbars[self.size - 1][4]
                # self.__volume[0] = kbars[self.size - 1][5]
                for idx, bar in enumerate(kbars, start=0):
                    self.__timestamp[idx] = bar[0]
                    self.__open_price[idx] = bar[1]
                    self.__high_price[idx] = bar[2]
                    self.__low_price[idx] = bar[3]
                    self.__close_price[idx] = bar[4]
                    self.__volume[idx] = bar[5]

                self.inited = True
                isOK = True
        except Exception as ex:
            isOK = False
        finally:
            self.lock.release()

        return  isOK

    def kline_bar_update(self, bar: BarData):
        try:
            if self.lock.acquire():
                # self.__timestamp[0] = bar.timestamp
                # self.__open_price[0] = bar.open_price
                # self.__high_price[0] = bar.high_price
                # self.__low_price[0] = bar.low_price
                # self.__close_price[0] = bar.close_price
                # self.__volume[0] = bar.volume
                if bar.timestamp == self.__timestamp[self.size - 1]:
                    # self.__timestamp[self.size - 1] = bar.timestamp
                    self.__open_price[self.size - 1] = bar.open_price
                    self.__high_price[self.size - 1] = bar.high_price
                    self.__low_price[self.size - 1] = bar.low_price
                    self.__close_price[self.size - 1] = bar.close_price
                    self.__volume[self.size - 1] = bar.volume
        finally:
            self.lock.release()

    def set_backtest_start_candle(self, startCandle=10):
        self.start_candle = startCandle

    def kline_bar_new(self, bar: BarData):
        """
        Add new bar data into Kline.
        """
        self.count += 1
        if not self.inited and self.count >= self.start_candle:
            self.inited = True

        # [1,2,3,4,5,6,7,8,9,10]
        # [1,2,3,4,5,6,7,8,9] = [2,3,4,5,6,7,8,9,10]
        # [2,3,4,5,6,7,8,9,10, 10]
        self.__timestamp[:-1] = self.__timestamp[1:]
        self.__open_price[:-1] = self.__open_price[1:]
        self.__high_price[:-1] = self.__high_price[1:]
        self.__low_price[:-1] = self.__low_price[1:]
        self.__close_price[:-1] = self.__close_price[1:]
        self.__volume[:-1] = self.__volume[1:]

        # [2,3,4,5,6,7,8,9,10, 10] 然后最后一个数字被替换了.
        self.__timestamp[-1] = bar.timestamp
        self.__open_price[-1] = bar.open_price
        self.__high_price[-1] = bar.high_price
        self.__low_price[-1] = bar.low_price
        self.__close_price[-1] = bar.close_price
        self.__volume[-1] = bar.volume

        # # [1,2,3,4,5,6,7,8,9,10]
        # # [2,3,4,5,6,7,8,9,10] = [1,2,3,4,5,6,7,8,9]
        # # [x,1,2,3,4,5,6,7,8,9]
        # self.__timestamp[1:] = self.__timestamp[:-1]
        # self.__open_price[1:] = self.__open_price[:-1]
        # self.__high_price[1:] = self.__high_price[:-1]
        # self.__low_price[1:] = self.__low_price[:-1]
        # self.__close_price[1:] = self.__close_price[:-1]
        # self.__volume[1:] = self.__volume[:-1]

        # # [x,1,2,3,4,5,6,7,8,9]  最前一個數字被替換.
        # self.__timestamp[0] = bar.timestamp
        # self.__open_price[0] = bar.open_price
        # self.__high_price[0] = bar.high_price
        # self.__low_price[0] = bar.low_price
        # self.__close_price[0] = bar.close_price
        # self.__volume[0] = bar.volume

    @property
    def open(self):
        """
        Get open price time series.
        """
        return self.__open_price

    @property
    def high(self):
        """
        Get high price time series.
        """
        return self.__high_price

    @property
    def low(self):
        """
        Get low price time series.
        """
        return self.__low_price

    @property
    def close(self):
        """
        Get close price time series.
        """
        return self.__close_price

    @property
    def volume(self):
        """
        Get trading volume time series.
        """
        return self.__volume

    @property
    def timeframe(self):
        return self.__timestamp    

    def getBar(self, idx=0) -> BarData:
        """ 
            Get BarData in reverse order: '0' --> last bar; 1 --> previous bar, ...
        """
        bar: BarData = None
        try:
            if self.lock.acquire():
                if self.inited and idx >= 0 and idx < self.size:
                    # bar = BarData(self.__timestamp[idx], self.__open_price[idx], self.__high_price[idx], 
                    #     self.__low_price[idx], self.__close_price[idx], self.__volume[idx])
                    barIdx = self.size - 1 - idx
                    bar = BarData(self.__timestamp[barIdx], self.__open_price[barIdx], self.__high_price[barIdx], 
                        self.__low_price[barIdx], self.__close_price[barIdx], self.__volume[barIdx])
        finally:
            self.lock.release()

        return  bar

    def indicator_price(self, applied_price:int) -> []:
        taPrice = self.close
        if applied_price == PRICE_HIGH:
            taPrice = self.high
        elif applied_price == PRICE_LOW:
            taPrice = self.low
        elif applied_price == PRICE_OPEN:
            taPrice = self.open

        return  taPrice

    def sma(self, period, applied_price=PRICE_CLOSE, mode=MODE_SINGLE):
        """
        Simple moving average.
        """
        # result = talib.SMA(self.close, period)
        taPrice = self.indicator_price(applied_price)
        result = talib.SMA(taPrice, period)
        if mode:
            return result
        return result[-1]

    def ema(self, period, applied_price=PRICE_CLOSE, mode=MODE_SINGLE):
        # result = talib.EMA(self.close, period)
        taPrice = self.indicator_price(applied_price)
        result = talib.EMA(taPrice, period)
        if mode:
            return result
        return result[-1]

    def std(self, period, applied_price=PRICE_CLOSE, mode=MODE_SINGLE):
        """
        Standard deviation
        """
        # result = talib.STDDEV(self.close, period)
        taPrice = self.indicator_price(applied_price)
        result = talib.STDDEV(taPrice, period)
        if mode:
            return result
        return result[-1]

    def cci(self, period, mode=MODE_SINGLE):
        """
        Commodity Channel Index (CCI).
        """
        result = talib.CCI(self.high, self.low, self.close, period)
        if mode:
            return result
        return result[-1]

    def atr(self, period, mode=MODE_SINGLE):
        """
        Average True Range (ATR).
        """
        result = talib.ATR(self.high, self.low, self.close, period)
        if mode:
            return result
        return result[-1]

    def rsi(self, period, applied_price=PRICE_CLOSE, mode=MODE_SINGLE):
        """
        Relative Strenght Index (RSI).
        """
        # result = talib.RSI(self.close, period)
        taPrice = self.indicator_price(applied_price)
        result = talib.RSI(taPrice, period)
        if mode:
            return result
        return result[-1]

    def macd(self, fast_period=12, slow_period=26, signal_period=9, applied_price=PRICE_CLOSE, mode=MODE_SINGLE):
        """
        macd = 12 天 EMA - 26 天 EMA (DIF線：2 條不同天期的 EMA 相減).
        signal = 9 天 MACD的EMA (MACD 線：用 DIF 再取一次移動平均).
        hist = MACD - MACD signal (柱狀圖是用 DIF-MACD 所繪製。).

        用快慢線交叉 看出買賣點
            1.快線（DIF）向上突破 慢線（MACD）。→買進訊號
            2.快線（DIF）向下跌破 慢線（MACD）。→賣出訊號

        用柱狀圖 看出買賣點
            1. 柱線由負轉正，為買進訊號。
            2. 柱線由正轉負，為賣出訊號。
        """
        # macd, signal, hist = talib.MACD(
        #     self.close, fast_period, slow_period, signal_period
        # )
        taPrice = self.indicator_price(applied_price)
        macd, signal, hist = talib.MACD(
            taPrice, fast_period, slow_period, signal_period
        )
        if mode:
            return macd, signal, hist
        return macd[-1], signal[-1], hist[-1]

    def adx(self, period, mode=MODE_SINGLE):
        """
        ADX.
        """
        result = talib.ADX(self.high, self.low, self.close, period)
        if mode:
            return result
        return result[-1]

    def boll(self, period, dev, applied_price=PRICE_CLOSE, mode=MODE_SINGLE):
        """
        Bollinger Channel.
        """
        taPrice = self.indicator_price(applied_price)
        mid = self.sma(period, taPrice, mode)
        std = self.std(period, taPrice, mode)

        up = mid + std * dev
        down = mid - std * dev

        return up, down

    def keltner(self, period, dev, applied_price=PRICE_CLOSE, mode=MODE_SINGLE):
        """
        Keltner Channel.
        """
        taPrice = self.indicator_price(applied_price)
        mid = self.sma(period, taPrice, mode)
        atr = self.atr(period, mode)

        up = mid + atr * dev
        down = mid - atr * dev

        return up, down

    def donchian(self, period, mode=MODE_SINGLE):
        """
        Donchian Channel.
        """
        up = talib.MAX(self.high, period)
        down = talib.MIN(self.low, period)

        if mode:
            return up, down
        return up[-1], down[-1]

    def stoch(self, fastk_period=9, smoothk_period=3, smoothd_period=3, mode=MODE_SINGLE):
        """
        Stochastic (MA_TYPE=0; Smooth)
        """
        slowk, slowd = talib.STOCH(self.high, self.low, self.close,                         
                        fastk_period=fastk_period,
                        slowk_period=smoothk_period,
                        slowk_matype=talib.MA_Type.SMA,
                        slowd_period=smoothd_period,
                        slowd_matype=talib.MA_Type.SMA)

        if mode:
            return slowk, slowd
        return slowk[-1], slowd[-1]

"""
MQL4 Indicator API
=====================================================================================
iMACD
Calculates the Moving Averages Convergence/Divergence indicator and returns its value.
---------------------------------------------------------------------
double  iMACD(
   string       symbol,           // symbol
   int          timeframe,        // timeframe
   int          fast_ema_period,  // Fast EMA period
   int          slow_ema_period,  // Slow EMA period
   int          signal_period,    // Signal line period
   int          applied_price,    // applied price
   int          mode,             // line index
   int          shift             // shift
   );
---------------------------------------------------------------------
Parameters

symbol

[in]  Symbol name on the data of which the indicator will be calculated. NULL means the current symbol.

timeframe

[in]  Timeframe. It can be any of ENUM_TIMEFRAMES enumeration values. 0 means the current chart timeframe.

fast_ema_period

[in]  Fast EMA averaging period.

slow_ema_period

[in]  Slow EMA averaging period.

signal_period

[in]  Signal line averaging period.

applied_price

[in]  Applied price. It can be any of ENUM_APPLIED_PRICE enumeration values.

mode

[in]  Indicator line index. It can be one of the Indicators line identifiers enumeration values (0-MODE_MAIN, 1-MODE_SIGNAL).

shift

[in]  Index of the value taken from the indicator buffer (shift relative to the current bar the given amount of periods ago).

Returned value

Numerical value of the Moving Average of Oscillator indicator.

Note

In some systems it is called MACD Histogram and plotted as two lines. In MetaTrader 4 client terminal MACD is plotted as histogram.
-------------------------------------------------------------------------------------------------
Example:
if(iMACD(NULL,0,12,26,9,PRICE_CLOSE,MODE_MAIN,0)>iMACD(NULL,0,12,26,9,PRICE_CLOSE,MODE_SIGNAL,0)) return(0);
-------------------------------------------------------------------------------------------------
Price Constants
Calculations of technical indicators require price values and/or values of volumes, on which calculations will be performed. There are 7 predefined identifiers from the ENUM_APPLIED_PRICE enumeration, used to specify the desired price base for calculations.

ENUM_APPLIED_PRICE
ID	          Value	Description
PRICE_CLOSE	    0	Close price
PRICE_OPEN	    1	Open price
PRICE_HIGH	    2	The maximum price for the period
PRICE_LOW	    3	The minimum price for the period
PRICE_MEDIAN	4	Median price, (high + low)/2
PRICE_TYPICAL	5	Typical price, (high + low + close)/3
PRICE_WEIGHTED	6	Weighted close price, (high + low + close + close)/4

=============================================================================
iATR
Calculates the Average True Range indicator and returns its value.

double  iATR(
   string       symbol,     // symbol
   int          timeframe,  // timeframe
   int          period,     // averaging period
   int          shift       // shift
   );

=============================================================================
iCCI
Calculates the Commodity Channel Index indicator and returns its value.

double  iCCI(
   string       symbol,           // symbol
   int          timeframe,        // timeframe
   int          period,           // averaging period
   int          applied_price,    // applied price
   int          shift             // shift
   );

==============================================================================
iCCIOnArray
Calculates the Commodity Channel Index indicator on data, stored in array, and returns its value.

double  iCCIOnArray(
   double       array[],          // array with data
   int          total,            // number of elements
   int          period,           // averaging period
   int          shift             // shift
   );

==================================================================
talib.MA_Type

        MA_Type: 0=SMA, 1=EMA, 2=WMA, 3=DEMA, 4=TEMA, 5=TRIMA, 6=KAMA, 7=MAMA, 8=T3 (Default=SMA)
"""
