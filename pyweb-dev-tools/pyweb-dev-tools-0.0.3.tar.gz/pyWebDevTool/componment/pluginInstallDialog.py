# -*- coding: utf-8 -*-
import _thread
import time

from PyQt5.QtCore import pyqtSignal, Qt
from PyQt5.QtWidgets import QDialog, QFileDialog

from pyWebDevTool.componment.icon import AppIcon
from pyWebDevTool.componment.messageBox import MyQMessageBox
from pyWebDevTool.componment.plugin_install import Ui_Dialog
from pyWebDevTool.context.globalContext import Context
from pyWebDevTool.interfaces import installPlugin
from pyWebDevTool.util import dictUtil
from pyWebDevTool.util.loggerFactory import Logger

logger = Logger()


class PluginInstallDialog(QDialog, Ui_Dialog):
    plugin_install_finished_signal = pyqtSignal(bool, dict)

    def __init__(self, parent):
        super().__init__(parent)
        self.setAttribute(Qt.WA_DeleteOnClose, True)
        self.setupUi(self)
        self.show()
        self.setWindowTitle("安装插件")
        self.setWindowIconText("卸载插件")
        self.icon = AppIcon()
        self.setWindowIcon(self.icon)
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setWindowModality(Qt.ApplicationModal)
        self.type = 0  # 0 文件 1 地址
        self.init_type()
        self.buttonGroup.buttonClicked.connect(self.btn_type_click_event)
        self.pushButton_choose_file.clicked.connect(self.choose_plugin_file)
        self.pushButton_ok.clicked.connect(self.ok)
        self.pushButton_cancel.clicked.connect(self.close)

        self.plugin_install_finished_signal.connect(self.plugin_install_finished_event)
        # self.plugin_install_finished_signal.emit(True,{})

    def btn_type_click_event(self, button):
        if button == self.radioButton_file:
            self.type = 0
            self.init_type()
        else:
            self.type = 1
            self.edit.setPlaceholderText("选择插件压缩包")
            self.pushButton_choose_file.hide()
            self.pushButton_ok.setProperty()

    def init_type(self):
        self.edit.setPlaceholderText("输入插件包下载地址")
        self.pushButton_choose_file.show()

    def choose_plugin_file(self):
        fileName = QFileDialog.getOpenFileName(self, self.tr("Open Plugin Package"), "",
                                               self.tr("lugin Packages (*.zip)"))
        if fileName[0] != '':
            self.edit.setText(fileName[0])
            pass

    def ok(self):
        self.pushButton_ok.setDisabled(True)
        self.setCursor(Qt.WaitCursor)
        _thread.start_new_thread(self.__ok)

    def __ok(self):
        value = self.edit.text()
        try:
            time.sleep(3)
            if self.type == 0:
                packageInfo = installPlugin.install(value)
            else:
                packageInfo = installPlugin.install(None, value)
            self.plugin_install_finished_signal.emit(True, packageInfo)
        except Exception as e:
            logger.error(e)
            self.plugin_install_finished_signal.emit(False, {})

    def plugin_install_finished_event(self, ret, package_info):
        ret_desc = "成功" if ret else "失败"
        msg = "插件安装{}！\n插件分类：{}，名称:{}，版本号：{}。\n是否立即重新加载？".format(ret_desc, dictUtil.get_value(package_info, "class"),
                                                                 dictUtil.get_value(package_info, "name"),
                                                                 dictUtil.get_value(package_info, "version"))
        self.pushButton_ok.setDisabled(False)
        self.setCursor(Qt.ArrowCursor)
        infoBox = MyQMessageBox(text=msg).add_ok_btn().add_cancel_btn()
        infoBox.exec_()
        if ret:
            if infoBox.clickedButton() == infoBox.get_ok_btn():
                Context().mainWindowImpl.reload_all()
        self.close()
