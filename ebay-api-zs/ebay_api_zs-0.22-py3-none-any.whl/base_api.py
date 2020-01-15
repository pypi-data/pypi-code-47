import os
import json
import logging
from abc import ABC, abstractmethod

import requests
from .data import MarketplaceToLang

LOGFILE = os.path.join(
    os.path.dirname(os.path.dirname(__file__)),
    'log.txt'
)


logging.basicConfig(
    level=logging.DEBUG,
    filename=LOGFILE,
    format="%(asctime)s: %(levelname)s - %(funcName)s: %(message)s",
    filemode='w'
)


class EbayAPIError(Exception):
    pass


class EbayAPI(ABC):
    required_path_params = []
    required_query_params = []
    allowed_query_params = []

    def __init__(self, access_token: str, sandbox: bool, marketplace_id=None, response_timeout=42, silent: bool = True):
        self.access_token = access_token
        self.sandbox = sandbox
        self.marketplace_id = marketplace_id
        self.response_timeout = response_timeout
        self.silent = silent

    @property
    def lang(self):
        return MarketplaceToLang.get(self.marketplace_id, MarketplaceToLang['default'])

    @property
    def api_location_domain(self):
        return 'api'

    @property
    def api_location(self):
        if self.sandbox:
            return f"https://{self.api_location_domain}.sandbox.ebay.com"
        else:
            return f"https://{self.api_location_domain}.ebay.com"

    @property
    @abstractmethod
    def api_type_name(self):
        pass

    @property
    @abstractmethod
    def api_name(self):
        pass

    @property
    def api_version(self):
        return 'v1'

    @property
    @abstractmethod
    def method_type(self):
        '''
        eBay Inventory API call method (POST/GET/PUT/DELETE)
        '''
        pass

    @property
    @abstractmethod
    def resource(self):
        '''
        eBay Inventory API resource
        (location / inventory_item / inventory_item_group /
         offer / product_compatibility / listing)
        '''
        pass

    @property
    def url_path(self):
        return '/'.join(list(self.path_params.values()))

    @property
    def url_postfix(self):
        pass

    def build_url(self):
        '''
        Build eBay Inventory API URL
        '''
        return '/'.join(
            part for part in [
                self.api_location,
                self.api_type_name,
                self.api_name,
                self.api_version,
                self.resource,
                self.url_path,
                self.url_postfix,
            ]
            if part
        )

    @property
    def headers(self):
        '''
        eBay Inventory API headers
        '''
        return {
            'Authorization': f'Bearer {self.access_token}',
            'Content-Language': self.lang,
            'Content-Type': 'application/json',
            'Accept-Language': 'ru-RU',
            'Accept': 'application/json',
            'Accept-Charset': 'utf-8',
            'Accept-Encoding': 'application/gzip',
            'X-EBAY-C-MARKETPLACE-ID': self.marketplace_id,
        }

    def get_clean_path_params(self, params: dict):
        for req_param in self.required_path_params:
            if (req_param not in params) or (not params[req_param]):
                raise AttributeError(f"Обязательный параметр запроса '{req_param}' не задан.")

        for path_param in params:
            if path_param not in self.required_path_params:
                raise AttributeError(f"Задан лишний параметр запроса ({path_param}={params[path_param]}).")

        return params

    def get_clean_query_params(self, params: dict):
        for req_param in self.required_query_params:
            if req_param not in params:
                raise AttributeError(f"Обязательный параметр запроса '{req_param}' не задан.")

        for param, value in list(params.items()):
            if (not value) or (param not in self.allowed_query_params + self.required_query_params):
                logging.warning(f'Недопустимый параметр запроса {param}={value} не используется.')
                params.pop(param)
                continue

            clean_method = getattr(self, f'clean_{param}', None)
            if clean_method:
		if isinstance(value, str):
		    value = value.strip()
                param_is_valid, value, err_message = clean_method(value)
                if not param_is_valid:
                    message = f'Недопустимое значение параметра запроса ({param}={value}).\n{err_message}'
                    logging.error(message)
                    raise EbayAPIError(message)

        return params

    def make_request(self, payload=None, path_params={}, query_params={}, next_url=None):
        '''
        eBay Inventory API call
        '''
        self.payload = payload
        self.path_params = self.get_clean_path_params(path_params)
        self.query_params = self.get_clean_query_params(query_params)

        if next_url:
            self.url = self.api_location + next_url
            self.query_params = None
        else:
            self.url = self.build_url()

        is_success = False
        message = ''
        objects = {}
        response = None
        try:
            response = requests.request(
                method=self.method_type,
                url=self.url,
                params=self.query_params,
                headers=self.headers,
                data=self.payload,
                timeout=self.response_timeout,
            )
        except requests.exceptions.Timeout:
            message = f'TimeoutError (response timeout > {self.response_timeout})'
        except requests.exceptions.RequestException as err:
            message = str(err)
        else:
            is_success, message, objects = self.response_handler(response)

        if not self.silent:
            if is_success:
                logging.info(message)
            else:
                logging.error(message)

        return is_success, message, objects

    def response_handler(self, response):
        '''
        Message for API call response
        '''
        try:
            if not str(response.status_code).startswith('2'):
                response.raise_for_status()
        except requests.HTTPError:
            is_success = False
            message, objects = self.error_handler(response)
        else:
            is_success = True
            message, objects = self.success_handler(response)

        objects['response'] = response

        return is_success, message, objects

    def get_success_message(self):
        return "Запрос успешно выполнен.\n"

    def get_error_message(self):
        return "Ошибка при выполнении запроса.\n"

    def success_handler(self, response):
        message = self.get_success_message()
        try:
            objects = {
                'results': response.json(),
            }
        except json.decoder.JSONDecodeError:
            objects = {}

        return message, objects

    def error_handler(self, response):
        message = self.get_error_message()
        try:
            objects = response.json()
        except json.decoder.JSONDecodeError:
            objects = {}
        else:
            for error_num, error in enumerate(objects.get('errors', [])):
                if error.get('category', ''):
                    message += f"\n{error_num+1}) " + error.get('longMessage', error.get('message', ''))

                    params = error.get('parameters', [])
                    if params:
                        objects['params'] = params
        return message, objects

    @staticmethod
    def _clean_int(name, value, min_num, max_num):
        is_valid = True
        message = ''
        try:
            value = int(value)
        except ValueError:
            message = f'Параметр {name} должен быть целым числом.'
        if not (min_num <= value <= max_num):
            message = f'Параметр {name} должен быть в диапазоне [{min_num}:{max_num}].'
            message += f'\nЗначение параметра: {value}.'
        if message:
            is_valid = False
        return is_valid, value, message

    def clean_offset(self, offset, min_num=0, max_num=99):
        return self._clean_int('offset', offset, min_num, max_num)

    def clean_limit(self, limit, min_num=1, max_num=100):
        return self._clean_int('limit', limit, min_num, max_num)
