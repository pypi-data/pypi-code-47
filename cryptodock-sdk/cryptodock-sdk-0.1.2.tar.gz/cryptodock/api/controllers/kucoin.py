import requests

class Kucoin :

    def __init__(self, uri) :
        self.uri = uri

    def get(self, endpoint, params = {}) :
        response = requests.get(self.uri + '/kucoin' + endpoint, params)
        return response.json() if response.status_code > 199 and response.status_code < 300 else False

    def get_currencies(self) :
        return self.get("/currencies")

    def get_currency_detail(self, currency, chain) :
        return self.get("/currencies/{}".fornat(currency), {
            'chain': chain,
        })

    def get_fiat_prices(self, base, currencies) :
        return self.get("/prices/{}".format(base), {
            'currencies': currencies,
        })

    def get_market_list(self) :
        return self.get("/markets")

    def get_symbols_list(self, market) :
        return self.get("/symbols", {
            'market': market
        })

    def get_ticker(self, pair) :
        return self.get("/symbols/{}/tickers".format(pair))

    def get_all_tickers(self) :
        return self.get("/symbols/all/tickers")

    def get_trade_histories(self, pair) :
        return self.get("/symbols/{}/trades".format(pair))

    def get_klines(self, pair, start, end, granularity) :
        return self.get("/symbols/{}/klines".format(pair), {
            'start': start,
            'end': end,
            'granularity': granularity
        })

    def get_24_hour_stats(self, pair) :
        return self.get("/symbols/{}/24_hours".format(pair))

    def get_part_orderbook(self, pair, depth) :
        return self.get("/symbols/{}/orderbook/part".format(pair), {
            'depth': depth
        })

    def get_full_orderbook_aggregated(self, pair, depth) :
        return self.get("/symbols/{}/orderbook/full".format(pair), {
            'depth': depth
        })

    def get_full_orderbook_atomic(self, pair) :
        return self.get("/symbols/{}/orderbook/atomic".format(pair))
