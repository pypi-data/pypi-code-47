#!/usr/bin/env python
# coding=utf8
import threading


class Context(object):
    trayIcon = None

    mainWindowImpl = None

    mainThreadDelegate = None  # 主线程委托类

    webpack_server = None

    webpackLoadSuccessSignalObject = None

    _instance_lock = threading.Lock()

    def __new__(cls, *args, **kwargs):
        # 单例模式
        if not hasattr(Context, "_instance"):
            with Context._instance_lock:
                if not hasattr(Context, "_instance"):
                    Context._instance = object.__new__(cls)
        return Context._instance

    def __init__(self):
        """单例模式构造方法不能有逻辑"""
        pass
