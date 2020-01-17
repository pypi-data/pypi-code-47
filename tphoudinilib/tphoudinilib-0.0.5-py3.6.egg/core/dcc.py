#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
Module that contains DCC functionality for Houdini
"""

from __future__ import print_function, division, absolute_import

from Qt.QtWidgets import *

import hou
import hdefereval

import tpDccLib
from tpDccLib.abstract import dcc as abstract_dcc
from tpHoudiniLib.core import helpers, gui


class HoudiniDcc(abstract_dcc.AbstractDCC, object):

    class DialogResult(object):
        Yes = QMessageBox.Yes
        No = QMessageBox.No
        Cancel = QMessageBox.Cancel
        Close = QMessageBox.Close

    @staticmethod
    def get_name():
        """
        Returns the name of the DCC
        :return: str
        """

        return tpDccLib.Dccs.Houdini

    @staticmethod
    def get_extensions():
        """
        Returns supported extensions of the DCC
        :return: list(str)
        """

        return ['.hip', '.hiplc', '.hipnc', '.hip*']

    @staticmethod
    def get_dpi(value=1):
        """
        Returns current DPI used by DCC
        :param value: float
        :return: float
        """

        return 1.0

    @staticmethod
    def get_dpi_scale(value):
        """
        Returns current DPI scale used by DCC
        :return: float
        """

        return 1.0

    @staticmethod
    def get_version():
        """
        Returns version of the DCC
        :return: int
        """

        return helpers.get_houdini_version(as_string=False)

    @staticmethod
    def get_version_name():
        """
        Returns version of the DCC
        :return: int
        """

        return helpers.get_houdini_version(as_string=True)

    @staticmethod
    def get_main_window():
        """
        Returns Qt object that references to the main DCC window
        :return:
        """

        return gui.get_houdini_window()

    @staticmethod
    def execute_deferred(fn):
        """
        Executes given function in deferred mode
        """

        hdefereval.executeDeferred(fn)

    @staticmethod
    def object_exists(node):
        """
        Returns whether given object exists or not
        :return: bool
        """

        hou_node = hou.node(node)
        if hou_node:
            return True

        return False

    @staticmethod
    def node_name(node):
        """
        Returns the name of the given node
        :param node: str
        :return: str
        """

        return node.name()

    @staticmethod
    def selected_nodes(full_path=True):
        """
        Returns a list of selected nodes
        :param full_path: bool
        :return: list<hou.Node>
        """

        return hou.selectedNodes(True)

    @staticmethod
    def node_short_name(node):
        """
        Returns short name of the given node
        :param node: str
        :return: str
        """

        return node

    @staticmethod
    def scene_name():
        """
        Returns the name of the current scene
        :return: str
        """

        return hou.hipFile.name()

    @staticmethod
    def scene_path():
        """
        Returns the path of the current scene
        :return: str
        """

        return hou.hipFile.path()

    @staticmethod
    def confirm_dialog(title, message, button=None, cancel_button=None, default_button=None, dismiss_string=None):
        """
        Shows DCC confirm dialog
        :param title:
        :param message:
        :param button:
        :param cancel_button:
        :param default_button:
        :param dismiss_string:
        :return:
        """

        return QMessageBox.question(HoudiniDcc.get_main_window(), title, message)

    @staticmethod
    def warning(message):
        """
        Prints a warning message
        :param message: str
        :return:
        """

        QMessageBox.warning(HoudiniDcc.get_main_window(), 'Warning', message)

    @staticmethod
    def shelf_exists(shelf_name):
        """
        Returns whether given shelf already exists or not
        :param shelf_name: str
        :return: bool
        """

        return gui.shelf_exists(shelf_name=shelf_name)

    @staticmethod
    def create_shelf(shelf_name, shelf_label=None):
        """
        Creates a new shelf with the given name
        :param shelf_name: str
        :param shelf_label: str
        """

        return gui.create_shelf(shelf_name=shelf_name, shelf_label=shelf_label)

    @staticmethod
    def select_file_dialog(title, start_directory=None, pattern=None):
        """
        Shows select file dialog
        :param title: str
        :param start_directory: str
        :param pattern: str
        :return: str
        """

        return hou.ui.selectFile(start_directory=start_directory, title=title, pattern=pattern)

    @staticmethod
    def get_current_frame():
        """
        Returns current frame set in time slider
        :return: int
        """

        return gui.get_current_frame()

    @staticmethod
    def get_time_slider_range():
        """
        Return the time range from Maya time slider
        :return: list<int, int>
        """

        return gui.get_time_slider_range()


tpDccLib.Dcc = HoudiniDcc
