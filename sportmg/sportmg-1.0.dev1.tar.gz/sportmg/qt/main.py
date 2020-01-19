#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

from dve.io.table import TableDataBase
from sportmg.qt.widgets.mainwindow import MainWindow

import datetime

from PyQt5.QtWidgets import QApplication

APPLICATION_NAME = "Sport-mg"

def main():

    running_file_name = ".sportmg_running"

    running_data_schema = [
            {"header": "Date",           "default_value": datetime.datetime.now(), "dtype": datetime.datetime, "mapped": False},
            {"header": "Distance (km)",  "default_value": float(0),                "dtype": float,             "mapped": False,   "min_value": 0.,   "max_value": 100.},
            {"header": "Time (mn)",      "default_value": float(0),                "dtype": float,             "mapped": False,   "min_value": 0.,   "max_value": 60. * 24.},
            {"header": "Description",    "default_value": "",                      "dtype": str,               "mapped": True,    "widget": "QPlainTextEdit"}
        ]
    
    running_database = TableDataBase(running_data_schema, running_file_name)

    ###

    swimming_file_name = ".sportmg_swimming"

    swimming_data_schema = [
            {"header": "Date",                 "default_value": datetime.datetime.now(), "dtype": datetime.datetime, "mapped": False},
            {"header": "Pool lengths (x25m)",  "default_value": int(0),                  "dtype": int,               "mapped": False,   "min_value": 0,   "max_value": 200},
            {"header": "Time (mn)",            "default_value": float(0),                "dtype": float,             "mapped": False,   "min_value": 0.,   "max_value": 60. * 24.},
            {"header": "Description",          "default_value": "",                      "dtype": str,               "mapped": True,    "widget": "QPlainTextEdit"}
        ]
    
    swimming_database = TableDataBase(swimming_data_schema, swimming_file_name)

    ###

    bodybuilding_file_name = ".sportmg_bodybuilding"

    bodybuilding_data_schema = [
            {"header": "Date",         "default_value": datetime.datetime.now(), "dtype": datetime.datetime, "mapped": False,   "hidden": True},
            {"header": "Description",  "default_value": "",                      "dtype": str,               "mapped": True,  "widget": "QPlainTextEdit"}
        ]

    bodybuilding_database = TableDataBase(bodybuilding_data_schema, bodybuilding_file_name)

    ###

    running_data = running_database.load()
    swimming_data = swimming_database.load()
    bodybuilding_data = bodybuilding_database.load()

    app = QApplication(sys.argv)
    app.setApplicationName(APPLICATION_NAME)

    # Make widgets
    window = MainWindow(running_data, swimming_data, bodybuilding_data)

    # The mainloop of the application. The event handling starts from this point.
    # The exec_() method has an underscore. It is because the exec is a Python keyword. And thus, exec_() was used instead.
    exit_code = app.exec_()

    running_database.save(running_data)
    swimming_database.save(swimming_data)
    bodybuilding_database.save(bodybuilding_data)

    # The sys.exit() method ensures a clean exit.
    # The environment will be informed, how the application ended.
    sys.exit(exit_code)


if __name__ == '__main__':
    main()
