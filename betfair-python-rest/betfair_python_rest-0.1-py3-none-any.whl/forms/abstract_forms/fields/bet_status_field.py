from dataclasses import dataclass


@dataclass
class BetStatusField:
    '''
    Restricts the results to the specified status.
    '''
    bet_status: str
