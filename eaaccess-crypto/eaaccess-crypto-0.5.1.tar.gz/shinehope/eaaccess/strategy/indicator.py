# import copy
# import ccxt
from shinehope.eaaccess.constants import *
from shinehope.eaaccess.candlestick import Candlestick
from shinehope.eaaccess.dataaccess.klinestream import KlineStream
import shinehope.eaaccess.settings as settings
# from .strategy import BaseStrategy
from shinehope.eaaccess.marketdata import BarData, TimeFrame, Ticker
from shinehope.utils.mylogger import appLog
import shinehope.utils.myfunc as myfunc
from datetime import datetime
import pytz
import requests
import copy

class BaseIndicator(object):
    # def __init__(self, strategy:BaseStrategy, timeframe:TimeFrame):
    def __init__(self, strategy, timeframe:TimeFrame):
        super().__init__()

        # Exchange
        # 策略实例.
        self.strategy_instance = strategy
        # self.broker = strategy.broker
        self.exchange = self.strategy_instance.broker.exchange

        self.kline:Candlestick = Candlestick()
        self.symbol = self.strategy_instance.broker.symbol
        # self.run_mode = None
        self.run_mode = self.strategy_instance.broker.run_mode


        self.timeframe:TimeFrame = self.strategy_instance.broker.timeframe
        if timeframe is not None:
            self.timeframe = timeframe

        self.Bar: BarData = None
        # self._Ticker: Ticker = None

        # self.rule_cycle = 15            # 15 (15分)  60 (1H)  1440 (1D 一天)
        self.rule_cycle = myfunc.getCandleSizeMin(self.timeframe.value)
        # self.rule_bar: BarData = BarData()
        self.rule_volume = 0            # previouse-bar accumulated volume
        self.rule_timestamp = 0
        self.rule_pbar:BarData = BarData()

        # 回测的数据 kline stream 数据
        self.btest_kstream: KlineStream = None

    @property
    def Kline(self):
        return self.kline

    def set_backtest_stream(self, histDB:str, tblSymbol:str, tmFrom:int, tmEnd:int):
        if self.btest_kstream is None:
            self.btest_kstream = KlineStream(histDB, self.symbol, tblSymbol, self.timeframe.value)
            self.btest_kstream.set_range(tmFrom, tmEnd)

    def refresh_candles(self, streamBar:BarData = {}) -> bool:
        isOK = False
        if self.run_mode == "BACKTEST":
            if isinstance(streamBar, BarData):
                # bar:BarData = copy.copy(streamDatas)

                # print("kline_bar_update stream....", streamBar)
                bar = self.btest_kstream.nextBar()
                # print("kline_bar_update before....", bar)
                if bar:
                    isNew, sampleBar = self.btest_kstream.resample_bar(bar)
                    # print("kline_bar_update sample....", sampleBar, isNew)
                    if sampleBar:
                        if isNew:
                            # ea.broker.kline.kline_bar_new(bar)        # 2019.11.15
                            self.kline.kline_bar_new(sampleBar)
                            # # ea.broker.run_strategy(sampleBar)
                            # uiKline.kline_bar_new(sampleBar)
                        else:
                            self.kline.kline_bar_update(sampleBar)
                            # # ea.broker.run_strategy(sampleBar)
                            # uiKline.kline_bar_update(sampleBar)
                        # ea.broker.run_strategy(sampleBar)

                        self.Bar = sampleBar

                        # bar = self.kline.getBar()
                        # print("kline_bar_update end   ....", bar)
        elif self.run_mode in {'LIVE', 'DEMO'}:
            # self.strategy_instance.onTick('BTC/USDT', "TickBar")
            try:
                # <kline refresh>
                if self.kline.inited:
                    utcNow = datetime.now(tz=pytz.utc)
                    utcStamp = int(utcNow.timestamp() * 1000)
                    timeDelta = myfunc.getPeriodTimeDelta(self.timeframe)
                    bar = self.kline.getBar()
                    # print("kline_bar_refresh before...", bar, self.rule_volume)
                    appLog.info(f"{utcStamp}, {bar.timestamp}, {timeDelta}")
                    # if utcStamp >= ( bar.timestamp + timeDelta + 1000) :
                    if utcStamp >= ( bar.timestamp + timeDelta ) :
                        appLog.info("refresh kline...{} : {} bars({})".format(self.symbol, self.timeframe.value, self.kline.size))
                        ohlcv = self.exchange.fetch_ohlcv(self.symbol, timeframe=self.timeframe.value, limit=self.kline.size)

                        if len(ohlcv) != self.kline.size:
                            errMsg = f"fetchOHLCV kbars size != {self.kline.size} ..."
                            appLog.error(errMsg)
                            # print(errMsg)
                            return  

                        if not self.kline.kline_refresh(ohlcv):
                            appLog.error("kline_refresh error...")
                            return
                        bar = self.kline.getBar()
                        self.Bar = bar
                        self.rule_volume = bar.volume
                        self.rule_timestamp = bar.timestamp
                        # print("kline_bar_refresh end   ...", bar, self.rule_volume)
                    else:
                        # print("kline_bar_update before....", streamBar, self.rule_volume)
                        # 2019.11.14 改為全部訂閱 kline_1m
                        # self.kline.kline_bar_update(bar)
                        # self.Bar = bar
                        isNew, sampleBar = self.resample_bar(streamBar)
                        # print("kline_bar_update sample....", sampleBar, self.rule_volume, isNew)
                        if sampleBar:
                            # if isNew:
                            #     ea.broker.kline.kline_bar_new(bar)
                            #     # ea.broker.run_strategy(sampleBar)
                            #     uiKline.kline_bar_new(sampleBar)
                            # else:
                            #     # ea.broker.run_strategy(sampleBar)
                            #     uiKline.kline_bar_update(sampleBar)
                            # ea.broker.run_strategy(sampleBar)
                            if not isNew:
                                self.kline.kline_bar_update(sampleBar)
                                self.Bar = sampleBar

                        # #debug
                        # # print("kline_bar_update sample....", sampleBar, self.rule_volume, isNew)
                        # bar = self.kline.getBar()
                        # print("kline_bar_update end   ....", bar, self.rule_volume)    
                else:
                    appLog.info("init kline...{} : {} bars({})".format(self.symbol, self.timeframe.value, self.kline.size))
                    ohlcv = self.exchange.fetch_ohlcv(self.symbol, timeframe=self.timeframe.value, limit=self.kline.size)
                    
                    if len(ohlcv) != self.kline.size:
                        errMsg = f"fetchOHLCV kbars size != {self.kline.size} ..."
                        appLog.error(errMsg)
                        # print(errMsg)
                        return

                    if not self.kline.kline_refresh(ohlcv):
                        appLog.error("kline_refresh error...")
                        return

                    bar = self.kline.getBar()
                    self.Bar = bar
                    self.rule_volume = bar.volume
                    self.rule_timestamp = bar.timestamp                       
            except requests.exceptions.HTTPError as ex:
                appLog.warning("BaseIndicator.Capture HTTPError.." + str(ex))
            except Exception as ex:
                # print(str(ex))
                appLog.error(str(ex))
        # elif self.run_mode == 'PAPER':
        #     pass
        else:
            print(f"not supporting type({self.run_mode})")
        
        return  isOK

    def resample_bar(self, bar:BarData):
        """
            ex: 15m resample rule:

            resample(rule=15, on='timestamp').agg(
                {'open': 'first',
                'high': 'max',
                'low': 'min',
                'close': 'last',
                'volume': 'sum',
            })

            :return   bool, BarData

            由於 LIVE, DEMO 乃透過 websocket 去訂閱 kline_1m, 約每 2 秒(1分鐘內會發生數次) 會得到一次 bar
            若計算 15m 的 volume 直接累加 (sum), 會造成 volume 重複計算
        """
        newBar:BarData = None
        isNew = False
        try:
            # if not self.rule_bar:
            #     newBar = BarData()
            #     newBar.timestamp = bar.timestamp
            #     newBar.open_price = bar.open_price
            #     newBar.high_price = bar.high_price
            #     newBar.low_price = bar.low_price
            #     newBar.close_price = bar.close_price
            #     newBar.volume = bar.volume
            #     self.rule_bar = newBar
            # else:
            tstamp = self.Bar.timestamp + self.rule_cycle * 60 * 1000         # next bar timestamp (millisecond)
            if bar.timestamp >= tstamp:
                # 由於 LIVE, DEMO 模式下, 新的 Bar 產生時, 會重新 refresh kline, 此時會更動 self.Bar
                # 所以 resample_bar 不處理, 留給 <kline refresh> 處理 
                # self.Bar.timestamp = bar.timestamp
                # self.Bar.open_price = bar.open_price
                # self.Bar.high_price = bar.high_price
                # self.Bar.low_price = bar.low_price
                # self.Bar.close_price = bar.close_price
                # self.Bar.volume = bar.volume
                newBar = BarData()
                newBar.timestamp = self.Bar.timestamp
                newBar.open_price = self.Bar.open_price
                newBar.high_price = self.Bar.high_price
                newBar.low_price = self.Bar.low_price
                newBar.close_price = self.Bar.close_price
                newBar.volume = self.Bar.volume
                isNew = True
            else:
                newBar = BarData()
                newBar.timestamp = self.Bar.timestamp
                newBar.open_price = self.Bar.open_price

                if bar.high_price > self.Bar.high_price:
                    self.Bar.high_price = bar.high_price
                newBar.high_price = self.Bar.high_price

                if bar.low_price < self.Bar.low_price:
                    self.Bar.low_price = bar.low_price
                newBar.low_price = self.Bar.low_price

                self.Bar.close_price = bar.close_price
                newBar.close_price = self.Bar.close_price

                if bar.timestamp == self.Bar.timestamp:
                    # ??? 發現於 PERIOD 開始時, 使用 fetchOHLCV 所得的 volumn 值, 比之後透過 streaming 取得的 1m 的 volumn
                    # 還高 ??? ==> 使用 fetchOHLCV 配合 streaming 做累計的結果... 並無法取得最後一個 bar 的精準值
                    # 改為以下做法, 取得接近值
                    # self.Bar.volume = bar.volume
                    if bar.volume > self.rule_volume:
                        self.rule_volume = bar.volume
                    self.Bar.volume = self.rule_volume
                elif bar.timestamp > self.Bar.timestamp:
                    if bar.timestamp == self.rule_timestamp:
                        # self.Bar.volume = self.rule_volume + bar.volume
                        self.rule_pbar = bar
                    elif bar.timestamp > self.rule_timestamp:
                        self.rule_timestamp = bar.timestamp
                        self.rule_volume = round(self.rule_volume + self.rule_pbar.volume, 8)
                    self.Bar.volume = round(self.rule_volume + bar.volume, 8)
                newBar.volume = self.Bar.volume

                # newBar = self.Bar

        except Exception as ex:
            print(ex)
            isNew = False
            newBar = None

        return isNew, newBar

    def sma(self, period, applied_price=PRICE_CLOSE, mode=MODE_SINGLE):
        """
        Simple moving average.
        """
        result = self.kline.sma(period, applied_price, mode)
        return result

    def ema(self, period, applied_price=PRICE_CLOSE, mode=MODE_SINGLE):
        """
        EMA的全名是指數加權移動平均（Exponential Moving Average或簡稱為EMA）
        """
        result = self.kline.ema(period, applied_price, mode)
        return result

    def std(self, period, applied_price=PRICE_CLOSE, mode=MODE_SINGLE):
        """
        Standard deviation
        """
        result = self.kline.std(period, applied_price, mode)
        return result

    def cci(self, period, mode=MODE_SINGLE):
        """
        Commodity Channel Index (CCI).
        """
        result = self.kline.cci(period, mode)
        return result

    def atr(self, period, mode=MODE_SINGLE):
        """
        Average True Range (ATR).
        """
        result = self.kline.atr(period, mode)
        return result

    def rsi(self, period, applied_price=PRICE_CLOSE, mode=MODE_SINGLE):
        """
        Relative Strenght Index (RSI).
        """
        # # result = talib.RSI(self.close, period)
        # taPrice = self.indicator_price(applied_price)
        # result = talib.RSI(taPrice, period)
        # if mode:
        #     return result
        # return result[-1]

        result = self.kline.rsi(period, applied_price, mode)
        return result

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
        # # macd, signal, hist = talib.MACD(
        # #     self.close, fast_period, slow_period, signal_period
        # # )
        # taPrice = self.indicator_price(applied_price)
        # macd, signal, hist = talib.MACD(
        #     taPrice, fast_period, slow_period, signal_period
        # )
        # if mode:
        #     return macd, signal, hist
        # return macd[-1], signal[-1], hist[-1]
        
        macd, signal, hist = self.kline.macd(fast_period, slow_period, signal_period, applied_price, mode)
        return macd, signal, hist

    def adx(self, period, mode=MODE_SINGLE):
        """
        ADX.
        """        
        result = self.kline.adx(period, mode)
        return result

    def boll(self, period, dev, applied_price=PRICE_CLOSE, mode=MODE_SINGLE):
        """
        Bollinger Channel.
        """
        up, down = self.kline.boll(period, dev, applied_price, mode)
        return up, down

    def keltner(self, period, dev, applied_price=PRICE_CLOSE, mode=MODE_SINGLE):
        """
        Keltner Channel.
        """
        up, down = self.kline.keltner(period, dev, applied_price, mode)
        return up, down

    def donchian(self, period, mode=MODE_SINGLE):
        """
        Donchian Channel.
        """
        up, down = self.kline.donchian(period, mode)
        return up, down

    def stoch(self, fastk_period=9, smoothk_period=3, smoothd_period=3, mode=MODE_SINGLE):
        """
        Stochastic (MA_TYPE=0; Smooth)
        """
        slowk, slowd = self.kline.stoch(fastk_period, smoothk_period, smoothd_period, mode)
        return slowk, slowd

    def iCustom(self, applied_price=PRICE_CLOSE, mode=MODE_SINGLE, params={}):
        print("BaseIndicator.iCustom...")