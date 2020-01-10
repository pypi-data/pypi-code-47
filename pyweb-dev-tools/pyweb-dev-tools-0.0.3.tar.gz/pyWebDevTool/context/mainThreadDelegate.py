# -*- coding: utf-8 -*-
import sys

from PyQt5.QtCore import QObject, pyqtSignal, Qt


class MainThreadDelegate(QObject):
    """主线程移动委托类"""
    invokeSignal = pyqtSignal([object, str, dict], [str, str, dict])

    blockInvokeSignal = pyqtSignal([object, str, dict], [str, str, dict])

    def __init__(self):
        super().__init__()
        self.invokeSignal[object, str, dict].connect(self.obj_function_event)
        self.invokeSignal[str, str, dict].connect(self.function_event)
        self.blockInvokeSignal[object, str, dict].connect(self.obj_function_event, Qt.BlockingQueuedConnection)
        self.blockInvokeSignal[str, str, dict].connect(self.function_event, Qt.BlockingQueuedConnection)

    def obj_function_event(self, obj, function, params):
        func = getattr(obj, function)
        func(params)

    def function_event(self, module_name, function, params):
        module = sys.modules[module_name]
        self.obj_function_event(module, function, params)

    def move_to_ui_thread(self, obj=None, module=None, function=None, params=dict, block=True):
        """方法或函数移动到ui线程执行"""
        if block:
            if obj is not None:
                self.blockInvokeSignal[object, str, dict].emit(obj, function, params)
            if module is not None:
                self.blockInvokeSignal[str, str, dict].emit(module, function, params)
        else:
            if obj is not None:
                self.invokeSignal[object, str, dict].emit(obj, function, params)
            if module is not None:
                self.invokeSignal[str, str, dict].emit(module, function, params)
