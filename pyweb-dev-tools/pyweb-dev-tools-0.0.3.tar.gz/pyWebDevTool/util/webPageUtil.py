# -*- coding: utf-8 -*-
from pyWebDevTool.util import argumentUtil, fileUtil

from pyWebDevTool.context.globalContext import Context


def get_page_path(vue_router):
    c = Context()
    if argumentUtil.is_dev():
        return c.webpack_server.index_url + "/#" + vue_router
    else:
        return fileUtil.getParentPath(__file__) + "/resources/static/index.html#" + vue_router


def get_page_path_index():
    return fileUtil.getParentPath(__file__) + "/resources/static/README.html"


def get_page_path_debug():
    return get_page_path("/")


def get_page_path_loading():
    if argumentUtil.is_dev():
        return fileUtil.getParentPath(__file__) + "/resources/static/loading.html"
    return get_page_path_index()
