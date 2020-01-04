from loguru import logger
import uuid
import copy
import maya
from jamboree import Jamboree, DBHandler
from contextlib import ContextDecorator
from link_jam_handle.utils.trades.trade_type import TradeType
from link_jam_handle.utils.trades.trade import Trade
from link_jam_handle import PriceSet
from link_jam_handle.data.pricing import SimulatedPriceHandler
from link_jam_handle.utils.slippage import RandomUniformSlippageModel
from cytoolz import keyfilter
from typing import Dict, List

def omit(blacklist, d):
    return keyfilter(lambda k: k not in blacklist, d)


class timecontext(ContextDecorator):
    def __enter__(self):
        self.start = maya.now()._epoch
        return self

    def __exit__(self, *exc):
        self.end = maya.now()._epoch
        delta = self.end - self.start
        print(f"It took {delta}ms")
        return False

"""
Note: Will remove soon. Going through a concept.
"""

class PortfolioHandler(DBHandler):
    """Abstract handler that we use to keep track of portfolio information.
    """

    def __init__(self, base_instrument="USD", start_balance=10000, limit=100, lazy_load=False):
        super().__init__()
        # TODO: Lazy load should be replaced with the parameters `pre_load` and `just_in_time`
        self._base_instrument = base_instrument
        self.start_balance = start_balance
        self.entity = "portfolio"
        self.required = {
            "episode": str,
            "user_id": str,
            "exchange": str
        }
        self._balance = 0
        self._limit = limit

        self.lazy = lazy_load
        # Store a list of the portfolio & performance states
        self._performance = []
        self._portfolio = []
        self._holdings = [] # Holdings is current_price * amount for each currency 
        self._trades = []
        self._pricing = None
        self._allocator = None
        self._slippage_model = RandomUniformSlippageModel()
        self._instrument_precision = 8
        self._commission_percent = 0.3
        self._base_precision = 2


        self._min_trade_amount = 0.000001
        self._max_trade_amount = 1000000
        self._min_trade_price = 0.00000001
        self._max_trade_price = 100000000



        # Placeholder variables
        self.placeholders = {}

        
        
        
    # -------------------------------------------------------------------
    # --------------------- Properties & Setters ------------------------
    # -------------------------------------------------------------------
    

    @property
    def current_time(self):
        """ 
            # Current Time
            ---
            Get the current time for the portfolio.

            Gets the time from the price/dataset. If the datasource is live it should get the current price and use that. 
        """
        return self._pricing.current_time


    @property
    def limit(self):
        return self._limit
    
    @limit.setter
    def limit(self, limit):
        self._limit = limit


    @property
    def holdings(self):
        """ Get the holdings for the user """
        _holdings = self.load_holdings()
        filtration_list = ['user_id', 'episode', 'type', 'detail', 'exchange', 'live', 'timestamp']
        holdings = map(lambda x: omit(filtration_list, x), _holdings)
        return list(holdings)


    @property
    def performance(self):
        """ Get the performance of the user/exchange"""
        performance = self.load_performance()
        if isinstance(performance, dict):
            performance = [performance]
        
        filtration_list = ["episode", "live", 'user_id', 'type', 'timestamp', 'exchange', 'detail']
        
        performance_filtered = list(map(lambda x: omit(filtration_list, x), performance))
        logger.info(performance_filtered)
        return performance_filtered


    @property
    def portfolio(self):
        """ Get the latest portfolio of the user/exchange"""
        if self.lazy == True:
            portfolio = self.latest_portfolio()
            filtered_portfolio = omit(['user_id', 'episode', 'type', 'timestamp'], portfolio) 
            return filtered_portfolio
        else:
            if isinstance(self._portfolio, dict):
                filtered_portfolio = omit(['user_id', 'episode', 'type', 'timestamp'], self._portfolio) 
                return filtered_portfolio
            filtered_portfolio = omit(['user_id', 'episode', 'type', 'timestamp'], self._portfolio[-1])
            return filtered_portfolio
            

    @property
    def balance(self) -> float:
        if self.lazy == True:
            latest_balance = self.latest_performance()
            return latest_balance.get('balance', 0.0)
        latest_record = self._performance[-1]
        balance = latest_record.get("balance", 0.0)
        return balance
    

    @property
    def trades(self) -> List[Dict]:
        """ Get all of the trades for this user"""
        trades = self.load_trades()
        if isinstance(trades, dict):
            trades = [trades]
        filtration_list = ["episode", "exchange", "user_id", "type", "detail", "timestamp", "live"]
        trades_filtered = map(lambda x: omit(filtration_list, x), trades)
        return list(trades_filtered)

    
    @property
    def net_worth(self) -> float:
        net_worth = self.balance
        portfolio = self.portfolio
        if not portfolio:
            return net_worth


        portfolio_filtered = omit(['user_id', 'episode', 'type', 'time', 'timestamp', 'exchange', 'live'], portfolio)

        for symbol, amount in portfolio_filtered.items():
            if symbol == self._base_instrument:
                continue

            current_price = self.current_price(symbol=symbol)
            net_worth += current_price * amount

        return net_worth

    @property
    def pricing(self) -> PriceSet:
        if self._pricing is None:
            raise NotImplementedError("You need to add pricing")
        return self._pricing
    
    @pricing.setter
    def pricing(self, price_handler: PriceSet):
        self._pricing = price_handler

    @property
    def allocator(self):
        """ Allocation stuff for"""
        if self._allocator is None:
            raise NotImplementedError("You need to add pricing")
        return self._allocator

    @allocator.setter
    def allocator(self, allocation_handler):
        self._allocator = allocation_handler

    @property
    def profit_loss_percent(self) -> float:
        """Calculate the percentage change in net worth since the last reset.
        Returns:
            The percentage change in net worth since the last reset.
        """
        return float(self.net_worth / self.start_balance) * 100
    # Use to get counts inside of the database


    def get_count(self) -> int:
        count = self.count()
        return count


    def performance_count(self) -> int:
        alt = {"detail": "performance"}
        count = self.count(alt)
        return count

    
    def holdings_count(self) -> int:
        alt = {"detail": "holdings"}
        count = self.count(alt)
        return count


    # ----------------------------------------
    # -------------- Querying ----------------
    # ----------------------------------------


    def latest_portfolio(self):
        last_state = self.last()
        return last_state

    def latest_performance(self):
        alt = {"detail": "performance"}
        last_state = self.last(alt)
        return last_state


    def load_performance(self):
        alt = {"detail": "performance"}
        performance = self.many(self.limit, alt=alt)
        if isinstance(performance, dict):
            return [performance]
        return performance
    
    
    def load_portfolio(self):
        portfolio = self.many(self.limit)
        if isinstance(portfolio, dict):
            return [portfolio]
        return portfolio
    

    def load_trades(self):
        alt = {"detail": "trade"}
        trades = self.many(self.limit, alt=alt)
        if isinstance(trades, dict):
            return [trades]
        return trades
    

    def load_holdings(self):
        alt = {"detail": "holdings"}
        _holdings = self.many(self.limit, alt=alt)
        if isinstance(_holdings, dict):
            return [_holdings]
        return _holdings


    # ----------------------------------------
    # ---------------- Saving ----------------
    # ----------------------------------------

    def save_portfolio(self, data):
        """ Save portfolio """
        _data = copy.copy(self._query)
        _data.update(data)
        _data['type'] = self.entity
        _data['time'] = self.current_time
        _data['timestamp'] = maya.now()._epoch

        self._portfolio.append(_data)
        self.save(_data)

    def save_performance(self, data) -> None:
        """ Save performance information """
        alt = {"detail": "performance"}
        _data = copy.copy(self._query)
        _data.update(data)
        _data.update(alt)
        _data['time'] = self.current_time
        _data['type'] = self.entity
        _data['timestamp'] = maya.now()._epoch
        
        self._performance.append(_data)
        self.save(_data, alt=alt)

    

    def save_trade(self, data):
        alt = {"detail": "trade"}

        _data = copy.copy(self._query)
        _data.update(data)
        _data.update(alt)

        _data['type'] = self.entity
        _data['time'] = self.current_time
        _data['timestamp'] = maya.now()._epoch
        self._trades.append(_data)
        logger.debug(_data)
        self.save(_data, alt=alt)


    def save_holdings(self, data, timestamp=maya.now()._epoch):
        alt = {"detail": "holdings"}

        _data = copy.copy(self._query)
        _data.update(data)
        _data.update(alt)

        _data['type'] = self.entity
        _data['time'] = self.current_time
        _data['timestamp'] = maya.now()._epoch
        self._trades.append(_data)
        self.save(_data, alt=alt)

    # ----------------------------------------
    # ------------ Operations ----------------
    # ----------------------------------------    

    
    def _update_account(self, _trade:Trade):
        """ Updates the portfolio exchange account. """
        # TODO: Add timestamp to trade
        
        if self._is_valid_trade(_trade):
            self._make_trade(_trade)

        self.placeholders['portfolio'][self._base_instrument] = self.placeholders['balance']


        latest_performance = {
            'net_worth': self.net_worth,
            'balance': self.placeholders['balance']
        }

        self.save_performance(latest_performance)
        self.save_portfolio(self.placeholders['portfolio'])
        self._update_holdings()
    
    def _update_account_no_order(self):
        """ Updates the portfolio exchange account. """
        # TODO: Add timestamp to trade

        self.placeholders['portfolio'][self._base_instrument] = self.placeholders['balance']


        latest_performance = {
            'net_worth': self.net_worth,
            'balance': self.placeholders['balance']
        }

        self.save_performance(latest_performance)
        self.save_portfolio(self.placeholders['portfolio'])
        self._update_holdings()


    def _update_holdings(self):
        """ Duplication of net_worth code"""
        holdings = {}
        portfolio = self.portfolio
        if not portfolio:
            return 


        portfolio_filtered = omit(['user_id', 'episode', 'type', 'time', 'timestamp', 'exchange', 'live'], portfolio)

        """
                "exchange": "superhotfyre",
                "episode": "335f32a64a4a4812b8373a65782e7801",
                "user_id": "10",
                "type": "portfolio",
                "detail": "trade",
                "live": false,
                "symbol": "ABC",
                "trade_type": 1,
                "amount": 1,
                "price": 792.64,
                "time": 1579585984.351019,
                "timestamp": 1577778784.3788486

        """


        portfolio_items = portfolio_filtered.items()
        for symbol, amount in portfolio_items:
            if symbol == self._base_instrument:
                holdings[symbol] = amount
                continue

            current_price = self.current_price(symbol=symbol)
            total = current_price * amount
            holdings[symbol] = total

        self.save_holdings(holdings, timestamp=self.current_time)

    def _make_trade(self, trade:Trade):
        """ Trades on the account then updates it"""

        if not trade.is_hold:
            """ TODO: We'll need to save this in two places to make it work IRL"""
            self.save_trade({
                'symbol': trade.symbol,
                'trade_type': trade.trade_type.value,
                'amount': trade.amount,
                'price': trade.price
            })
        
        if trade.is_buy:
            self.placeholders['balance'] -= trade.amount * trade.price
            self.placeholders['portfolio'][trade.symbol] = self.placeholders['portfolio'].get(trade.symbol, 0) + trade.amount
        elif trade.is_sell:
            self.placeholders['balance'] += trade.amount * trade.price
            self.placeholders['portfolio'][trade.symbol] = self.placeholders['portfolio'].get(trade.symbol, 0) - trade.amount
        
        


    def _is_valid_trade(self, _trade:Trade) -> bool:
        
        if _trade.is_buy and self.placeholders['balance'] < _trade.amount * _trade.price:
            logger.error("Not enough to buy")
            return False
        elif _trade.is_sell and self.placeholders['portfolio'].get(_trade.symbol, 0) < _trade.amount:
            logger.error("Not enough to sell")
            return False
        

        is_both = _trade.amount >= self._min_trade_amount and _trade.amount <= self._max_trade_amount

        if is_both: logger.success("Both conditions succeeded")
        return is_both


    def execute_trade(self, trade:Trade) -> Trade:
        self.placeholders['portfolio'] = self.latest_portfolio()
        self.placeholders['balance'] = self.balance

        current_price = self.current_price(symbol=trade.symbol)
        commission = self._commission_percent / 100
        filled_trade = trade.copy()
        

        if filled_trade.is_hold or not self._is_valid_trade(filled_trade):
            filled_trade.amount = 0



        if filled_trade.is_buy:
            price_adjustment = (1 + commission)
            filled_trade.price = round(current_price * price_adjustment, self._base_precision)
            filled_trade.amount = round((filled_trade.price * filled_trade.amount) / filled_trade.price,
                                        self._instrument_precision)
        elif filled_trade.is_sell:
            price_adjustment = (1 - commission)
            filled_trade.price = round(current_price * price_adjustment, self._base_precision)
            filled_trade.amount = round(filled_trade.amount, self._instrument_precision)

        if not filled_trade.is_hold:
            filled_trade = self._slippage_model.fill_order(filled_trade, current_price)
        

        self._update_account(filled_trade)
        return filled_trade

    def instrument_balance(self, symbol: str):
        """ Get the balance for the instrument """
        portfolio = self.latest_portfolio()

        if symbol in portfolio.keys():
            return portfolio[symbol]
        return 0.0

    

    
    # -------------------------------------------------------
    # ------------------ Reset Conditions -------------------
    # -------------------------------------------------------
    



    def _reset_portfolio(self):
        count = self.get_count()
        if count == 0:
            self.save_portfolio({f"{self._base_instrument}": float(self.start_balance), "time": self.current_time})

    def _reset_performance(self):
        """ Reset the performance inside of a given exchange """
        count = self.performance_count()
        if count == 0:
            self.save_performance({"balance": float(self.start_balance), "net_worth": float(self.start_balance), "time": self.current_time})
    
    def _reset_holdings(self):
        """ Reset the holdings inside of a given exchange """
        count = self.holdings_count()
        if count == 0:
            self.save_holdings({f"{self._base_instrument}": float(self.start_balance), "time": self.current_time})

    def _reset_price(self):
        """ Resets the price. If it's a backtest or simulation, we'll pull information into place so we can backtest. """
        self.pricing.reset()
    
    def _reset_allocation(self):
        self.allocator.reset()


    def update(self):
        """ Update the exchange. """
        self._update_holdings()


    def reset(self, _time=maya.now()._epoch):
        """ Determines if we're re-initiating """
        self._reset_price()
        self._reset_allocation()
        self._reset_performance()
        self._reset_portfolio()
        self._reset_performance()
        if self.lazy == False:
            """ This means we're loading all of the records upfront"""
            self._performance = self.load_performance()
            self._portfolio   = self.load_portfolio()
    

    def step(self, trade:Trade=None) -> dict:
        self.placeholders['portfolio'] = self.latest_portfolio()
        self.placeholders['balance'] = self.balance

        final_dict = {'obs': {}, 'done': False}
        prices_information = self.pricing.step()
        self.allocator.step(prices_information)
        if trade is not None:
            self.execute_trade(trade)
        final_dict['done'] = prices_information.get("done", True)
        final_dict['obs']["assets"] = prices_information.get("assets", {})
        # we'd put all of the portfolio information here by asset. 
        final_dict['obs']["portfolio"] = {}
        # get percentages
        return final_dict
    

    def step_no_trade(self) -> dict:
        self.placeholders['portfolio'] = self.latest_portfolio()
        self.placeholders['balance'] = self.balance

        final_dict = {'obs': {}, 'done': False}
        prices_information = self.pricing.step()
        self.allocator.step(prices_information)
        self._update_account_no_order()
        final_dict['done'] = prices_information.get("done", True)
        final_dict['obs']["assets"] = prices_information.get("assets", {})
        # we'd put all of the portfolio information here by asset. 
        final_dict['obs']["portfolio"] = {}
        # get percentages
        return final_dict

    def close(self):
        pass



def main():
    """ Should run through everything returning zero right now"""
    asset_list = ["BTC", "ATL", "TRX", "ETH", "BCH", "XRP", "LTC", "EOS", "ADA", "XMR", "LINK", "HT"]
    jambo = Jamboree()
    episode_id = uuid.uuid4().hex
    user_id = uuid.uuid4().hex
    portfolio_handler = PortfolioHandler()
    price_handler = SimulatedPriceHandler()
    price_handler['episode'] = episode_id # set this to live if we're trying to use live prices.
    price_handler['exchange'] = "binance"
    price_handler['live'] = False
    price_handler['obs_num'] = 1500
    price_handler.event = jambo
    price_handler.add_assets(asset_list)


    portfolio_handler.limit = 1000
    portfolio_handler.event = jambo
    portfolio_handler['episode'] = episode_id
    portfolio_handler['user_id'] = user_id
    portfolio_handler['exchange'] = "binance"
    portfolio_handler.pricing = price_handler
    portfolio_handler.reset()

    for _ in range(1000):
        step_information = portfolio_handler.step()
        logger.info(step_information.keys())




if __name__ == "__main__":
    main()