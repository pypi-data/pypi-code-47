# Testing indicators
import pandas as pd

from utils.ohlcv import OHLCV

ohlcv = OHLCV()

src = ohlcv.btc['close']

from indicators.bollinger import bollinger

test = bollinger(ohlcv.btc)
pd.DataFrame(test)
