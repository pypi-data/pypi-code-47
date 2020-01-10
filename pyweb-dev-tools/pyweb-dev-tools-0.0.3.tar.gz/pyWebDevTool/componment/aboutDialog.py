# -*- coding: utf-8 -*-
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QDialog

from pyWebDevTool.componment.about import Ui_Dialog
from pyWebDevTool.componment.icon import AppIcon
from pyWebDevTool.util.loggerFactory import Logger

logger = Logger()


class AboutDialog(QDialog, Ui_Dialog):

    def __init__(self, parent):
        super().__init__(parent)
        self.setupUi(self)
        self.setAttribute(Qt.WA_DeleteOnClose, True)
        self.setWindowTitle("关于")
        self.setWindowIconText("关于")
        self.label.setOpenExternalLinks(True)  # 如果没有这句，就只能通过linkActivated信号，连接到自定义槽函数中打开

        self.icon = AppIcon()
        self.setWindowIcon(self.icon)
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setWindowModality(Qt.ApplicationModal)
        self.pushButton.clicked.connect(self.close)
        self.show()
