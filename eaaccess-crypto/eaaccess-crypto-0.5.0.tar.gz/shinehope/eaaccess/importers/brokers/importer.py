import ccxt

class Importer(object):
    def __init__(self, exchange_name='binance'):
        super(Importer, self).__init__()

        # Exchange
        self.exchange_name = exchange_name
        self.exchange: ccxt.Exchange = None

    def connect(self, apiKey=None, apiSecret=None, apiPasswd=None, hostname = {}):
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
    
    def fetch_ohlcv(self, symbol, timeframe='1m', since=None, limit=None, params={}) -> list:
        try:
            ohlcv = []
            ohlcv = self.exchange.fetch_ohlcv(symbol, timeframe=timeframe, since=since, limit=limit)
            return ohlcv
        except ccxt.NetworkError as e:
            print(exchange.id, 'fetch_ohlcv failed due to a network error:', str(e))
            return []
            # retry or whatever
            # ...
        except ccxt.ExchangeError as e:
            print(exchange.id, 'fetch_ohlcv failed due to exchange error:', str(e))
            return []
            # retry or whatever
            # ...
        except Exception as e:
            print(exchange.id, 'fetch_ohlcv failed with:', str(e))
            return []
            # retry or whatever
            # ...  
