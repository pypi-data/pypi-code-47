"""
Module Python fot Secursus Api
"""

import json
import httpx


class Consts:
    """The class Constants"""
    BASE_URL = 'https://developer.secursus.com/api/'
    ERROR_URI_FIELD_FORMAT = 'Your Api URI must be an string.'
    ERROR_PARAMS_FIELD_FORMAT = 'Your Api parameters must be an dictionary.'
    ERROR_METHOD_FIELD_FORMAT = 'Only methods allowed is "GET", "POST" or "DELETE" for the Api request.'
    ERROR_ID_FIELD_FORMAT = 'Your parcels id must be a string.'
    ERROR_DATA_FIELD_FORMAT = 'Your arguments data must be an dictionary.'
    ERROR_AMOUNT_FIELD_FORMAT = 'Your parcels value must be a integer.'
    ERROR_UNKNOW_API_ID_FIELD_FORMAT = 'The Api ID is required.'
    ERROR_UNKNOW_API_KEY_FIELD_FORMAT = 'The Api Key is required.'
    AVAILABLE_METHOD = ['GET', 'POST', 'DELETE']


class Api:
    """The class api"""

    def __init__(self, api_id='', api_key=''):
        """Api constructor"""
        if not isinstance(api_id, str):
            raise Exception(Consts.ERROR_UNKNOW_API_ID_FIELD_FORMAT)

        if not isinstance(api_key, str):
            raise Exception(Consts.ERROR_UNKNOW_API_KEY_FIELD_FORMAT)

        self.api_id = api_id
        self.api_key = api_key

        self.check_authentification()

    def cancel_parcel_order(self, id_parcel):
        """Cancel parcel order"""
        if not isinstance(id_parcel, str):
            raise Exception(Consts.ERROR_ID_FIELD_FORMAT)

        return self.send_request('parcels/' + id_parcel + '/delete', {}, 'DELETE')

    def create_parcel_order(self, data):
        """Create parcel order"""
        if not isinstance(data, dict):
            raise Exception(Consts.ERROR_DATA_FIELD_FORMAT)

        return self.send_request('parcels/new', data, 'POST')

    def get_insurance_amount(self, amount):
        """Get the insurance Amount"""
        if not isinstance(amount, int):
            raise Exception(Consts.ERROR_AMOUNT_FIELD_FORMAT)

        return self.send_request('parcels/price', {'parcel_value': amount}, 'POST')

    def retrieve_parcel_order(self, id_parcel):
        """Retrieve parcel order details"""
        if not isinstance(id_parcel, str):
            raise Exception(Consts.ERROR_ID_FIELD_FORMAT)

        return self.send_request('parcels/' + id_parcel, {}, 'GET')

    def retrieve_current_report(self):
        """Retrieve Current report"""
        return self.send_request('parcels', {}, 'GET')

    def retrieve_history_report(self):
        """Retrieve History report"""
        return self.send_request('parcels/all', {}, 'GET')

    def send_request(self, uri, params={}, method='GET'):
        """Send request to Api"""
        if not isinstance(uri, str):
            raise Exception(Consts.ERROR_URI_FIELD_FORMAT)

        if not isinstance(params, dict):
            raise Exception(Consts.ERROR_PARAMS_FIELD_FORMAT)

        if not isinstance(method, str) or method not in Consts.AVAILABLE_METHOD:
            raise Exception(Consts.ERROR_METHOD_FIELD_FORMAT)

        client = httpx.Client(
            auth=(self.api_id, self.api_key),
            base_url=Consts.BASE_URL,
            headers={
                'Accept': 'application/json',
                'Content-type': 'application/json',
            }
        )
        response = client.request(method, uri, data=json.dumps(params))

        body = json.loads(response.read().decode())
        if body['response']['success']:
            return body

        raise Exception(body['response']['detail'])

    def check_authentification(self):
        """Check Api authentification"""
        return self.send_request('auth')
