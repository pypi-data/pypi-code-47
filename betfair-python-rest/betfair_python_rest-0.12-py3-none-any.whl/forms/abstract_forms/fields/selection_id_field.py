from dataclasses import dataclass


@dataclass
class SelectionIdField:
    '''
    The unique id for the market.
    '''
    selection_id: int
