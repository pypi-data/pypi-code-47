# import numpy as np
# import pandas as pd
import os
import sqlite3
from shinehope.eaaccess.marketdata import BarData, Ticker
import shinehope.utils.myfunc as myfunc

class KlineStream(object):
    def __init__(self, dbFile, symbol='BTC/USDT', tblSymbol='USDT_BTC', candleSize='15m'):
        """Constructor"""
        self.dbFileName = dbFile
        self.symbol = symbol
        self.tbl_symbol = tblSymbol
        self.candleSize = candleSize
        self.timeFrom = None
        self.timeTo = None
        # self.kline_df: pd.DataFrame = None
        self.kline_bars = None
        self.kline_bars_curr: int = -1
        self.kline_bars_total: int = 0
        self.tickInfo: Ticker = Ticker()
        self.fetchOffect = 0
        self.fetchSize = 2 * 24 * 60    # 2 days == 2880 分 (筆)
        # self.rule_cycle = "15T"       # 15T (15分)  1H  1D (一天) 1W 1M
        self.rule_cycle = 15            # 15 (15分)  60 (1H)  1440 (1D 一天)
        self.rule_bar: BarData = BarData()
    
    def set_range(self, timeFrom, timeTo) -> bool:
        isOK = False
        if timeTo <= timeFrom:
            return  isOK

        self.timeFrom = timeFrom
        self.timeTo = timeTo

        # # trailChar = self.candleSize[-1]
        # # valueHead = self.candleSize[:-1]
        # # if trailChar == 'm':
        # #     self.rule_cycle = valueHead + "T"
        # # elif trailChar == 'h':
        # #     self.rule_cycle = valueHead + "H"
        # # elif trailChar == 'd':
        # #     self.rule_cycle = valueHead + "D"
        # trailChar = self.candleSize[-1]
        # valueHead = int(self.candleSize[:-1])
        # if trailChar == 'm':
        #     self.rule_cycle = valueHead * 1
        # elif trailChar == 'h':
        #     self.rule_cycle = valueHead * 60
        # elif trailChar == 'd':
        #     self.rule_cycle = valueHead * 24 * 60
        self.rule_cycle = myfunc.getCandleSizeMin(self.candleSize)

        if self.kline_bars == None:
            isOK = self.fetch_bars()

        return isOK


    def nextBar(self) -> BarData:
        bar: BarData = None
        if self.timeFrom == None:
            return None

        isOK = True
        if self.kline_bars_curr >= self.kline_bars_total:
            # pass
            # dataRow = self.kline_df.loc[self.kline_bars_total - 1, : ]
            # lastTime = int(dataRow.open_time.timestamp())
            dataRow = self.kline_bars[self.kline_bars_total - 1]
            lastTime = int(dataRow[0] / 1000)                               # start
            # print("lastTime: ", lastTime, self.timeTo)
            if lastTime < self.timeTo:
                # self.fetchOffect += self.kline_bars_total
                self.fetchOffect += self.fetchSize
                isOK = self.fetch_bars()
        # else:

        if isOK:
            # dataRow = self.kline_df.loc[self.kline_bars_curr, : ]          # pandas Series
            # print("self.kline_bars_curr: ", self.kline_bars_curr, self.kline_bars_total)
            dataRow = self.kline_bars[self.kline_bars_curr]
            # print(type(dataRow))
            # print(type(dataRow.open_time))
            bar = BarData()
            # bar.timestamp = int(dataRow.open_time.timestamp()) * 1000       # pandas Timestamp
            # bar.open_price = round(dataRow.open, 8)
            # bar.high_price = round(dataRow.high, 8)
            # bar.low_price = round(dataRow.low, 8)
            # bar.close_price = round(dataRow.close, 8)
            # bar.volume = round(dataRow.volume, 8)
            bar.timestamp = dataRow[0]                              # start
            bar.open_price = round(dataRow[1], 8)                   # open
            bar.high_price = round(dataRow[2], 8)                   # high
            bar.low_price = round(dataRow[3], 8)                    # low
            bar.close_price = round(dataRow[4], 8)                  # close
            bar.volume = round(dataRow[5], 8)                       # volume
            self.kline_bars_curr += 1          

        return  bar

    def fetch_bars(self) -> bool:
        if not os.path.exists(self.dbFileName):
            return False

        isOK = False
        try:
            conn = sqlite3.connect(self.dbFileName)
            # cursor = conn.cursor()
            qryTime = self.timeFrom * 1000
            sql = (f"select start, open, high, low, close, volume from candles_{self.tbl_symbol} where "
                f"start >= {qryTime} order by start asc limit {self.fetchSize} offset {self.fetchOffect};")
            cursor = conn.execute(sql)
            rows = cursor.fetchall()
            rowCnts = len(rows)
            if rowCnts > 0:
                self.kline_bars = rows
                self.kline_bars_curr = 0
                self.kline_bars_total = rowCnts

                isOK = True
            else:
                isOK = False
        except Exception as ex:
            print(ex)
        finally:
            cursor.close()
            conn.close()

        return isOK

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

            由於 BACKTEST 乃由 1m 去生成其它時區(ex: 15m), 而 1m 的 ohlcv 中 volume 及 1m 最後的值,
            所以計算 15m 的 volume 直接累加 (sum)
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
            tstamp = self.rule_bar.timestamp + self.rule_cycle * 60 * 1000         # next bar timestamp (millisecond)
            if bar.timestamp >= tstamp:
                self.rule_bar.timestamp = bar.timestamp
                self.rule_bar.open_price = bar.open_price
                self.rule_bar.high_price = bar.high_price
                self.rule_bar.low_price = bar.low_price
                self.rule_bar.close_price = bar.close_price
                self.rule_bar.volume = bar.volume
                newBar = BarData()
                newBar.timestamp = self.rule_bar.timestamp
                newBar.open_price = self.rule_bar.open_price
                newBar.high_price = self.rule_bar.high_price
                newBar.low_price = self.rule_bar.low_price
                newBar.close_price = self.rule_bar.close_price
                newBar.volume = self.rule_bar.volume
                isNew = True
            else:
                newBar = BarData()
                newBar.timestamp = self.rule_bar.timestamp
                newBar.open_price = self.rule_bar.open_price

                if bar.high_price > self.rule_bar.high_price:
                    self.rule_bar.high_price = bar.high_price
                newBar.high_price = self.rule_bar.high_price

                if bar.low_price < self.rule_bar.low_price:
                    self.rule_bar.low_price = bar.low_price
                newBar.low_price = self.rule_bar.low_price

                self.rule_bar.close_price = bar.close_price
                newBar.close_price = self.rule_bar.close_price

                self.rule_bar.volume = round(self.rule_bar.volume + bar.volume, 8)
                newBar.volume = self.rule_bar.volume

                # newBar = self.rule_bar

        except Exception as ex:
            print(ex)
            isNew = False
            newBar = None

        return isNew, newBar

    def bar_tickinfo(self, bar:BarData, spread=1.5) -> Ticker:
        tickInfo = Ticker()
        tickInfo.symbol = self.symbol
        tickInfo.rawsymbol = myfunc.getRawAPISymbol(self.symbol)
        tickInfo.timestamp = bar.timestamp
        tickInfo.high = bar.high_price
        tickInfo.low = bar.low_price
        tickInfo.bid = bar.close_price
        tickInfo.bidVolume = bar.volume             ## ??
        tickInfo.ask = bar.close_price + spread
        tickInfo.askVolume = bar.volume
        # volume weighed average price  ??  (2019.11.12 先定義為 best ASK, BID VWAP...)
        tickInfo.vwap = round((tickInfo.ask + tickInfo.bid) / 2, 8)      
        tickInfo.open = bar.open_price              # opening price
        tickInfo.close = bar.close_price  
        tickInfo.last = tickInfo.close              # same as `close`, duplicated for convenience
        tickInfo.previousClose = None
        tickInfo.change = None          # Price change (absolute change, `last - open`)
        tickInfo.percentage = None      # Price change percent (relative change, `(change/open) * 100`)
        tickInfo.baseVolume = None      # Total traded base asset volume (volume of base currency traded for last 24 hours)
        tickInfo.quoteVolume = None 
        # self.Ticker = tickInfo

        return tickInfo

"""

    | price  | amount
----|----------------  ↓
  a |  1.200 | 200     ↓
  s |  1.100 | 300     ↓
  k |  0.900 | 100     ↓
----|----------------  ↓
  b |  0.800 | 100     ↓ sell 150 for 0.700
  i |  0.700 | 200     --------------------
  d |  0.500 | 100

"""