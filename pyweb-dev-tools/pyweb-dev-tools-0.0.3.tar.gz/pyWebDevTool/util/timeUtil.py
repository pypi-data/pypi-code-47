# -*- coding: utf-8 -*-
import datetime


def time2str(time=datetime.datetime.now(), fmt="%Y-%m-%d %H:%M:%S"):
    return datetime.datetime.strftime(time, fmt)
