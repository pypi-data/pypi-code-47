#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
Module that contains functions and classes related with Maya menus
"""

from __future__ import print_function, division, absolute_import


import tpDccLib
from tpDccLib.abstract import menu as abstract_menu


class HoudiniMenu(abstract_menu.AbstractMenu, object):
    def __init__(self, name='HoudiniMenu'):
        super(HoudiniMenu, self).__init__()

        self.name = name

    def create_menu(self, file_path=None, parent_menu=None):
        """
        Creates a new DCC menu app
        If file path is not given the menu is created without items
        :param name: str, name for the menu
        :param file_path: str, path where JSON menu file is located
        :param parent_menu: str, Name of the menu to append this menu to
        :return: variant, nativeMenu || None
        """

        return


tpDccLib.Menu = HoudiniMenu
