#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author:  renoyuan
# @file: log_hanlder.py
# @time: 2019/12/29 10:46
# @Software: PyCharm


import datetime
import os


class LogHandler(object):

    def __init__(self, address: str, *args, **kwargs):
        self.log_address = address
        islive = os.path.exists(address + "logs")
        if not islive:
            with open("{}/logs".format(self.log_address), "w+", encoding="utf-8") as file:
                file.write('')

    def output_log(self, error):
        if error != "wrapped C/C++ object of type TextCtrl has been deleted":
            with open("{}/logs".format(self.log_address), "a+", encoding="utf-8") as file:
                file.write(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S') + '\t' + str(error) + '\n')
        self.clean_logs_file()

    def clean_logs_file(self):
        size = os.path.getsize("{}/logs".format(self.log_address))
        if size >= 200000000:
            with open("{}/logs".format(self.log_address), "w+", encoding="utf-8") as file:
                file.write('')


if __name__ == '__main__':
    log_obj = LogHandler('.')
    log_obj.output_log('123456')
