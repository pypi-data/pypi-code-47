from dataclasses import dataclass
from datetime import datetime
from . import SelectionIdField


@dataclass
class LimitOrderOnClose(SelectionIdField):
    '''
    Place a new LIMIT order (simple exchange bet for immediate execution)
    :param liability: The size of the bet. See Min BSP Liability
    :param price: The limit price of the bet if LOC

    '''
    liability: float
    price: float

    @property
    def data(self):
        return {
            'liability': self.liability,
            'price': self.price,
        }
