#!/usr/bin/env python
# -*- coding: utf-8 -*-
from PySide2.QtWebEngineWidgets import QWebEngineView, QWebEnginePage
from PySide2.QtCore import QUrl
import webbrowser
import PySide2


class WebEnginePage(QWebEnginePage):

    def javaScriptConsoleMessage(self, level, message, lineNumber,
                                 sourceID):  # real signature unknown; restored from __doc__
        """ javaScriptConsoleMessage(self, level: PySide2.QtWebEngineWidgets.QWebEnginePage.JavaScriptConsoleMessageLevel, message: str, lineNumber: int, sourceID: str) """
        print("javaScriptConsoleMessageCall#message = %s" % (message))

    def acceptNavigationRequest(self, url, _type, isMainFrame):
        if _type == QWebEnginePage.NavigationTypeLinkClicked:
            webbrowser.open(url.url(), new=1, autoraise=True)
            return False
        return True

    # 处理https错误提示
    def certificateError(self, certificateError: PySide2.QtWebEngineWidgets.QWebEngineCertificateError) -> bool:
        return True


class PreView(QWebEngineView):
    def __init__(self, *args, **kwargs):
        super(PreView, self).__init__(*args, **kwargs)
        # self.setSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Expanding)
        self.setPage(WebEnginePage(self))
        self.loadFinishStatus = False
        self.needCall = list()
        self.preContent = None
        self.loadFinished.connect(self.loadFinishCall)

        self.percentageOfTop = None

    def initHtml(self):
        self.setHtml('''<!DOCTYPE html>
<html lang="zh-cn">
<head>
    <meta charset="UTF-8"/>
    <meta content="width=device-width, initial-scale=1.0" name="viewport"/>
    <meta content="IE=edge, chrome=1" http-equiv="X-UA-Compatible"/>
    <meta content="text/html; charset=utf-8" http-equiv="content-type"/>
    <link href="https://cdn.bootcss.com/github-markdown-css/3.0.1/github-markdown.min.css" rel="stylesheet">
    <link rel="stylesheet"
          href="https://cdn.jsdelivr.net/gh/highlightjs/cdn-release@9.16.2/build/styles/default.min.css">
    <script type="text/javascript"
            src="https://cdn.jsdelivr.net/gh/highlightjs/cdn-release@9.16.2/build/highlight.min.js"></script>
    <script type="text/javascript" src="https://cdnjs.cloudflare.com/ajax/libs/mermaid/7.1.2/mermaid.min.js"></script>
    <script type="text/javascript"
            src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.5/MathJax.js?config=TeX-MML-AM_CHTML"></script>
    <script type="text/javascript">
        MathJax.Hub.Config({
            tex2jax: {
                inlineMath: [
                    ['$', '$'],
                    ['(', ')']
                ]
            }
        });
    </script>
    <style>
        img {
            max-width: 100%;
        }
    </style>
</head>
<body id="preArea">
<div id="preMkContent">
</div>
</body>
</html>''')

    def urlChanged(self, *args, **kwargs):  # real signature unknown
        print("urlChanged# args:%s and kwargs:%s" % (args, kwargs))
        QWebEngineView.urlChanged(self, *args, **kwargs)

    def loadStarted(self, *args, **kwargs):  # real signature unknown
        print("loadStarted# args:%s and kwargs:%s" % (args, kwargs))
        QWebEngineView.loadStarted(self, *args, **kwargs)

    def loadFinishCall(self, *args, **kwargs):  # real signature unknown
        print("loadFinishCall# args:%s and kwargs:%s" % (args, kwargs))
        self.loadFinishStatus = True
        for call in self.needCall:
            call()
        self.needCall.clear()

    def setPreContent(self, data):

        self.preContent = data
        if self.loadFinishStatus:
            self.realLoadPreContent()
        else:
            self.needCall.append(self.realLoadPreContent)

    def realLoadPreContent(self):
        if self.loadFinishStatus:
            self.preContent = str(self.preContent).replace("'", "\\\'")
            self.preContent = str(self.preContent).replace('"', "\\\"")

            javascriptStr = 'window.document.getElementById("preMkContent").innerHTML = \"%s\"' % str(
                self.preContent).replace(
                "\n",
                "")
            print(javascriptStr)
            self.page().runJavaScript(javascriptStr)

    def scrollContent(self, percentageOfTop=None):
        self.percentageOfTop = percentageOfTop

        if self.loadFinishStatus:
            self.realScrollContent()
        else:
            self.needCall.append(self.realScrollContent)

    def realScrollContent(self):
        if self.loadFinishStatus:
            javascriptStr = '''var scrollingElement = (document.scrollingElement || document.body);
scrollingElement.scrollTop = scrollingElement.scrollHeight * %s;''' % self.percentageOfTop
        self.page().runJavaScript(javascriptStr)
