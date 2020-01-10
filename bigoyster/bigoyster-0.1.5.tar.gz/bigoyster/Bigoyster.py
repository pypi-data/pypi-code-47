import requests
import logging
import json
import random
import string

_logger = logging.getLogger(__name__)


class Bigoyster:
    token = False
    username = False
    password = False
    base_url = False

    def __init__(self, base_url='https://api.bigoyster.com/', token=False, username=False, password=False):
        self.base_url = base_url
        self.username = username
        self.password = password

        if token:
            self.token = token
        else:
            self.token = self.get_token(username, password)

    def get_token(self, username, password):
        url = self.base_url + "api-token-auth/"

        payload = {
            "username": username,
            "password": password
        }
        response = requests.post(url, json=payload)
        if response.status_code == 200:
            return json.loads(response.text)['token']
        else:
            print('GET TOKEN FAILED')
            return False

    def get_headers(self):
        headers = {
            'Authorization': "Token " + self.token,
        }
        return headers

    def call_create_api(self, object, values):
        baseurl = self.base_url
        url = baseurl + object + '/create/'

        response = requests.post(url, json=values, headers=self.get_headers(), timeout=5)
        print(response.elapsed)
        if response.status_code == 201:
            result = json.loads(response.text)
            return True, result
        elif response.status_code == 401:
            print('NOT AUTHORIZED')
            if self.get_token(username=self.username, password=self.password):
                print('RETRY')
                return self.call_create_api(object, values)
        elif response.status_code >= 400:
            print('400s BAD REQUEST')
            print(response.text)

        else:
            print('UNHANDLED STATUS CODE')
            print(response.text)
        return False, response

    def call_action_api(self, object, action, values):
        baseurl = self.base_url
        url = baseurl + object + '/' + action + '/'

        response = requests.post(url, json=values, headers=self.get_headers(), timeout=5)
        print(response.elapsed)
        if response.status_code == 200:
            result = json.loads(response.text)
            return True, result
        elif response.status_code == 401:
            print('NOT AUTHORIZED')
            if self.get_token(username=self.username, password=self.password):
                print('RETRY')
                return self.call_action_api(object, action, values)
        elif response.status_code >= 400:
            print('400s BAD REQUEST')
            print(response.text)

        else:
            print('UNHANDLED STATUS CODE')
            print(response.text)
        return False, response

    def call_get_api(self, object, params):
        baseurl = self.base_url
        url = baseurl + object + '/get/'

        response = requests.get(url, params=params, headers=self.get_headers(), timeout=5)
        print(response.elapsed)
        if response.status_code == 200:
            result = json.loads(response.text)
            return result
        elif response.status_code == 401:
            print('NOT AUTHORIZED')
            if self.get_token(username=self.username, password=self.password):
                print('RETRY')
                return self.call_get_api(object, params)
        elif response.status_code == 404:
            print('NOT FOUND')
            return False
        elif response.status_code >= 400:
            print('400s BAD REQUEST')

        else:
            print('UNHANDLED STATUS CODE')
        return response

    def call_list_api(self, object, params):
        baseurl = self.base_url
        url = baseurl + object + '/list/'

        response = requests.get(url, params=params, headers=self.get_headers(), timeout=5)
        print(response.elapsed)
        if response.status_code == 200:
            result = json.loads(response.text)
            return result
        elif response.status_code == 401:
            print('NOT AUTHORIZED')
            if self.get_token(username=self.username, password=self.password):
                print('RETRY')
                return self.call_get_api(object, params)
        elif response.status_code == 404:
            print('NOT FOUND')
            return False
        elif response.status_code >= 400:
            print('400s BAD REQUEST')

        else:
            print('UNHANDLED STATUS CODE')
        return response

    # HELPER FUNCTIONS BELOW
    def get_consumer_by_phone(self, device_id, phone):
        return self.call_get_api('consumer', {'phone': phone, 'device_id': device_id})

    def get_consumer_coupons(self, device_id, consumer_id, upcs='', qtys='', prices='', txn_line_refs=''):
        """
        Get all consumer coupons with optional parameters
        :param consumer_id: UUID
        :param upcs: comma separated string
        :param qtys: comma separated string
        :param prices: comma separated string
        :param txn_line_refs: comma separated string
        :return:
        """
        auth_code = ''.join(random.choices(string.ascii_letters + string.digits, k=16))
        params = {
            "consumer": consumer_id,
            "status": "active",
            "upcs": upcs,
            "qtys": qtys,
            "prices": prices,
            "txn_line_refs": txn_line_refs,
            'auth_code': auth_code,
            'device_id': device_id
        }
        # result = self.call_list_api('coupon', params=params)
        success, result = self.call_action_api('coupon', 'auth', params)
        return result

    def create_consumer(self, device_id, phone):
        # add to petzmobile
        success, result = self.call_create_api('consumer', {'phone': phone, 'device_id': device_id})
        if success:
            return result
        else:
            return {'success': False, 'addl_info': result.text}

    def capture_coupons(self, device_id, consumer_id, auth_code):
        values = {
            'event_type': 'POS003',
            'device': device_id,
            'consumer': consumer_id,
            'addl_info': {'auth_code': auth_code}
        }
        success, result = self.call_create_api('event', values)

        success = result.get('is_valid')
        todays_savings = '${:,.2f}'.format(result.get('todays_savings'))
        total_savings = '${:,.2f}'.format(result.get('total_savings'))
        receipt_lines = []
        # receipt_lines.append("Today's savings: %s " % todays_savings)
        receipt_lines.append("Petzmobile Lifetime Savings: %s" % total_savings)
        return {'success': success.lower() == 'true', 'receipt_lines': receipt_lines}

    def get_campaign_upcs(self, device_id):
        params = {
            "view": "criteria",
            "status": "active"
        }
        result = self.call_list_api('campaign', params=params).get('results')
        upcs = []
        for c in result:
            for upc in c.get('criteria', {}).get('valid_products', []):
                if upc not in upcs:
                    upcs.append(upc)
        return upcs

    def create_retail_coupon(self, device_id, valid_start, valid_end, marketing, criteria):
        """
        create_retail_coupon(device_id, valid_start, valid_end, marketing, criteria)
        marketing = {
         'headline': 'headline text',
         'description': 'Description text',
         'categories': ['cat', 'dog']
        }
        criteria = {
            '"per_customer_limit"': 1
        }
        :param device_id:
        :param valid_start
        :param valid_end
        :param marketing:
        :param criteria:
        :return:
        """
        return {'success': 'True'}

    def refund_coupon(self, device_id, coupon_id, qty, amount):
        values = {
            'event_type': 'CPN005',
            'device': device_id,
            'coupon': coupon_id,
            'addl_info': {'qty': qty, 'amount': amount}
        }
        success, result = self.call_create_api('event', values)
        return {'success': success}

    def create_retail_settlement(self, device_id):
        return {'success': 'True'}

    def get_pos_device(self, device_type, device_ref, friendly_name=''):
        if not friendly_name:
            friendly_name = device_ref
        values = {
            'name': friendly_name,
            'pos_ref': device_ref,
            'device_type': device_type
        }
        success, result = self.call_action_api('device', 'get', values=values)
        if success:
            return result
        else:
            return {'success': False, 'addl_info': result.text}

