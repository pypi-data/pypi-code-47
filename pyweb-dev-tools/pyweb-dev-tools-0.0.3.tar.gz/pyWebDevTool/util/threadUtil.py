# -*- coding: utf-8 -*-
from pyWebDevTool.context.globalContext import Context


def move_to_ui_thread(obj=None, module=None, function=None, params=dict, block=True):
    """方法或函数移动到ui线程执行"""
    __bridge = Context().browser.bridge
    if block:
        if obj is not None:
            __bridge.blockInvokeSignal[object, str, dict].emit(obj, function, params)
        if module is not None:
            __bridge.blockInvokeSignal[str, str, dict].emit(module, function, params)
    else:
        if obj is not None:
            __bridge.invokeSignal[object, str, dict].emit(obj, function, params)
        if module is not None:
            __bridge.invokeSignal[str, str, dict].emit(module, function, params)
