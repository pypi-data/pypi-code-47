#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author:  renoyuan
# @file: log_hanlder.py
# @time: 2019/12/29 10:46
# @Software: PyCharm


import datetime


class LogHandler(object):
    def __init__(self, address, *args, **kwargs):
        self.log_address = address

    def output_log(self, e):
        with open("{}/logs".format(self.log_address), "a+", encoding="utf-8") as file:
            file.write(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S') + '\t' + str(e)+'\n')


if __name__ == '__main__':
    log_obj = LogHandler('.')
    log_obj.output_log('123456')
