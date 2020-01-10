# -*- coding: utf-8 -*-
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidgetAction, QLabel

from pyWebDevTool.componment.css.commonCss import BLUE_STYLE


class MyQWidgetAction(QWidgetAction):
    """自定义的action 覆盖样式"""

    def __init__(self, title="", parent=None, triggered=None):
        if triggered is None:
            super().__init__(parent)
        else:
            super().__init__(parent, triggered=triggered)
        self.parent = parent
        label = QLabel(title)
        label.setProperty("type", "QWidgetAction_label")
        label.setMargin(5)
        label.setMinimumWidth(50)
        label.setStyleSheet("QLabel[type=\"QWidgetAction_label\"]:hover" + BLUE_STYLE)
        label.setAlignment(Qt.AlignLeft)
        self.setDefaultWidget(label)

