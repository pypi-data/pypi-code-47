from dataclasses import dataclass


@dataclass
class MarketIdsField:
    '''
    One or more market ids.
    The number of markets returned
    depends on the amount of data you
    request via the price projection.
    '''
    market_ids: list
