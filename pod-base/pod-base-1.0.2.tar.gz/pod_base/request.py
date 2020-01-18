# coding=utf-8
import json
import requests

from .exceptions import *


class Request(object):
    __slots__ = ("headers", "_last_response", "_result", "last_ott", "error_code", "original_result", "_total_items",
                 "base_url", "_reference_number")

    def __init__(self, base_url, *arg, **kwargs):
        self.headers = {
            "Content-Type": "application/x-www-form-urlencoded"
        }
        self._last_response = None
        self._result = ""
        self.last_ott = ""
        self.error_code = 0
        self.original_result = {}
        self._total_items = 0
        self._reference_number = ""
        self.base_url = base_url

    @staticmethod
    def _prepare_params(params=None):
        if params is None or type(params) is not dict:
            params = {}

        return params

    def _prepare_headers(self, headers=None):
        if headers is not None and type(headers) is dict:
            self.headers.update(headers)

        return self.headers

    def call(self, url, method="post", params=None, headers=None):
        url = self.base_url + url
        params = self._prepare_params(params)
        headers = self._prepare_headers(headers)

        try:
            method = method.lower()
            if method == "post":
                self._last_response = requests.post(url, data=params, headers=headers)
            elif method == "put":
                self._last_response = requests.put(url, data=params, headers=headers)
            elif method == "delete":
                self._last_response = requests.delete(url, headers=headers)
            else:
                self._last_response = requests.get(url, params=params, headers=headers)

            return self._parse_response()

        except requests.exceptions.RequestException as e:
            raise HTTPException(e)

    def _parse_response(self):
        if 300 >= self._last_response.status_code < 200:
            raise HTTPException(message="خطا در فراخوانی API", status_code=self._last_response.status_code,
                                raw_result=self._last_response.content)

        content = self._last_response.content
        if content:
            self.original_result = json.loads(content.decode("utf-8"))
        else:
            self.original_result = ""
        self._set_last_ott()
        self._set_reference_number()
        self._set_total_items()
        self._check_error()
        if "result" in self.original_result:
            self._result = self.original_result["result"]
        else:
            self._result = ""

        return self._result

    def _set_reference_number(self):
        if "referenceNumber" in self.original_result:
            self._reference_number = self.original_result["referenceNumber"]
        else:
            _reference_number = None

    def _check_error(self):
        if "hasError" not in self.original_result or not self.original_result["hasError"]:
            return

        if "errorCode" in self.original_result:
            self.error_code = self.original_result["errorCode"]
        else:
            self.error_code = 0

        if self.error_code == 0:
            return

        if "message" in self.original_result:
            message = self.original_result["message"]
        else:
            message = "error in call api"

        raise APIException(message, reference_number=self._reference_number, error_code=self.error_code)

    def _set_total_items(self):
        if "count" in self.original_result:
            self._total_items = int(self.original_result["count"])
        else:
            self._total_items = 0

    def _set_last_ott(self):
        if "ott" in self.original_result:
            self.last_ott = self.original_result["ott"]
        elif "Ott" in self.original_result:
            self.last_ott = self.original_result["Ott"]
        else:
            self.last_ott = ""

    def last_response(self):
        """
        جواب خام دریافتی از پلتفرم

        :return: :class:`Response <Response>` object
        :rtype: requests.Response
        """
        return self._last_response

    def result(self):
        return self._result

    def total_items(self):
        """
        تعداد کل نتایج

        :return: int
        """
        return self._total_items
