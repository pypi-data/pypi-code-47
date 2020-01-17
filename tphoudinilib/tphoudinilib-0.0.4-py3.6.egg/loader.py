#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
Initialization module for tpHoudiniLib
"""

from __future__ import print_function, division, absolute_import

import os
import inspect

# Do not remove Houdini imports
import hou

from tpPyUtils import importer

# =================================================================================

logger = None

# =================================================================================


class tpHoudiniLib(importer.Importer, object):
    def __init__(self, *args, **kwargs):
        super(tpHoudiniLib, self).__init__(module_name='tpHoudiniLib', *args, **kwargs)

    def get_module_path(self):
        """
        Returns path where tpHoudiniLib module is stored
        :return: str
        """

        try:
            mod_dir = os.path.dirname(inspect.getframeinfo(inspect.currentframe()).filename)
        except Exception:
            try:
                mod_dir = os.path.dirname(__file__)
            except Exception:
                try:
                    import tpDccLib
                    mod_dir = tpDccLib.__path__[0]
                except Exception:
                    return None

        return mod_dir


def init_dcc(do_reload=False):
    """
    Initializes module
    :param do_reload: bool, Whether to reload modules or not
    """

    tphoudini_importer = importer.init_importer(importer_class=tpHoudiniLib, do_reload=False)

    global logger
    logger = tphoudini_importer.logger

    tphoudini_importer.import_modules()
    tphoudini_importer.import_packages(only_packages=True)
    if do_reload:
        tphoudini_importer.reload_all()


def init_ui(do_reload=False):
    tphoudini_importer = importer.init_importer(importer_class=tpHoudiniLib, do_reload=False)

    global logger
    logger = tphoudini_importer.logger

    tphoudini_importer.import_modules(skip_modules=['tpHoudiniLib.core'])
    tphoudini_importer.import_packages(only_packages=True, skip_modules=['tpHoudiniLib.core'])
    if do_reload:
        tphoudini_importer.reload_all()
