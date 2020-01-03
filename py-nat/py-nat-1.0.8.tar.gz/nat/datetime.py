#!/usr/bin/python3
# -*- coding: utf8 -*-
#
# @author: natloc_developer
# @date: 2019/12/31
# @time: 16:52
# @doc:
# Copyright © 2019 natloc_developer. All rights reserved.
#

import time
import datetime


# 获取时间戳
# return double
def getTi():
    return time.time()


# 获取当前时刻的对象
# 可直接获取成员属性；如：now = nat.datetime.now(); now.year
def now():
    return datetime.datetime.now()