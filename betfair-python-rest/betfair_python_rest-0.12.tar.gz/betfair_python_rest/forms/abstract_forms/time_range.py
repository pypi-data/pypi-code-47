from dataclasses import dataclass
from datetime import datetime


@dataclass
class TimeRange:
    '''
    The TimeRange can be useful in listClearedOrders request.
    Let's look at an example of using:
    ___
    time_range_obj = TimeRange(from_date='YOUR_DATETIME', to_date-'YOUR_DATETIME')
    api_manager = BetFairAPIManagerBetting(login='login', password='password', api_kay='api_key')
    list_current_orders_response = api_manager.list_current_orders(time_range=time_range_obj)
    ___
    '''
    from_date: datetime.date
    to_date: datetime.date

    @property
    def time_range_data(self):
        return {
            'from': self.from_date,
            'to': self.to_date
        }
