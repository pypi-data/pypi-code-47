#!/usr/bin/env python
# coding=utf8
import os
import sys
import time

import win32api
import win32process
from multiprocessing import Process

from PyQt5.QtCore import QCoreApplication

from pyWebDevTool.context.globalContext import Context
from pyWebDevTool.util import argumentUtil


def processExists(processname):
    p = os.popen('tasklist /FI "IMAGENAME eq %s"' % processname)
    x = p.read()
    p.close()
    from pyWebDevTool.util.loggerFactory import Logger
    logger = Logger()
    logger.info("processExists：返回：{}".format(x))
    if x == "信息: 没有运行的任务匹配指定标准。\n":
        return False
    return True


def killProcess(processname):
    from pyWebDevTool.util.loggerFactory import Logger
    logger = Logger()
    if not processExists(processname):
        logger.info("进程未找到：{}".format(processname))
        return False
    p = os.popen('taskkill /F /IM "%s"' % processname)
    x = p.read()
    p.close()
    logger.info("killProcess：返回：{}".format(x))
    return True


def startProcess(processPath, args=None):
    from pyWebDevTool.util.loggerFactory import Logger
    logger = Logger()
    logger.info("启动程序：{}".format(processPath))
    if os.path.exists(processPath):
        if args is None:
            args = ""
        """非独立进程 父进程就是调用该方法的程序"""
        ret = win32api.ShellExecute(0, 'open', r'' + processPath, args, '', 1)
        logger.info("启动程序结果:{}".format(str(ret)))
        return True
    else:
        logger.error("程序启动失败，启动程序文件未找到：{}".format(processPath))
        return False


def restart_self():
    from pyWebDevTool.util.loggerFactory import Logger
    logger = Logger()
    logger.info("重启程序")
    # 因为重启的是本身 必须先启动再关闭 否则先停止了后续程序不再执行
    if argumentUtil.is_exe():
        args = ""
        for i in range(len(sys.argv)):
            args += '"' + sys.argv[i] + '" '
        """独立进程 没有父进程"""
        win32process.CreateProcess(sys.executable, args,
                                   None, None, 0, win32process.CREATE_NO_WINDOW, None, None,
                                   win32process.STARTUPINFO())
    else:
        p = Process(target=__start_python_process, args=())
        p.start()
    time.sleep(3)
    stop_self()


def __start_python_process():
    args = ""
    for i in range(len(sys.argv)):
        args += '"' + sys.argv[i] + '" '
    startProcess(sys.executable, args)


def stop_self():
    from pyWebDevTool.util.loggerFactory import Logger
    logger = Logger()
    logger.info("退出程序")
    context = Context()
    if context.mainWindowImpl is not None:
        context.mainWindowImpl.close()
    if context.trayIcon is not None:
        context.trayIcon.hideTrayIcon()
    if argumentUtil.is_dev():
        Context.webpack_server.stop()
    QCoreApplication.instance().quit()
    sys.exit(0)


def findPidByPort(port=-1):
    with os.popen("netstat -ano|findstr %s" % str(port)) as f:
        ret = f.read()
    v = ret.split("\n")
    if len(v) == 0:
        return None
    v = v[0].split(" ")
    ar = []
    for i in v:
        if i != '':
            ar.append(i)
    if len(ar) == 0:
        return None
    pid = ar[len(ar) - 1]
    return pid


def killProcessByPid(pid):
    if os.system("taskkill /F /pid %s" % str(pid)) == 0:
        return True
    return False


def killProcessByPort(port):
    pid = findPidByPort(port)
    if pid is None:
        return False
    return killProcessByPid(pid)
