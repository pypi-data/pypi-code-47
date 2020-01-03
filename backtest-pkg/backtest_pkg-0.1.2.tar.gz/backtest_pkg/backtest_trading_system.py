import pandas as pd 

class trading_system:

    def __init__(self, capital=10**6):
        self.capital = capital
        self.__init_account()
        self.__init_order_book()

    # Handling accoutn initiation:
    def __init_account(self):
        '''
        On attribute 'account', use a dictionary to store holding information. 
        The dictionary has keys ['cash', 'shares'], values cash amount, number of holding shares.
        '''
        self.account = {'cash': self.capital, 'share': 0}
        self.transaction_record = pd.DataFrame(columns=['Date', 'Side', 'Quantity', 'Price'])  
    
    # Handling order book initiation:
    def __init_order_book(self):
        '''
        Initiate the order book to contain order information for execution.
        market orders: record to number of shares to buy/sell in market
        limit orders: a pd.Series with key string format of limit price, value integer format of buy/sell shares.
        target orders: same as limit order, different execution rules.
        '''
        self.market_book = 0
        self.limit_buy_book = pd.Series()
        self.limit_sell_book = pd.Series()
        self.target_buy_book = pd.Series()
        self.target_sell_book = pd.Series()

    def set_price(self, OHLC):
        '''
        OHLC data should have shape n by 4, with columns ['open', 'high', 'low', 'clos'] price data.
        '''
        OHLC.columns = list('OHLC')
        OHLC.index = pd.to_datetime(OHLC.index)
        self.__price = OHLC

    @property
    def account_value(self):
        current_price = self.current_trading_data['C']
        return self.account['cash'] + self.account['share']*current_price

 ###################   Create Orders   ###############################
    def market_order(self, side, quantity):
        '''
        side: either 'B' or 'S'
        quatity: number of shares to buy/sell at market price.
        '''
        if side == 'B':
            self.market_book += quantity
        elif side == 'S':
            self.market_book -= quantity
        else:
            raise "Unknown Side!"
    
    def limit_order(self, side, quantity, price):
        '''
        side: 'B' or 'S'
        quantity: number of shares to buy/sell
        price: limit price to buy/sell
        '''
        price = float(price)
        if side == 'B':
            self.limit_buy_book[price] = self.limit_buy_book.get(price, 0) + quantity
        elif side == 'S':
            self.limit_sell_book[price] = self.limit_sell_book.get(price, 0) + quantity
        else:
            raise "Unknown Side!"

    def target_order(self, side, quantity, price):
        '''
        side: 'B' or 'S'
        quantity: number of shares to buy.
        price: exact price to buy. (No transaction for higher or lower price)
        '''
        price = float(price)
        if side == 'B':
            self.target_buy_book[price] = self.target_buy_book.get(price, 0) + quantity
        elif side == 'S':
            self.target_sell_book[price] = self.target_sell_book.get(price, 0) + quantity
        else:
            raise "Unknown Side!"
            
#####################   Execution    #########################
    def _load_trading_data(self, date):
        '''
        On attribute 'current_trading_data', use a pd.Series to store OHLC price on given date.
        '''
        date = pd.to_datetime(date)
        self.current_trading_data = self.__price.loc[date, :]
        self.current_trading_date = date

    # to do: handling shorting money/shares? how to deal with remaining orders, return?
    def  transaction(self, date, side, qty, price):
        '''
        Execute give transaction and update transaction record. Return executed qty.
        '''
        if side == 'B':
            # If not enough cash, will buy as much as possible.
            if self.account['cash'] < qty*price:
                qty = int(self.account['cash']/price)
            if qty == 0:
                return 0
            # Transaction:
            self.account['cash'] -= qty*price
            self.account['share'] += qty 
            self.transaction_record = self.transaction_record.append({'Date':date, 'Side': 'B', 'Quantity':qty, 'Price': price}, ignore_index = True)
            return qty

        elif side  == 'S':
            # If not enough share, will sell all.
            if self.account['share'] < qty:
                qty = self.account['share']
            if qty ==0:
                return 0
            # Transaction
            self.account['cash'] += qty*price
            self.account['share'] -= qty 
            self.transaction_record = self.transaction_record.append({'Date':date, 'Side': 'S', 'Quantity':qty, 'Price': price}, ignore_index = True)
            return qty
        else:
            raise 'Unknown Side'


    ####################     Market orders     #######################
    def execute_market_orders(self):
        open_price = self.current_trading_data['O']
        date = self.current_trading_date

        # Market trade are execute at open price:
        market_shares = self.market_book
        if market_shares == 0:
            return
        elif market_shares>0:
            executed_share = self.transaction(date, 'B', market_shares, open_price)
            self.market_book -= executed_share
        else:
            executed_share = self.transaction(date, 'S', -market_shares, open_price)
            self.market_book += executed_share

    ####################     Target Orders    ####################
    def execute_target_orders(self):
        low_price = self.current_trading_data['L']    
        high_price = self.current_trading_data['H']
        date = self.current_trading_date

        # Target buy:
        numerical_index = pd.to_numeric(self.target_buy_book.index)
        execute_index = (numerical_index <= high_price) & (numerical_index >= low_price)
        for price in numerical_index[execute_index]:
            execute_share = self.transaction(date, 'B', self.target_buy_book[float(price)], price)
            self.target_buy_book[float(price)] -= execute_share
            # print(self.target_buy_book)
        self.target_buy_book = self.target_buy_book[self.target_buy_book !=0] # Update book
        # print(self.target_buy_book)

        # Target sell:
        numerical_index = pd.to_numeric(self.target_sell_book.index)
        execute_index = (numerical_index <= high_price) & (numerical_index >= low_price)
        for price in numerical_index[execute_index]:
            execute_share = self.transaction(date, 'S', self.target_sell_book[float(price)], price)
            self.target_sell_book[float(price)] -= execute_share
        self.target_sell_book = self.target_sell_book[self.target_sell_book !=0] # Update book
        
    ####################     Limit Orders   ####################
    def execute_limit_orders(self):
        open_price = self.current_trading_data['O']
        high_price = self.current_trading_data['H']
        low_price = self.current_trading_data['L']
        date = self.current_trading_date

        # open buy:
        numerical_index = pd.to_numeric(self.limit_buy_book.index)
        execute_index = (numerical_index >= open_price)
        for price in numerical_index[execute_index]:
            execute_share = self.transaction(date, 'B', self.limit_buy_book[float(price)], open_price)
            self.limit_buy_book[float(price)] -= execute_share
        self.limit_buy_book = self.limit_buy_book[self.limit_buy_book!=0] # Update book

        # intraday buy:
        numerical_index = pd.to_numeric(self.limit_buy_book.index)
        execute_index = (numerical_index >= low_price)
        for price in numerical_index[execute_index]:
            execute_share = self.transaction(date, 'B', self.limit_buy_book[float(price)], price)
            self.limit_buy_book[float(price)] -= execute_share
        self.limit_buy_book = self.limit_buy_book[self.limit_buy_book!=0] # Update book

        # open sell:
        numerical_index = pd.to_numeric(self.limit_sell_book.index)
        execute_index = (numerical_index <= open_price)
        for price in numerical_index[execute_index]:
            execute_share = self.transaction(date, 'S', self.limit_sell_book[float(price)], open_price)
            self.limit_sell_book[float(price)] -= execute_share
        self.limit_sell_book = self.limit_sell_book[self.limit_sell_book!=0] # Update book

        # intraday sell:
        numerical_index = pd.to_numeric(self.limit_sell_book.index)
        execute_index = (numerical_index <= high_price)
        for price in numerical_index[execute_index]:
            execute_share = self.transaction(date, 'S', self.limit_sell_book[float(price)], price)
            self.limit_sell_book[float(price)] -= execute_share
        self.limit_sell_book = self.limit_sell_book[self.limit_sell_book!=0] # Update book

    
    def execute(self, date):
        self._load_trading_data(date)
        self.execute_market_orders()
        self.execute_limit_orders()
        self.execute_target_orders()


###################   Strategy   ########################







class universe:
    def __init__(self, OHLC = dict()):
        '''
        OHLC is a dictionary with key as identity of security (Ticker, SEDOL, ISIN or any other id) and value as data frame with columns ['O', 'H', 'L', 'C'] and rows dates of corresponding data.
        '''
        self.OHLC = OHLC
    
    def append(self, id, OHLC_df):
        self.OHLC[id] = OHLC_df
    
    def merge(self, OHLC_dict):
        self.OHLC = {**self.OHLC, **OHLC_dict}

class orders:
    '''
    Each order should has id (Ticker/SEDOL or anything recognized in the universe), side (B/S), quantity, type (Market/Limit/Target) and price. It should be a pd.Series with corresponding indexes.
    Order record is a data frame of columns ['id', 'side', 'quantity', 'type', 'price']
    '''
    def __init__(self, order_record=None):
        if order_record:
            self.record = order_record
        else:
            self.record = pd.DataFrame(columns=['id', 'side', 'quantity', 'type', 'price'])

    def append(self, order):
        '''
        order is a pd.Series with index ['id', 'side', 'quantity', 'type', 'price'].
        '''
        self.record = self.record.append(order, ignore_index = True)
    
    def merge(self, new_order_record):
        '''
        new_order_record is pd.DataFrame with columns ['id', 'side', 'quantity', 'type', 'price'].
        '''
        self.record = pd.concat([self.record, new_order_record], axis=1, join='inner')

    def delete(self, order=None, order_record=None):
        pass


class account:
    '''
    Account contains information of holding. It is a data frame of columns ['quantity', 'price', 'value'], index as id of security or 'cash'.
    Transactions will record quantity change in account.
    '''
    def __init__(self, capital = 10**6):
        self.holding = pd.DataFrame(columns=['quantity', 'price', 'value'])
        self.holding.loc['Cash', :] = [capital, 1, capital]
    


class signal:

    '''
    signal is a model for evaluating features like lagged OHLC data, fundamental data, related security information, macro data (like GDP growth, interest rate change, FX movement) to output trading recomendation. 
    The API here is much like sk-learn models if it needs to be updated or trained with new data. The model can also be hard-code rules for certain logic. The output can be a direct trade label (Buy, Sell, Hold or numerical values 1, 0, -1) or a rating for each trade label, or a probability distribution of each label.
    '''
    def __init__(self):
        pass



