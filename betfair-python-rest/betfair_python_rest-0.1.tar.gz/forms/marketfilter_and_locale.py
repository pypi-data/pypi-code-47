from .abstract_forms.base import BaseForm
from .abstract_forms import MarketFilter, LocaleField
from dataclasses import dataclass


@dataclass
class MarketFilterAndLocaleForm(BaseForm, MarketFilter, LocaleField):
    '''
    Class for combining MarketFilter object and 'locale' field.
    The MarketFilter form used in the Betfair Exchange API
    is quite common and consists of dozens of arguments.
    In this case, it would be a bad idea to copy the arguments
     from method to method along with docstring. Instead of
     copy paste, a separate class was added, in which all the
      attributes of the form will be defined once, then an
      instance of this class will be passed to the input of
      the methods that perform http requests, and there the
      contents of the class will simply be translated into
      a dictionary format and submitted to the request.
    Let's look at an example with the BetFairAPIManager.list_event_types request
    Instead of taking dozens of MarketFilter arguments, the function always
    takes two: market_filter for the BetFairMarketFilter class and locale
    for choosing the response language. So, it should be used like that:
    ___
    market_filter = MarketFilterAndLocaleForm(text_query='Text'. race_types='Chase')
    api_manager = BetFairAPIManagerBetting(login='login', password='password', api_kay='api_key')
    list_event_types_response = api_manager.list_event_types(request_class_object=market_filter)
    ___
    You can find details about params in parent classes
    '''
    @property
    def data(self):
        return {'filter': self.market_filter_data, 'locale': self.locale}
