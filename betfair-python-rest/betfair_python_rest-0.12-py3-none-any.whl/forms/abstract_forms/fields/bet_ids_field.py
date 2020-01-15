from dataclasses import dataclass


@dataclass
class BetIdsField:
    '''
    One or more market ids.
    The number of markets returned
    depends on the amount of data you
    request via the price projection.
    '''
    bet_ids: list = None
