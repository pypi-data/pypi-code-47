from .abstract_forms.base import BaseForm
from .abstract_forms import (CustomerStrategyRefsField,
                             PlaceInstructionsField,
                             PlaceAndReplaceOrdersFields)
from dataclasses import dataclass


@dataclass
class PlaceOrderForm(BaseForm, CustomerStrategyRefsField,
                     PlaceAndReplaceOrdersFields, PlaceInstructionsField):
    '''
    Class for request method
    It should be used like that:
    ___
    market_book_form = PlaceOrderForm(**your_data)
    api_manager = BetFairAPIManagerBetting(login='login', password='password', api_kay='api_key')
    list_event_types_response = api_manager.place_orders(request_class_object=market_filter)
    ___
    You can find details about params in parent classes
    '''
    is_async: bool = None
    market_version: str = None

    @property
    def data(self):
        return {'marketId': self.market_id,
                'instructions': self.instructions_data,
                'customerRef': self.customer_ref,
                'marketVersion': {'version': self.market_version},
                'customerStrategyRef': self.customer_strategy_refs,
                'async': self.is_async}
