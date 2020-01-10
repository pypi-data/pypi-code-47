# -*- coding: utf-8 -*-
import _thread
import os
import time
from multiprocessing import Process

from PyQt5.QtCore import QObject, pyqtSignal

from pyWebDevTool.context import const
from pyWebDevTool.context.globalContext import Context
from pyWebDevTool.util import httpUtil, configUtil, argumentUtil
from pyWebDevTool.util.loggerFactory import Logger

logger = Logger()


class WebpackServer:

    def __init__(self):
        super().__init__()
        self.port = configUtil.get_config_val(configUtil.BaseConfigEnum.webpack_server_port)
        self.ip = configUtil.get_config_val(configUtil.BaseConfigEnum.webpack_server_ip)
        self.index_url = "http://{}:{}".format(self.ip, self.port)
        _thread.start_new_thread(self.waitWebpackLoaded, ())

    def start(self):
        p = Process(target=self._run, args=())
        p.daemon = True
        p.start()

    def _run(self):
        os.chdir(const.DEV_WEB_ROOT_ABS_PATH)
        os.system("npm run dev")

    def waitWebpackLoaded(self):
        while True:
            time.sleep(0.5)
            try:
                res = httpUtil.get(self.index_url)
                if res.status_code == 200:
                    logger.info("webpack加载完毕...")
                    Context().webpackLoadSuccessSignalObject.emit()
                    break
            except Exception as e:
                # logger.error(e)
                pass

    def stop(self):
        from pyWebDevTool.util.processUtil import killProcessByPort
        logger.info("停止webpack_server,port:{}".format(self.port))
        killProcessByPort(self.port)


class WebpackLoadSuccessSignalObject(QObject):
    webpackLoadSuccessSignal = pyqtSignal()

    def __init__(self):
        super().__init__()
        self.webpackLoadSuccessSignal.connect(self.webpackLoadSuccessEvent)

    def emit(self):
        self.webpackLoadSuccessSignal.emit()

    def webpackLoadSuccessEvent(self):
        """webpack加载完毕事件"""
        Context().mainWindowImpl.load_default_tab()
        if argumentUtil.is_dev():
            # dev环境加载调试页面
            Context().mainWindowImpl.open_debug_page()
