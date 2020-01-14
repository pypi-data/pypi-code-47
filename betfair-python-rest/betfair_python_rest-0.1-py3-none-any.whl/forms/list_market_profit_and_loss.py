from .abstract_forms.base import BaseForm
from .abstract_forms import MarketIdsField
from dataclasses import dataclass


@dataclass
class ListMarketProfitAndLossForm(BaseForm, MarketIdsField):
    '''
    Class for request method listMarketProfitAndLoss
    It should be used like that:
    ___
    request_class_object = ListMarketProfitAndLossForm(**your_data)
    api_manager = BetFairAPIManagerBetting(login='login', password='password', api_kay='api_key')
    list_event_types_response = api_manager.list_market_profit_and_loss(request_class_object=request_class_object)
    ___
    You can find details about params in parent classes

    :param include_settle_bets: Option to include settled
     bets (partially settled markets only). Defaults
      to false if not specified.

    :param include_bsp_bets: Option to include BSP bets.
    Defaults to false if not specified.

    :param net_of_commission: Option to return profit
    and loss net of users current commission rate
    for this market including any special tariffs.
    Defaults to false if not specified.
    '''
    include_settle_bets: bool = None
    include_bsp_bets: bool = None
    net_of_commission: bool = None

    @property
    def data(self):
        return {'marketIds': self.market_ids,
                'includeSettledBets': self.include_settle_bets,
                'includeBspBets': self.include_bsp_bets,
                'netOfCommission': self.net_of_commission
                }
