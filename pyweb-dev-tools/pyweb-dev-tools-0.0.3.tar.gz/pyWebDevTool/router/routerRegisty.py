# -*- coding: utf-8 -*-


""" router注册器 不要随意删除！"""
import importlib

from pyWebDevTool.util import packageInfoUtil, pluginStoreUtil

from pyWebDevTool.util.loggerFactory import Logger

logger = Logger()


def printRouters():
    # 获取插件package-info.json信息 加载py文件
    package_infos = packageInfoUtil.list_package_infos()
    load_modules(package_infos)


def load_modules(package_infos):
    for p in package_infos:
        path = pluginStoreUtil.get_plugin_module(p)
        logger.debug("加载router：" + path)
        importlib.import_module(path)
