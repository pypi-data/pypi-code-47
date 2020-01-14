from dataclasses import dataclass
from .fields import CustomerStrategyRefsField


@dataclass
class CustomerRefs(CustomerStrategyRefsField):
    '''
    The TimeRange can be useful in listClearedOrders request.
    Let's look at an example of using:
    ___
    time_range_obj = TimeRange(from_date='YOUR_DATETIME', to_date-'YOUR_DATETIME')
    api_manager = BetFairAPIManagerBetting(login='login', password='password', api_kay='api_key')
    list_current_orders_response = api_manager.list_current_orders(time_range=time_range_obj)
    ___
    List of params:
    :param customer_order_refs: Optionally restricts the results
    to the specified customer order references.

    '''
    customer_order_refs: list = None
