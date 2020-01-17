#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Module that contains manager that handles Artella Project Maya Menu
"""

from __future__ import print_function, division, absolute_import

__author__ = "Tomas Poveda"
__license__ = "MIT"
__maintainer__ = "Tomas Poveda"
__email__ = "tpovedatd@gmail.com"

import logging
from functools import partial

from six import string_types

from Qt.QtWidgets import *

import tpDccLib as tp
from tpPyUtils import decorators
from tpQtLib.core import menu

import artellapipe
import artellapipe.register
from artellapipe.managers import menu as core_menu
from artellapipe.utils import resource

LOGGER = logging.getLogger()


class ArtellaMayaMenuManager(core_menu.ArtellaMenuManager, object):
    def __init__(self):
        super(ArtellaMayaMenuManager, self).__init__()

    def create_main_menu(self):
        self._menu = menu.SearchableMenu(
            objectName=self._menu_object_name, title=self._menu_name, parent=self._get_parent_menubar())
        self._get_parent_menubar().addMenu(self._menu)
        self._menu.setObjectName(self._menu_object_name)
        self._menu.setTearOffEnabled(True)

    def create_tray_menu(self):
        self._tray_menu = QMenu(parent=self._get_parent_menubar())
        self._tray_menu.setIcon(self._project.tray_icon)
        self._get_parent_menubar().addMenu(self._tray_menu)
        self._tray_menu.setObjectName(self._tray_object_menu_name)
        self._tray_menu.setTearOffEnabled(True)

        tray_children = self._project.config.get('tray', 'children', default=list())
        for child in tray_children:
            item_lbl = child.get('label', '')
            item_command = child.get('command', '')
            item_icon_name = child.get('icon', '')
            item_tip = child.get('tip', '')
            if not item_lbl:
                continue
            if item_lbl == 'separator':
                self._tray_menu.addSeparator()
            else:
                item_icon = resource.ResourceManager().icon(item_icon_name)
                if item_icon and not item_icon.isNull():
                    new_item = QAction(item_icon, item_lbl, self._tray_menu)
                else:
                    new_item = QAction(self._tray_menu, text=item_lbl)
                if item_command:
                    new_item.triggered.connect(partial(self._launch_command, item_command))
                if item_tip:
                    new_item.setToolTip(item_tip)
                    new_item.setStatusTip(item_tip)
                self._tray_menu.addAction(new_item)

    def create_project_description_menu(self):
        description = '|      [{}]'.format(self._project.get_environment())
        self._project_description_menu = QMenu(description, parent=self._get_parent_menubar())
        self._get_parent_menubar().addMenu(self._project_description_menu)
        self._project_description_menu.setObjectName(self._project_description_menu_name)
        self._project_description_menu.setTearOffEnabled(False)

    def create_bug_tracker_action(self):
        self._bug_tracker_action = QAction(self._get_parent_menubar())
        self._bug_tracker_action.setIcon(resource.ResourceManager().icon('bug'))
        self._get_parent_menubar().addAction(self._bug_tracker_action)
        self._bug_tracker_action.setObjectName(self._bug_object_action_name)
        self._bug_tracker_action.triggered.connect(partial(self._launch_tool_by_name, 'bugtracker'))

    def get_menu_names(self):
        """
        Returns a list with the names of the created menus
        :return: list
        """

        return [self._menu_object_name, self._tray_object_menu_name, self._bug_object_action_name,
                self._project_description_menu_name]

    def clean_menus(self):
        """
        Removes all already existing menus
        :return: bool
        """

        if not self._parent:
            return False

        if not self._menu_name or not self._menu_object_name:
            LOGGER.warning('Impossible to clean menus because menu info is not initialized!')
            return False

        for child_widget in self._get_parent_menubar().children():
            if child_widget.objectName() in self.get_menu_names():
                LOGGER.debug('Removing old "{}" menu ...'.format(self._project.name, child_widget.objectName()))
                child_widget.deleteLater()

        return True

    def get_menu(self, menu_name):
        """
        Returns the menu object if extsi; otherwise None
        :param str menu_name: name of the menu to get
        :return: QMenu
        """

        if menu_name == self._menu.objectName():
            return self._menu

        return self._sub_menus.get(menu_name)

    def create_menus(self):
        """
        Creates all the menus
        """

        if not self._project:
            LOGGER.warning("Impossible to create menus because project is not defined!")
            return False

        if tp.Dcc == tp.Dccs.Unknown or not self._parent:
            return

        self.clean_menus()
        self.create_project_description_menu()
        self.create_main_menu()

        menus_config = self.config.get('menus', default=list())
        if menus_config:
            for menu_data in menus_config:
                for _, data in menu_data.items():
                    for i in iter(data):
                        if isinstance(i, string_types) and i == 'separator':
                            self._menu.addSeparator()
                            continue
                        self._menu_creator(self._menu, i)

        # Tools Menus
        tools_menu_data = artellapipe.ToolsMgr().get_tool_menus() or dict()
        for tool_path, data in tools_menu_data.items():
            for i in iter(data):
                if isinstance(i, string_types) and i == 'separator':
                    self._menu.addSeparator()
                    continue
                self._menu_creator(self._menu, i)

        self.create_tray_menu()
        self.create_bug_tracker_action()

        return True

    def _menu_creator(self, parent_menu, data):
        menu = self.get_menu(data['label'])
        if menu is None and data.get('type', '') == 'menu':
            only_dev = data.get('only_dev', False)
            if only_dev and not self._project.is_dev():
                return
            menu = parent_menu.addMenu(data['label'])
            menu.setObjectName(data['label'])
            menu.setTearOffEnabled(True)
            self._sub_menus[data['label']] = menu

        if 'children' not in data:
            return

        for i in iter(data['children']):
            action_type = i.get('type', 'command')
            only_dev = i.get('only_dev', False)
            if only_dev and not self._project.is_dev():
                continue
            if action_type == 'separator':
                self._menu.addSeparator()
                continue
            elif action_type == 'group':
                sep = self._menu.addSeparator()
                sep.setText(i['label'])
                continue
            elif action_type == 'menu':
                self._menu_creator(menu, i)
                continue
            self._add_action(i, menu)

    def _add_action(self, item_info, parent):

        item_type = item_info.get('type', 'tool')
        if item_type == 'tool':
            self._add_tool_action(item_info, parent)
        else:
            self._add_menu_item_action(item_info, parent)

    def _add_menu_item_action(self, item_info, parent):
        menu_item_id = item_info.get('id', None)

        menu_item_ui = item_info.get('ui', None)
        if not menu_item_ui:
            LOGGER.warning('Menu Item "{}" has not a ui specified!. Skipping ...'.format(menu_item_id))
            return
        menu_item_command = item_info.get('command', None)
        if not menu_item_command:
            LOGGER.warning('Menu Item "{}" does not defines a command to execute. Skipping ...'.format(menu_item_id))
            return
        menu_item_language = item_info.get('language', 'python')

        menu_item_icon_name = menu_item_ui.get('icon', 'artella')
        menu_item_icon = resource.ResourceManager().icon(menu_item_icon_name)
        menu_item_label = menu_item_ui.get('label', 'No_label')
        is_checkable = menu_item_ui.get('is_checkable', False)
        is_checked = menu_item_ui.get('is_checked', False)
        tagged_action = menu.SearchableTaggedAction(label=menu_item_label, icon=menu_item_icon, parent=self._parent)
        if is_checkable:
            tagged_action.setCheckable(is_checkable)
            tagged_action.setChecked(is_checked)
            tagged_action.connect(partial(self._launch_command, menu_item_command, menu_item_language))
            tagged_action.toggled.connect(partial(self._launch_command, menu_item_command, menu_item_language))
            if menu_item_ui.get('load_on_startup', False):
                self._launch_command(menu_item_command, menu_item_language, is_checked)
        else:
            tagged_action.triggered.connect(partial(self._launch_command, menu_item_command, menu_item_language))
            if menu_item_ui.get('load_on_startup', False):
                self._launch_command(menu_item_command, menu_item_language)

        tagged_action.tags = set(item_info.get('tags', []))

        parent.addAction(tagged_action)

    def _add_tool_action(self, item_info, parent):
        tool_id = item_info.get('id', None)
        tool_type = item_info.get('type', 'tool')

        tool_data = artellapipe.ToolsMgr().get_tool_data_from_id(tool_id)
        if tool_data is None:
            LOGGER.warning('Menu : Failed to find Tool: {}, type {}'.format(tool_id, tool_type))
            return

        tool_icon = None
        tool_icon_name = tool_data['config'].data.get('icon', None)
        if tool_icon_name:
            tool_icon = resource.ResourceManager().icon(tool_icon_name)
        tool_menu_ui_data = tool_data['config'].data.get('menu_ui', {})
        label = tool_menu_ui_data.get('label', 'No_label')
        tagged_action = menu.SearchableTaggedAction(label=label, icon=tool_icon, parent=self._parent)
        is_checkable = tool_menu_ui_data.get('is_checkable', False)
        is_checked = tool_menu_ui_data.get('is_checked', False)
        if is_checkable:
            tagged_action.setCheckable(is_checkable)
            tagged_action.setChecked(is_checked)
            tagged_action.connect(partial(self._launch_tool, tool_data))
            tagged_action.toggled.connect(partial(self._launch_tool_by_id, tool_id))
        else:
            tagged_action.triggered.connect(partial(self._launch_tool_by_id, tool_id))

        icon = tool_menu_ui_data.get('icon', None)
        if icon:
            pass

        tagged_action.tags = set(tool_data['config'].data.get('tags', []))

        parent.addAction(tagged_action)

    def _get_parent_menubar(self):
        if not self._parent:
            return None

        if hasattr(self._parent, 'menuBar'):
            return self._parent.menuBar()
        else:
            menubars = self._parent.findChildren(QMenuBar)
            if not menubars:
                return None
            return menubars[0]


@decorators.Singleton
class ArtellaMayaMenuManagerSingleton(ArtellaMayaMenuManager, object):
    def __init__(self):
        ArtellaMayaMenuManager.__init__(self)


if tp.is_maya():
    artellapipe.register.register_class('Menu', ArtellaMayaMenuManager)
    artellapipe.register.register_class('MenuMgr', ArtellaMayaMenuManagerSingleton)
