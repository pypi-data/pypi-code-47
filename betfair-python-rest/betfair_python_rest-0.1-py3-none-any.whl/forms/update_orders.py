from .abstract_forms.base import BaseForm
from .abstract_forms import (MarketIdField, CustomerRefField, UpdateInstructionsField)
from dataclasses import dataclass


@dataclass
class UpdateOrdersForm(BaseForm, CustomerRefField, UpdateInstructionsField, MarketIdField):
    '''
    Class for request method
    It should be used like that:
    ___
    market_book_form = UpdateOrdersForm(**your_data)
    api_manager = BetFairAPIManagerBetting(login='login', password='password', api_kay='api_key')
    list_event_types_response = api_manager.update_orders(request_class_object=market_filter)
    ___

    '''

    @property
    def data(self):
        if self.instructions is not None:
            return {'marketId': self.market_id,
                    'instructions': self.instructions_data,
                    'customerRef': self.customer_ref,
                    }
