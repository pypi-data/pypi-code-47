from dataclasses import dataclass
from . import SelectionIdField, LimitOrder, LimitOrderOnClose


@dataclass
class PlaceInstruction(SelectionIdField):
    '''
    Instruction to place a new order
    :param order_type: string, see OrderType enum

    :param handicap: The handicap associated with the
     runner in case of Asian handicap markets (e.g.
      marketTypes ASIAN_HANDICAP_DOUBLE_LINE,
      ASIAN_HANDICAP_SINGLE_LINE) null otherwise.

    :param side: BACK or LAY (see SideChoices enum)

    :param limit_order: LimitOrder class object.
    A simple exchange bet for immediate execution

    :param limit_on_close_order: LimitOrderOnClose class object.
    Bets are matched if, and only if, the returned starting
    price is better than a specified price. In the case
     of back bets, LOC bets are matched if the calculated
     starting price is greater than the specified price.
     In the case of lay bets, LOC bets are matched if
      the starting price is less than the specified price.
       If the specified limit is equal to the starting
        price, then it may be matched, partially matched,
        or may not be matched at all, depending on how
        much is needed to balance all bets against each
        other (MOC, LOC and normal exchange bets)

    :param market_on_close_order_liability: Bets remain unmatched
    until the market is reconciled. They are matched and
     settled at a price that is representative of the
      market at the point the market is turned in-play.
      The market is reconciled to find a starting price
      and MOC bets are settled at whatever starting price
       is returned. MOC bets are always matched and settled,
       unless a starting price is not available for the
       selection. Market on Close bets can only be placed
        before the starting price is determined

    :param customer_order_ref: An optional reference customers
    can set to identify instructions.
     No validation will be done on uniqueness
     and the string is limited to 32 characters. If an empty
      string is provided it will be treated as null.
    '''
    order_type: str
    side: str
    handicap: float = None
    limit_order: LimitOrder = None
    limit_on_close_order: LimitOrderOnClose = None
    market_on_close_order_liability: object = None
    customer_order_ref: str = None

    @property
    def data(self):
        if self.market_on_close_order_liability:
            market_close = {'liability': self.market_on_close_order_liability}
        else:
            market_close = None
        return {
            'orderType': self.order_type,
            'selectionId': self.selection_id,
            'handicap': self.handicap,
            'side': self.side,
            'limitOrder': self.limit_order.data if self.limit_order else None,
            'limitOnCloseOrder': self.limit_on_close_order.data if self.limit_on_close_order else None,
            'marketOnCloseOrder': market_close,
            'customerOrderRef': self.customer_order_ref,
        }
