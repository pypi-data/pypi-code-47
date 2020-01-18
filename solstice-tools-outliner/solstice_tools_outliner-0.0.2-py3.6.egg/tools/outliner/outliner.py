#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Tool that allow to manage scene assets for Solstice
"""

from __future__ import print_function, division, absolute_import

__author__ = "Tomas Poveda"
__license__ = "MIT"
__maintainer__ = "Tomas Poveda"
__email__ = "tpovedatd@gmail.com"

import tpDccLib as tp

import artellapipe
from artellapipe.tools.outliner import outliner


class SolsticeOutlinerWidget(outliner.ArtellaOutlinerWidget, object):
    def __init__(self, project, config, parent=None):
        super(SolsticeOutlinerWidget, self).__init__(project=project, config=config, parent=parent)


class SolsticeOutlinerTool(artellapipe.Tool, object):

    def __init__(self, project, config):
        super(SolsticeOutlinerTool, self).__init__(project=project, config=config)

    def ui(self):
        super(SolsticeOutlinerTool, self).ui()

        self._outliner = SolsticeOutlinerWidget(project=self._project, config=self.config)
        self.main_layout.addWidget(self._outliner)

    def post_attacher_set(self):
        """
        Function that is called once an attacher has been set
        """

        self.register_callback(tp.DccCallbacks.NodeSelect, fn=self._outliner.select_asset)
