from .abstract_forms.base import BaseForm
from .abstract_forms import BookForm, MarketIdsField
from dataclasses import dataclass


@dataclass
class ListMarketBookForm(BaseForm, BookForm, MarketIdsField):
    '''
    Class for request method
    It should be used like that:
    ___
    market_book_form = ListMarketBookForm(**your_data)
    api_manager = BetFairAPIManagerBetting(login='login', password='password', api_kay='api_key')
    list_event_types_response = api_manager.list_market_book(request_class_object=market_filter)
    ___
    You can find details about params in parent classes
    '''

    @property
    def data(self):
        return {'marketIds': self.market_ids, 'priceProjection': self.price_projection_data,
                'orderProjection': self.order_projection, 'matchProjection': self.match_projection,
                'includeOverallPosition': self.include_overall_position,
                'partitionMatchedByStrategyRef': self.partition_matched_by_strategy_ref,
                'customerStrategyRefs': self.customer_strategy_refs,
                'currencyCode': self.currency_code, 'locale': self.locale,
                'matchedSince': self.matched_since, 'betIds': self.bet_ids}
