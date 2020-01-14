from . import LocaleField, StrategyRefs, PriceProjection, OrderProjectionField, BetIdsField
from dataclasses import dataclass
from datetime import datetime


@dataclass
class BookForm(LocaleField, StrategyRefs, PriceProjection, OrderProjectionField, BetIdsField):
    '''
    Class for request method
    It should be used like that:
    ___
    market_book_form = ListMarketBookForm(**your_data)
    api_manager = BetFairAPIManagerBetting(login='login', password='password', api_kay='api_key')
    list_event_types_response = api_manager.list_market_book(request_class_object=market_filter)
    ___
    You can find details about params in parent classes, some of them listed below:

    :param match_projection: If you ask for orders, specifies the
    representation of matches.

    :param include_overall_position: If you ask for orders, returns
    matches for each selection. Defaults to true if unspecified.

    :param currency_code: A Betfair standard currency code. If not
    specified, the default currency code is used.

    :param matched_since: If you ask for orders, restricts the results
    to orders that have at least one fragment matched since the
    specified date (all matched fragments of such an
     order will be returned even if some were matched
     before the specified date). All EXECUTABLE orders will
      be returned regardless of matched date.

    '''
    order_projection: str = None
    match_projection: str = None
    include_overall_position: bool = None

    currency_code: str = None
    matched_since: datetime.date = None

    @property
    def data(self):
        return {'priceProjection': self.price_projection_data,
                'orderProjection': self.order_projection, 'matchProjection': self.match_projection,
                'includeOverallPosition': self.include_overall_position,
                'partitionMatchedByStrategyRef': self.partition_matched_by_strategy_ref,
                'customerStrategyRefs': self.customer_strategy_refs,
                'currencyCode': self.currency_code, 'locale': self.locale,
                'matchedSince': self.matched_since, 'betIds': self.bet_ids}
