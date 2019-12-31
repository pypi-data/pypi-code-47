"""
    Broker Class
"""
import os
# import itertools
import numpy as np
# import matplotlib as mpl
# import matplotlib.pyplot as plt
# import matplotlib.dates as mdates
# import pandas as pd
import collections
import ccxt
import  threading
import  time
import requests
from shinehope.utils.mylogger import appLog
import shinehope.utils.myfunc as myfunc
import copy

# from .strategy.strategy import BaseStrategy       #  Circular Import ==> ( 移至檔案尾 ??)
from .marketdata import BarData, TimeFrame, Ticker, OrderData, TradeData, TradeType
from .candlestick import Candlestick
import shinehope.eaaccess.settings as settings
from shinehope.eaaccess.dataaccess.sqlite import DBAccess
from shinehope.eaaccess.dataaccess.klinestream import KlineStream
from shinehope.eaaccess.backtest import UIReport

# for WebSocket Stream
import websocket
import ssl
import json
from datetime import datetime
import pytz

class Broker(object):
    # onTimer = threading.Thread
    # tickContinue = True

    def __init__(self, exchange_name='binance'):
        super(Broker, self).__init__()

        # object init status
        self.tickContinue = True
        self.kline:Candlestick = Candlestick()
        self.symbol = 'BTC/USDT'
        self.symbol_base = 'BTC'
        self.symbol_quota = 'USDT'
        self.rawsymbol = ''
        self.timeframe = TimeFrame.PERIOD_D1
        self.wst = None
        self.ws = None
        self.fetchRetrys = 1
        self.retryWaits = 3         # seconds

        # EA thread synchronous
        self.ealock = threading.Lock()
        self.recready = False
        self.recdata = None
        self.ea_thread:threading.Thread = None

        # WekSocket StreamNames
        self.sname_ticker = "<symbol>@ticker"
        self.sname_kline = "<symbol>@kline_<interval>"

        # Exchange
        self.exchange_name = exchange_name
        self.exchange: ccxt.Exchange = None

        # 策略实例.
        self.strategy_instance = None

        # 手续费
        # self.commission = 2/1000
        self.fee_rate = {
            'taker' : 1/1000,
            'maker' : 1/1000,
            'currency' : "USDT"
        }
        # # 滑点率，设置为万5
        self.slipper_rate = 5/10000

        # # 杠杆的比例, 默认使用杠杆.
        # self.leverage = 1.0

        # # 滑点率，设置为万5
        # self.slipper_rate = 5/10000

        # # 购买的资产的估值，作为计算爆仓的时候使用.
        # self.asset_value = 0

        # # 最低保证金比例, 使用bitfinex 的为例子.
        # self.min_margin_rate = 0.15

        # 初始本金.
        self.start_cash = 1_000_000       # USDT
        self.start_bar:BarData = None
        # self.bar_count = 0

        # self.strategy_class = None

        # # 交易的数据.
        # self.trades = []

        # # 当前提交的订单.
        # self.active_orders = []

        # 回测的数据 kline stream 数据
        self.btest_kstream: KlineStream = None
        self.dbaccess: DBAccess = None

        # ## for BackTest Graph show
        # self.xaxis = []
        # self.yaxis = []

        # self.pos = 0  # 当前的持仓量..

        # # 是否是运行策略优化的方法。
        # self.is_optimizing_strategy = False

        # 記錄目前 Broker run mode
        self.run_mode = None
        self.Bar: BarData = None
        self.Ticker: Ticker = None

        self.rule_cycle = 15            # 15 (15分)  60 (1H)  1440 (1D 一天)
        # self.rule_bar: BarData = BarData()
        self.rule_volume = 0            # previouse-bar accumulated volume
        self.rule_timestamp = 0
        self.rule_pbar:BarData = BarData()

        # Get EAAccess setting (config.toml)
        # import toml
        # settings = toml.load('./configs/config.toml')
        # self.wss_endpoint = settings['rawapi'][exchange_name]['endpoint']
        self.wss_endpoint = settings.wssEndPoint


    def set_strategy(self, strategy=None, runmode="BACKTEST", symbol='BTC/USDT', timeframe=TimeFrame.PERIOD_M15):
        """
        设置要跑的策略类.
        :param strategy_class:
        :return:
        """
        from .strategy.strategy import BaseStrategy
        self.strategy_instance: BaseStrategy = strategy
        self.run_mode = runmode
        self.symbol = symbol
        pos = self.symbol.find("/")
        self.symbol_base = self.symbol[:pos]
        self.symbol_quota = self.symbol[pos + 1:]
        self.timeframe:TimeFrame = timeframe
        self.rule_cycle = myfunc.getCandleSizeMin(self.timeframe.value)

        # self.onTimer = threading.Thread(target = self.onTimerRun)
        # self.onTimer.start()
        if self.wst == None and self.run_mode in {'LIVE', 'DEMO'}:
            # issue websockect connection
            # WebSocket Stream
            # self.rawsymbol = symbol.replace("/", "").lower()
            self.rawsymbol = myfunc.getRawAPISymbol(self.symbol)
            # # self.rawsymbol = "btcusdt"          # All symbols for streams are lowercase (( 但之前 API 中需使用大寫....亂七八糟))
            # # streamName = f"{symbol}@kline_5m"
            # streamName = f"{self.rawsymbol}@ticker"
            # wssUrl = f"wss://stream.binance.com:9443/ws/{streamName}"
            """             
            Combined streams are accessed at /stream?streams=<streamName1>/<streamName2>/<streamName3>
            Combined stream events are wrapped as follows: {"stream":"<streamName>","data":<rawPayload>} 
            """
            # streamName1 = f"{self.rawsymbol}@ticker"
            # streamName2 = f"{self.rawsymbol}@kline_15m"
            self.sname_ticker = f"{self.rawsymbol}@ticker"
            # 2019.11.14
            # self.sname_kline = f"{self.rawsymbol}@kline_{self.timeframe.value}"
            self.sname_kline = f"{self.rawsymbol}@kline_1m"
            # wssUrl = f"wss://stream.binance.com:9443/stream?streams={self.sname_ticker}/{self.sname_kline}"
            wssUrl = f"{self.wss_endpoint}/stream?streams={self.sname_ticker}/{self.sname_kline}"
            self.ws = websocket.WebSocketApp(wssUrl,
                                    on_message = self.on_message,
                                    on_error = self.on_error,
                                    on_close = self.on_close)
            self.ws.on_open = self.on_open
            # self.synCnts = 8

            self.wst = threading.Thread(target=self.ws_connect)
            # self.wst.daemon = True
            self.wst.start()

            ## create EA run thread
            self.ea_thread = threading.Thread(target=self.ea_start)
            self.ea_thread.setDaemon(True)
            self.ea_thread.start()

    def set_market(self, symbol=None, timeframe:TimeFrame=None):
        """
        设置要跑的市場及時區.
        :param symbol, timeframe(TimeFrame):
        :return:
        """
        if symbol:
            self.symbol = symbol
            pos = self.symbol.find("/")
            self.symbol_base = self.symbol[:pos]
            self.symbol_quota = self.symbol[pos + 1:]
            # settings.symbol = self.symbol
            if self.run_mode == "DEMO":
                self.fee_rate['taker'] = self.exchange.markets[self.symbol]['taker']
                self.fee_rate['maker'] = self.exchange.markets[self.symbol]['maker']

        if timeframe:
            self.timeframe = timeframe
            settings.candleSize = timeframe.value
            self.rule_cycle = myfunc.getCandleSizeMin(self.timeframe.value)

    def set_fee_rate(self, marketFee:{}):
        self.fee_rate = marketFee.copy()
        
    # def set_leverage(self, leverage: float):
    #     """
    #     设置杠杆率.
    #     :param leverage:
    #     :return:
    #     """
    #     self.leverage = leverage

    # def set_commission(self, commission: float):
    #     """
    #     设置手续费.
    #     :param commission:
    #     :return:
    #     """
    #     self.commission = commission

    # def set_backtest_stream(self, histDB:str, tblSymbol, tmFrom, tmEnd):
    #     self.btest_kstream = KlineStream(histDB, self.symbol, tblSymbol, settings.candleSize)
    #     self.btest_kstream.set_range(tmFrom, tmEnd)
    def set_backtest_stream(self, kstream:KlineStream):
        # self.btest_kstream = KlineStream(histDB, self.symbol, tblSymbol, settings.candleSize)
        # self.btest_kstream.set_range(tmFrom, tmEnd)
        self.btest_kstream = kstream

        # set Indicator's kline stream
        for keyname, myIndi in self.strategy_instance.indicators.items():
            myIndi.set_backtest_stream(self.btest_kstream.dbFileName, self.btest_kstream.tbl_symbol,
                self.btest_kstream.timeFrom, self.btest_kstream.timeTo)

    def set_dbaccess(self, dbaccess:DBAccess):
        self.dbaccess = dbaccess

    def set_start_cash(self):
        """
            只支援以 USDT 為 cash 的 Crypto Currency
        """
        balance = self.fetch_balance()
        cash = 0.0
        for asset, amount in balance['total'].items():
            if asset == "USDT":
                cash += amount
            # elif asset == "BTC":       # ==> 轉為 USDT
            else:                       # ==> 轉為 USDT  ((當啟動時已有 Crypto Currency 時需轉為 USDT))
                # avgp = round((self.start_bar.high_price + self.start_bar.low_price) / 2 , 8)
                avgp = self.start_bar.close_price
                cash += amount * avgp 
        self.start_cash = round(cash, 8)

    # def buy(self, volume, price=None):
    #     """
    #     这里生成订单.
    #     order需要包含的信息， order_id, order_price, volume, order_time.
    #     :param price:
    #     :param volume:
    #     :return:
    #     """
    #     print(f"做多下单: {volume}@{price}")

    #     """
    #     在这里生成订单， 等待价格到达后成交.
    #     """

    # def backtest_buy(self, volume, price=0.001) -> str:
    def paper_buy(self, volume:float, price=0.001, orderType=TradeType.TYPE_MARKET) -> str:
        """
        这里生成订单.
        order需要包含的信息， order_id, order_price, volume, order_time.
        :param price:
        :param volume:
        :return:
        """
        costLimit = self.exchange.markets[self.symbol]['limits']['cost']['min']
        cost = round(price * volume, 8)
        if cost < costLimit:
            appLog.warning(f"violate minimum cost({costLimit} USDT) Limit : {cost} !!!")
            return None   

        ## check balance...
        bal = self.fetch_balance()
        freeQuota = 0.0
        if self.symbol_quota in bal.keys():
            freeQuota = bal[self.symbol_quota]['free']
            if volume * price > freeQuota:
                appLog.warning(f"has insufficient funds ({self.symbol_quota}: {freeQuota}) !!!")
                return None
        else:
            appLog.warning(f"has insufficient funds ({self.symbol_quota}: {freeQuota}) !!!")
            return None

        dTime = datetime.fromtimestamp(self.Bar.timestamp / 1000)
        sTime = dTime.strftime("%Y-%m-%d %H:%M:%S")
        pos = self.symbol.find("/")
        asset = self.symbol[:pos]
        quota = self.symbol[pos+1:]
        outMsg = "%s: Paper trader simulated a BUY      %.8f %s => %.8f %s" % (sTime, price, quota, volume, asset )
        appLog.info(outMsg)
        """
        在这里生成订单， 等待价格到达后成交.
        """
        order = OrderData()
        dtNow = datetime.now()
        tstamp = dtNow.timestamp()
        order.order_id = str(tstamp)
        ## 2019.11.30 bug... 
        # order.timestamp = self.Bar.timestamp              ## 使用此..記錄 order 的時間變為是 Bar 的 timestamp (ex: 15m)
        if self.run_mode == "BACKTEST":
            order.timestamp = self.Bar.timestamp
        else:
            order.timestamp = self.Ticker.timestamp
        order.status = "open"
        order.symbol = self.symbol
        order.order_type = orderType.value
        order.side = "buy"
        order.price = price
        order.amount = volume
        order.filled = 0.0
        order.remaining = volume
        isOK = self.dbaccess.orderNew(order, self.fee_rate)
        if isOK:
            self.check_order(order.order_id)
            return order.order_id
        return None



    # def sell(self, price, volume):
    #     print(f"做多平仓下单: {volume}@{price}")  #
    #     """
    #     在这里生成订单， 等待价格到达后成交.
    #     """

    # def backtest_sell(self, volume, price=None) -> str:
    def paper_sell(self, volume:float, price=None, orderType=TradeType.TYPE_MARKET) -> str:
        ## check cost limit
        costLimit = self.exchange.markets[self.symbol]['limits']['cost']['min']
        cost = round(price * volume, 8)
        if cost < costLimit:
            appLog.warning(f"violate minimum cost({costLimit} USDT) Limit : {cost} !!!")
            return None   

        ## check balance...
        bal = self.fetch_balance()
        freeBase = 0.0
        if self.symbol_base in bal.keys():
            freeBase = bal[self.symbol_base]['free']
            if volume > freeBase:
                appLog.warning(f"has insufficient assets ({self.symbol_base}: {freeBase}) !!!")
                return None
        else:
            appLog.warning(f"has insufficient assets ({self.symbol_base}: {freeBase}) !!!")
            return None

        dTime = datetime.fromtimestamp(self.Bar.timestamp / 1000)
        sTime = dTime.strftime("%Y-%m-%d %H:%M:%S")
        pos = self.symbol.find("/")
        asset = self.symbol[:pos]
        quota = self.symbol[pos+1:]
        outMsg = "%s: Paper trader simulated a SELL      %.8f %s <= %.8f %s" % (sTime, price, quota, volume, asset)
        appLog.info(outMsg)
        """
        在这里生成订单， 等待价格到达后成交.
        """
        order = OrderData()
        dtNow = datetime.now()
        tstamp = dtNow.timestamp()
        order.order_id = str(tstamp)
        ## 2019.11.30 bug... 
        # order.timestamp = self.Bar.timestamp              ## 使用此..記錄 order 的時間變為是 Bar 的 timestamp (ex: 15m)
        if self.run_mode == "BACKTEST":
            order.timestamp = self.Bar.timestamp
        else:
            order.timestamp = self.Ticker.timestamp
        order.status = "open"
        order.symbol = self.symbol
        order.order_type = orderType.value
        order.side = "sell"
        order.price = price
        order.amount = volume
        order.filled = 0.0
        order.remaining = volume
        isOK = self.dbaccess.orderNew(order, self.fee_rate)
        if isOK:
            self.check_order(order.order_id)
            return order.order_id
        return None

    def market_sell_order(self, amount, params={}):
        pos = None
        try:
            if self.run_mode == "BACKTEST":
                # avgp = round((self.Bar.high_price + self.Bar.low_price) / 2 , 8)
                # pos = self.backtest_sell(amount, self.Ticker.bid)
                pos = self.paper_sell(amount, self.Ticker.bid)
            elif self.run_mode == "DEMO":
                pos = self.paper_sell(amount, self.Ticker.bid)
            elif self.run_mode == "LIVE":
                if self.exchange.has['createMarketSellOrder']:
                    pos = self.exchange.create_market_sell_order(self.symbol, amount, params=params)
        except:
            raise

        return pos

    def market_buy_order(self, amount, params={}) -> str:
        pos = None
        try:
            if self.run_mode == "BACKTEST":
                # avgp = round((self.Bar.high_price + self.Bar.low_price) / 2 , 8)
                # pos = self.backtest_buy(amount, self.Ticker.ask)
                pos = self.paper_buy(amount, self.Ticker.ask)
            elif self.run_mode == "DEMO":
                pos = self.paper_buy(amount, self.Ticker.ask)
            elif self.run_mode == "LIVE":
                if self.exchange.has['createMarketBuyOrder']:
                    pos = self.exchange.create_market_buy_order(self.symbol, amount, params=params)
        except:
            raise

        return pos

    def limit_sell_order(self, amount, price, params={}):
        pos = None
        try:
            if self.run_mode == "BACKTEST":
                # avgp = round((self.Bar.high_price + self.Bar.low_price) / 2 , 8)
                # pos = self.backtest_sell(amount, self.Ticker.bid)
                pos = self.paper_sell(amount, price, TradeType.TYPE_LIMIT)
            elif self.run_mode == "DEMO":
                pos = self.paper_sell(amount, price, TradeType.TYPE_LIMIT)
            elif self.run_mode == "LIVE":
                if self.exchange.has['createLimitSellOrder']:
                    pos = self.exchange.create_limit_sell_order(self.symbol, amount, price, params=params)
        except:
            raise

        return pos

    def limit_buy_order(self, amount, price, params={}):
        pos = None
        try:
            if self.run_mode == "BACKTEST":
                # avgp = round((self.Bar.high_price + self.Bar.low_price) / 2 , 8)
                # pos = self.backtest_buy(amount, self.Ticker.ask)
                pos = self.paper_buy(amount, price, TradeType.TYPE_LIMIT)
            elif self.run_mode == "DEMO":
                pos = self.paper_buy(amount, price, TradeType.TYPE_LIMIT)
            elif self.run_mode == "LIVE":
                if self.exchange.has['createLimitBuyOrder']:
                    pos = self.exchange.create_limit_buy_order(self.symbol, amount, params=params)
        except:
            raise

        return pos

    # def short(self, price, volume):
    #     print(f"做空下单: {volume}@{price}")
    #     """
    #     在这里生成订单， 等待价格到达后成交.
    #     """

    # def cover(self, price, volume):
    #     print(f"做空平仓下单: {volume}@{price}")
    #     """
    #     在这里生成订单， 等待价格到达后成交.
    #     """

    def fetch_balance(self) -> {}:
        """ 
        {
            //-------------------------------------------------------------------------
            // indexed by availability of funds first, then by currency

            'free':  {           // money, available for trading, by currency
                'BTC': 321.00,   // floats...
                'USD': 123.00,
                ...
            },

            'used':  { ... },    // money on hold, locked, frozen, or pending, by currency

            'total': { ... },    // total (free + used), by currency

            //-------------------------------------------------------------------------
            // indexed by currency first, then by availability of funds

            'BTC':   {           // string, three-letter currency code, uppercase
                'free': 321.00   // float, money available for trading
                'used': 234.00,  // float, money on hold, locked, frozen or pending
                'total': 555.00, // float, total balance (free + used)
            },

            'USDT':   {           // ...
                'free': 123.00   // ...
                'used': 456.00,
                'total': 579.00,
            },

            ...
        }
        """
        balance = {}
        try:  
            if self.run_mode == "BACKTEST":
                balance = self.dbaccess.fetchBalance()
                # return balance
            elif self.run_mode == "DEMO":
                balance = self.dbaccess.fetchBalance()
            elif self.run_mode == "LIVE":
                # msgBal = self.exchange.fetch_balance()
                # balance = json.loads(msgBal)
                # return  balance
                if self.exchange.has['fetchBalance']:
                    balance = self.exchange.fetch_balance()
        except Exception as ex:
            # print(str(ex))
            appLog.error(str(ex))

        return balance

    def fetch_open_orders(self, symbol, since:int=None)->[]:
        """
            ??? fetchOpenOrders, fetchClosedOrders, fetchOrders, fetchOrder
        """
        orders = []
        try:
            if self.run_mode == "LIVE":
                if self.exchange.has['fetchOpenOrders']:
                    since = self.exchange.milliseconds() - 86400000  # -1 day from now
                    # orders = self.exchange.fetch_orders(self.symbol, since)
                    orders = self.exchange.fetch_open_orders(symbol, since)
            elif self.run_mode in {'BACKTEST', 'DEMO'}:
                orders = self.dbaccess.fetchPendingOrders(since)
        except Exception as ex:
            # print(str(ex))
            appLog.error(str(ex))

        return orders

    def fetch_my_trades(self, symbol, since:int=None)->[]:
        """
            ??? fetchMyTrades (private)
        """
        orders = []
        try:
            if self.run_mode == "LIVE":
                if exchange.has['fetchMyTrades']:
                    since = self.exchange.milliseconds() - 86400000  # -1 day from now
                    orders = self.exchange.fetch_my_trades(symbol, since)
            elif self.run_mode in {'BACKTEST', 'DEMO'}:
                orders = self.dbaccess.fetchMyTrades(since)
        except Exception as ex:
            # print(str(ex))
            appLog.error(str(ex))

        return orders

    # def fetch_ohlcv(self, timeframe='1m', since=None, limit=None, params={}) -> list:
    #     ohlcv = []

    #     retryCnts = 0
    #     isContinued = True
    #     while isContinued:
    #         try:
    #             if self.exchange.has['fetchOHLCV']:
    #                 ohlcv = self.exchange.fetch_ohlcv(self.symbol, timeframe=timeframe, since=since, limit=limit, params=params)
    #                 isContinued = False
    #         except ccxt.DDoSProtection:
    #             print(self.exchange.id, 'fetch_ohlcv failed due to a DDoSProtection:')
    #             raise       
    #         except ccxt.RequestTimeout as ex:
    #             print(self.exchange.id, 'fetch_ohlcv failed due to a RequestTimeout:')
    #             retryCnts += 1
    #             if retryCnts > self.fetchRetrys: 
    #                 raise
    #             else:
    #                 isContinued = True
    #                 time.sleep(self.retryWaits)               
    #         # except ccxt.NetworkError:
    #         #     print(self.exchange.id, 'fetch_ohlcv failed due to a NetworkError error:')
    #         #     raise
    #         # except ccxt.ExchangeError as e:
    #         #     print(exchange.id, 'fetch_ohlcv failed due to exchange error:', str(e))
    #         #     return []
    #         # except Exception as e:
    #         #     print(exchange.id, 'fetch_ohlcv failed with:', str(e))
    #         #     return []

    #     return ohlcv

    def fetch_ticker(self, symbol=None, params={}) -> Ticker:
        tickInfo:Ticker = None

        if self.run_mode == "BACKTEST":
            return self.Ticker
        elif self.run_mode in {"LIVE", "DEMO"}:           
            retryCnts = 0
            isContinued = True
            while isContinued:
                try:
                    if self.exchange.has['fetchTicker']:
                        qrySymbol = self.symbol
                        if symbol:
                            qrySymbol = symbol
                        ticker = self.exchange.fetch_ticker(qrySymbol, params=params)
                        if ticker:
                            tickInfo = Ticker()
                            tickInfo.symbol = ticker['symbol']
                            tickInfo.rawsymbol = None
                            tickInfo.timestamp = ticker['timestamp']
                            tickInfo.high = ticker['high']
                            tickInfo.low = ticker['low']
                            tickInfo.bid = ticker['bid']
                            tickInfo.bidVolume = ticker['bidVolume']
                            tickInfo.ask = ticker['ask']
                            tickInfo.askVolume = ticker['askVolume']
                            tickInfo.vwap = ticker['vwap']
                            tickInfo.open = ticker['open']
                            tickInfo.close = ticker['close']  
                            tickInfo.last = ticker['last']
                            tickInfo.previousClose = ticker['previousClose']
                            tickInfo.change = ticker['change']
                            tickInfo.percentage = ticker['percentage']
                            tickInfo.baseVolume = ticker['baseVolume']
                            tickInfo.quoteVolume = ticker['quoteVolume'] 
                        isContinued = False
                except ccxt.DDoSProtection:
                    appLog.error('fetch_ticker failed due to a DDoSProtection:')
                    isContinued = False
                    # raise       
                except ccxt.RequestTimeout as ex:
                    appLog.warning('fetch_ticker failed due to a RequestTimeout:')
                    retryCnts += 1
                    if retryCnts > self.fetchRetrys:
                        isContinued = False 
                        # raise
                    else:
                        isContinued = True
                        time.sleep(self.retryWaits)
                except ccxt.NetworkError:
                    appLog.error('fetch_ticker failed due to a NetworkError error:')
                    isContinued = False
                    # raise
                except ccxt.ExchangeError as e:
                    appLog.error('fetch_ticker failed due to exchange error:', str(e))
                    isContinued = False
                    # return []
                except Exception as e:
                    print(exchange.id, 'fetch_ticker failed with:', str(e))
                    # return []    
                    isContinued = False
                    raise

        return tickInfo



    def fetch_order_book(self):
        """ 
            {
                'bids': [
                    [ price, amount ], // [ float, float ]
                    [ price, amount ],
                    ...
                ],
                'asks': [
                    [ price, amount ],
                    [ price, amount ],
                    ...
                ],
                'timestamp': 1499280391811, // Unix Timestamp in milliseconds (seconds * 1000)
                'datetime': '2017-07-05T18:47:14.692Z', // ISO8601 datetime string with milliseconds
            }
        """
        if self.run_mode in {"BACKTEST", "DEMO"}:
            bar = self.kline.getBar()
            orderBook = {
                'bids': [
                    [bar.high_price, bar.volume]
                ],
                'asks': [
                    [bar.low_price, bar.volume]
                ],
                'timestamp': bar.timestamp
            }
        elif self.run_mode == "LIVE":
            orderBook = self.exchange.fetch_order_book(self.symbol)
        return orderBook

    def run_strategy(self, streamDatas = {}, uiKline:UIReport=None):
        if self.run_mode == "BACKTEST":
            if isinstance(streamDatas, Ticker):
                bar = self.kline.getBar()
                if bar:
                    tickInfo:Ticker = copy.copy(streamDatas)
                    self.Ticker = tickInfo
                    self.strategy_instance.onTick(tickInfo)

            if isinstance(streamDatas, BarData):
                streamBar:BarData = copy.copy(streamDatas)
                # print("kline_bar_update before....", streamBar)
                isNew, sampleBar = self.btest_kstream.resample_bar(streamBar)
                # print("kline_bar_update sample....", sampleBar, isNew)
                if sampleBar:
                    if isNew:
                        # ea.broker.kline.kline_bar_new(bar)        # 2019.11.15
                        self.kline.kline_bar_new(sampleBar)
                        # ea.broker.run_strategy(sampleBar)
                        uiKline.kline_bar_new(sampleBar)
                    else:
                        self.kline.kline_bar_update(sampleBar)
                        # ea.broker.run_strategy(sampleBar)
                        uiKline.kline_bar_update(sampleBar)
                    # ea.broker.run_strategy(sampleBar)

                    self.Bar = sampleBar
                    # # self.bar_count += 1
                    # # self.kline.kline_bar_new(bar)
                    # self.kline.kline_bar_update(bar)
                    
                    """ 
                        # Candlestick (Kline) 會參考需多少 bars 的資料才啟動
                        [tradingAdvisor.startCandle] ... 若未達到 ==> ( bar === None )
                        ==> 所以 self.start_bar Kline ready 的第一個 bar
                    """
                    bar = self.kline.getBar()
                    # print("kline_bar_update end   ....", bar)
                    # time.sleep(0.3)
                    if bar:                                 
                        if not self.start_bar:
                            self.start_bar = self.Bar
                            self.set_start_cash()               

                ## for Indicators Kline refresh
                for keyname, myIndi in self.strategy_instance.indicators.items():
                    myIndi.refresh_candles(streamBar)      
                    
                # self.Bar = bar
                # # self.bar_count += 1
                # # self.kline.kline_bar_new(bar)
                # self.kline.kline_bar_update(bar)
                
                # """ 
                #     # Candlestick (Kline) 會參考需多少 bars 的資料才啟動
                #     [tradingAdvisor.startCandle] ... 若未達到 ==> ( bar === None )
                #     ==> 所以 self.start_bar Kline ready 的第一個 bar
                # """
                # bar = self.kline.getBar()
                # # print("kline_bar_update end   ....", bar)
                # if bar:                                 
                #     if not self.start_bar:
                #         self.start_bar = self.Bar
                #         self.set_start_cash()           

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
                    # appLog.info(f"refresh Kline ?? {utcStamp}, {bar.timestamp}, {timeDelta}")
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
                        marketData = streamDatas["data"]
                        streamName = streamDatas["stream"].strip()
                        # if marketData['e'] == "24hrTicker":
                        if streamName == self.sname_ticker:
                            # appLog.debug(f"on_message...{marketData['e']}")
                            # appLog.info(f"run_strategy...{marketData['e']}")
                            # appLog.debug(f"Event: {marketData['E']}  ASK: {marketData['a']}  BID: {marketData['b']}")
                            tickInfo = Ticker()
                            tickInfo.symbol = self.symbol        # string symbol of the market ('BTC/USD', 'ETH/BTC', ...)
                            tickInfo.rawsymbol = marketData['s']     # Exchange's raw cryptocurrency symbol
                            tickInfo.timestamp = int(marketData['E'])   # int (64-bit Unix Timestamp in milliseconds since Epoch 1 Jan 1970)
                            tickInfo.high = float(marketData['h'])             # highest price
                            tickInfo.low = float(marketData['l'])              # lowest price
                            tickInfo.bid = float(marketData['b'])              # current best bid (buy) price
                            tickInfo.bidVolume = float(marketData['B'])        # current best bid (buy) amount (may be missing or undefined)
                            tickInfo.ask = float(marketData['a'])              # current best ask (sell) price
                            tickInfo.askVolume = float(marketData['A'])        # current best ask (sell) amount (may be missing or undefined)
                            tickInfo.vwap = float(marketData['w'])             # volume weighed average price
                            tickInfo.open = float(marketData['o'])             # opening price
                            tickInfo.close = float(marketData['c'])            # price of last trade (closing price for current period)
                            tickInfo.last = float(marketData['c'])             # same as `close`, duplicated for convenience
                            tickInfo.previousClose = float(marketData['x'])    # closing price for the previous period
                            tickInfo.change = float(marketData['p'])           # Price change (absolute change, `last - open`)
                            tickInfo.percentage = float(marketData['P'])        # Price change percent (relative change, `(change/open) * 100`)
                            tickInfo.baseVolume = float(marketData['v'])       # Total traded base asset volume (volume of base currency traded for last 24 hours)
                            tickInfo.quoteVolume = float(marketData['q'])      # Total traded quote asset volume (volume of quote currency traded for last 24 hours)

                            self.Ticker = tickInfo
                            ## 2019.11.18 added
                            # 2019.11.26 bug fixed for self.run_mode
                            if self.run_mode in {'BACKTEST', 'DEMO'}:
                                self.check_order("TICK-CHECKORDERS")

                            self.strategy_instance.onTick(tickInfo)
                        elif streamName == self.sname_kline:
                            appLog.debug(f"run_strategy...{marketData['e']}")
                            # appLog.info(f"run_strategy...{marketData['e']}")
                            # print(f"Event: {marketData['E']}  o: {marketData['k']['o']}  c: {marketData['k']['c']} h: {marketData['k']['h']} l: {marketData['k']['l']} x: {marketData['k']['x']}")       
                            # print(f"Event: {marketData['E']}  o: {marketData['k']['o']}  c: {marketData['k']['c']} h: {marketData['k']['h']} l: {marketData['k']['l']} t: {marketData['k']['t']} T:{marketData['k']['T']}")       
                            bar = BarData()
                            bar.timestamp = int(marketData['k']['t'])
                            bar.open_price = float(marketData['k']['o'])
                            bar.high_price = float(marketData['k']['h'])
                            bar.low_price = float(marketData['k']['l'])
                            bar.close_price = float(marketData['k']['c'])
                            bar.volume = float(marketData['k']['V'])
                            # print("kline_bar_update before....", bar, self.rule_volume)
                            # 2019.11.14 改為全部訂閱 kline_1m
                            # self.kline.kline_bar_update(bar)
                            # self.Bar = bar
                            isNew, sampleBar = self.resample_bar(bar)
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
                            
                            ## for Indicators Kline refresh
                            for keyname, myIndi in self.strategy_instance.indicators.items():
                                myIndi.refresh_candles(bar)                                     
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

                # marketData = streamDatas["data"]
                # streamName = streamDatas["stream"].strip()
                # # if marketData['e'] == "24hrTicker":
                # if streamName == self.sname_ticker:
                #     appLog.debug(f"on_message...{marketData['e']}")
                #     # appLog.info(f"on_message...{marketData['e']}")
                #     # appLog.debug(f"Event: {marketData['E']}  ASK: {marketData['a']}  BID: {marketData['b']}")
                #     tickInfo = Ticker()
                #     tickInfo.symbol = self.symbol        # string symbol of the market ('BTC/USD', 'ETH/BTC', ...)
                #     tickInfo.rawsymbol = marketData['s']     # Exchange's raw cryptocurrency symbol
                #     tickInfo.timestamp = int(marketData['E'])   # int (64-bit Unix Timestamp in milliseconds since Epoch 1 Jan 1970)
                #     tickInfo.high = float(marketData['h'])             # highest price
                #     tickInfo.low = float(marketData['l'])              # lowest price
                #     tickInfo.bid = float(marketData['b'])              # current best bid (buy) price
                #     tickInfo.bidVolume = float(marketData['B'])        # current best bid (buy) amount (may be missing or undefined)
                #     tickInfo.ask = float(marketData['a'])              # current best ask (sell) price
                #     tickInfo.askVolume = float(marketData['A'])        # current best ask (sell) amount (may be missing or undefined)
                #     tickInfo.vwap = float(marketData['w'])             # volume weighed average price
                #     tickInfo.open = float(marketData['o'])             # opening price
                #     tickInfo.close = float(marketData['c'])            # price of last trade (closing price for current period)
                #     tickInfo.last = float(marketData['c'])             # same as `close`, duplicated for convenience
                #     tickInfo.previousClose = float(marketData['x'])    # closing price for the previous period
                #     tickInfo.change = float(marketData['p'])           # Price change (absolute change, `last - open`)
                #     tickInfo.percentage = float(marketData['P'])        # Price change percent (relative change, `(change/open) * 100`)
                #     tickInfo.baseVolume = float(marketData['v'])       # Total traded base asset volume (volume of base currency traded for last 24 hours)
                #     tickInfo.quoteVolume = float(marketData['q'])      # Total traded quote asset volume (volume of quote currency traded for last 24 hours)

                #     self.Ticker = tickInfo
                #     self.strategy_instance.onTick(tickInfo)
                # elif streamName == self.sname_kline:
                #     appLog.debug(f"on_message...{marketData['e']}")
                #     # appLog.info(f"on_message...{marketData['e']}")
                #     # print(f"Event: {marketData['E']}  o: {marketData['k']['o']}  c: {marketData['k']['c']} h: {marketData['k']['h']} l: {marketData['k']['l']} x: {marketData['k']['x']}")       
                #     # print(f"Event: {marketData['E']}  o: {marketData['k']['o']}  c: {marketData['k']['c']} h: {marketData['k']['h']} l: {marketData['k']['l']} t: {marketData['k']['t']} T:{marketData['k']['T']}")       
                #     bar = BarData()
                #     bar.timestamp = int(marketData['k']['t'])
                #     bar.open_price = float(marketData['k']['o'])
                #     bar.high_price = float(marketData['k']['h'])
                #     bar.low_price = float(marketData['k']['l'])
                #     bar.close_price = float(marketData['k']['c'])
                #     bar.volume = float(marketData['k']['V'])
                #     # print("kline_bar_update before....", bar, self.rule_volume)
                #     # 2019.11.14 改為全部訂閱 kline_1m
                #     # self.kline.kline_bar_update(bar)
                #     # self.Bar = bar
                #     isNew, sampleBar = self.resample_bar(bar)
                #     # print("kline_bar_update sample....", sampleBar, self.rule_volume, isNew)
                #     if sampleBar:
                #         # if isNew:
                #         #     ea.broker.kline.kline_bar_new(bar)
                #         #     # ea.broker.run_strategy(sampleBar)
                #         #     uiKline.kline_bar_new(sampleBar)
                #         # else:
                #         #     # ea.broker.run_strategy(sampleBar)
                #         #     uiKline.kline_bar_update(sampleBar)
                #         # ea.broker.run_strategy(sampleBar)
                #         if not isNew:
                #             self.kline.kline_bar_update(sampleBar)
                #             self.Bar = sampleBar

                #     # #debug
                #     # # print("kline_bar_update sample....", sampleBar, self.rule_volume, isNew)
                #     # bar = self.kline.getBar()
                #     # print("kline_bar_update end   ....", bar, self.rule_volume)
                    
                #     ## for Indicators Kline refresh
                #     for keyname, myIndi in self.strategy_instance.indicators.items():
                #         myIndi.refresh_candles(bar)                             

            except requests.exceptions.HTTPError as ex:
                appLog.warning("strategy_client.Capture HTTPError.." + str(ex))
            except Exception as ex:
                # print(str(ex))
                appLog.error(str(ex))
        # elif self.run_mode == 'PAPER':
        #     pass
        else:
            print(f"not supporting type({self.run_mode})")

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

    # def kline_bar_new(self, bar: BarData):
    #     self.kline.kline_bar_new(bar)

    #     dTime = datetime.fromtimestamp(bar.timestamp / 1000)
    #     sTime = dTime.strftime("%Y-%m-%d %H:%M:%S")
    #     avgp = round((bar.high_price + bar.low_price) / 2 , 8)
    #     self.yaxis.append(avgp)
    #     # self.xaxis.append(sTime)
    #     # self.xaxis.append(bar.timestamp)
    #     self.xaxis.append(dTime)


    def calculate(self, testStart, testEnd):
        """ 
            统计成交的信息.. 夏普率、 盈亏比、胜率、 最大回撤 年化率/最大回撤        
        """
        # 拿到成交的信息，把成交的记录统计出来.
        # for trade in self.trades:
        #     """
        #      order_id 
        #      trade_id
        #      price,
        #      volume 
             
        #      10000 --> 1BTC
        #      12000 --> 1BTC  -- >  2000
        #     """
        appLog.info("")

        # start time
        dTime = datetime.fromtimestamp(testStart)
        sTime = dTime.strftime("%Y-%m-%d %H:%M:%S")
        prefix = "(PROFIT REPORT) start time:"
        outMsg = "%-60s %s" % (prefix, sTime)
        appLog.info(outMsg)        

        # end time
        dTime = datetime.fromtimestamp(testEnd)
        sTime = dTime.strftime("%Y-%m-%d %H:%M:%S")
        prefix = "(PROFIT REPORT) end time:"
        outMsg = "%-60s %s" % (prefix, sTime)
        appLog.info(outMsg)

        # Candles Size & skip candles
        prefix = "(PROFIT REPORT) Market Symbol:"
        outMsg = "%-60s %s" % (prefix, self.symbol)
        appLog.info(outMsg)

        # Candles Size & skip candles
        prefix = "(PROFIT REPORT) Candles size @ skip:"
        outMsg = "%-60s %s @ %d" % (prefix, settings.candleSize, self.kline.start_candle)
        appLog.info(outMsg)

        appLog.info("")
        ## 
        # Market Price
        prefix = "(PROFIT REPORT) start price:"
        # avgpStart = round((self.start_bar.high_price + self.start_bar.low_price) / 2 , 8)
        # outMsg = "%-60s %.2f USDT" % (prefix, avgpStart)
        # avgpStart = round((self.start_bar.high_price + self.start_bar.low_price) / 2 , 8)
        priceStart = self.start_bar.close_price
        outMsg = "%-60s %.2f USDT" % (prefix, priceStart)
        appLog.info(outMsg)   

        prefix = "(PROFIT REPORT) end price:"
        bar = self.kline.getBar()
        # avgpEnd = round((bar.high_price + bar.low_price) / 2 , 8)
        # outMsg = "%-60s %.2f USDT" % (prefix, avgpEnd)
        priceEnd= bar.close_price
        outMsg = "%-60s %.2f USDT" % (prefix, priceEnd)
        appLog.info(outMsg)   

        prefix = "(PROFIT REPORT) market:"
        # diff = avgpEnd - avgpStart
        diff = priceEnd - priceStart
        outMsg = "%-60s %.2f" % (prefix, diff)
        appLog.info(outMsg)      

        appLog.info("")
        ##
        #         
        tradeSum = self.dbaccess.tradeSummary()
        prefix = "(PROFIT REPORT) amount of trades:"        
        trades = tradeSum['trades']
        outMsg = "%-60s %d" % (prefix, trades)
        appLog.info(outMsg)

        prefix = "(PROFIT REPORT) original balance:"        
        outMsg = "%-60s %.8f USDT" % (prefix, self.start_cash)
        appLog.info(outMsg)

        balance = self.fetch_balance()
        cash = 0.0
        for asset, amount in balance['total'].items():
            if asset == "USDT":
                cash += amount
            # elif asset == "BTC":       # ==> USDT
            else:
                # avgp = round((self.start_bar.high_price + self.start_bar.low_price) / 2 , 8)
                # cash += amount * avgpEnd
                cash += amount * priceEnd
        prefix = "(PROFIT REPORT) current balance:"        
        outMsg = "%-60s %.8f USDT" % (prefix, cash)
        appLog.info(outMsg)

        prefix = "(PROFIT REPORT) profit:"  
        profit = cash - self.start_cash      
        outMsg = "%-60s %.8f USDT" % (prefix, profit)
        appLog.info(outMsg)

        appLog.info("")

    def check_order(self, orderID=None):
        """
        根据订单信息， 检查是否满足成交的价格， 然后生成交易的记录.
        :param bar:
        :return:
        """
        """
        在这里比较比较订单的价格与当前价格是否满足成交，如果满足，在这里撮合订单。
        """
        try:
            if orderID == "TICK-CHECKORDERS":
                # pass
                pendingOrders = self.dbaccess.fetchPendingOrders()
                for pendingOrder in pendingOrders:
                    self.check_order(pendingOrder['id'])
            else:
                order = self.dbaccess.orderFetch(orderID)
                if order.side == "buy":
                    if self.Ticker.ask <= order.price:
                        # if order.amount <= self.Bar.volume:       
                        if order.remaining <= self.Bar.volume:       
                            self.dbaccess.orderFilled(order, self.fee_rate)
                        else:
                            self.dbaccess.orderFilled(order, self.fee_rate, self.Bar.volume)
                elif order.side == "sell":
                    if self.Ticker.bid >= order.price:
                        # if order.amount <= self.Bar.volume:       
                        if order.remaining <= self.Bar.volume:                               
                            self.dbaccess.orderFilled(order, self.fee_rate)
                        else:
                            self.dbaccess.orderFilled(order, self.fee_rate, self.Bar.volume)
        except Exception as ex:
            appLog.error(str(ex))                 
            raise

    # def report_profit(self, timeFrom, timeTo):
    #     """
    #         Show Backtest UI result
    #     """
    #     # x = np.linspace(-1,1,50)
    #     # y = 2 * x + 1
    #     # plt.plot(x, y)
    #     # plt.show()
    #     # plt.plot(self.kline.timeframe, self.kline.close)
    #     # plt.plot(self.xaxis, self.yaxis)
    #     # """
    #     #     C:\Users\user\AppData\Local\Programs\Python\Python37-32\lib\site-packages\pandas\plotting\_matplotlib\converter.py:103: 
    #     #     FutureWarning: Using an implicitly registered datetime converter for a matplotlib plotting method. The converter was 
    #     #     registered by pandas on import. Future versions of pandas will require you to explicitly register matplotlib converters.

    #     #     o register the converters:
    #     #     >>>> from pandas.plotting import register_matplotlib_converters
    #     #     >>>> register_matplotlib_converters()

    #     # D:\EAIoT\EAAccess\eacrypto\eaaccess\broker.py:731: FutureWarning: 'pandas.tseries.converter.register' has been moved
    #     # and renamed to 'pandas.plotting.register_matplotlib_converters'.
    #     # converter.register()
    #     # """
    #     # from pandas.tseries import converter
    #     # converter.register()
    #     # import matplotlib as mpl
    #     import matplotlib.pyplot as plt
    #     import matplotlib.dates as mdates

    #     import pandas as pd
    #     pd.plotting.register_matplotlib_converters()

    #     import matplotlib.dates as mdates

    #     # plt.style.use("ggplot")
    #     # mpl.use('GTK3Agg') # to use GTK UI
    #     plt.style.use("bmh")
    #     fig, ax = plt.subplots()
    #     ax.plot(self.xaxis, self.yaxis)
    #     fig.set_size_inches(12, 7)
    #     fig.canvas.manager.window.wm_geometry("+150+50")
    #     ##
    #     # 此做法會造成無法看到全部總圖 ...
    #     #
    #     # tmStart = timeTo - 30 * 86400
    #     # tmEnd = timeTo + 1 * 86400
    #     # sShowTime = datetime.fromtimestamp(tmStart)
    #     # eShowTime = datetime.fromtimestamp(tmEnd)
    #     # ax.set_xlim((sShowTime, eShowTime))

    #     myFmt = mdates.DateFormatter("%m-%d %H:%M")
    #     ax.xaxis.set_major_formatter(myFmt)

    #     ## Rotate date labels automatically
    #     fig.autofmt_xdate()
    #     plt.show()

    # def optimize_strategy(self, **kwargs):
    #     """
    #     优化策略， 参数遍历进行..
    #     :param kwargs:
    #     :return:
    #     """
    #     self.is_optimizing_strategy = True

    #     optkeys = list(kwargs)
    #     vals = iterize(kwargs.values())
    #     optvals = itertools.product(*vals)  #
    #     optkwargs = map(zip, itertools.repeat(optkeys), optvals)
    #     optkwargs = map(dict, optkwargs)  # dict value...

    #     for params in optkwargs:
    #         print(params)

    #     # 参数列表, 要优化的参数, 放在这里.

    #     cash = self.start_cash
    #     leverage = self.leverage
    #     commission = self.commission
    #     for params in optkwargs:

    #         self.strategy_class.params = params
    #         self.set_cash(cash)
    #         self.set_leverage(leverage)
    #         self.set_commission(commission)
    #         self.run()
    
    # def connect(self, exchange_name, apiKey, apiSecret, apiPasswd = None, hostname = {}): 
    def connect(self, apiKey, apiSecret, apiPasswd = None, hostname = {}):
        try:
            exchange_class = getattr(ccxt, self.exchange_name)   # 获取交易所的名称 ccxt.binance
            exchange: ccxt.Exchange
            if hostname:
                exchange = exchange_class(hostname)  # 交易所的类. 类似 ccxt.bitfinex()
            else:
                exchange = exchange_class({
                    'options': {
                        'adjustForTimeDifference': True,  # ←---- resolves the timestamp
                    },
                    'enableRateLimit': True,  # ←---------- required as described in the Manual
                })  # 交易所的类. 类似 ccxt.bitfinex()            
                # exchange = exchange_class()
            exchange.apiKey = apiKey
            exchange.secret = apiSecret
            exchange.password = apiPasswd

            exchange.load_markets()
            print(f"Connect to {self.exchange_name}: {exchange.status['status']}")

            self.exchange = exchange
            if self.run_mode == "DEMO":
                self.fee_rate['taker'] = self.exchange.markets[self.symbol]['taker']
                self.fee_rate['maker'] = self.exchange.markets[self.symbol]['maker']
            # return  exchange
            return  True
        except AttributeError as ex:
            print("ExchangeNameError: " + str(ex))
            # return  None
            return  False
        except Exception as ex:
            print("Exception: " + str(ex))
            # return  None
            return  False

    # def onTimerRun(self):
    #     self.run()
    #     while self.tickContinue:
    #         time.sleep(10)
    #         self.run()

    def on_message(self, message):
        # appLog.info("websocket-client on_message...")
        # appLog.debug("websocket-client on_message...")
        if self.tickContinue:
            try:
                if self.ealock.acquire():
                    self.recready = True
                    self.recdata = message
            except Exception as ex:
                appLog.error(str(ex))  
            finally:
                self.ealock.release()
        else:
            # self.ws.close()
            pass

    
    def on_error(self, error):
        appLog.error("websocket-client on_error..." + str(error))
    
    def on_close(self):
        appLog.warning("websocket-client on_close...")
    
    def on_open(self):
        appLog.info("websocket-client on_open...")

    def ws_connect(self):
        while self.tickContinue:
            try:
                self.ws.run_forever(sslopt={"cert_reqs": ssl.CERT_NONE, "check_hostname": False}, ping_interval=60, ping_timeout=10)
                if not self.tickContinue:
                    # print("dispose Broker....")
                    appLog.warning("dispose Broker....")
                    break
                # print("After self.ws.run_forever....")
                appLog.warning("After self.ws.run_forever....")
                time.sleep(20)
            except Exception as ex:
                appLog.error(str(ex))

    def ea_start(self):
        try:
            self.strategy_instance.onInit()
            while self.tickContinue:
                # print("ea_start.tickContinue...", self.tickContinue)
                try:
                    if self.ealock.acquire():
                        if self.recready:  
                            if self.recdata:
                                streamDatas = json.loads(self.recdata)
                                self.recready = False
                                self.ealock.release()

                                self.run_strategy(streamDatas)
                            else:
                                self.recready = False
                                appLog.error("ea_start thread... self.recdata False !!!")
                        else:
                            self.ealock.release()
                            time.sleep(1)
                except Exception as ex:
                    appLog.error(str(ex))                    
                finally:
                    if self.ealock.locked():
                        self.ealock.release()
            # print("ea_start.... finished...")
        finally:
            # print("broker...onDeinit")
            self.strategy_instance.onDeinit()
            os._exit(0)



# def iterize(iterable):
#     '''Handy function which turns things into things that can be iterated upon
#     including iterables
#     '''
#     niterable = list()
#     for elem in iterable:
#         if isinstance(elem, str):
#             elem = (elem,)
#         elif not isinstance(elem, collections.Iterable):
#             elem = (elem,)

#         niterable.append(elem)

#     return niterable

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