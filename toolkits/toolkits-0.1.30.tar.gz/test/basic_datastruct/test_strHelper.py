# -*- coding: utf-8 -*-
import os
import pprint

import pytest
from unipath import Path

from system.strHelper import StrHelper


@pytest.fixture()
def str_helper():
    str_helper = StrHelper()
    return str_helper


class TestStrHelper(object):
    def test_match_phone_info(self, str_helper):
        test_str = ' 175****3754 158****5552 158****5552 13412337575 15812311265 user_id-1334321093 '
        match_pattern = [
            {
                "name": "phone",
                "reg": r'((13[0-9])|(14[5,7])|(15[0-3,5-9])|(17[0,3,5-8])|(18[0-9])|166|190|192|19[6-9]|(147))\d{8}'
            },
            {
                "name": "phone_mask",
                "reg": r'[0-9]{3}\*{4}[0-9]{4}'
            },
            {
                "name": "user_id",
                "reg": r'user_id-([0-9]+)'
            }]
        data_match = str_helper.match_phone_info(test_str, match_pattern)
        assert data_match['phone'] is not None

    @staticmethod
    def test_md5(str_helper):
        str_md5 = str_helper.md5_str("root")
        assert str_md5 == "63A9F0EA7BB98050796B649E85481845"

    def test_multi_search(self, str_helper):
        search_words = [u"宝马", u"马", u"奔驰", u"保时捷"]
        search_str = u"哎呀，今天在楼下看到了宝马，我老家倒是有养马的，以前的邻居有个奔驰，不对是保时捷，大爷的，都是马"
        ret = str_helper.multi_search(search_str, search_words)
        pprint.pprint(ret)

        assert ret[0][1] == u"宝马"
