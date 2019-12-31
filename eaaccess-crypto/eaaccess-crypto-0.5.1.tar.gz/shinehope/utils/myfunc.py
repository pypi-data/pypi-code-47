from shinehope.eaaccess.marketdata import TimeFrame
# import configparser
# import os


def getPeriodTimeDelta(period:TimeFrame) -> int:  # return milliseconds
    if period == TimeFrame.PERIOD_M1:
        return 1 * 60 * 1000
    elif period == TimeFrame.PERIOD_M5:
        return 5 * 60 * 1000
    elif period == TimeFrame.PERIOD_M15:
        return 15 * 60 * 1000
    elif period == TimeFrame.PERIOD_M30:
        return 30 * 60 * 1000
    elif period == TimeFrame.PERIOD_H1:
        return 1 * 60 * 60 * 1000
    elif period == TimeFrame.PERIOD_H4:
        return 4 * 60 * 60 * 1000
    elif period == TimeFrame.PERIOD_D1:
        return 24 * 60 * 60 * 1000
    else:
        return 0

def getCandleSizeMin(candleSize:str) -> int:  # return milliseconds
    """
        '15m' --> 15    (15 * 1)
        '1h'  --> 60    (1 * 60)
        '1d'  --> 1440  (1 * 24 * 60)
    """
    trailChar = candleSize[-1]
    valueHead = int(candleSize[:-1])
    minCandles = None
    if trailChar == 'm':
        minCandles = valueHead * 1
    elif trailChar == 'h':
        minCandles = valueHead * 60
    elif trailChar == 'd':
        minCandles = valueHead * 24 * 60

    return  minCandles

def getRawAPISymbol(ccxt_symbol, exchange_name='binance') -> str:
    rawsymbol = ""
    if exchange_name == 'binance':
        rawsymbol = ccxt_symbol.replace("/", "").lower()

    return  rawsymbol

   
