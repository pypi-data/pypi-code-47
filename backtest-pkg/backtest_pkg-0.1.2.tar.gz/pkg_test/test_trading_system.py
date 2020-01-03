#%%%%%%%%%%%%%%%%%%%%%%%%%%%
import os
import backtest_pkg.backtest_trading_system as bt 
import importlib
import pandas as pd 
from pandas_datareader import data
# import matplotlib.pyplot as plt


#%%%%%%%%%%%%%%%%   Code for first download    %%%%%%
start_date = '2010-01-01'
end_date = '2018-12-31'

ticker_list = ['AAPL','GOOG','FB', 'MSFT']
for ticker in ticker_list:
    price_data = data.DataReader(ticker, 'yahoo', start_date, end_date)
    price_data.to_csv(f'pkg_test/Technical Data/{ticker}.csv')


#%%%%%%%%%%%%%%%%%%%%%%%%%%
importlib.reload(bt)

def show_result():
    print(trade_sys.account)
    print(trade_sys.account_value)
    print(trade_sys.transaction_record)
    print('Market order book:')
    print(trade_sys.market_book)
    print('Limit order book:')
    print(trade_sys.limit_buy_book)
    print(trade_sys.limit_sell_book)
    print('Target order book:')
    print(trade_sys.target_buy_book)
    print(trade_sys.target_sell_book)

price_data = pd.read_csv('pkg_test/Technical Data/MSFT.csv', index_col=0)
trade_sys = bt.trading_system()
trade_sys.set_price(price_data[['Open', 'High', 'Low', 'Close']])
trade_sys.market_order('B', 1)
trade_sys.limit_order('B', 1, 29)
trade_sys.limit_order('S', 2, 31)
trade_sys.target_order('B', 1, 32)
trade_sys.target_order('S', 3, 35)
show_result()


# %%%%%%%%%%%%%%%%%   Market order %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
importlib.reload(bt)

trade_sys = bt.trading_system(100)
trade_sys.set_price(price_data[['Open', 'High', 'Low', 'Close']])
testing_period = price_data.index[:20]

side = 1
for date in testing_period:
    if side > 0:
        trade_sys.market_order('B', 1)
        trade_sys.execute(date)
    # else:
    #     trade_sys.market_order('S', 1)
    #     trade_sys.execute(date)
    side = -side 

#%%%%%%%%%%%%%%%%%%   Target Order   %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
importlib.reload(bt)

trade_sys = bt.trading_system()
trade_sys.set_price(price_data[['Open', 'High', 'Low', 'Close']])
testing_period = price_data.index[:20]

# for price in [31.5, 31., 30.5, 30.0, 29.5, 29.0]:
    # trade_sys.target_order('B', 1, price)
trade_sys.market_order('B', 3)
for price in [31.5, 31., 30.5, 30.0, 29.5, 29.0]:
    trade_sys.target_order('S', 1, price)

for date in testing_period:
    trade_sys.execute(date)
show_result()

#%%%%%%%%%%%%%%%%%%%   Limit Order   %%%%%%%%%%%%%%%%%%%%%%%%%%%%
importlib.reload(bt)

trade_sys = bt.trading_system()
trade_sys.set_price(price_data[['Open', 'High', 'Low', 'Close']])
testing_period = price_data.index[:20]

# for price in [31.5, 31., 30.5, 30.0, 29.5, 29.0]:
    # trade_sys.limit_order('B', 1, price)
trade_sys.market_order('B', 5)
for price in [31.5, 31., 30.5, 30.0, 29.5, 29.0]:
    trade_sys.target_order('S', 1, price)

for date in testing_period:
    trade_sys.execute(date)

show_result()


#%%%%%%%%%%%%%%%%%%    Golden Cross strategy   %%%%%%%%%%%%%%%
# ticker = '3988.HK'
# ticker = '0823.HK'
ticker = '0001.HK'
# price_data = pd.read_csv(f'pkg_test/Technical Data/{ticker}.csv', index_col=0)
price_data = data.DataReader(ticker, 'yahoo', start_date, end_date)

# Prepare data for the strategy:
adjusted_close = price_data['Adj Close']
moving_avg_5 = adjusted_close.rolling(5).mean().dropna()
moving_avg_20 = adjusted_close.rolling(20).mean().dropna()

# Setting up trading system:
capital = 10000
trade_sys = bt.trading_system(capital)
trade_sys.set_price(price_data[['Open', 'High', 'Low', 'Close']])
testing_period = price_data.index[21:]

PnL_ts = pd.Series()
for date in testing_period:
    trade_sys.execute(date)
    PnL_ts[date] = trade_sys.account_value - capital

    current_avg5 = moving_avg_5.shift(0)[date]
    pre_avg5 = moving_avg_5.shift(1)[date]
    current_avg20 = moving_avg_20.shift(0)[date]
    pre_avg20 = moving_avg_20.shift(1)[date]
    share_to_trade = int(0.1*capital/price_data.loc[date, 'Close'])
    # Buy on crossing upward:
    if (current_avg5>=current_avg20) and (pre_avg5<pre_avg20):
        trade_sys.market_order('B', share_to_trade)
    # Sell all on crossing downward:
    if (current_avg5<current_avg20) and (pre_avg5>=pre_avg20):
        trade_sys.market_order('S', trade_sys.account['share'])
    
    
PnL_ts.plot()    








