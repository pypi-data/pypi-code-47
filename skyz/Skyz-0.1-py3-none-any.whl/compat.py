# -*- coding: utf-8 -*-
"""
    skyz.compat
    ~~~~~~~~~~~

    Some py2/py3 compatibility support based on a stripped down
    version of six so we don't have to depend on a specific version
    of it.

    :copyright: 2020 Pancubs.org
    :license: BSD-3-Clause
"""
import sys

PY2 = sys.version_info[0] == 2

try: # Python 2compat
    text_type = unicode
    string_types = (str, unicode)
    numeric_types = (int, long)
except NameError: # Python 3
    text_type = str
    string_types = (str,)
    numeric_types = (int,)

if not PY2:
    iterkeys = lambda d: iter(d.keys())
    itervalues = lambda d: iter(d.values())
    iteritems = lambda d: iter(d.items())

else:
    iterkeys = lambda d: d.iterkeys()
    itervalues = lambda d: d.itervalues()
    iteritems = lambda d: d.iteritems()
