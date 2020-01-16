#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
Initialization module for tpNameIt
"""

from __future__ import print_function, division, absolute_import

import os
import inspect
import logging.config

# =================================================================================

logger = None
resource = None

# =================================================================================


def init(do_reload=False, dev=False):
    """
    Initializes module
    :param do_reload: bool, Whether to reload modules or not
    :param dev: bool, Whether artellapipe is initialized in dev mode or not
    """

    # Load logger configuration
    logging.config.fileConfig(get_logging_config(), disable_existing_loggers=False)


    from tpPyUtils import importer
    from tpQtLib.core import resource as resource_utils

    class tpNameItResource(resource_utils.Resource, object):
        RESOURCES_FOLDER = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'resources')

    class tpNameIt(importer.Importer, object):
        def __init__(self, *args, **kwargs):
            super(tpNameIt, self).__init__(module_name='tpNameIt', *args, **kwargs)

        def get_module_path(self):
            """
            Returns path where tpNameIt module is stored
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

    tpnameit_importer = importer.init_importer(importer_class=tpNameIt, do_reload=False)

    global logger
    global resource
    logger = tpnameit_importer.logger
    resource = tpNameItResource

    tpnameit_importer.import_modules()
    tpnameit_importer.import_packages(only_packages=True)

    if do_reload:
        tpnameit_importer.reload_all()


def run(do_reload=False):
    init(do_reload=do_reload)
    from tpNameIt.core import nameit
    win = nameit.run()
    return win
