import json
from abc import abstractmethod
from .base_api_manager import BaseAPIManager


class BetFairAPIManagerAccounts(BaseAPIManager):
    '''
    The class provides the functional of Betfair Exchange API, described by company on link below:
    https://docs.developer.betfair.com/
    '''

    root = 'https://api.betfair.{}/exchange/account/rest/v1.0'

    def create_developer_app_keys(self, app_name):
        '''
        Create 2 Application Keys for given user; one 'Delayed and
        the other 'Live'. You must apply to have
         your 'Live' App Key activated.

         :param app_name: A Display name for the application.
        '''
        return self._make_request('createDeveloperAppKeys', data={'appName': app_name})

    def get_developer_app_keys(self):
        '''
        Get all application keys owned by the given developer/vendor
        '''
        return self._make_request('getDeveloperAppKeys')

    def get_account_funds(self, wallet=None):
        '''
        Returns the available to bet amount, exposure
         and commission information.

        :param wallet: Name of the wallet in question.
        Global wallet is returned by default
        '''
        response = self._make_request('getAccountFunds', data={'wallet': wallet})
        return response

    def transfer_funds(self):
        '''
        Transfer funds between the UK Exchange and other wallets.
        '''
        raise Exception('This operatio is currently deprecated '
                        'due to the removal of the AUS wallet')

    def get_account_details(self):
        '''
        Returns the details relating your account,
        including your discount rate and Betfair
         point balance.
        '''

        response = self._make_request('getAccountDetails')
        return response

    def get_account_statement(self, locale=None, from_record=None, record_count=None,
                              item_data_range_from=None, item_data_range_to=None,
                              include_item=None, wallet=None):
        '''
        Please see the Additional Information for details of how
        getAccountStatement output is affected in
         the event of market resettlement.

        :param locale: The language to be used where applicable.
        If not specified, the customer account default is returned.

        :param from_record: Specifies the first record that will be returned.
        Records start at index zero. If not specified then it will default to 0.
        :param record_count: Specifies the maximum number of records to
        be returned. Note that there is a page size limit of 100.
        :param item_data_range_from:
        :param item_data_range_to:
        Return items with an itemDate within this date range,
        between item_data_range_from and item_data_range_to.
        Both from and to date times are inclusive. If from is not specified
        then the oldest available items will be in range.
        If to is not specified then the latest items will be in range.
        Range is currently only applied when include_item
        is set to ALL or not specified, else items are NOT bound.

        :param include_item: Which items to include, if not specified then defaults to ALL.
        :param wallet: Which wallet to return statementItems for.
        If unspecified then the UK wallet will be selected

        '''
        response = self._make_request('getAccountStatement',
                                      data={'locale': locale, 'fromRecord': from_record,
                                            'recordCount': record_count,
                                            'itemDateRange': {
                                                'from': item_data_range_from,
                                                'to': item_data_range_to
                                            },
                                            'includeItem': include_item, 'wallet': wallet})
        return response

    def list_currency_rates(self, from_currency=None):
        '''
        Returns a list of currency rates based on given currency.
        Please note: the currency rates are updated once every
         hour a few seconds after the hour.

         :param from_currency: The currency from which the rates
         are computed. Please note: GBP is currently the
         only based currency support
        '''
        response = self._make_request('getAccountDetails', data={'fromCurrency': from_currency})
        return response
