# -*- coding: utf-8 -*-
import os

from pyWebDevTool.util.loggerFactory import Logger

logger = Logger()


def explorer_open(path):
    abspath = os.path.abspath(path)
    logger.debug("打开目录 %s" % abspath)
    os.system("explorer.exe %s" % abspath)
