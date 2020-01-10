# -*- coding: utf-8 -*-
'''


lw李文写的
模拟能够处理止盈止损指令的broker。
'''


from pyalgotrade import loggerHelpbylw
from pyalgotrade.const import ORDER_TYPE,ORDER_STATUS,STOP_PROFIT_LOSS_ORDER_STATUS,POSITION_SIDE
from pyalgotrade.stoplossorder_3rdAccount import StopProfitOrder,StopLossOrder,trailingOrder


from gm.api import get_orders,OrderSide_Buy,OrderSide_Sell,PositionEffect_Open,PositionEffect_Close,PositionEffect_CloseToday,PositionEffect_CloseYesterday
from gm.api import OrderStatus_Filled
from pyalgotrade import observer

from pyalgotrade.utils import createCusPositionFromGmPosition,cusPositionSideToGMPositionSide
from pyalgotrade import commonHelpBylw
from functools import partial
import  datetime
import  json
import time
class SimulationStopLossProfitBroker():
    def __init__(self,bTestID,orderLog=None,stopOrderLog=None,subfunList=None,unsubfunList=None):

        self.bTestID=bTestID
        self.orderLog=orderLog #这个是委托的日志，用来真正下委托的时候记录的日志
        self.stopOrderLog=stopOrderLog  #这个用来记录，止损，止盈，跟踪止盈等指令，建立起来后的，要写个日志。

        self._stoploss_orders = []
        # self._stoploss_orders = {}

        #这2个list 是  装的函数，一个是用来订阅行情，一个是用来退订行情.函数通过偏函数处理了，即
        #包裹了一个频率的字段，symbol字段在内部来提供
        self.subfunList=subfunList
        self.unsubfunList=unsubfunList




        self.stoplossOrderCreatedEvent = observer.Event()

    def getSLOrdersSymbols(self):
        return set([o._targetSymbol for o in self._stoploss_orders])

        # return set([o._targetSymbol for o in self._stoploss_orders.values()])



    def addStopOrder(self,o):
        self._stoploss_orders.append(o)

    # def addStopOrder(self,o):
    #
    #     sym=o.getSymbol()
    #     self._stoploss_orders.append(o)
    #




    #1、持仓没有了，则建立在该持仓上面的slorder要剔除掉

    # def deleteSLOrders(self,context):
    #     tempOrders=[]
    #
    #     for aOrders in self._stoploss_orders:
    #         symbol_=aOrders._targetSymbol
    #         side_=aOrders.target_order_position.positionSide
    #         gmposi=context.account().position(symbol_,side_)
    #         if gmposi is not None:
    #             tempOrders.append(aOrders)
    #     self._stoploss_orders=tempOrders

    # 2、已经下单了。比如止损单，已经达到了，然后下出了单子。
    def deleteSLOrders(self):
        self._stoploss_orders = [o for o in self._stoploss_orders if not o.is_final()]





    def ontick(self,tick,context=None):
        asymbol = tick.symbol
        matchOrders = [o for o in self._stoploss_orders if o._targetSymbol == asymbol]

        for aspOrder in matchOrders:
            aspOrder.on_tick_hq(tick,context=context)
        self.deleteSLOrders()

# def simulateTrade(self):
        






        # self.deleteSLOrders()
        # self._stoploss_orders = [o for o in self._stoploss_orders if not o.is_final()]

    def onOrderRsp(self,gmOrderObj,context):
        #context 关于平仓指令,有2个名字，一个是平仓的信号名字，即因为什么信号平仓，另外一个是平仓的是针对哪个开仓信号。要存为list
        #context关于开仓指令的名字，只需要存为一个，开仓的信号名字

        if  gmOrderObj.positionEffect in [PositionEffect_Close,PositionEffect_CloseToday,PositionEffect_CloseYesterday]:
            # if context.is_backtest_model():
            #     self._create_clear_order_fromGmOrders(gmOrderObj)

           #委托已成 后，平仓委托 需要取查 该持仓是否 还在，如果不在了，就要剔除相关止盈止损指令等。
            symbol_=gmOrderObj.symbol
            side_=gmOrderObj.positionSide

            gmside=cusPositionSideToGMPositionSide(side_)
            gmposi=context.account().position(symbol_,gmside)
            if gmposi is None:
                
                for aOrders in self._stoploss_orders:
                    if symbol_ == aOrders.getSymbol() and side_ == aOrders.target_order_position.positionSide:
                        aOrders.setStatus(STOP_PROFIT_LOSS_ORDER_STATUS.ORDER_CANCELED)
        
                self.deleteSLOrders()

        if  gmOrderObj.positionEffect in [PositionEffect_Open]:
            symbol_=gmOrderObj.symbol
            side_=gmOrderObj.positionSide
            gmside = cusPositionSideToGMPositionSide(side_)
            time.sleep(4)
            gmposi=context.account().position(symbol_,gmside)
            # print(symbol_,' ',side_,' ',gmposi)
            if gmposi is None:
                print(symbol_,' ',gmside,' ',gmOrderObj.positionEffect,' ',gmOrderObj.created_at)
            aposi=createCusPositionFromGmPosition(gmposi)
            context._createSOrder(aposi,context.bTestParams,self)

    def onTradeRsp(self, gmTrade, context):


        if gmTrade.positionEffect in [PositionEffect_Open]:
            symbol_ = gmTrade.symbol
            side_ = gmTrade.positionSide
            gmside = cusPositionSideToGMPositionSide(side_)

            gmposi = context.account().position(symbol_, gmside)
            # print(symbol_,' ',side_,' ',gmposi)
            if gmposi is None:
                print(symbol_, ' ', gmside, ' ', gmOrderObj.positionEffect, ' ', gmOrderObj.created_at)
            aposi = createCusPositionFromGmPosition(gmposi)
            context._createSOrder(aposi, context.bTestParams, self)





    def create_stop_order(self,aOrderPosition,stopThresh,stopCommand='stoploss'):


       
        


       


       
        if stopCommand=='stoploss':
            o = StopLossOrder.__from_create__(aOrderPosition, 'percent', stopThresh,orderLog=self.orderLog)

            if self.stopOrderLog is not None:
                orderInfo=o.getOrderInfo()
                dtstr=datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                msgStr='stopLoss '+\
                    ' symbol:'+orderInfo['symbol']+ \
                    ' cost:' + str(round(orderInfo['cost'],2)) + \
                    ' clearPrice:' + str(round(orderInfo['clearPrice'], 2)) + \
                    ' status:' + orderInfo['status'].value
                    # self.stopOrderLog.info("%s,%s,%s,%s,%s,%s",dtstr,'stopLoss',orderInfo['symbol'],orderInfo['cost'],\
                #                        orderInfo['clearPrice'],orderInfo['status'])
                self.stopOrderLog.info("%s,%s",dtstr,msgStr)
        if stopCommand=='stopprofit':
            o = StopProfitOrder.__from_create__(aOrderPosition, 'percent', stopThresh,orderLog=self.orderLog)
            if self.stopOrderLog is not None:
                orderInfo = o.getOrderInfo()
                dtstr = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                msgStr = 'stopProfit ' + \
                         ' symbol:' + orderInfo['symbol'] + \
                         ' cost:' + str(round(orderInfo['cost'], 2)) + \
                         ' clearPrice:' + str(round(orderInfo['clearPrice'], 2)) + \
                         ' status:' + orderInfo['status'].value
                # self.stopOrderLog.info("%s,%s,%s,%s,%s,%s",dtstr,'stopLoss',orderInfo['symbol'],orderInfo['cost'],\
                #                        orderInfo['clearPrice'],orderInfo['status'])
                self.stopOrderLog.info("%s,%s", dtstr, msgStr)
                
        self._subHQ(o.getSymbol())
        self._unsubHQ(o) #这里不是退订行情，而是给条件单 的事件 订阅一个退订函数。
        self.addStopOrder(o)



    #给symbol 订阅行情
    def _subHQ(self,symbol):
        for afun in self.subfunList:
            afun(symbol)
        # self.stoplossOrderCreatedEvent.emit(atradeOrder.symbol) #大概是订阅的tick函数要执行下


    #这个是具体的条件单订阅退订行情的函数，等到这些条件单失效，就会调用这些函数 来退订行情
    def _unsubHQ(self,o):
        for afun in self.unsubfunList:
            o.getOrderInvalidEvent().subscribe(afun)



    def create_trailing_order(self,aOrderPosition,trailing_type,trailingThresh,stop_type,stopThresh):

        # assert atradeOrder.status == ORDER_STATUS.FILLED
        # if atradeOrder.status == ORDER_STATUS.FILLED:

        # underLySym = commonHelpBylw.getMainContinContract(aOrderPosition.symbol)
        # orderLog = loggerHelpbylw.getFileLogger(self.bTestID + '-' + underLySym + '-orderlog',
        #                                         'log\\' + self.bTestID + '\\' + underLySym + '-orderRecord.txt',
        #                                         mode_='a')

        o = trailingOrder(aOrderPosition,stop_type,stopThresh,trailing_type,trailingThresh,orderLog=self.orderLog)
        

        if self.stopOrderLog is not None:
            orderInfo = o.getOrderInfo()
            dtstr = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            msgStr = 'stopTrailing ' + \
                     ' symbol:' + orderInfo['symbol'] + \
                     ' cost:' + str(round(orderInfo['cost'], 2)) + \
                     ' trailingPrice:' + str(round(orderInfo['trailingPrice'], 2)) + \
                     ' status:' + orderInfo['status'].value+ \
                     ' hh:' + str(orderInfo['hh']) + \
                     ' ll:' + str(orderInfo['ll'])
                # self.stopOrderLog.info("%s,%s,%s,%s,%s,%s",dtstr,'stopLoss',orderInfo['symbol'],orderInfo['cost'],\
            #                        orderInfo['clearPrice'],orderInfo['status'])
            self.stopOrderLog.info("%s,%s", dtstr, msgStr)

        self._subHQ(o.getSymbol())
        self._unsubHQ(o)
        self.addStopOrder(o)
            # self.addOrderPosition(aOrderPosition)

            # self.stoplossOrderCreatedEvent.emit(atradeOrder.symbol) #大概是订阅的tick函数要执行下


    # def onClearOrder(self,clearGmOrderObj,clearPositionSignalNames):
    #
    #
    #     for aOP in self.orderPostions:
    #         aOP.onClearOrder(clearGmOrderObj,clearPositionSignalNames)
    #
    #
    #
            
        