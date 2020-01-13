#!/usr/bin/env python
# coding=utf-8

import json
import logging
import requests
from saasy import __version__

from requests.compat import urljoin

logger = logging.getLogger('root')
logging.root.setLevel(logging.NOTSET)


class Config(object):
    DEFAULT_API_URL = 'https://emails.pixelpassion.io/api/'
    version = 'v0'
    user_agent = 'saasy-python/v' + str(__version__)

    def __init__(self, version=None, api_url=None):
        if version is not None:
            self.version = version
        self.api_url = api_url or self.DEFAULT_API_URL


class Response(object):

    def __init__(self, response):
        if response is not None:
            self.response = response

        self.formatted_request = "{} {}".format(response.request.method, response.request.url)
        self.request = response.request
        self.data = json.loads(response.text)

    @property
    def status_code(self):
        return self.response.status_code


class Client(object):

    def __init__(self, auth_token, **kwargs):
        self.auth_token = auth_token
        self.debug = kwargs.get('debug', False)

        version = kwargs.get('version', None)
        api_url = kwargs.get('api_url', None)

        self.config = Config(version=version, api_url=api_url)

    def _build_url(self, resource):
        url = urljoin(self.config.api_url, self.config.version + '/')
        url += '%s/' % str(resource)
        return url

    def _build_headers(self):
        headers = {
            'Authorization': 'Token %s' % self.auth_token,
            'Content-type': 'application/json',
            'User-agent': self.config.user_agent,
        }

        return headers

    def api_call(self, method, resource, data=None):

        url = self._build_url(resource)
        headers = self._build_headers()

        if headers['Content-type'] == 'application/json':
            data = json.dumps(data)

        req_method = getattr(requests, method)

        try:
            response = req_method(url, data, headers=headers)
            return response
        except requests.exceptions.Timeout:
            raise TimeoutError
        except requests.RequestException as e:
            raise ApiError(e)
        except Exception as e:
            raise

    def parse_response(self, requests_response):

        response = Response(requests_response)

        if self.debug is True:
            logging.debug('%s' % response.formatted_request)
            logging.debug('%s' % response.request.headers)
            logging.debug('%s' % response.request.body)
            logging.debug('%s' % response.status_code)
            logging.debug('%s' % response.data)

        if response.status_code in [200, 201]:
            return response.data
        elif response.status_code in [400, ]:
            raise BadRequestError(response.data["message"])
        elif response.status_code in [500, ]:
            raise UnknownApiError(response.data["message"])
        else:
            logger.debug("Not yet handled API Response")
            return response.data

    def create_mail(self, data):

        response = self.api_call("post", "mails", data)
        return self.parse_response(response)

    def send_mail(self, mail_id):
        response = self.api_call("post", "mails/{}/send".format(mail_id))
        return self.parse_response(response)


class ApiError(Exception):
    pass


class TimeoutError(ApiError):
    pass


class BadRequestError(ApiError):
    pass


class UnknownApiError(ApiError):
    pass