from .abstract_forms.base import BaseForm
from .abstract_forms import MarketFilter, MarketProjectionField, LocaleField
from dataclasses import dataclass


@dataclass
class ListMarketCatalogueForm(BaseForm, MarketFilter, MarketProjectionField, LocaleField):
    '''
    Class for request method
    It should be used like that:
    ___
    market_filter = MarketFilterAndTimeGranularityForm(text_query='Text', time_granularity=TimeGranularity.DAYS)
    api_manager = BetFairAPIManagerBetting(login='login', password='password', api_kay='api_key')
    list_event_types_response = api_manager.list_time_ranges(request_class_object=market_filter)
    ___
    You can find details about params in parent classes, some of them listed below:
    :param market_sort: string. The order of the results.
         Will default to RANK if not passed. RANK is an assigned priority
         that is determined by our Market Operations
         team in our back-end system. A result's
         overall rank is derived from the ranking
          given to the flowing attributes for
          the result. EventType, Competition, StartTime,
          MarketType, MarketId. For example, EventType
          is ranked by the most popular sports types and marketTypes
           are ranked in the following order:
           ODDS ASIAN LINE RANGE
           If all other dimensions of the result
           are equal, then the results are ranked in MarketId order.
           Variables listed in 	MarketSort enum
    :param max_results: limit on the total number of
    results returned, must be greater than 0 and
     less than or equal to 1000
    '''
    max_results: int = 500
    market_sort: str = None

    @property
    def data(self):
        return {'filter': self.market_filter_data, 'marketProjection': self.market_projection,
                'sort': self.market_sort, 'maxResults': self.max_results,
                'locale': self.locale}
