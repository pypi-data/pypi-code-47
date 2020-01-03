#!/usr/bin/python3
# -*- coding: utf8 -*-
#
# @author: natloc
# @date: 2019-10-16
# @time: 01:06
# @doc:
# Copyright © 2019 natloc. All rights reserved.
#

import urllib2

import nat.string


# 请求 url 的数据
# return: string   # 请求返回的数据
def reqUrl(urlStr):
    """
    请求 url 的数据
    :param urlStr:
    :return: 请求返回的数据
    """
    urlStr = nat.string.trim(urlStr)
    if "" != urlStr:
        req = urllib2.Request(urlStr)
        resp = urllib2.urlopen(req)
        return resp.read()

    else:
        return ""
