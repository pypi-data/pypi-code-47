from .abstract_forms.base import BaseForm
from .abstract_forms import (MarketIdField, CustomerRefField, CancelInstruction)
from dataclasses import dataclass
from typing import List


@dataclass
class CancelOrdersForm(BaseForm, CustomerRefField, MarketIdField):
    '''
    Class for request method
    It should be used like that:
    ___
    market_book_form = CancelOrdersForm(**your_data)
    api_manager = BetFairAPIManagerBetting(login='login', password='password', api_kay='api_key')
    list_event_types_response = api_manager.cancel_orders(request_class_object=market_filter)
    ___
    You can find details about params in parent classes
    :param instructions: All instructions need to be
     on the same market. If not supplied all unmatched
      bets on the market (if market id is passed)
      are fully cancelled.  The limit of cancel
      instructions per request is 60
    '''
    instructions: List[CancelInstruction] = None
    market_id: str = None

    @property
    def data(self):
        if self.instructions is not None:
            return {'marketId': self.market_id,
                    'instructions': [instruction.data for instruction in self.instructions],
                    'customerRef': self.customer_ref
                    }
