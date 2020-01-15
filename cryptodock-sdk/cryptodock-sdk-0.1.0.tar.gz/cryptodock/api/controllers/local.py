import requests

class Local :

    def __init__(self, uri) :
        self.uri = uri

    def get(self, endpoint, params = {}) :
        response = requests.get(self.uri + '/local' + endpoint, params)
        return response.json() if response.status_code > 199 and response.status_code < 300 else response

    def get_exchanges(self, names=None, fields=None) :
        return self.get("/exchanges", {
            'names': names,
            'fields': fields
        })

    def get_products(self, pairs=None, exchanges=None, fields=None) :
        return self.get("/products", {
            'pairs': pairs,
            'exchanges': exchanges,
            'fields': fields
        })

    def get_tickers(self, pairs=None, exchanges=None, fields=None, start=None, end=None, limit=-1, order='DESC') :
        return self.get("/tickers", {
            'pairs': pairs,
            'exchanges': exchanges,
            'fields': fields,
            'start': start,
            'end': end,
            'limit': limit,
            'order': order
        })


    def get_trades(self, pairs=None, exchanges=None, fields=None, start=None, end=None, limit=-1, order='DESC') :
        return self.get("/trades", {
            'pairs': pairs,
            'exchanges': exchanges,
            'fields': fields,
            'start': start,
            'end': end,
            'limit': limit,
            'order': order
        })

    def get_klines(self, pairs=None, exchanges=None, fields=None, start=None, end=None, period=3600, limit=-1, order='DESC') :
        return self.get("/klines", {
            'pairs': pairs,
            'exchanges': exchanges,
            'fields': fields,
            'start': start,
            'end': end,
            'period': period,
            'limit': limit,
            'order': order
        })
