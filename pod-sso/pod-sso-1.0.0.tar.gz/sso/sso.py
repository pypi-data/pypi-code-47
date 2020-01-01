# coding=utf-8
from __future__ import unicode_literals
import base64
import json
from pod_base import PodBase, ConfigException, PodException
from os import path
from pod_base.request import Request, HTTPException
from Crypto.Hash import SHA256
from Crypto.Signature import PKCS1_v1_5
from Crypto.PublicKey import RSA
from sys import version_info

from .exceptions import SSOException

try:
    from urllib.parse import urlencode
except ImportError:
    from urllib import urlencode

try:
    FileNotFoundError
except NameError:
    FileNotFoundError = IOError


class PodSSO(PodBase):
    PROMPT_LOGIN = "login"
    PROMPT_SIGNUP = "signup"

    TOKEN_HINT_ACCESS_TOKEN = "access_token"
    TOKEN_HINT_REFRESH_TOKEN = "refresh_token"
    TOKEN_HINT_ID_TOKEN = "id_token"

    IDENTITY_TYPE_PHONE = "phone_number"
    IDENTITY_TYPE_EMAIL = "email"

    RESPONSE_TYPE_CODE = "code"
    RESPONSE_TYPE_TOKEN = "token"
    RESPONSE_TYPE_ID = "id"

    REFERRER_TYPE_ID = "id"
    REFERRER_TYPE_USERNAME = "username"
    REFERRER_TYPE_PHONE = "phone_number"
    REFERRER_TYPE_EMAIL = "email"
    REFERRER_TYPE_NATIONAL_CODE = "nationalcode"

    DEVICE_TYPE_MOBILE_PHONE = "Mobile Phone"
    DEVICE_TYPE_DESKTOP = "Desktop"
    DEVICE_TYPE_TABLET = "Tablet"
    DEVICE_TYPE_CONSOLE = "Console"
    DEVICE_TYPE_TV_DEVICE = "TV Device"

    __slots__ = ("_client_id", "_client_secret", "_redirect_url", "__private_key")

    def __init__(self, client_id, client_secret, redirect_url, api_token, token_issuer="1", server_type="sandbox",
                 config_path=None, sc_api_key="", sc_voucher_hash=None):
        here = path.abspath(path.dirname(__file__))
        self._client_id = client_id
        self._client_secret = client_secret
        self._redirect_url = redirect_url
        self._services_file_path = path.join(here, "services.ini")
        super(PodSSO, self).__init__(api_token, token_issuer, server_type, config_path, sc_api_key, sc_voucher_hash,
                                     path.join(here, "json_schema.json"))
        self._request = Request(self.__sso_server())
        self.__private_key = False

    def __sso_server(self):
        sso_server = self._get_config("sso_server")

        if sso_server:
            return sso_server

        raise ConfigException("Can`t find sso_server for {0} mode".format(self._server_type))

    def get_login_url(self, redirect_uri="", scope="", response_type="code", prompt=PROMPT_LOGIN, state="",
                      code_challenge="", code_challenge_method="S256"):
        """
        تولید لینک انتقال کاربر به سرور SSO

        :type redirect_uri: str لینک بازگشت از سرور SSO
        :type scope: str|list لیست اسکوپ های مورد نیاز
        :param response_type: str نحوه دریافت اطلاعات از سرور SSO
        :param prompt: str عملیات مورد نظر (PodSSO.PROMPT_LOGIN یا PodSSO.PROMPT_SIGNUP)
        :param state: str وضعیت
        :param code_challenge: str کد
        :param code_challenge_method: str 	متد رمز نگاری کد
        :rtype: str
        """
        prompt = prompt.lower()
        if prompt != PodSSO.PROMPT_SIGNUP:
            prompt = PodSSO.PROMPT_LOGIN

        params = {
            "client_id": self._client_id,
            "redirect_uri": redirect_uri or self._redirect_url,
            "response_type": response_type,
            "prompt": prompt
        }

        if type(scope) is list and scope:
            params["scope"] = "+".join(scope)
        elif type(scope) is str and scope:
            params["scope"] = scope

        if state:
            params["state"] = state

        if code_challenge and code_challenge_method:
            params["code_challenge"] = code_challenge
            params["code_challenge_method"] = code_challenge_method

        return "{}/oauth2/authorize/?{}".format(self.__sso_server(), urlencode(params)).replace("%2B", "+")

    def call(self, url, method="post", params=None, headers=None):
        try:
            params.update({
                "client_id": self._client_id,
                "client_secret": self._client_secret
            })

            self._request.call(url=url, method=method, params=params, headers=headers)
            return self._request.original_result
        except HTTPException as e:
            if e.status_code:
                err = json.loads(e.raw_result.decode("utf-8"))
                raise SSOException(status_code=e.status_code, error_description=err["error_description"],
                                   error=err["error"])

            raise e

    def get_access_token(self, code, redirect_url="", code_verifier=""):
        """
        دریافت access token از code دریافتی از سرور SSO

        :type code: str کد دریافتی از سرور SSO
        :type redirect_url: str آدرس بازگشت . این آدرس باید دقیقا مانند آدرسی باشد که در پنل کسب و کاری ثبت شده است
        :type code_verifier: str
        :return: dict
        """

        params = {
            "code": code
        }

        if redirect_url is not None:
            params["redirect_uri"] = redirect_url or self._redirect_url

        if code_verifier:
            params["code_verifier"] = code_verifier

        return self.__get_token(params=params)

    def refresh_access_token(self, refresh_token):
        """
        دریافت access token جدید با استفاده از refresh token

        :type refresh_token: str
        :return: dict
        """

        params = {
            "refresh_token": refresh_token,
        }

        return self.__get_token(params=params, grant_type="refresh_token")

    def __get_token(self, params, grant_type="authorization_code"):
        """
        :param params: dict
        :param grant_type: str
        :return: dict
        """
        params.update({
            "grant_type": grant_type
        })

        return self.call("/oauth2/token/", params=params)

    def get_token_info(self, token, token_type_hint=TOKEN_HINT_ACCESS_TOKEN):
        """

        :param token:
        :param token_type_hint:
        :return: dict
        """

        assert not (token_type_hint != PodSSO.TOKEN_HINT_ACCESS_TOKEN and
                    token_type_hint != PodSSO.TOKEN_HINT_REFRESH_TOKEN and
                    token_type_hint != PodSSO.TOKEN_HINT_ID_TOKEN)

        params = {
            "token": token,
            "token_type_hint": token_type_hint
        }

        return self.call("/oauth2/token/info", params=params)

    def revoke_token(self, token, token_type_hint=TOKEN_HINT_ACCESS_TOKEN):
        """
        ابطال توکن

        :param token: str
        :param token_type_hint: str
        :return: bool
        """
        assert not (token_type_hint != PodSSO.TOKEN_HINT_ACCESS_TOKEN and
                    token_type_hint != PodSSO.TOKEN_HINT_REFRESH_TOKEN)

        params = {
            "token": token,
            "token_type_hint": token_type_hint
        }

        self.call("/oauth2/token/revoke", params=params)
        return 300 > self._request._last_response.status_code >= 200

    def handshake(self, device_uid, device_name="", device_lat=None, device_lon=None,
                  device_type=DEVICE_TYPE_MOBILE_PHONE, device_os="", device_os_version=""):
        """
        ثبت دستگاه در پلتفرم پاد

        :param device_uid: str
        :param device_name: str
        :param device_lat: float
        :param device_lon: float
        :param device_type: str
        :param device_os: str
        :param device_os_version: str
        :return: dict
        """

        params = {
            "device_uid": device_uid,
        }
        if device_name:
            params["device_name"] = device_name

        if device_type:
            params["device_type"] = device_type

        if device_os:
            params["device_os"] = device_os

        if device_os_version:
            params["device_os"] = device_os_version

        if device_lat is not None and device_lon is not None:
            params["device_lat"] = float(device_lat)
            params["device_lon"] = float(device_lon)

        self._validate(params, "handshake")

        headers = {
            "Authorization": "Bearer {}".format(self._api_token)
        }

        return self.call("/oauth2/clients/handshake/{}".format(self._client_id), params=params, headers=headers)

    def set_private_key(self, private_key_path):
        """
        تنظیم کردن کلید خصوصی

        :param private_key_path: str مسیر فایل PEM کلید خصوصی
        :raise PodException
        """
        try:
            with open(private_key_path, "r") as private_key:
                self.__private_key = RSA.importKey(private_key.read())

        except FileNotFoundError:
            raise PodException("private key not found")

    def __sign(self):
        """
        :rtype: str
        :raise PodException
        """

        if not self.__private_key:
            raise PodException("Please set Private key path")

        data = b"host: accounts.pod.ir"

        digest = SHA256.new()
        digest.update(data)

        signer = PKCS1_v1_5.new(self.__private_key)
        sig = signer.sign(digest)
        if version_info[0] == 2:
            return str(base64.b64encode(sig))

        return str(base64.b64encode(sig), "utf-8")

    def authorize(self, key_id, identity, identity_type=IDENTITY_TYPE_PHONE, login_as_user_id="", state="",
                  redirect_uri="", callback_uri="", response_type=RESPONSE_TYPE_CODE, scope="", code_challenge="",
                  code_challenge_method="S256", referrer="", referrer_type=REFERRER_TYPE_USERNAME):
        """
        ارسال کد تاییدیه به کاربر برای ورود از طریق OTP

        :param key_id: str  شناسه دستگاه - این مقدار را می توانید از خروجی متد handshake بدست آورید
        :param identity: str شناسه
        :param identity_type: str نوع مقدار شناسه - شماره موبایل یا ایمیل
        :param login_as_user_id: str
        :param state: str
        :param redirect_uri: str
        :param callback_uri: str
        :param response_type: str
        :param scope: str|list
        :param code_challenge: str
        :param code_challenge_method: str
        :param referrer: str
        :param referrer_type: str
        :return: dict
        """

        params = {
            "keyId": key_id,
            "identity": identity,
            "identityType": identity_type,
            "loginAsUserId": login_as_user_id,
            "state": state,
            "redirect_uri": redirect_uri,
            "callback_uri": callback_uri,
            "response_type": response_type,
            "code_challenge": code_challenge,
            "code_challenge_method": code_challenge_method,
            "referrer": referrer,
            "referrerType": referrer_type,
        }

        if type(scope) is list and scope:
            params["scope"] = "+".join(scope)
        elif type(scope) is str and scope:
            params["scope"] = scope

        params = {k: v for k, v in params.items() if v}

        self._validate(params, "authorize")

        signature = self.__sign()
        headers = {
            "Authorization": "Signature keyId={},signature={},headers=host".format(key_id, signature)
        }

        return self.call("/oauth2/otp/authorize/{}".format(identity), params=params, headers=headers)

    def verify_otp(self, key_id, otp, identity):
        """

        :param key_id: str  شناسه دستگاه - این مقدار را می توانید از خروجی متد handshake بدست آورید
        :param otp: str کد دریافتی از کاربر
        :param identity: str شناسه - شماره موبایل یا ایمیل که در مرحله authorize وارد کرده اید
        :return: dict
        """

        params = {
            "otp": otp,
        }
        signature = self.__sign()

        headers = {
            "Authorization": "Signature keyId={},signature={},headers=host".format(key_id, signature)
        }

        return self.call("/oauth2/otp/verify/{}".format(identity), params=params, headers=headers)
