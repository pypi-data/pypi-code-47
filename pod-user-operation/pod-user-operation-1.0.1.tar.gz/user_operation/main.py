# coding=utf-8
from os import path
from pod_base import PodBase, calc_offset


class PodUserOperation(PodBase):

    def __init__(self, api_token, token_issuer="1", server_type="sandbox", config_path=None,
                 sc_api_key="", sc_voucher_hash=None):
        here = path.abspath(path.dirname(__file__))
        self._services_file_path = path.join(here, "services.ini")
        super(PodUserOperation, self).__init__(api_token, token_issuer, server_type, config_path, sc_api_key,
                                               sc_voucher_hash, path.join(here, "json_schema.json"))

    def get_user_profile(self, access_token="", client_id="", client_secret=""):
        """
        دریافت پروفایل کاربر

        :param access_token: str اکسس توکن کاربر
        :param client_id: str شناسه کلاینت
        :param client_secret: str کد دسترسی کلاینت
        :return: dict
        """
        headers = self._get_headers()
        headers["_token_"] = access_token
        params = {}
        if client_id:
            params["client_id"] = client_id

        if client_secret:
            params["client_secret"] = client_secret

        return self._request.call(super(PodUserOperation, self)._get_sc_product_id("/nzh/getUserProfile"),
                                  headers=headers, params=params)

    def edit_profile_with_confirmation(self, access_token, params):
        """
        ویرایش اطلاعات پروفایل کاربر

        :param access_token: str
        :param params: dict
        :return: dict
        """
        headers = self._get_headers()
        headers["_token_"] = access_token

        self._validate(params, "editProfileWithConfirmation")

        return self._request.call(super(PodUserOperation, self)._get_sc_product_id("/nzh/editProfileWithConfirmation",
                                                                                   "post"),
                                  headers=headers, params=params)

    def get_list_address(self, access_token, page=1, size=20):
        """
        دریافت لیست آدرس های کاربر

        :param access_token: str
        :param page: int
        :param size: int
        :return: list of dict
        """
        headers = self._get_headers()
        headers["_token_"] = access_token
        params = {
            "offset": calc_offset(page, size),
            "size": size
        }

        return self._request.call(super(PodUserOperation, self)._get_sc_product_id("/nzh/listAddress"),
                                  headers=headers, params=params)

    def edit_confirm_profile(self, access_token, code, cell_phone_number):
        """
        تایید تغییرات پروفایل کاربر

        :param access_token: str اکسس توکن کاربر
        :param code: str کد دریافتی از کاربر
        :param cell_phone_number: str شماره موبایلی که کد برای آن ارسال شده است
        :return: dict
        """

        params = {
            "code": code,
            "cellphoneNumber": cell_phone_number
        }
        self._validate(params, "editConfirmProfile")
        headers = self._get_headers()
        headers["_token_"] = access_token

        return self._request.call(super(PodUserOperation, self)._get_sc_product_id("/nzh/confirmEditProfile", "post"),
                                  headers=headers, params=params)
