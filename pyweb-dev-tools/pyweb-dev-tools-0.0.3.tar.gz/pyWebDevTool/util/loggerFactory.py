#!/usr/bin/env python
# coding=utf8

"""
该日志类可以把不同级别的日志输出到不同的日志文件中
"""

import inspect
import logging
import os
import threading
import time
from logging import handlers as hl

from numpy import long

from pyWebDevTool.util import fileUtil

level_info = {
    logging.INFO: {
        "name": "/Log/client-info.log",
        "backupCount": 7
    },
    logging.ERROR: {
        "name": "/Log/client-error.log",
        "backupCount": 7
    },
    logging.DEBUG: {
        "name": "/Log/client-debug.log",
        "backupCount": 2  # 保留两个
    }
}

handlers = {}


def createHandlers():
    logLevels = level_info.keys()
    for level in logLevels:
        info_level_ = level_info[level]
        filename = fileUtil.getRootPath() + info_level_['name']
        dir = os.path.abspath(os.path.dirname(filename))
        fileUtil.mkdir(dir)
        # 实例化TimedRotatingFileHandler
        # interval是时间间隔，backupCount是备份文件的个数，如果超过这个个数，就会自动删除，when是间隔的时间单位，单位有以下几种：
        # S 秒
        # M 分
        # H 小时、
        # D 天、
        # W 每星期（interval==0时代表星期一）
        # midnight 每天凌晨
        handlers[level] = hl.TimedRotatingFileHandler(filename=filename, when="D", interval=1,
                                                      backupCount=info_level_['backupCount'],
                                                      encoding='utf-8')  # 往文件里写入#指定间隔时间自动生成文件的处理器
# 加载模块时创建全局变量
createHandlers()


class Logger(object):
    _instance_lock = threading.Lock()

    def printfNow(self):
        ct = time.time()
        local_time = time.localtime(ct)
        data_head = time.strftime("%Y-%m-%d %H:%M:%S", local_time)
        data_secs = (ct - long(ct)) * 1000
        time_stamp = "%s.%03d" % (data_head, data_secs)
        return time_stamp

    def __new__(cls, *args, **kwargs):
        if not hasattr(Logger, "_instance_"):
            with Logger._instance_lock:
                if not hasattr(Logger, "_instance_"):
                    setattr(Logger, "_instance_", object.__new__(cls))
                    getattr(Logger, "_instance_").__init_logger()
        return getattr(Logger, "_instance_")

    def __init__(self, level=logging.DEBUG):
        pass

    def __init_logger(self, level=logging.DEBUG):
        self.__loggers = {}
        logLevels = handlers.keys()
        for level in logLevels:
            logger = logging.getLogger(str(level))
            logger.addHandler(handlers[level])
            logger.addHandler(logging.StreamHandler())
            logger.setLevel(level)
            self.__loggers.update({level: logger})

    def getLogMessage(self, level, message):
        frame, filename, lineNo, functionName, code, unknowField = inspect.stack()[2]
        '''日志格式：[时间] [类型] [记录代码] 信息'''
        return "[%s] [%s] %s - [line %s] - %s %s" % (
            self.printfNow(), level.upper(), filename, lineNo, functionName, message)

    def debug(self, message):
        self.__loggers[logging.DEBUG].debug(message)

    def info(self, message):
        message = self.getLogMessage("info", message)
        self.__loggers[logging.INFO].info(message)

    def error(self, message):
        message = self.getLogMessage("error", message)
        self.__loggers[logging.ERROR].error(message)
        self.__loggers[logging.INFO].info(message)
        self.__loggers[logging.DEBUG].debug(message)

    def warning(self, message):
        message = self.getLogMessage("warning", message)
        self.__loggers[logging.ERROR].warning(message)
        self.__loggers[logging.INFO].info(message)
        self.__loggers[logging.DEBUG].debug(message)

    def critical(self, message):
        message = self.getLogMessage("critical", message)
        self.__loggers[logging.ERROR].critical(message)
        self.__loggers[logging.INFO].info(message)
        self.__loggers[logging.DEBUG].debug(message)


if __name__ == "__main__":
    logger = Logger()
    logger.debug("debug")
    logger = Logger()
    logger.info("info")
    logger = Logger()
    logger.warning("warning")
    logger = Logger()
    logger.error("error")
    logger = Logger()
    logger.critical("critical")
