# coding=utf-8
from os import path
from pod_base import PodBase, calc_offset


class PodCommon(PodBase):

    def __init__(self, api_token, token_issuer="1", server_type="sandbox", config_path=None,
                 sc_api_key="", sc_voucher_hash=None):
        here = path.abspath(path.dirname(__file__))
        self._services_file_path = path.join(here, "services.ini")
        super(PodCommon, self).__init__(api_token, token_issuer, server_type, config_path, sc_api_key, sc_voucher_hash,
                                        path.join(here, "json_schema.json"))

    def get_ott(self):
        """
        دریافت آخرین توکن یکبار مصرف

        :return
        """
        self._request.call(super(PodCommon, self)._get_sc_product_id("/nzh/ott"), headers=self._get_headers())
        return self._request.last_ott

    def currency_list(self):
        """
        دریافت لیست ارزها

        :return: list
        """
        return self._request.call(super(PodCommon, self)._get_sc_product_id("/nzh/currencyList"),
                                  headers=self._get_headers())

    def guild_list(self, name="", page=1, size=50):
        """
        لیست اصناف

        :param str name: جستجو در نام اصناف
        :param int page: شماره صفحه
        :param int size: تعداد آیتم در هر صفحه
        :return: list
        """
        params = {
            "offset": calc_offset(page, size),
            "size": size
        }
        if name.__len__():
            params["name"] = name

        return self._request.call(super(PodCommon, self)._get_sc_product_id("/nzh/guildList"), params=params,
                                  headers=self._get_headers())

    def add_tag_tree_category(self, name, desc=""):
        """
        ایجاد دسته بندی برچسب درختی

        :param str name: نام دسته بندی
        :param str desc: توضحیات
        :return
        """

        params = {
            "name": name,
            "desc": desc
        }

        result = self._request.call(super(PodCommon, self)._get_sc_product_id("/nzh/biz/addTagTreeCategory", "post"),
                                    params=params,
                                    headers=self._get_headers())

        return result

    def get_tag_tree_category_list(self, params=None, page=1, size=50):
        """
        لیست دسته بندی های برچسب درختی

        :param dict params: فیلترها
        :param int page: شماره صفحه
        :param int size: تعداد آیتم در هر صفحه
        :return: list
        """
        if params is None:
            params = {}

        params.update({
            "offset": calc_offset(page, size),
            "size": size
        })

        return self._request.call(super(PodCommon, self)._get_sc_product_id("/nzh/biz/getTagTreeCategoryList"),
                                  params=params, headers=self._get_headers())

    def update_tag_tree_category(self, category_id, name, desc, enable=True):
        """
        ویرایش اطلاعات دسته بندی برچسب درختی

        :param int category_id: شناسه دسته بندی
        :param str name: نام جدید دسته بندی
        :param str desc: توضیحات جدید دسته بندی
        :param bool enable: وضعیت فعال یا غیرفعال بودن دسته بندی
        :return
        """
        params = {
            "id": category_id,
            "name": name,
            "desc": desc,
            "enable": enable.__str__().lower(),
        }

        return self._request.call(super(PodCommon, self)._get_sc_product_id("/nzh/biz/updateTagTreeCategory", "post"),
                                  params=params,
                                  headers=self._get_headers())

    def add_tag_tree(self, name, code, category_id, parent_id=0):
        """
        اضافه کردن تگ به درخت تگ ها

        :param str name: نام تگ
        :param str code: کد تگ
        :param int category_id: شناسه دسته بندی درخت تگ
        :param int parent_id: شناسه تگ پدر
        :return
        """

        params = {
            "name": name,
            "categoryId": category_id,
            "code": code
        }

        if parent_id > 0:
            params["parentId"] = parent_id

        return self._request.call(super(PodCommon, self)._get_sc_product_id("/nzh/biz/addTagTree", "post"),
                                  params=params, headers=self._get_headers())

    def _get_tag_tree_list(self, params):
        self._validate(params, "get_tag_tree_list")

        return self._request.call(super(PodCommon, self)._get_sc_product_id("/nzh/biz/getTagTreeList"), params=params,
                                  headers=self._get_headers())

    def get_tag_tree_list(self, category_id, level_count=3, level=0, parent_id=0):
        """
        لیست برچسب درختی

        :param int category_id: شناسه دسته بندی برچسب درختی
        :param int level_count: تعداد سطح ها
        :param int level: سطح شروع
        :param int parent_id: شناسه والد
        :return: list
        """

        params = {
            "categoryId": category_id,
            "levelCount": level_count,
            "level": level
        }

        if parent_id > 0:
            params["parentId"] = parent_id
            del params["level"]

        return self._get_tag_tree_list(params)

    def get_tag_tree(self, tag_tree_id):
        """
        دریافت جزئیات یک برچسب درختی

        :param int tag_tree_id: شناسه برچسب درختی
        :return
        """
        params = {
            "id": tag_tree_id
        }

        result = self._get_tag_tree_list(params)
        if len(result):
            return result[0]

        return {}

    def update_tag_tree(self, tag_tree_id, name, parent_id=0, enable=True):
        """
        ویرایش برچسب درختی

        :param int tag_tree_id: شناسه برچسب درختی
        :param str name: نام برچسب درختی
        :param int parent_id: شناسه والد برچسب درختی
        :param bool enable: فعال یا غیرفعال بودن برچسب
        :return
        """
        params = {
            "id": tag_tree_id,
            "name": name,
            "enable": enable.__str__().lower()
        }

        if parent_id > 0:
            params["parentId"] = parent_id

        return self._request.call(super(PodCommon, self)._get_sc_product_id("/nzh/biz/updateTagTree", "post"),
                                  params=params, headers=self._get_headers())
