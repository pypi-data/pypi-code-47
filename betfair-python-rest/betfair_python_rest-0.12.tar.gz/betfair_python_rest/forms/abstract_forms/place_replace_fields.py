from dataclasses import dataclass
from . import MarketIdField, CustomerRefField


@dataclass
class PlaceAndReplaceOrdersFields(CustomerRefField, MarketIdField):
    '''
    :param is_async: An optional flag (not setting equates to false)
     which specifies if the orders should be placed asynchronously.
     Orders can be tracked via the Exchange Stream API or or the API-NG
     by providing a customerOrderRef for each place order.
     An order's status will be PENDING and no bet ID will be returned.
     This functionality is available for all bet types -
     including Market on Close and Limit on Close

    :param customer_ref: Optional parameter allowing the client
    to pass a unique string (up to 32 chars) that is
     used to de-dupe mistaken re-submissions.
     CustomerRef can contain: upper/lower chars, digits,
      chars : - . _ + * : ; ~ only.
      Please note: There is a time window associated
      with the de-duplication of duplicate
      submissions which is 60 seconds.

    :param market_version: Optional parameter allowing the
     client to specify which version of the market the
    orders should be placed on. If the current market
    version is higher than that sent on an order,
    the bet will be lapsed.
    '''
    is_async: bool = None
    customer_ref: str = None
    market_version: str = None
