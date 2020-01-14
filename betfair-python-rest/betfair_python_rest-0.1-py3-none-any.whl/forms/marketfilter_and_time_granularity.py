from .abstract_forms.base import BaseForm
from .abstract_forms import MarketFilter, TimeGranularityField
from dataclasses import dataclass


@dataclass
class MarketFilterAndTimeGranularityForm(BaseForm, MarketFilter, TimeGranularityField):
    '''
    Class for request method
    It should be used like that:
    ___
    market_filter = MarketFilterAndTimeGranularityForm(text_query='Text', time_granularity=TimeGranularity.DAYS)
    api_manager = BetFairAPIManagerBetting(login='login', password='password', api_kay='api_key')
    list_event_types_response = api_manager.list_time_ranges(request_class_object=market_filter)
    ___
    You can find details about params in parent classes
    '''

    @property
    def data(self):
        return {'filter': self.market_filter_data, 'granularity': self.time_granularity}
