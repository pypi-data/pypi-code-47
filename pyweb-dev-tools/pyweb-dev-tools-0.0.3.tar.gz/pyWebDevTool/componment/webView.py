# -*- coding: utf-8 -*-
import os

from PyQt5.QtCore import Qt
from PyQt5.QtWebEngineWidgets import QWebEngineView, QWebEngineProfile, QWebEnginePage, QWebEngineSettings

from pyWebDevTool.context import const
from pyWebDevTool.util import fileUtil

from pyWebDevTool.util.loggerFactory import Logger

logger = Logger()


class MyQWebEnginePage(QWebEnginePage):

    def __init__(self, *__args):
        super().__init__(*__args)
        self.settings().setFontFamily(QWebEngineSettings.StandardFont, "微软雅黑")

    """重写javascript控制台消息方法，日志可打印在后台"""

    def javaScriptConsoleMessage(self, level, message, lineNumber, sourceId):
        if level == QWebEnginePage.InfoMessageLevel:
            level_desc = "info"
            logger.debug("浏览器日志: level:{},line: {}, message: {}".format(level_desc, lineNumber, message))
        elif level == QWebEnginePage.WarningMessageLevel:
            level_desc = "warning"
            logger.info("浏览器日志: level:{},line: {}, message: {}".format(level_desc, lineNumber, message))
        else:
            level_desc = "error"
            logger.error("浏览器日志: level:{},line: {}, message: {}".format(level_desc, lineNumber, message))

    def acceptNavigationRequest(self, QUrl, NavigationType, isMainFrame):
        url = QUrl.toDisplayString()
        if NavigationType == QWebEnginePage.NavigationTypeLinkClicked and url in const.BROWSER_URL:
            import webbrowser
            webbrowser.open(url)
            return False
        return True


class MyQWebEngineView(QWebEngineView):
    """自定义QWebEngineView 设置缓存和cookie目录，支持超链接跳转"""

    def __init__(self, *args, **kwargs):
        super(MyQWebEngineView, self).__init__(*args, **kwargs)
        self.setAttribute(Qt.WA_DeleteOnClose, True)
        defaultProfile = QWebEngineProfile.defaultProfile()
        defaultProfile.setPersistentCookiesPolicy(QWebEngineProfile.ForcePersistentCookies)
        defaultProfile.setCachePath(fileUtil.getRootPath() + os.sep + "temp" + os.path.sep + "browser_cache")
        defaultProfile.setPersistentStoragePath(
            fileUtil.getRootPath() + os.sep + "temp" + os.path.sep + "browser_cache")
        # 绑定cookie被添加的信号槽
        defaultProfile.cookieStore().cookieAdded.connect(self.onCookieAdd)
        from PyQt5.QtNetwork import QNetworkCookieJar
        self.cookies = QNetworkCookieJar()

    def onCookieAdd(self, cookie):  # 处理cookie添加的事件
        self.cookies.insertCookie(cookie)

    def get_cookies(self):
        return self.cookies

    # 支持网页超链接跳转
    def createWindow(self, QWebEnginePage_WebWindowType):
        return self
