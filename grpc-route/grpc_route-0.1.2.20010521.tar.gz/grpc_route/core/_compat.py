# -*- coding: utf-8 -*- 
# @Time     : 2020-01-02 11:49
# @Author   : binger

import sys

try:
    import builtins
except ImportError:
    import __builtin__ as builtins

PY2 = sys.version_info[0] == 2
WIN = sys.platform.startswith("win")
