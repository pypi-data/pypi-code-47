from dataclasses import dataclass
from .ex_best_offers_overrides import ExBestOffersOverrides


@dataclass
class PriceProjection(ExBestOffersOverrides):
    '''
    The TimeRange can be useful in listClearedOrders request.
    Let's look at an example of using:
    ___
    time_range_obj = TimeRange(from_date='YOUR_DATETIME', to_date-'YOUR_DATETIME')
    api_manager = BetFairAPIManagerBetting(login='login', password='password', api_kay='api_key')
    list_current_orders_response = api_manager.list_current_orders(time_range=time_range_obj)
    ___
    List of params:
    :param price_data: The basic price data you want to receive in the response.

    :param virtualise: Indicates if the returned prices should include
    virtual prices. Applicable to EX_BEST_OFFERS and EX_ALL_OFFERS
    priceData selections, default value is false.
    Please note: This must be set to 'true' replicate
     the display of prices on the Betfair Exchange website.

    :param rollover_stakes: Indicates if the volume returned at
     each price point should be the absolute value or a cumulative
     sum of volumes available at the price and all better prices.
     If unspecified defaults to false. Applicable to EX_BEST_OFFERS
      and EX_ALL_OFFERS price projections. Not supported as yet.
    '''
    price_data: list = None
    ex_best_offers_overrides: ExBestOffersOverrides = None
    virtualise: bool = None
    rollover_stakes: bool = None

    @property
    def price_projection_data(self):
        return {
            'priceData': self.price_data,
            'exBestOffersOverrides': self.ex_best_offers_overrides_data,
            'virtualise': self.virtualise,
            'rolloverStakes': self.rollover_stakes,
        }
