#!/usr/bin/python
# -*- coding: utf8 -*-
#
# @author: natloc
# @date: 2019/10/11
# @time: 21:40
# @doc:
# Copyright © 2019 natloc. All rights reserved.
#

import sys



# 设置默认为 utf8 编码
def setDefaultUTF8():
    __setDefaultEncoding('utf-8')


# 设置默认编码
def __setDefaultEncoding(encoding):
    reload(sys)
    sys.setdefaultencoding(encoding)