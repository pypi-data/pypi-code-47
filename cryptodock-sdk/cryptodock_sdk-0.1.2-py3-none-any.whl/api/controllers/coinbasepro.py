import requests

class CoinbasePro :

    def __init__(self, uri) :
        self.uri = uri

    def get(self, endpoint, params = {}) :
        response = requests.get(self.uri + '/coinbasepro' + endpoint, params)
        return response.json() if response.status_code > 199 and response.status_code < 300 else False

    def get_products(self) :
        return self.get("/public/products")

    def get_product_orderbook(self, pair, level) :
        return self.get("/public/products/{}/orderbook".format(pair), {
            'level': level
        })

    def get_product_ticker(self, pair) :
        return self.get("/public/products/{}/ticker".format(pair))

    def get_product_trades(self, pair, after) :
        return self.get("/public/products/{}/trades".format(pair), {
            'after': after
        })

    def get_product_historic_rates(self, pair, start, end, granularity) :
        return self.get("/public/products/{}/historic".format(pair), {
            'start': start,
            'end': end,
            'granularity': granularity
        })

    def get_product_24_hour_stats(self, pair) :
        return self.get("/public/products/{}/24_hours".format(pair))

    def get_currencies(self) :
        return self.get("/public/public/currencies")

    def get_time(self) :
        return self.get("/public/time")

    def get_coinbase_accounts(self) :
        return self.get("/auth/accounts/coinbase")

    def get_payment_methods(self) :
        return self.get("/auth/accounts/payment_methods")

    def get_accounts(self) :
        return self.get("/auth/accounts")

    def get_account(self, account_id) :
        return self.get("/auth/accounts/{}".format(account_id))

    def get_account_history(self, account_id, before) :
        return self.get("/auth/accounts/{}/history".format(account_id), {
            'before': before
        })

    def get_account_transfers(self, account_id) :
        return self.get("/auth/accounts/{}/transfers".format(account_id), {
            'before': before
        })

    def get_account_holds(self, account_id) :
        return self.get("/auth/accounts/{}/holds".format(account_id), {
            'before': before
        })

    def buy(self, pair, price, size) :
        return self.get("/auth/buy/{}".format(pair), {
            'price': price,
            'size': size
        })

    def sell(self, pair, price, size) :
        return self.get("/auth/sell/{}".format(pair), {
            'price': price,
            'size': size
        })

    def place_order(self, pair, price, size, side) :
        return self.get("/auth/orders/place/{}".format(pair), {
            'price': price,
            'size': size,
            'side': side
        })

    def cancel_order(self, order_id) :
        return self.get("/auth/orders/cancel/{}".format(order_id))

    def cancel_orders(self) :
        return self.get("/auth/orders/cancel/open")

    def cancel_all_orders(self, pair) :
        return self.get("/auth/orders/cancel/{}".format(pair))

    def get_orders(self) :
        return self.get("/auth/orders")

    def get_order(self, order_id) :
        return self.get("/auth/orders/{}".format(order_id))

    def get_fills(self, pair) :
        return self.get("/auth/fills/{}".format(pair))

    def get_fundings(self) :
        return self.get("/auth/fundings")

    def repay(self, amount, currency) :
        return self.get("/auth/repay", {
            'amount', amount,
            'currency', currency
        })

    def margin_transfer(self, margin_profile_id, type, amount, currency) :
        return self.get("/auth/margin_transfer", {
            'margin_profile_id', margin_profile_id,
            'type', type,
            'amount', amount,
            'currency', currency
        })

    def close_position(self) :
        return self.get("/auth/close_position")

    def convert(self, fromCurrency, to, amount) :
        return self.get("/auth/convert", {
            'from', fromCurrency,
            'to', to,
            'amount', amount
        })

    def deposit(self, amount, currency, coinbase_account_id) :
        return self.get("/auth/deposit", {
            'amount', amount,
            'currency', currency,
            'coinbase_account_id', coinbase_account_id
        })

    def withdraw(self, amount, currency, coinbase_account_id) :
        return self.get("/auth/withdraw", {
            'amount', amount,
            'currency', currency,
            'coinbase_account_id', coinbase_account_id
        })

    def deposit_crypto(self, currency) :
        return self.get("/auth/deposit_crypto", {
            'currency', currency
        })

    def withdraw_crypto(self, amount, currency, crypto_address) :
        return self.get("/auth/withdraw_crpyo", {
            'amount', amount,
            'currency', currency,
            'crypto_address', crypto_address
        })

    def deposit_payment(self, amount, currency, payment_method_id) :
        return self.get("/auth/deposit_payment", {
            'amount', amount,
            'currency', currency,
            'payment_method_id', payment_method_id
        })

    def withdraw_payment(self, amount, currency, payment_method_id) :
        return self.get("/auth/withdraw_payment", {
            'amount', amount,
            'currency', currency,
            'payment_method_id', payment_method_id
        })

    def get_trailing_volume(self) :
        return self.get("/auth/trailing_volume")
