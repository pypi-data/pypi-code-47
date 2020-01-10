# -*- coding: utf-8 -*-
import cgitb
import datetime
import importlib
import os
import sys

from PyQt5.QtWidgets import QApplication

from pyWebDevTool.componment.mainWindowImpl import MainWindowImpl
from pyWebDevTool.componment.trayIcon import TrayIcon
from pyWebDevTool.context.globalContext import Context
from pyWebDevTool.context.mainThreadDelegate import MainThreadDelegate
from pyWebDevTool.util import argumentUtil, fileUtil, processUtil
from pyWebDevTool.webpack.webpackServer import WebpackLoadSuccessSignalObject


class App:

    def __init__(self):
        now = datetime.datetime.now()
        # 加载资源
        importlib.import_module("pyWebDevTool.assert_rc")

        # 主线程异常不会导致程序无响应 会记录日志
        cgitb.enable(logdir="Log", format="text")
        # 主程序 与qtWebEngineProcess合并到一个进程
        os.putenv("QTWEBENGINE_REMOTE_DEBUGGING", "9223")
        os.putenv("QTWEBENGINE_CHROMIUM_FLAGS", "-single-process")
        # 开启webpack
        if argumentUtil.is_dev():
            from pyWebDevTool.webpack.webpackServer import WebpackServer
            Context.webpack_server = WebpackServer()
            Context.webpack_server.start()
        os.chdir(fileUtil.getRootPath())
        app = QApplication(sys.argv)
        self.mainWindowImpl = MainWindowImpl()
        Context().mainWindowImpl = self.mainWindowImpl
        self.trayIcon = TrayIcon(self.mainWindowImpl, self)
        Context().mainThreadDelegate = MainThreadDelegate()
        Context().trayIcon = self.trayIcon

        Context().webpackLoadSuccessSignalObject = WebpackLoadSuccessSignalObject()

        now_end = datetime.datetime.now()
        from pyWebDevTool.util.loggerFactory import Logger
        logger = Logger()
        logger.info("程序启动完成，耗时：{}s".format(str(now_end - now)))
        sys.exit(app.exec_())

    def stop(self):
        processUtil.stop_self()


