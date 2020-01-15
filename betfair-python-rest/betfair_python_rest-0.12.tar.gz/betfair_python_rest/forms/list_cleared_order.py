from .abstract_forms.base import BaseForm
from .abstract_forms import (MarketIdsField, EventAndEventTypeIds,
                             RunnerIdsField, BetIdsField, CustomerRefs,
                             RecordPagination, TimeRange, LocaleField, BetStatusField)
from dataclasses import dataclass


@dataclass
class ListClearedOrdersForm(BaseForm, EventAndEventTypeIds, RunnerIdsField,
                            BetIdsField, CustomerRefs, LocaleField, RecordPagination,
                            MarketIdsField, BetStatusField, TimeRange):
    '''
    Class for request method
    It should be used like that:
    ___
    market_book_form = ListClearedOrdersForm(**your_data)
    api_manager = BetFairAPIManagerBetting(login='login', password='password', api_kay='api_key')
    list_event_types_response = api_manager.list_cleared_orders(request_class_object=market_filter)
    ___
    You can find details about params in parent classes
    '''
    market_ids: list = None
    side: str = None
    group_by: str = None
    include_item_description: bool = None

    @property
    def data(self):
        return {
            'betStatus': self.bet_status, 'eventTypeIds': self.event_type_ids,
            'eventIds': self.event_ids, 'marketIds': self.market_ids,
            'runnerIds': self.runner_ids, 'betIds': self.bet_ids,
            'side': self.side, 'settledDateRange': self.time_range_data,
            'groupBy': self.group_by, 'locale': self.locale,
            'includeItemDescription': self.include_item_description,
            'fromRecord': self.from_record, 'recordCount': self.record_count
        }
