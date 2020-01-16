#!/usr/bin/env python
# -*- coding: utf-8 -*-
from PySide2.QtWidgets import QDialog, QVBoxLayout, QShortcut, QApplication
from mkedit.core.widgets import PreView
from PySide2.QtGui import QKeySequence
from PySide2.QtCore import QSize


class PrewViewDialog(QDialog):
    def __init__(self, parent=None):
        QDialog.__init__(self, parent)
        self.mainLayout = QVBoxLayout(self)
        self.preView = PreView(self)
        self.mainLayout.addWidget(self.preView)
        self.setLayout(self.mainLayout)
        desktop = QApplication.desktop()
        desktop.width() / 2,
        size = QSize()
        size.setHeight(int(desktop.height() * 0.9))
        size.setWidth(int(desktop.width() * 0.33))
        self.setFixedSize(size)
        shortcut = QShortcut(QKeySequence("Ctrl+W"), self)
        shortcut.activated.connect(self.closePreView)

    def closePreView(self):
        self.close()

    def setPreHtml(self, html):
        self.preView.initHtml()
        self.preView.setPreContent(html)
        self.show()
