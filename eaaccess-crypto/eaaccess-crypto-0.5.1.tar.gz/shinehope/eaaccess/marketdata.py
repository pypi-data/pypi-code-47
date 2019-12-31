"""
    market data types (shared classes)
        BarData, TimeFrame..., etc.
"""
# from enum import Enum
import enum

class BarData(object):
    """
    K 线数据模型.
    """
    def __init__(self, timestamp:int = 0, open_price = 0.0, high_price = 0.0, low_price = 0.0, close_price = 0.0, volume = 0.0):
        super(BarData, self).__init__()

        self.timestamp:int = timestamp      # UTC timestamp in milliseconds, integer
        self.open_price = open_price
        self.high_price = high_price
        self.low_price = low_price
        self.close_price = close_price
        self.volume = volume                # (V)olume (in terms of the base currency), float

    def __str__(self):
        return f"{self.timestamp} {self.open_price} {self.high_price} {self.low_price} {self.close_price} {self.volume}"


class TradeData(object):
    """
    Maker fees are paid when you provide liquidity to the exchange i.e. you market-make an order and someone else fills it. 
    Maker fees are usually lower than taker fees. Similarly, taker fees are paid when you take liquidity from the exchange and 
    fill someone else's order.

    Do not rely on precalculated values, because market conditions change frequently. 
    It is difficult to know in advance whether your order will be a market taker or maker.
    {
        'info':         { ... },                    // the original decoded JSON as is
        'id':           '12345-67890:09876/54321',  // string trade id
        'timestamp':    1502962946216,              // Unix timestamp in milliseconds
        'datetime':     '2017-08-17 12:42:48.000',  // ISO8601 datetime with milliseconds
        'symbol':       'ETH/BTC',                  // symbol
        'order':        '12345-67890:09876/54321',  // string order id or undefined/None/null
        'type':         'limit',                    // order type, 'market', 'limit' or undefined/None/null
        'side':         'buy',                      // direction of the trade, 'buy' or 'sell'
        'takerOrMaker': 'taker',                    // string, 'taker' or 'maker'
        'price':        0.06917684,                 // float price in quote currency
        'amount':       1.5,                        // amount of base currency
        'cost':         0.10376526,                 // total cost (including fees), `price * amount`
        'fee':          {                           // provided by exchange or calculated by ccxt
            'cost':  0.0015,                        // float
            'currency': 'ETH',                      // usually base currency for buys, quote currency for sells
            'rate': 0.002,                          // the fee rate (if available)
        },
    }
    """
    trade_id = "none"
    timestamp = 0
    symbol = "BTC/USDT"
    order_id = "none"
    trade_type = "limit"
    side = "buy"
    takerOrMaker = "taker"
    price = 0.0
    amount = 0.0
    cost = 0.0
    fee = {}

class OrderData(object):
    """ ccxt (2019.10.20)
    {
        'id':                '12345-67890:09876/54321', // string
        'datetime':          '2017-08-17 12:42:48.000', // ISO8601 datetime of 'timestamp' with milliseconds
        'timestamp':          1502962946216, // order placing/opening Unix timestamp in milliseconds
        'lastTradeTimestamp': 1502962956216, // Unix timestamp of the most recent trade on this order
        'status':     'open',         // 'open', 'closed', 'canceled'
        'symbol':     'ETH/BTC',      // symbol
        'type':       'limit',        // 'market', 'limit'
        'side':       'buy',          // 'buy', 'sell'
        'price':       0.06917684,    // float price in quote currency
        'amount':      1.5,           // ordered amount of base currency
        'filled':      1.1,           // filled amount of base currency
        'remaining':   0.4,           // remaining amount to fill
        'cost':        0.076094524,   // 'filled' * 'price' (filling price used where available)
        'trades':    [ ... ],         // a list of order trades/executions
        'fee': {                      // fee info, if available
            'currency': 'BTC',        // which currency the fee is (usually quote)
            'cost': 0.0009,           // the fee amount in that currency
            'rate': 0.002,            // the fee rate (if available)
        },
        'info': { ... },              // the original unparsed order structure as is
    }
    """
    order_id = "none"
    timestamp = 0
    status = "open"
    symbol = "BTC/USDT"
    order_type = "market"
    side = "buy"
    price = 0.0
    amount = 0.0
    filled = 0.0
    remaining = 0.0

class TradeOperation(enum.IntEnum):
    OP_BUY = 0          # Buy operation
    OP_SELL = 1         # Sell operation
    OP_BUYLIMIT = 2     # Buy limit pending order
    OP_SELLLIMIT = 3    # Sell limit pending order
    # OP_BUYSTOP = 4      # Buy stop pending order
    # OP_SELLSTOP = 5	    # Sell stop pending order


class StrEnum(str, enum.Enum):
    pass

class TimeFrame(StrEnum):
    PERIOD_M1 = '1m'
    PERIOD_M5 = '5m'
    PERIOD_M15 = '15m'
    PERIOD_M30 = '30m'
    PERIOD_H1 = '1h'
    PERIOD_H4 = '4h'
    PERIOD_D1 = '1d'
    # PERIOD_W1 = '1w'
    # PERIOD_MN1 = '1M'

class TradeType(StrEnum):
    TYPE_MARKET = "market"
    TYPE_LIMIT = "limit"

class Ticker(object):
    def __init__(self):
        super(Ticker, self).__init__()

        self.symbol = None          # string symbol of the market ('BTC/USD', 'ETH/BTC', ...)
        self.rawsymbol = None       # Exchange's raw cryptocurrency symbol
        self.timestamp = 0          # int (64-bit Unix Timestamp in milliseconds since Epoch 1 Jan 1970)
        self.high = 0.0             # highest price
        self.low = 0.0              # lowest price
        self.bid = 0.0              # current best bid (buy) price
        self.bidVolume = 0.0        # current best bid (buy) amount (may be missing or undefined)
        self.ask = 0.0              # current best ask (sell) price
        self.askVolume = 0.0        # current best ask (sell) amount (may be missing or undefined)
        self.vwap = 0.0             # volume weighed average price
        self.open = 0.0             # opening price
        self.close = 0.0            # price of last trade (closing price for current period)
        self.last = 0.0             # same as `close`, duplicated for convenience
        self.previousClose = 0.0    # closing price for the previous period
        self.change = 0.0           # Price change (absolute change, `last - open`)
        self.percentage = 0.0       # Price change percent (relative change, `(change/open) * 100`)
        self.baseVolume = 0.0       # Total traded base asset volume (volume of base currency traded for last 24 hours)
        self.quoteVolume = 0.0      # Total traded quote asset volume (volume of quote currency traded for last 24 hours)

    def __str__(self):
        return f"{{s:{self.symbol} t:{self.timestamp} ask:{self.ask} askV:{self.askVolume} bid:{self.bid} bidV:{self.bidVolume},...}}"