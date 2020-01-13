from typing import Container

from PyQt5 import QtCore, QtGui, QtWidgets

from ..settings import Settings


class TestWindow(QtWidgets.QWidget):
    def __init__(self, settings: Settings):
        super().__init__()

        self.settings = settings
        self.translate = QtCore.QCoreApplication.translate

        self.setObjectName("TestWindow")
        self.setWindowTitle(self.translate("TestWindow", "test"))
        self.setGeometry(*self.settings.get_text_position(), *self.settings.get_text_size())
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.setWindowFlags(self.windowFlags() | QtCore.Qt.WindowStaysOnTopHint)

        self.layout = QtWidgets.QGridLayout(self)

        self.label = QtWidgets.QLabel(self)
        self.label.setText("Test")
        red, green, blue, alpha = self.settings.get_text_color()
        self.label.setStyleSheet(f"color: rgba({red}, {green}, {blue}, {alpha})")
        self.label.setFont(QtGui.QFont(self.settings.text_font, self.settings.text_fontsize))

        self.layout.addWidget(self.label)

    def closeEvent(self, event):
        event.ignore()
        self.hide()


class ShowWindow(QtWidgets.QWidget):
    def __init__(self, settings: Settings):
        super().__init__()

        self.settings = settings
        self.translate = QtCore.QCoreApplication.translate

        self.setObjectName("ShowWindow")
        self.setWindowTitle(self.translate("ShowWindow", "show"))
        self.setGeometry(*self.settings.get_text_position(), *self.settings.get_text_size())
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground) 
        self.setWindowFlags(QtCore.Qt.Tool | QtCore.Qt.FramelessWindowHint)
        self.setWindowFlags(self.windowFlags() | QtCore.Qt.WindowStaysOnTopHint)

        self.show_timer = QtCore.QTimer()
        self.show_timer.timeout.connect(self.hide_text)

        self.layout = QtWidgets.QGridLayout(self)

        self.label = QtWidgets.QLabel(self)
        self.label.setGeometry(0, 0, *self.settings.get_text_size())
        red, green, blue, alpha = self.settings.get_text_color()
        self.label.setStyleSheet(f"color: rgba({red}, {green}, {blue}, {alpha})")
        self.label.setFont(QtGui.QFont(self.settings.text_font, self.settings.text_fontsize))

        self.layout.addWidget(self.label)

    def closeEvent(self, event):
        event.ignore()

    def show_text(self, keys: Container[str]):
        self.label.setText("+".join(sorted(keys)))

        self.show()

        self.show_timer.stop()
        self.show_timer.start(self.settings.text_time)

    def hide_text(self):
        self.hide()
        self.show_timer.stop()
