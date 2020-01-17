# -*- coding: utf-8 -*-

"""
Tool to export/import shader files
"""

from __future__ import print_function, division, absolute_import

__author__ = "Tomas Poveda"
__license__ = "MIT"
__maintainer__ = "Tomas Poveda"
__email__ = "tpovedatd@gmail.com"

from tpQtLib.core import base
from tpQtLib.widgets import tabs

import artellapipe
from artellapipe.tools.shadersmanager.widgets import shaderslibrary, assetsviewer


class ShadersManager(artellapipe.Tool, object):

    def __init__(self, project, config):
        super(ShadersManager, self).__init__(project=project, config=config)

    def ui(self):
        super(ShadersManager, self).ui()

        self._shaders_widget = ShadersWidget(project=self._project, config=self._config)
        self.main_layout.addWidget(self._shaders_widget)


class ShadersWidget(base.BaseWidget, object):
    def __init__(self, project, config, parent=None):
        self._project = project
        self._config = config
        super(ShadersWidget, self).__init__(parent=parent)

    def ui(self):
        super(ShadersWidget, self).ui()

        tab = tabs.TearOffTabWidget()
        self.main_layout.addWidget(tab)
        tab.setTabsClosable(False)

        self._shaders_library = shaderslibrary.ArtellaShadersLibrary(project=self._project)
        self._assets_viewer = assetsviewer.ArtellaAssetShadersViewer(project=self._project)

        tab.addTab(self._assets_viewer, 'Assets')
        tab.addTab(self._shaders_library, 'Library')
