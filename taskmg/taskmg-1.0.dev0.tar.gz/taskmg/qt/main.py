#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

from dve.io.table import TableDataBase
from taskmg.qt.widgets.mainwindow import MainWindow

import datetime

from PyQt5.QtWidgets import QApplication

APPLICATION_NAME = "Task-Mg"

def main():

    task_file_name = ".taskmg_tasks"

    task_data_schema = [
            {"header": "Creation date",          "default_value": datetime.datetime.now(), "dtype": datetime.datetime, "mapped": False},
            {"header": "Label",                  "default_value": "",                      "dtype": str,               "mapped": False,},
            {"header": "Priority",               "default_value": int(0),                  "dtype": int,               "mapped": False,  "min_value": 0,  "max_value": 5},
            {"header": "Archived",               "default_value": False,                   "dtype": bool,              "mapped": False},
            #{"header": "Chauffage",              "default_value": "n.c.",                  "dtype": str,               "mapped": False,  "values": ("n.c.", "Électrique", "Gaz", "Fioul", "PAC air", "Bois", "Granules")},
            #{"header": "GPS",                    "default_value": "",                      "dtype": str,               "mapped": True,  "widget": "QLineEdit"},
            {"header": "Description",            "default_value": "",                      "dtype": str,               "mapped": True,  "widget": "QPlainTextEdit"}
        ]
    
    task_database = TableDataBase(task_data_schema, task_file_name)

    ###

    tracker_file_name = ".taskmg_tracker"

    tracker_data_schema = [
            {"header": "Creation date",          "default_value": datetime.datetime.now(), "dtype": datetime.datetime, "mapped": False},
            {"header": "Label",                  "default_value": "",                      "dtype": str,               "mapped": False,},
            {"header": "Priority",               "default_value": int(0),                  "dtype": int,               "mapped": False,  "min_value": 0,  "max_value": 5},
            {"header": "Archived",               "default_value": False,                   "dtype": bool,              "mapped": False},
            #{"header": "Chauffage",              "default_value": "n.c.",                  "dtype": str,               "mapped": False,  "values": ("n.c.", "Électrique", "Gaz", "Fioul", "PAC air", "Bois", "Granules")},
            #{"header": "GPS",                    "default_value": "",                      "dtype": str,               "mapped": True,  "widget": "QLineEdit"},
            {"header": "Description",            "default_value": "",                      "dtype": str,               "mapped": True,  "widget": "QPlainTextEdit"}
        ]
    
    tracker_database = TableDataBase(tracker_data_schema, tracker_file_name)

    ###

    task_data = task_database.load()
    tracker_data = tracker_database.load()

    app = QApplication(sys.argv)
    app.setApplicationName(APPLICATION_NAME)

    # Make widgets
    window = MainWindow(task_data, tracker_data)

    # The mainloop of the application. The event handling starts from this point.
    # The exec_() method has an underscore. It is because the exec is a Python keyword. And thus, exec_() was used instead.
    exit_code = app.exec_()

    task_database.save(task_data)
    tracker_database.save(tracker_data)

    # The sys.exit() method ensures a clean exit.
    # The environment will be informed, how the application ended.
    sys.exit(exit_code)


if __name__ == '__main__':
    main()
