"""
    Base Strategy for EAAccess/Crypto
"""
import numpy as np
# import pandas as pd
import  threading
import  time
import  datetime
import  os, sys
from ..marketdata import BarData, TimeFrame, Ticker
from ..broker import Broker        # Circular Import ==> ( 移至檔案尾 ??)
from .indicator import BaseIndicator
import shinehope.eaaccess.globalvars as _globalvars
import shinehope.eaaccess.settings as settings
from shinehope.eaminer.MinerTalk import MinerTalk
# from shinehope.utils.definitions import ROOT_DIR
from shinehope.utils.definitions import EAACCESS_DIR
from shinehope.utils.mylogger import appLog
import toml
from typing import Dict
import importlib.util
from shinehope.eaaccess.dataaccess.sqlite import DBAccess

class BaseStrategy(object):

    __coordMillis = 10000               # seconds * 1000
    onTimer = threading.Thread
    # tickContinue = True

    # broker:Broker = None  # 经纪人..
    # data = None

    def __init__(self, aiBoxVer='V01.00.00'):
        super(BaseStrategy, self).__init__()
        # self.data = data
        self.__tickContinue = True
        self.multiple = False
        self.__exitVal = None
        self.Globals = None
        self._pipeconn = None
        self.aiBoxVer = aiBoxVer
        self.broker: Broker = None
        self.settings = settings.settings
        self.broker_conn_status = False
        self.indicators: Dict[str, BaseIndicator] = {}
        self.confBox:{} = None
        self.confAcc:{} = None
        self.accountID = None
        self.runMode = "DEMO"

    @property
    def Kline(self):
        return self.broker.kline

    @property
    def MarketInfo(self):
        return self.broker.exchange.markets

    @property
    def Market(self):
        return self.broker.exchange.markets[self.Symbol]

    @property
    def Symbol(self):
        return self.broker.symbol

    @property
    def SymbolBase(self):
        return self.broker.symbol_base

    @property
    def SymbolQuota(self):
        return self.broker.symbol_quota

    def _init_settings(self, exitVal=None, conn=None, ns=None):
        self.multiple = True

        self.__exitVal = exitVal
        self._pipeconn = conn

        self.Globals = ns


        self._AiBoxVer = _globalvars.GlobalVarGet('AiBoxVer')

    def onInit(self):
        """
        策略开始运行.
        :return:
        """
        # appLog.debug("onInit...")
        appLog.info("onInit...")

    def onDeinit(self):
        """
        策略运行结束.
        :return:
        """
        # appLog.debug("onDeinit...")
        appLog.info("onDeinit...sleep 3 sec (simulate programming cleaning steps)")
        time.sleep(3)
        appLog.info("onDeinit...done")

    # def next_bar(self, bar: BarData):
    #     raise NotImplementedError("请在子类中实现该方法..")
    def getBar(self, idx=0):
        return self.Kline.getBar(idx)

    def getBalance(self) -> {}:
        return self.broker.fetch_balance()

    def getOpenOrders(self, since:int=None) -> []:
        return self.broker.fetch_open_orders(self.broker.symbol, since)

    def getMyTrades(self, since:int =None) -> []:
        return self.broker.fetch_my_trades(self.broker.symbol, since)

    # def buy(self, price, volume):
    def buy(self, volume) -> str:
        """
        :param volume: 数量
        :return:
        """
        # self.broker.buy(price, volume)
        pos = self.broker.market_buy_order(volume)
        return pos

    def buy_limit(self, volume, price) -> str:
        """
        :param price: 价格
        :param volume: 数量
        :return:
        """
        # self.broker.buy(price, volume)
        pos = self.broker.limit_buy_order(volume, price)
        return pos


    # def sell(self, price, volume):
    def sell(self, volume):
        """
        :param price: 价格
        :param volume: 数量
        :return:
        """
        pos = self.broker.market_sell_order(volume)
        return pos

    # def sell(self, price, volume):
    def sell_limit(self, volume, price):
        """
        :param price: 价格
        :param volume: 数量
        :return:
        """
        pos = self.broker.limit_sell_order(volume, price)
        return pos        


    def aiboxConnect(self, exchange_name, apiKey, apiSecret, accID, apiPasswd=None, hostname={}):
        self.accountID = accID
        self.loadWorkerConfigs()
        # accConf = minerConf['ExpertAdvisor'][accID]
        tradeSymbol = self.confAcc['CurrAVL']
        pos = tradeSymbol.find("/")
        currAsset = tradeSymbol[:pos]
        currQuote = tradeSymbol[pos + 1:]
        settings.symbol = f"{currAsset}/{currQuote}"
        self.runMode = self.confAcc['tradeMode']
        settings.candleSize = self.settings['market']['candleSize'].strip()

        self.broker = Broker(exchange_name)
        dbaccess = None
        if self.runMode == 'DEMO': 
            dbaccess = DBAccess()
            initRun = settings._configs['paper']['initRun']
            if settings._initForce:
                initRun = True

            balExisted = dbaccess.initTradeDB(accID, initRun)
            if not balExisted:
                bal = settings._configs['balances']
                # dbaccess.loadBalance(tradeDB, bal)
                dbaccess.loadBalance(bal)

            self.broker.set_dbaccess(dbaccess)

        self.broker_conn_status = self.connect(self.broker, apiKey, apiSecret, apiPasswd, hostname)
        if not self.broker_conn_status:
            print(f"Cannot connect to {exchange_name}; Key: {apiKey} Secret: {apiSecret}")
        # else:
        #     self.loadWorkerConfigs()

    # def connect(self, exchange_name, apiKey, apiSecret, apiPasswd = None, hostname = {}):
    def connect(self, broker: Broker, apiKey, apiSecret, apiPasswd = None, hostname = {}):
        try:
            # exchange_class = getattr(ccxt, exchange_name)   # 获取交易所的名称 ccxt.binance
            # exchange: ccxt.Exchange
            # if hostname:
            #     exchange = exchange_class(hostname)  # 交易所的类. 类似 ccxt.bitfinex()
            # else:
            #     exchange = exchange_class()  # 交易所的类. 类似 ccxt.bitfinex()            

            # exchange.apiKey = apiKey
            # exchange.secret = apiSecret
            # exchange.password = apiPasswd

            # exchange.load_markets()
            # print(f"Connect to {exchange_name}: {exchange.status['status']}")

            # exchange = Broker.connect(self, exchange_name, apiKey, apiSecret, apiPasswd, hostname)
            exchange = broker.connect(apiKey, apiSecret, apiPasswd, hostname)
            # self.broker = broker
            self.broker.set_strategy(self, runmode=self.runMode, symbol=settings.symbol,
                timeframe=TimeFrame(settings.candleSize))

            """     
            To check the existence of a local variable:
        
            if 'myVar' in locals():
            # myVar exists.

            To check the existence of a global variable:
            if 'myVar' in globals():
            # myVar exists.

            To check if an object has an attribute:
            if hasattr(obj, 'attr_name'):  
            """
            # obj.attr_name exists.
            if hasattr(self, '_pipeconn'):
                MinerTalk._conn_c_set(self._pipeconn)

            """ 啟動 OnTimer """
            # self.onTimerRun()       # 此種作法會造成 thread id 不斷增加 ((表示 thread 消失後再產生))
            # if settings.appMode in {'LIVE', 'DEMO'}:
            if self.runMode in {'LIVE', 'DEMO'}:
                self.onTimer = threading.Thread(target = self.onTimerRun)
                self.onTimer.setDaemon(True)
                self.onTimer.start()
           
            return  exchange
        except AttributeError as ex:
            appLog.error("ExchangeNameError: " + str(ex))
            print("ExchangeNameError: " + str(ex))
            return  None
        except Exception as ex:
            appLog.error("Exception: " + str(ex))
            print("Exception: " + str(ex))
            return  None

    def loadWorkerConfigs(self):
        import toml

        minerConf = None
        if settings.appMode == "BACKTEST":
            if settings._ConfFile is not None:
                configs  = toml.load(settings._ConfFile)
                minerConf = configs['MinerConfig']
        else:
            confFile = os.path.join(EAACCESS_DIR, 'configs', 'MinerConfig.toml')
            minerConf = toml.load(confFile)         

        self.confBox = minerConf['Worker']
        # self.confAcc = minerConf['ExpertAdvisor'][settings.accountID]
        self.confAcc = minerConf['ExpertAdvisor'][self.accountID]
        
    def coordinationIntervalMillis(self):
        return  self.__coordMillis

    def onTimerRun(self):
        self.coordinate()
        self.__coordMillis = self.coordinationIntervalMillis()
        fSec = round(self.__coordMillis / 1000, 3)
        # RecursionError: maximum recursion depth exceeded while calling a Python object
        # # print("onTimerRun..." + str(fSec))
        # # threading.Timer(fSec, self.onTimerRun).start()      # 此種作法會造成 thread id 不斷增加 ((表示 thread 消失後再產生))
        # time.sleep(fSec)
        # self.onTimerRun()

        # while self.__tickContinue:
        #     time.sleep(fSec)
        #     self.coordinate()


        if self.multiple:
            if self.__exitVal:            
                if fSec < 1.0:
                    while self.__tickContinue:
                        time.sleep(fSec)
                        if self.__exitVal.value == 1:
                            self.dispose()
                        else:
                            self.coordinate()
                else:
                    tSec = 0.0
                    while tSec < fSec:
                        # print('exitVal', self.__exitVal)
                        if self.__tickContinue:
                            time.sleep(1)
                            tSec += 1.0
                            # print('exitVal', self.__exitVal, tSec, fSec)
                            if self.__exitVal.value == 1:
                                self.dispose()

                            if tSec >= fSec:
                                self.coordinate()
                                tSec = 0.0
                        else:
                            break
            else:
                while self.__tickContinue: 
                    time.sleep(fSec)
                    self.coordinate()
        else:
            while self.__tickContinue: 
                time.sleep(fSec)
                self.coordinate()
        appLog.info("strategy onTimerRun stop...")
        # time.sleep(2)

    def dispose(self):
        appLog.info('dispose Strategy...')
        self.__tickContinue = False
        self.broker.tickContinue = False
        # self.broker.ws.close()

    def coordinate(self):
        """
            settings.appMode == "BACKTEST" 時, 不執行此功能
        """
        # pass
        print("BaseStrategy coordinate: " + datetime.datetime.now().strftime("%m/%d/%Y, %H:%M:%S"))

    def onTick(self, tickInfo:Ticker):
        # pass
        print(datetime.datetime.now().strftime("%m/%d/%Y, %H:%M:%S"))
        print(f"BaseStrategy onTick({tickInfo.symbol}:{tickInfo}): ")

    def addIndicator(self, keyname:str, filename:str, timeframe:TimeFrame=None) -> BaseIndicator:
        """
            :keyname    indicator keyname, using self.indicators[keyname] to retrieve this BaseIndicator object
            :filename   indicator file name--not including ext name, ex: myindicator.pyc --> using myindicator as filename
            :timeframe  TimeFrame ( ex: TimeFrame.PERIOD_M15 )

            :return     BaseIndicator
        """
        if not isinstance(timeframe, TimeFrame):
            return None

        if not filename:
            return None

        if not keyname:
            return None

        if timeframe is None:
            self.timeframe = self.broker.timeframe
        else:
            self.timeframe = timeframe

        try:
            indicatorDir = os.path.join(EAACCESS_DIR, 'strategy', 'indicators')
            if os.path.isdir(indicatorDir):
                isValid = False
                indFileName = filename + ".py"
                indFilePath = os.path.join(indicatorDir, indFileName)
                if os.path.isfile(indFilePath):
                    MODULE_PATH = indFilePath
                    isValid = True
                else:
                    indFileName = filename + ".pyc"
                    indFilePath = os.path.join(indicatorDir, indFileName)
                    if os.path.isfile(indFilePath):
                        isValid = True
                        MODULE_PATH = indFilePath
                    else:
                        isValid = False

                if isValid:
                    print(f'Importing external ({MODULE_PATH}) as IndicatorCustom')
                    # MODULE_NAME = "EAAccessStrategy"
                    MODULE_NAME = filename

                    spec = importlib.util.spec_from_file_location(MODULE_NAME, MODULE_PATH)
                    print("spec.name is " + str(spec.name))
                    module = importlib.util.module_from_spec(spec)
                    sys.modules[spec.name] = module 
                    spec.loader.exec_module(module)

                    # # strategy_client = module
                    # EAAccessStrategy = module
                    # # print(strategy_client.__version__)

                    self.indicators[keyname] = module.IndicatorCustom(self, timeframe)
                    myIndi:BaseIndicator = self.indicators[keyname]
                    ## 無法在此設定, 
                    # 因 onInit 時做 addIndicator() 時, EABackTest.py 還未初始化 Broker 的 Klinestream 
                    # (( 也就是 self.broker.btest_kstream 為 None 還未有值 ))...
                    # 改為在 Broker 的 set_backtest_stream(kstream) 時初始化 Indicator 的 Klinestream
                    # myIndi.set_backtest_stream(self.broker.btest_kstream.dbFileName, self.broker.btest_kstream.tbl_symbol,
                    #     self.broker.btest_kstream.timeFrom, self.broker.btest_kstream.timeTo)
                    return myIndi
                else:
                    return None
            else:
                return None
        except Exception as ex:
            print(ex)
            return None

        return None

# from ..broker import Broker
