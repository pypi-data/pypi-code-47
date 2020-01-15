from dataclasses import dataclass
from datetime import datetime


@dataclass
class EventAndEventTypeIds:
    '''
    The TimeRange can be useful in listClearedOrders request.
    Let's look at an example of using:
    ___
    time_range_obj = TimeRange(from_date='YOUR_DATETIME', to_date-'YOUR_DATETIME')
    api_manager = BetFairAPIManagerBetting(login='login', password='password', api_kay='api_key')
    list_current_orders_response = api_manager.list_current_orders(time_range=time_range_obj)
    ___
    :param event_type_ids: list of strings, Restrict markets by event type associated
        with the market. (i.e., Football, Hockey, etc)

    :param event_ids: list of strings, Restrict markets by the event id associated
         with the market.
    '''
    event_type_ids: list = None
    event_ids: list = None
