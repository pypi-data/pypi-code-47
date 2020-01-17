#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
Module that contains generic functionality when dealing with projects
"""

from __future__ import print_function, division, absolute_import

import os

from Qt.QtCore import *
from Qt.QtWidgets import *
from Qt.QtGui import *

import tpDccLib as tp
import tpQtLib
from tpPyUtils import path, folder, fileio, settings
from tpDccLib.core import consts


class ProjectData(object):
    def __init__(self, name, project_path, settings, options):
        self._name = name
        self._project_path = project_path
        self._settings = settings
        self._options = options

    def get_name(self):
        return self._name

    def get_path(self):
        return self._project_path

    def get_full_path(self):
        return path.join_path(self._project_path, self._name)

    def get_settings(self):
        return self._settings

    def get_options(self):
        return self._options

    name = property(get_name)
    project_path = property(get_path)
    full_path = property(get_full_path)
    settings = property(get_settings)
    options = property(get_options)

    def get_project_file(self):
        """
        Returns path where project file is located
        :return: str
        """

        return path.join_path(self.full_path, consts.PROJECTS_NAME)

    def get_options_file(self):
        """
        Returns path where project options file is located
        :return:
        """

        self._setup_options()

        return self.options.get_file()

    def has_options(self):
        """
        Returns whether the project has options or not
        :return: bool
        """

        self._setup_options()

        return self.options.has_settings()

    def has_option(self, name, group=None):
        """
        Returns whether the project has given option or not
        :param name: str, name of the option
        :param group: variant, str || None, group of the option (optional)
        :return: bool
        """

        self._setup_options()

        if group:
            name = '{}.{}'.format(group, name)
        else:
            name = str(name)

        return self.options.has_setting(name)

    def add_option(self, name, value, group=None, option_type=None):
        """
        Adds a new option to the project options file
        :param name: str, name of the option
        :param value: variant, value of the option
        :param group: variant, str || None, group of the option (optional)
        :param option_type: variant, str || None, option type (optional)
        """

        self._setup_options()

        if group:
            name = '{}.{}'.format(group, name)
        else:
            name = str(name)

        if option_type == 'script':
            value = [value, 'script']

        self.options.set(name, value)

    def set_option(self, name, value, group=None):
        """
        Set an option of the option settings file. If the option does not exist, it will be created
        :param name: str, name of the option we want to set
        :param value: variant, value of the option
        :param group: variant, str || None, group of the option (optional)
        """

        if group:
            name = '{}.{}'.format(group, name)
        else:
            name = str(name)

        self.options.set(name, value)

    def get_unformatted_option(self, name, group=None):
        """
        Returns option without format (string format)
        :param name: str, name of the option we want to retrieve
        :param group: variant, str || None, group of the option (optional)
        :return: str
        """

        self._setup_options()

        if group:
            name = '{}.{}'.format(group, name)
        else:
            name = str(name)

        value = self.options.get(name)

        return value

    def get_option(self, name, group=None):
        """
        Returns option value with proper format (to force string use get_unformatted_option function)
        :param name: str, name of the option we want to retrieve
        :param group: variant, str || None, group of the option (optional)
        :return: variante
        """

        self._setup_options()

        value = self.get_unformatted_option(name, group)
        new_value = None

        try:
            new_value = eval(value)
        except Exception:
            pass

        if value is None:
            tp.logger.warning('Impossible to access option with proper format from {}'.format(self.options.directory))
            if group:
                tp.logger.warning('Could not find option: "{}" in group: "{}"'.format(name, group))
            else:
                tp.logger.warning('Could not find option: {}'.format(name))

        if type(new_value) == list or type(new_value) == tuple or type(new_value) == dict:
            value = new_value
        if type(value) == str or type(value) == unicode:
            if value.find(',') > -1:
                value = value.split(',')

        tp.logger.debug('Accessed Project Option - Option: "{}" | Group: "{}" | Value: "{}"'.format(name, group, value))

        return value

    def get_option_match(self, name, return_first=True):
        self._setup_options()
        options_dict = self.options.settings_dict
        found = dict()
        for key in options_dict:
            if key.endswith(name):
                if return_first:
                    tp.logger.debug('Accessed - Option: {}, value: {}'.format(name, options_dict[key]))
                found[name] = options_dict[key]

        return found

    def get_options(self):
        """
        Returns all optiosn contained in the settings file
        :return: str
        """

        self._setup_options()
        options = list()
        if self.options:
            options = self.options.get_settings()

        return options

    def clear_options(self):
        """
        Clears all the options of the task
        """

        if self.options:
            self.options.clear()

    def get_project_image(self):
        """
        Returns the image used by the project
        :return: QPixmap
        """

        from tpQtLib.core import image

        if not self._settings:
            self._load_project()

        project_file = self.get_project_file()
        if not self._settings.has_settings():
            tp.logger.warning('No valid project data found on Project Data File: {}'.format(project_file))

        encoded_image = self._settings.get('image')
        if not encoded_image:
            return

        encoded_image = encoded_image.encode('utf-8')
        return QPixmap.fromImage(image.base64_to_image(encoded_image))

    def update_project(self):

        if not self._settings:
            self._load_project()

        project_file = self.get_project_file()
        if not self._settings.has_settings():
            tp.logger.warning('No valid project data found on Project Data File: {}'.format(project_file))

        self._name = self._settings.get('name')
        self._project_path = path.get_dirname(path.get_dirname(project_file))

    def set_project_image(self, image_path):
        """
        Updates project image icon
        :param image_path: str, path that points to the image of the new project icon
        """

        from tpQtLib.core import image

        if not os.path.isfile(image_path):
            tp.logger.warning('Given image path "{}" is not valid!'.format(image_path))
            return False

        if not self._settings:
            self._load_project()

        project_file = self.get_project_file()
        if not self._settings.has_settings():
            tp.logger.warning('No valid project data found on Project Data File: {}'.format(project_file))

        self._settings.set('image', image.image_to_base64(image_path))

        return True

    def create_project(self):
        project_full_path = self.full_path
        if path.is_dir(project_full_path):
            tp.logger.warning('Project Path {} already exists! Choose another one ...'.format(project_full_path))
            return

        folder.create_folder(name=self.name, directory=self.project_path)
        self._set_default_settings()

        return self

    def create_folder(self, name, relative_path=None):
        if relative_path is None:
            folder.create_folder(name=name, directory=self.full_path)
        else:
            folder.create_folder(name=name, directory=path.join_path(self.full_path, relative_path))
    # endregion

    # region Private Functions
    def _load_project(self):
        self._set_default_settings()
        self._setup_options()

    def _set_settings_path(self, folder_path):
        if not self._settings:
            self._load_project()

        project_file_path = self.get_project_file()
        project_file = path.get_basename(project_file_path)
        self._settings.set_directory(folder_path, project_file)

    def _set_options_path(self, folder_path):
        if not self._options:
            self._load_project()

        self._options.set_directory(folder_path, 'options.json')

    def _set_default_settings(self):

        from tpQtLib.core import image

        project_file_path = self.get_project_file()
        project_path = path.get_dirname(project_file_path)
        self._settings = settings.JSONSettings()
        self._set_settings_path(project_path)
        self._settings.set('version', '0.0.0')
        self._settings.set('name', self.name)
        self._settings.set('path', self.project_path)
        self._settings.set('full_path', self.full_path)
        self._settings.set('image', image.image_to_base64(tpQtLib.resource.get('icons', 'rignode_icon') + '.png'))

    def _setup_options(self):

        if not self._options:
            self._options = settings.JSONSettings()

        self._options.set_directory(os.path.dirname(self.get_project_file()), 'options.json')
    # endregion


class Project(QWidget, ProjectData):
    projectOpened = Signal(object)
    projectRemoved = Signal()
    projectImageChanged = Signal(str)

    def __init__(self, name, project_path, settings=None, options=None, parent=None):
        ProjectData.__init__(self, name=name, project_path=project_path, settings=settings, options=options)
        QWidget.__init__(self, parent=parent)

        self.setMaximumWidth(160)
        self.setMaximumHeight(200)

        self.main_layout = QVBoxLayout()
        self.main_layout.setContentsMargins(0, 0, 0, 0)
        self.main_layout.setSpacing(0)
        self.setLayout(self.main_layout)

        widget_layout = QVBoxLayout()
        widget_layout.setContentsMargins(0, 0, 0, 0)
        widget_layout.setSpacing(0)
        main_frame = QFrame()
        main_frame.setFrameStyle(QFrame.StyledPanel | QFrame.Raised)
        main_frame.setLineWidth(1)
        main_frame.setLayout(widget_layout)
        self.main_layout.addWidget(main_frame)

        self.project_btn = QPushButton('', self)
        self.project_btn.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.project_btn.setIconSize(QSize(120, 120))
        project_lbl = QLabel(self.name)
        project_lbl.setStyleSheet('background-color:rgba(0, 0, 0, 150);')
        project_lbl.setAlignment(Qt.AlignCenter)
        widget_layout.addWidget(self.project_btn)
        widget_layout.addWidget(project_lbl)

        self.setup_signals()

    def contextMenuEvent(self, event):
        menu = QMenu(self)
        remove_icon = tpQtLib.resource.icon(name='delete', extension='png')
        remove_action = QAction(remove_icon, 'Remove', menu)
        remove_action.setStatusTip(consts.DELETE_PROJECT_TOOLTIP)
        remove_action.setToolTip(consts.DELETE_PROJECT_TOOLTIP)
        remove_action.triggered.connect(self._on_remove_project)

        folder_icon = tpQtLib.resource.icon(name='open_folder', extension='png')
        folder_action = QAction(folder_icon, 'Open in Browser', menu)
        folder_action.setStatusTip(consts.OPEN_PROJECT_IN_EXPLORER_TOOLTIP)
        folder_action.setToolTip(consts.OPEN_PROJECT_IN_EXPLORER_TOOLTIP)
        folder_action.triggered.connect(self._on_open_in_browser)

        image_icon = tpQtLib.resource.icon(name='picture', extension='png')
        set_image_action = QAction(image_icon, 'Set Project Image', menu)
        set_image_action.setToolTip(consts.SET_PROJECT_IMAGE_TOOLTIP)
        set_image_action.setStatusTip(consts.SET_PROJECT_IMAGE_TOOLTIP)
        set_image_action.triggered.connect(self._on_set_project_image)

        for action in [remove_action, None, folder_action, None, set_image_action]:
            if action is None:
                menu.addSeparator()
            else:
                menu.addAction(action)

        menu.exec_(self.mapToGlobal(event.pos()))

    def setup_signals(self):
        self.project_btn.clicked.connect(self._on_open_project)

    @classmethod
    def create_project_from_data(cls, project_data_path):
        """
        Creates a new project using a project data JSON file
        :param project_data_path: str, path where project JSON data file is located
        :return: Project
        """

        if project_data_path is None or not path.is_file(project_data_path):
            tp.logger.warning('Project Data Path {} is not valid!'.format(project_data_path))
            return None

        project_data = settings.JSONSettings()
        project_options = settings.JSONSettings()
        project_dir = path.get_dirname(project_data_path)
        project_name = path.get_basename(project_data_path)
        project_data.set_directory(project_dir, project_name)
        project_options.set_directory(project_dir, 'options.json')
        if not project_data or not project_data.has_settings():
            tp.logger.warning('No valid project data found on Project Data File: {}'.format(project_data_path))

        project_name = project_data.get('name')
        project_path = path.get_dirname(path.get_dirname(project_data_path))
        project_image = project_data.get('image')

        tp.logger.debug('New Project found [{}]: {}'.format(project_name, project_path))
        new_project = cls(name=project_name, project_path=project_path, settings=project_data,
                              options=project_options)
        if project_image:
            new_project.set_image(project_image)

        return new_project

    def open(self):
        """
        Opens project
        """

        self._on_open_project()

    def set_image(self, encoded_image):

        from tpQtLib.core import image

        if not encoded_image:
            return

        encoded_image = encoded_image.encode('utf-8')
        self.project_btn.setIcon(QIcon(QPixmap.fromImage(image.base64_to_image(encoded_image))))

    def remove(self):

        from tpQtLib.core import qtutils

        if not path.is_dir(self.full_path):
            tp.logger.warning('Impossible to remove Project Path: {}'.format(self.full_path))
            return False

        project_name = self.name
        project_path = self.project_path

        result = qtutils.get_permission(message='Are you sure you want to delete project: {}'.format(self.name),
                                        title='Deleting Project', cancel=False)
        if not result:
            return

        valid_delete = folder.delete_folder(folder_name=project_name, directory=project_path)
        if valid_delete is None:
            return False

        return True

    def load_project_data(self):
        """
        Return dictionary data contained in the project
        :return: dict
        """

        if not self.settings:
            return

        return self.settings.data()

    def get_project_nodes(self):
        """
        Returns path where nodes should be stored
        :return: str
        """

        return [os.path.join(self.full_path, 'nodes'), os.path.join(self.full_path, 'components')]
    # endregion

    # region Private Functions
    def _on_open_project(self):
        tp.logger.debug('Loading project "{}" ...'.format(self.full_path))
        self.projectOpened.emit(self)

    def _on_remove_project(self):
        valid_remove = self.remove()
        if valid_remove:
            self.projectRemoved.emit()

    def _on_open_in_browser(self):
        fileio.open_browser(self.full_path)

    def _on_set_project_image(self):
        image_file = tp.Dcc.select_file_dialog(
            title='Select Project Image File',
            pattern="PNG Files (*.png)")

        if image_file is None or not path.is_file(image_file):
            tp.logger.warning('Selected Image "{}" is not valid!'.format(image_file))
            return

        valid_change = self.set_project_image(image_file)

        if valid_change:
            self.projectImageChanged.emit(image_file)
