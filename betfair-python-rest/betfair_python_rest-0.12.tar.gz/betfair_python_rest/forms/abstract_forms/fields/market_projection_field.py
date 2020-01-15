from dataclasses import dataclass


@dataclass
class MarketProjectionField:
    '''
    List of params of MarketFilter below.
        :param market_projection: string. The type and
         amount of data returned about the market.
         The variables listed in MarketProjection enum
    '''
    market_projection: list = None
