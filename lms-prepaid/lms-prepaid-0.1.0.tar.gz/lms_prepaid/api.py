import requests

APP_API_ENDPOINT='https://evc-net.com/api/app'
DEFAULT_DEVICE_ID='1233456789'
DEFAULT_APPVERSION='4.1.2'

class InvalidRequest(Exception):
    pass

class InvalidCreditResponse(Exception):
    pass

class LmsCredit(object):
    amount = 0
    currency = None

    def __init__(self, amount, currency):
        self.amount = float(amount)
        self.currency = currency

class LmsApi(object):
    def __init__(self, card_id, device_id = DEFAULT_DEVICE_ID, app_version = DEFAULT_APPVERSION):
        self._card_id = card_id
        self._device_id = device_id
        self._app_version = app_version
        self._card_registration_code = None # What is this? How to use
        self._dump_responses = False

    def set_dump_responses(self, dump):
        self._dump_responses = dump

    def _post_action(self, action, additional_parameters = None):
        parameters = {
            'deviceId': self._device_id,
            'version': self._app_version,
            'cardRegistrationCode': self._card_registration_code,
            'cardExternalId': self._card_id,
        }
        if additional_parameters:
            for key, value in additional_parameters:
                parameters[key] = value
        data = requests.post(APP_API_ENDPOINT, json={
                    'action': action,
                    'parameters': parameters
               }).json()
        if (self._dump_responses):
            print(data)
        if data['status'] == 'invalidRequest':
            raise InvalidRequest()
        return data

    def get_credit(self):
        data = self._post_action('getCredit')
        if not 'amount' in data or not 'currency' in data:
            raise InvalidCreditResponse()
        return LmsCredit(data['amount'], data['currency'])
