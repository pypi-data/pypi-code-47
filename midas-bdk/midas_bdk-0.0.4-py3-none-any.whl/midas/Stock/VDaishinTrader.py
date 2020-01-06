from midasbdk.midas.Stock.Trader import Trader

class VDaishinTrader(Trader):
    def buy(self, stock, price, amount, timestamp, usertag=''):
        super().buy(stock,price,amount, timestamp, usertag)
        super().buyContracted(stock,price,amount, timestamp, usertag)

    def sell(self, stock, price, amount, timestamp, usertag=''):
        super().sell(stock,price,amount, timestamp, usertag)
        super().sellContracted(stock,price,amount, timestamp, usertag)
