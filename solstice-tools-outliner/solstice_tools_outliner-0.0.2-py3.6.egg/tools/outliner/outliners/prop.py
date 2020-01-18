#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
Module that contains outliner implementations for Solstice Prop assets
"""

from __future__ import print_function, division, absolute_import

__author__ = "Tomas Poveda"
__license__ = "MIT"
__maintainer__ = "Tomas Poveda"
__email__ = "tpovedatd@gmail.com"

import logging
from functools import partial

from Qt.QtCore import *
from Qt.QtWidgets import *

import tpDccLib as tp

import artellapipe
from artellapipe.utils import resource
from artellapipe.tools.outliner.widgets import baseoutliner

from solstice.core import utils

LOGGER = logging.getLogger()


class SolsticePropsOutliner(baseoutliner.BaseOutliner, object):

    overrideAdded = Signal(object, object)
    overrideRemoved = Signal(object, object)

    def __init__(self, project, parent=None):
        super(SolsticePropsOutliner, self).__init__(project=project, parent=parent)

    def _create_context_menu(self, menu, item):
        replace_icon = resource.ResourceManager().icon('replace')
        delete_icon = resource.ResourceManager().icon('delete')
        override_add_icon = resource.ResourceManager().icon('override_add')
        override_delete_icon = resource.ResourceManager().icon('override_delete')
        override_export_icon = resource.ResourceManager().icon('save')
        load_shaders_icon = resource.ResourceManager().icon('shading_load')
        unload_shaders_icon = resource.ResourceManager().icon('shading_unload')

        replace_menu = QMenu('Replace by', self)
        replace_menu.setIcon(replace_icon)
        show_replace_menu = self._create_replace_actions(replace_menu, item)
        if show_replace_menu:
            menu.addMenu(replace_menu)

        remove_action = QAction(delete_icon, 'Delete', menu)
        menu.addAction(remove_action)
        menu.addSeparator()

        add_override_menu = QMenu('Add Override', menu)
        add_override_menu.setIcon(override_add_icon)
        valid_override = self._create_add_override_menu(add_override_menu, item)
        if valid_override:
            menu.addMenu(add_override_menu)

        remove_override_menu = QMenu('Remove Override', menu)
        remove_override_menu.setIcon(override_delete_icon)
        has_overrides = self._create_remove_override_menu(remove_override_menu, item)
        if has_overrides:
            menu.addMenu(remove_override_menu)

        save_override_menu = QMenu('Save Overrides', menu)
        save_override_menu.setIcon(override_export_icon)
        export_overrides = self._create_save_override_menu(save_override_menu, item)
        if export_overrides:
            menu.addMenu(save_override_menu)

        if valid_override or has_overrides or export_overrides:
            menu.addSeparator()

        load_shaders_action = QAction(load_shaders_icon, 'Load Shaders', menu)
        unload_shaders_action = QAction(unload_shaders_icon, 'Unload Shaders', menu)
        menu.addAction(load_shaders_action)
        menu.addAction(unload_shaders_action)

        remove_action.triggered.connect(partial(self._on_remove, item))
        load_shaders_action.triggered.connect(partial(self._on_load_shaders, item))
        unload_shaders_action.triggered.connect(partial(self._on_unload_shaders, item))

    def _create_replace_actions(self, replace_menu, item):
        """
        Internal function that creates replacement options for current file
        :param replace_menu: QMenu
        :return: bool
        """

        rig_icon = resource.ResourceManager().icon('rig')
        alembic_icon = resource.ResourceManager().icon('alembic')

        rig_action = QAction(rig_icon, 'Rig', replace_menu)
        gpu_cache_action = QAction(alembic_icon, 'Gpu Cache', replace_menu)
        replace_menu.addAction(rig_action)
        replace_menu.addAction(gpu_cache_action)

        rig_replace_menu = QMenu()
        rig_action.setMenu(rig_replace_menu)
        rig_root_control_action = QAction('Root Control', replace_menu)
        rig_main_control_action = QAction('Main Control', replace_menu)
        rig_replace_menu.addAction(rig_root_control_action)
        rig_replace_menu.addAction(rig_main_control_action)

        gpu_cache_replace_menu = QMenu()
        gpu_cache_action.setMenu(gpu_cache_replace_menu)
        gpu_cache_root_control_action = QAction('Root Control', replace_menu)
        gpu_cache_main_control_action = QAction('Main Control', replace_menu)
        gpu_cache_replace_menu.addAction(gpu_cache_root_control_action)
        gpu_cache_replace_menu.addAction(gpu_cache_main_control_action)

        if item.asset_node.is_rig():
            rig_action.setEnabled(False)
        if item.asset_node.is_gpu_cache():
            gpu_cache_action.setEnabled(False)

        rig_root_control_action.triggered.connect(partial(self._on_replace_rig, item, 'root_ctrl'))
        rig_main_control_action.triggered.connect(partial(self._on_replace_rig, item, 'main_ctrl'))
        gpu_cache_root_control_action.triggered.connect(partial(self._on_replace_gpu_cache, item, 'root_ctrl'))
        gpu_cache_main_control_action.triggered.connect(partial(self._on_replace_gpu_cache, item, 'main_ctrl'))

        return replace_menu

    def _on_load_shaders(self, item):
        """
        Internal callback function that is called when Load Shaders context action is triggered
        """

        item.asset_node.load_shaders()

    def _on_unload_shaders(self, item):
        """
        Internal callback function that is called when Unload Shaders context action is triggered
        """

        item.asset_node.unload_shaders()

    def _on_replace_rig(self, item, rig_control=None):
        """
        Internal callback function that is called when an asset is replaced by a rig
        :param item: OutlinerAssetItem
        :param rig_control: str
        """

        valid_replace = item.asset_node.replace_by_rig(rig_control=rig_control)
        if not valid_replace:
            return False

        self.refresh()

        return True

        # if not rig_control:
        #     rig_control = 'root_ctrl'
        #
        # if item.asset_node.is_rig():
        #     LOGGER.warning('You have already rig file of the asset loaded!')
        #
        # rig_file_class = artellapipe.FilesMgr().get_file_class('rig')
        # if not rig_file_class:
        #     LOGGER.warning('Impossible to reference rig file because Rig File Class (rig) was not found!')
        #     return
        #
        # current_matrix = tp.Dcc.node_matrix(item.asset_node.node)
        #
        # rig_file = rig_file_class(item.asset_node.asset)
        # ref_nodes = rig_file.import_file(reference=True)
        # if not ref_nodes:
        #     LOGGER.warning('No nodes imported into current scene for rig file!')
        #     return None
        #
        # root_ctrl = None
        # for node in ref_nodes:
        #     root_ctrl = utils.get_control(node=node, rig_control=rig_control)
        #     if root_ctrl:
        #         break
        # if not root_ctrl:
        #     return False
        #
        # tp.Dcc.set_node_matrix(root_ctrl, current_matrix)
        # item.asset_node.remove()
        # self.refresh()
        #
        # return True

    def _on_replace_gpu_cache(self, item, rig_control=None):
        """
        Internal callback function that is called when an asset is replaced by a rig
        :param item: OutlinerAssetItem
        :param rig_control: str
        """

        valid_replace = item.asset_node.replace_by_gpu_cache(rig_control=rig_control)
        if not valid_replace:
            return False

        self.refresh()

        return True

        # if not rig_control:
        #     rig_control = 'root_ctrl'
        #
        # main_ctrl = item.asset_node.get_control(rig_control)
        # if not main_ctrl:
        #     LOGGER.warning('No Main Control found for Asset Node: {}'.format(item.asset_node.node))
        #     return False
        #
        # main_world_translate = tp.Dcc.node_world_space_translation(main_ctrl)
        # main_world_rotation = tp.Dcc.node_world_space_rotation(main_ctrl)
        # main_world_scale = tp.Dcc.node_world_space_scale(main_ctrl)
        #
        # if item.asset_node.is_gpu_cache():
        #     LOGGER.warning('You have already gpu cache file of the asset loaded!')
        #
        # gpu_cache_file_class = artellapipe.FilesMgr().get_file_class('gpualembic')
        # if not gpu_cache_file_class:
        #     LOGGER.warning('Impossible to import gpu cache file because Rig File Class (rig) was not found!')
        #     return False
        #
        # gpu_cache_file = gpu_cache_file_class(item.asset_node.asset)
        # ref_nodes = gpu_cache_file.import_file()
        # if not ref_nodes:
        #     LOGGER.warning('No nodes imported into current scene for gpu cache file!')
        #     return False
        #
        # if isinstance(ref_nodes, (list, tuple)):
        #     gpu_cache_node = ref_nodes[0]
        # else:
        #     gpu_cache_node = ref_nodes
        #
        # tp.Dcc.translate_node_in_world_space(gpu_cache_node, main_world_translate)
        # tp.Dcc.rotate_node_in_world_space(gpu_cache_node, main_world_rotation)
        # tp.Dcc.scale_node_in_world_space(gpu_cache_node, main_world_scale)
        #
        # item.asset_node.remove()
        # self.refresh()
        #
        # return True
