from midasbdk.midas.Stock.Trader import Trader

class VDaishinTrader(Trader):
    def __init__(self):
        pass

    def buy(self, stock, price, amount):
		super().buy(stock,price,amount)
		super().buyContracted(stock,price,amount)
