from dataclasses import dataclass


@dataclass
class OrderProjectionField:
    '''
    Optionally restricts the results to the specified order
     status. Allowed variables listed in OrderProjection enum.

    List of params:
    :param order_projection:  Optionally restricts the results to the specified order

    '''
    order_projection: str = None
