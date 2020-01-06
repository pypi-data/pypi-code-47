# -*- coding: UTF-8 -*-
# Copyright 2014-2019 Rumma & Ko Ltd
# License: BSD (see file COPYING for details)
"""This is the main module of Lino Tera.

.. autosummary::
   :toctree:

   lib


"""

from .setup_info import SETUP_INFO

__version__ = SETUP_INFO['version']

srcref_url = 'https://github.com/lino-framework/tera/blob/master/%s'
doc_trees = ['docs', 'dedocs']
intersphinx_urls = {
    'docs' : "http://tera.lino-framework.org",
    'dedocs' : "http://de.tera.lino-framework.org",
}

