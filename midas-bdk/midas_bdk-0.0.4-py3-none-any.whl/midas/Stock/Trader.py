import logging
import json

class Trader(object):
    def __init__(self):
        self.tax = 0.003
        self.commision = 0.002

        self.buyOrder = []
        self.deposit = []
        self.sellOrder = []
    
    def buy(self, stock, price, amount, timestamp, usertag=''):
        order = {'stock':stock, 'price':price, 'amount':amount}   # TODO : add time
        self.buyOrder.append(order)
        report = json.dumps({'stock':stock, 'price':price, 'volume':amount, 'event':'buy_order', 'time':timestamp, 'usertag':usertag})
        logging.info(report)

    def buyContracted(self, stock, price, amount, timestamp, usertag=''):
        # TODO : search correct order and calculate remaining amount
        order = self.buyOrder.pop()
        self.deposit.append(order)
        report = json.dumps({'stock':stock, 'price':price, 'volume':amount, 'event':'buy_complete', 'time':timestamp, 'usertag':usertag})
        logging.info(report)

    def cancelBuyOrder(self, stock):
        pass

    def cancelSellOrder(self, stock):
        pass

    def sell(self, stock, price, amount, timestamp, usertag=''):
        order = {'stock':stock, 'price':price, 'amount':amount}
        self.sellOrder.append(order)
        report = json.dumps({'stock':stock, 'price':price, 'volume':amount, 'event':'sell_order', 'time':timestamp, 'usertag':usertag})
        logging.info(report)
        print('sell order -> ',order)

    def sellContracted(self, stock, price, amount, timestamp, usertag=''):
        self.completeTrade(self.deposit.pop(),self.sellOrder.pop())
        report = json.dumps({'stock':stock, 'price':price, 'volume':amount, 'event':'sell_complete', 'time':timestamp, 'usertag':usertag})
        logging.info(report)

    def completeTrade(self,buyContract, sellContract):
        self.buy_price = buyContract['price']
        self.sell_price =sellContract['price']
        print('buy:{}, sell:{}'.format(self.buy_price,self.sell_price))

    def getTradeProfit(self):
        return (self.sell_price*(1.0-self.tax-self.commision) - self.buy_price)/self.buy_price

