#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Seaky
# @Date:   2019/8/14 11:56

from datetime import datetime

# pip3 install python-dateutil
from dateutil.relativedelta import relativedelta


def datetime_now():
    return datetime.now()


def last_month():
    return datetime.now() - relativedelta(months=1)


def datetime_to_string(dt=None, fmt="%Y-%m-%d %H:%M:%S"):
    if not dt:
        dt = datetime_now()
    return dt.strftime(fmt)


def string_to_datetime(s, fmt):
    return datetime.strptime(s, fmt)


def datetime_to_timestamp(dt=None):
    if not dt:
        dt = datetime.now()
    return int(datetime.timestamp(dt))


def timestamp_to_datetime(timestamp):
    return datetime.fromtimestamp(timestamp)


def timestamp_to_string(timestamp, *args, **kwargs):
    return datetime_to_string(timestamp_to_datetime(timestamp), *args, **kwargs)


def string_to_timestamp(s, fmt):
    return int(datetime_to_timestamp(string_to_datetime(s, fmt)))
