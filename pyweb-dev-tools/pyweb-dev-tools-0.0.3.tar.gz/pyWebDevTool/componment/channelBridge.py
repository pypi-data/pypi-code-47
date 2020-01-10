# -*- coding: utf-8 -*-
import _thread
import json
import sys

from PyQt5.QtCore import QObject, pyqtSignal, pyqtSlot, Qt

from pyWebDevTool.context.globalContext import Context
from pyWebDevTool.router.private.privateRouterRegisty import printPrivateRouters
from pyWebDevTool.router.routeContext import rc
from pyWebDevTool.router.private.privateRouteContext import _private_rc
# 导入该目录所有router模块
from pyWebDevTool.router.routerRegisty import printRouters

printRouters()

printPrivateRouters()


class ChannelBridge(QObject):
    callbackSignal = pyqtSignal(str, str)

    def __init__(self, parent=None):
        super().__init__(parent)
        self.view = parent
        self.callbackSignal.connect(self.js_callback)

    @pyqtSlot(str, result=str)
    def qt_private_service(self, options):
        return self.qt_service(options, _private_rc)

    @pyqtSlot(str, result=str)
    def qt_service(self, options, router_context=None):
        if router_context is None:
            router_context = rc
        dic_op = json.loads(options)
        mode = self.thread_mode(dic_op)
        if mode == "ui":
            # print("使用ui线程处理，可以直接操作ui，但不要执行耗时操作，否则会导致ui卡顿")
            self.router(dic_op, router_context)
        elif mode == "child":
            # print("进入子线程处理，不能直接操作ui，要操作ui请使用 threadUtil.move_to_ui_thread ,可以进行耗时操作，不会导致ui卡顿")
            _thread.start_new_thread(self.router, (dic_op, router_context))
        else:
            msg = "非法的线程模式，仅支持 ui/child,默认为child"
            # print(msg)
            self.callbackSignal.emit(dic_op['callback'], {
                "code": -1,
                "msg": msg
            })
        return ""

    def router(self, dic_op, router_context):
        callback = dic_op['callback']
        ret = router_context.serve(dic_op['fullPath'], dic_op['params'])
        if type(ret) == str:
            result = ret
        elif type(ret) == dict or type(ret) == list:
            result = json.dumps(ret, ensure_ascii=False)
        else:
            result = ""
            try:
                result = str(ret)
            except:
                pass
        self.callbackSignal.emit(callback, result)

    def js_callback(self, callback, params):
        self.view.page().runJavaScript(callback + "('" + params + "')")

    def thread_mode(self, options):
        if "threadMode" in options:
            return options["threadMode"]
        return "child"
