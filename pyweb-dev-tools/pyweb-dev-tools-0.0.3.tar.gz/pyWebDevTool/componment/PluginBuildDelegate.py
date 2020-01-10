# -*- coding: utf-8 -*-
import threading

from PyQt5.QtCore import Qt, QObject, pyqtSignal
from PyQt5.QtWidgets import QMessageBox

from pyWebDevTool.componment.messageBox import MyQMessageBox
from pyWebDevTool.interfaces import buildPlugin
from pyWebDevTool.util import cmdUtil


class PluginBuildDelegate(QObject):
    plugin_build_finished_signal = pyqtSignal(list)

    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.plugin_build_finished_signal.connect(self.plugin_build_finished_event)

    def build_plugin(self):
        self.parent.setCursor(Qt.WaitCursor)
        threading.Thread(target=self._build_plugin, args=(), daemon=True).start()

    def _build_plugin(self):
        plugin_info = buildPlugin.build()
        # time.sleep(1)
        # plugin_info = []
        self.plugin_build_finished_signal.emit(plugin_info)

    def plugin_build_finished_event(self, plugin_info):
        box = MyQMessageBox(icon=QMessageBox.Information,
                            text="插件构建完毕，本次成功构建{}个插件。".format(len(plugin_info))).add_ok_btn().add_cancel_btn()
        box.get_ok_btn().setText("打开插件目录")
        box.get_cancel_btn().setText("确定")
        box.exec_()
        if box.clickedButton() == box.get_ok_btn():
            cmdUtil.explorer_open(buildPlugin.PLUGIN_DIST_PATH)
        self.parent.setCursor(Qt.ArrowCursor)
