from .abstract_forms.base import BaseForm
from .abstract_forms import BookForm, MarketIdField, SelectionIdField
from dataclasses import dataclass


@dataclass
class ListRunnerBookForm(BaseForm, BookForm, SelectionIdField, MarketIdField):
    '''
    Class for request method
    It should be used like that:
    ___
    market_book_form = ListRunnerBookForm(**your_data)
    api_manager = BetFairAPIManagerBetting(login='login', password='password', api_kay='api_key')
    list_event_types_response = api_manager.list_runner_book(request_class_object=market_filter)
    ___
    You can find details about params in parent classes

    :param handicap: The projection of price data you want to receive in the response.
    '''
    handicap: float = None

    @property
    def data(self):
        return {'marketId': self.market_id, 'selectionId': self.selection_id, 'handicap': self.handicap,
                'priceProjection': self.price_projection_data,
                'orderProjection': self.order_projection, 'matchProjection': self.match_projection,
                'includeOverallPosition': self.include_overall_position,
                'partitionMatchedByStrategyRef': self.partition_matched_by_strategy_ref,
                'customerStrategyRefs': self.customer_strategy_refs,
                'currencyCode': self.currency_code, 'locale': self.locale,
                'matchedSince': self.matched_since, 'betIds': self.bet_ids}
