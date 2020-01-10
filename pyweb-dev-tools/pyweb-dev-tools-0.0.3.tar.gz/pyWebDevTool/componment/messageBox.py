# -*- coding: utf-8 -*-
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMessageBox

from pyWebDevTool.util import qResourceUtil


class MyQMessageBox(QMessageBox):

    def __init__(self, parent=None, icon=QMessageBox.Question, title="提示", text=""):
        super().__init__(parent)
        self.setWindowFlags(self.windowFlags() | Qt.FramelessWindowHint | Qt.Tool)
        self.setIcon(icon)
        self.setWindowTitle(title)
        self.setText(text)
        self.myBtnCss = qResourceUtil.get_qss("myQBtn.qss")
        self.myQDialog = qResourceUtil.get_qss("myQDialog.qss")

    def add_ok_btn(self):
        self.qok = self.addButton("是", QMessageBox.YesRole)
        self.qok.setProperty("name", "primary")
        return self

    def get_ok_btn(self):
        return self.qok

    def add_cancel_btn(self):
        self.qno = self.addButton("否", QMessageBox.NoRole)
        self.qno.setProperty("name", "default")
        return self

    def get_cancel_btn(self):
        return self.qno

    def exec(self):
        self.setStyleSheet(self.myQDialog + self.myBtnCss)
        return super().exec()

    def exec_(self):
        self.setStyleSheet(self.myQDialog + self.myBtnCss)
        return super().exec_()

    def keyPressEvent(self, QKeyEvent):
        if QKeyEvent.key() == Qt.Key_Enter:
            self.get_ok_btn().click()
        elif QKeyEvent.key() == Qt.Key_Escape:
            self.get_cancel_btn().click()
        else:
            pass
