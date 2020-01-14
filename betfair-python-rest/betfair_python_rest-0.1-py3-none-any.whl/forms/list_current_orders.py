from .abstract_forms.base import BaseForm
from .abstract_forms import (MarketIdsField, OrderProjectionField, BetIdsField,
                             CustomerRefs, TimeRange, RecordPagination)
from dataclasses import dataclass


@dataclass
class ListCurrentOrdersForm(BaseForm, BetIdsField, OrderProjectionField,
                            CustomerRefs, RecordPagination, MarketIdsField):
    '''
    Class for request method
    It should be used like that:
    ___
    request_data_object = ListCurrentOrdersForm(**your_data)
    api_manager = BetFairAPIManagerBetting(login='login', password='password', api_kay='api_key')
    list_event_types_response = api_manager.list_current_orders(request_class_object=request_data_object)
    ___
    You can find details about params in parent classes, some of them listed below:
    :param market_ids: Optionally restricts the results to the
     specified market IDs. A maximum of 250 marketId's,
      or a combination of 250 marketId's & betId's are permitted.

    :param date_range: Optionally restricts the results to
     be from/to the specified date, these dates
      are contextual to the orders being returned
      and therefore the dates used to filter on
      will change to placed, matched, voided or
       settled dates depending on the orderBy.
       This date is inclusive, i.e. if an order
       was placed on exactly this date (to the millisecond)
       then it will be included in the results.
       If the from is later than the to, no results
        will be returned.

    :param order_by: Specifies how the results will be ordered.
    If no value is passed in, it defaults to BY_BET.
    Also acts as a filter such that only orders with
     a valid value in the field being ordered by will
      be returned (i.e. BY_VOID_TIME returns only
      voided orders, BY_SETTLED_TIME (applies to partially
      settled markets) returns only settled orders and
      BY_MATCH_TIME returns only orders with a matched date
      (voided, settled, matched orders)). Note that specifying an
       orderBy parameter defines the context of the date filter
        applied by the dateRange parameter (placed, matched,
        voided or settled date) - see the dateRange parameter
        description (above) for more information.
        See also the OrderBy enum.

    :param sort_dir: Specifies the direction the
    results will be sorted in.
    If no value is passed in, it defaults to EARLIEST_TO_LATEST.
    '''

    market_ids: list = None
    customer_order_refs: list = None
    date_range: TimeRange = None
    order_by: str = None
    sort_dir: str = None

    @property
    def data(self):
        return {
            'betIds': self.bet_ids, 'marketIds': self.market_ids,
            'orderProjection': self.order_projection,
            'customerOrderRefs': self.customer_order_refs,
            'customerStrategyRefs': self.customer_strategy_refs,
            'dateRange': self.date_range, 'orderBy': self.order_by,
            'sortDir': self.sort_dir, 'fromRecord': self.from_record,
            'recordCount': self.record_count
        }
