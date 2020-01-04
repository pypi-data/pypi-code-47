from platform import platform
import time
from urllib.parse import urlencode
import requests
import hashlib 
import hmac
import binascii

class KittyWait(Exception):
    pass

class KittyCap:
    module_name = 'KC'
    module_version = '1.1.7'
    module_http_header = {}
    base_url = 'https://api.kittycore.xyz/api/v1/kittycore/cap'

    def __init__(self, username, api_key):
        self.is_authenticated = False
        self.api_key = api_key
        self.api_username = username
        self.module_http_header['User-Agent'] = f'{KittyCap.module_name}/{KittyCap.module_version} ({platform()};)'

        check_login = self.__authenticate(username)
        if check_login['status']:
            self.is_authenticated = True
        else:
            self.error = {}
            self.error['message'] = check_login['message']
            self.error['code'] = check_login['code']

    def credit(self):
        response = self.__request('/credit')
        if response['status']:
            return response['data']['credit']
        else:
            raise Exception(response['message'])

    def recaptcha2(self, sitekey, url):
        response = self.__request(
            '/recaptcha2/request', 
            'post', 
            {
                'sitekey': sitekey,
                'url': url
            }
        )
        if response['status']:
            return response['data']['ticket_id']
        else:
            raise Exception(response['message'])


    def get_ticket_response(self, ticket_id):
        response = self.__request(
            '/ticket/info', 
            'post', 
            {'ticket_id': ticket_id}
        )
        if response['status']:
            return response['data']['key']
        elif response['code'] == 405:
            raise KittyWait()
        else:
            raise Exception(response['message'])

    def __authenticate(self, username):
        response = self.__request('/authenticate', 'post')
        return response

    def __request(self, endpoint, method='get', data={}):

        # Data
        data.update({
            'generated_at' : int(time.time())
        })
        data_query_string = urlencode(data)

        # Headers
        headers = {}
        headers['Username'] = self.api_username
        try:
            headers['Authorization'] = self.__sign_message(data_query_string, self.api_key)
        except:
            return {'status': False, 'code': 601, 'message': 'api key is malformed.'}
        
        headers.update(KittyCap.module_http_header) # Add module http header

        request_url = f'{KittyCap.base_url}{endpoint}'

        if method.lower() == 'get':
            response = requests.get(f'{request_url}?{data_query_string}', headers=headers)
        elif method.lower() == 'post':
            response = requests.post(request_url, data=data, headers=headers)
        
        if response.status_code == 481 or response.status_code == 403:
            return {'status': False, 'code': 481, 'message': 'FireEye Protection blocked your request, if you using any VPN, disconnect and try again.'}
    
        try:
            return response.json()
        except:
            return {'status': False, 'code': 600, 'message': 'connection error.'}

    def __sign_message(self, message, key):
        byte_key = binascii.unhexlify(key)
        message = message.encode()
        return hmac.new(byte_key, message, hashlib.sha256).hexdigest().upper()
