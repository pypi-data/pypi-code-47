# -*- coding: utf-8 -*-


""" router注册器 不要随意删除！"""
from pyWebDevTool.util.loggerFactory import Logger

from pyWebDevTool.router.private import pluginRouter

modules = [pluginRouter]

logger = Logger()


def printPrivateRouters():
    for module in modules:
        logger.debug("加载私有router：" + module.__name__)
