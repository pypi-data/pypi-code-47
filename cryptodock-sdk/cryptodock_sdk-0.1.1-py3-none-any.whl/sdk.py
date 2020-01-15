from . import CryptoDockApi, CryptoDockStrategy, CryptoDockBacktest

class CryptoDockSdk :

    def __init__(self) :
        self.Strategy = CryptoDockStrategy
        self.Backtest = CryptoDockBacktest
        self.Api = CryptoDockApi
