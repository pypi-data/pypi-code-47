# -*- coding: utf-8 -*-
from PyQt5.QtWidgets import QMenu, QSystemTrayIcon, QAction, QMessageBox
from pyWebDevTool.componment.messageBox import MyQMessageBox

from pyWebDevTool.componment.icon import AppIcon
from pyWebDevTool.util import processUtil, qResourceUtil


class TrayIcon(QSystemTrayIcon):
    def __init__(self, mainWindowImpl, app=None):
        super(TrayIcon, self).__init__()
        self.app = app
        self.mainWindowImpl = mainWindowImpl
        self.menu_qss = qResourceUtil.get_qss("myQMenu.qss")
        self.showMenu()
        self.icon = AppIcon()
        self.setIcon(self.icon)
        self.activated[QSystemTrayIcon.ActivationReason].connect(self.iconActivated)
        self.show()

    def showMenu(self):
        """设计托盘的菜单"""
        self.menu = QMenu()
        self.menu.setStyleSheet(self.menu_qss)
        a1 = QAction("最小化", self.menu, triggered=self.min)

        self.menu.addAction(a1)

        a3 = QAction("重启", self, triggered=self.restart)
        self.menu.addAction(a3)

        self.menu.addSeparator()

        a2 = QAction("退出", self, triggered=self.quit)
        self.menu.addAction(a2)
        self.setContextMenu(self.menu)

    def min(self):
        self.browser.hide()

    def quit(self):
        box = MyQMessageBox(text="是否确定退出？").add_ok_btn().add_cancel_btn()
        box.exec_()
        if box.clickedButton() == box.get_ok_btn():
            """完整的退出"""
            processUtil.stop_self()

    def restart(self):
        box = MyQMessageBox(text="是否确定重启？").add_ok_btn().add_cancel_btn()
        box.exec_()
        if box.clickedButton() == box.get_ok_btn():
            """重启"""
            processUtil.restart_self()

    def iconActivated(self, QSystemTrayIcon_ActivationReason):
        if QSystemTrayIcon_ActivationReason == QSystemTrayIcon.DoubleClick:
            self.mainWindowImpl.show()

    def hideTrayIcon(self, title="开始退出"):
        self.showMessage("提示", title, self.icon, msecs=1000)
        self.setVisible(False)
