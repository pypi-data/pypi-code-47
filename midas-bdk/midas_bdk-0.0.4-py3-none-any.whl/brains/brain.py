from abc import *

import logging
import json

from functools import wraps


class regfeature(object):
    def __init__(self, method):
        self._method = method
    def __call__(self, obj, *args, **kwargs):
        return self._method(obj, *args, **kwargs)
    @classmethod
    def methods(cls, subject):
        def g():
            for name in dir(subject):
                method = getattr(subject, name)
                if isinstance(method, regfeature):
                    yield name, method
        return [method._method for name,method in g()]

def execfeature(func):
    @wraps(func)
    def wrapper(self, *args, **kwargs):
        for f in self.feature:
            v, vname = f(self, *args, **kwargs)
            statement = 'self.{} = v'.format(vname)
            exec(statement)
        return func(self, *args, **kwargs)
    return wrapper

class Brain(metaclass=ABCMeta):
    def __init__(self, trader):
        self.trader = trader
        self.cnt = 0
        self.position = False

        self.num_trade_brain = 0
        self.num_period_brain = 0
        self.profit_sum_brain = 0.0

        self.stockStat = []
        self.feature = []

        for f in regfeature.methods(self.__class__):
            self.feature.append(f)

    def getFeatureBatch(self, data):
        max_len = len(data)
        req_len = self.getRequiredSeqLen()

        feature_seq = []
        for f in self.feature:
            s = []
            for i in range(max_len-req_len):
                v, _ = f(self, data[i:])
                s.append(v)
            feature_seq.append({'name':f.__name__,'data':s})
        return feature_seq

    @abstractmethod
    def getCandidates(self):
        pass
    
    @abstractmethod
    def getRequiredSeqLen(self):
        pass

    def registerFeature(self, func):
        self.feature.append(func)

    def processBuy(self, code, price, vol, date, usertag=''):
        self.trader.buy(code, price, vol, date, usertag) 
        self.cnt = 0
        self.position = True

        if code not in [s['code'] for s in self.stockStat]:
            self.stockStat.append({'code':code, 'numtrade':0, 'numperiod':0, 'profit':0.0})

    def skipBuy(self):
        pass

    def resetPosition(self):
        self.position = False

    def processSell(self, code, price, vol, date, usertag=''):
        self.trader.sell(code, price , vol, date, usertag)
        
        self.cnt = self.cnt + 1
        self.num_trade_brain += 1
        self.num_period_brain += self.getTradePeriod()
        self.profit_sum_brain += self.getTradeProfit()
        self.position = False

        stock_stat = (next(item for item in self.stockStat if item['code'] == code))
        #stock_stat cannot be null
        stock_stat['numtrade'] += 1
        stock_stat['numperiod'] += self.getTradePeriod()
        stock_stat['profit'] += self.getTradeProfit()

    def skipSell(self):
        self.cnt = self.cnt + 1

    def getTradePeriod(self):
        return self.cnt

    def getTradeProfit(self):
        return self.trader.getTradeProfit()

    def getLatestTradeProfitPerTimeUnit(self):
        return self.getTradeProfit()/self.getTradePeriod()

    def reportBrainOperation(self):
        print('\nNumber of Trade : {}'.format(self.num_trade_brain))
        print('Average period of each trade : {}'.format(self.num_period_brain/self.num_trade_brain))
        print('Average profit per trade : {} %'.format(100.0*self.profit_sum_brain/self.num_trade_brain))

        report = json.dumps({'event':'summary_brain', 
                             'num-trade':self.num_trade_brain, 
                             'avg-period-trade':self.num_period_brain/self.num_trade_brain if self.num_trade_brain > 0 else 0, 
                             'avg-profit-trade':100.0*self.profit_sum_brain/self.num_trade_brain if self.num_trade_brain > 0 else 0, 
                             'avg-profit-timeunit':100.0*self.profit_sum_brain/self.num_period_brain if self.num_period_brain > 0 else 0})
        logging.info(report)

        for stock in self.stockStat:
            report = json.dumps({'event':'summary_stock', 
                             'code':stock['code'],
                             'num-trade':stock['numtrade'],
                             'avg-period-trade':stock['numperiod']/stock['numtrade'] if stock['numtrade'] > 0 else 0, 
                             'avg-profit-trade':100.0*stock['profit']/stock['numtrade'] if stock['numtrade'] > 0 else 0, 
                             'avg-profit-timeunit':100.0*stock['profit']/stock['numperiod'] if stock['numperiod'] > 0 else 0})
            logging.info(report)

            




