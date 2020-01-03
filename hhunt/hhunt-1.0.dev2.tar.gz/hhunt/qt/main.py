#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

from dve.io.table import TableDataBase
from hhunt.qt.widgets.mainwindow import MainWindow

import datetime

from PyQt5.QtWidgets import QApplication

APPLICATION_NAME = "House hunter"

def main():

    house_file_name = ".house_hunter_maisons"

    house_data_schema = [
            {"header": "Date",                   "default_value": datetime.datetime.now(), "dtype": datetime.datetime, "mapped": False},
            {"header": "Score Lo",               "default_value": int(0),                  "dtype": int,               "mapped": False,  "min_value": 0,  "max_value": 5},
            {"header": "Score Gre",              "default_value": int(0),                  "dtype": int,               "mapped": False,  "min_value": 0,  "max_value": 5},
            {"header": "Prix honoraires inclus", "default_value": int(0),                  "dtype": int,               "mapped": False,  "min_value": 0,  "max_value": 450000},
            {"header": "Charges copropriété",    "default_value": int(0),                  "dtype": int,               "mapped": False,  "min_value": 0,  "max_value": 9999},
            {"header": "Surface intérieur",      "default_value": int(0),                  "dtype": int,               "mapped": False,  "min_value": 0,  "max_value": 999},
            {"header": "Surface terrain",        "default_value": int(0),                  "dtype": int,               "mapped": False,  "min_value": 0,  "max_value": 9999},
            {"header": "Surface séjour",         "default_value": int(0),                  "dtype": int,               "mapped": False,  "min_value": 0,  "max_value": 999},
            {"header": "Visité",                 "default_value": False,                   "dtype": bool,              "mapped": False},
            {"header": "Chambres",               "default_value": int(0),                  "dtype": int,               "mapped": False,  "min_value": 0,  "max_value": 9},
            {"header": "SdB",                    "default_value": int(0),                  "dtype": int,               "mapped": False,  "min_value": 0,  "max_value": 9},
            {"header": "WC",                     "default_value": int(0),                  "dtype": int,               "mapped": False,  "min_value": 0,  "max_value": 9},
            {"header": "DPE",                    "default_value": int(0),                  "dtype": int,               "mapped": False,  "min_value": 0,  "max_value": 999},
            {"header": "GES",                    "default_value": int(0),                  "dtype": int,               "mapped": False,  "min_value": 0,  "max_value": 999},
            {"header": "Chauffage",              "default_value": "n.c.",                  "dtype": str,               "mapped": False,  "values": ("n.c.", "Électrique", "Gaz", "Fioul", "PAC air", "Bois", "Granules")},
            {"header": "ECS",                    "default_value": "n.c.",                  "dtype": str,               "mapped": False,  "values": ("n.c.", "Ballon", "Gaz", "Fioul")},
            {"header": "Places parking",         "default_value": int(0),                  "dtype": int,               "mapped": False,  "min_value": 0,  "max_value": 9},
            {"header": "Ville",                  "default_value": "",                      "dtype": str,               "mapped": False},
            #{"header": "Application",  "default_value": False,                   "dtype": bool,              "mapped": False},
            #{"header": "Catégorie",    "default_value": "Entreprise",            "dtype": str,               "mapped": False,  "values": ("Entreprise", "IR/IE", "PostDoc")},
            #{"header": "Année construction",     "default_value": datetime.datetime.now(), "dtype": datetime.datetime, "mapped": False},
            {"header": "GPS",                    "default_value": "",                      "dtype": str,               "mapped": True,  "widget": "QLineEdit"},
            {"header": "URL",                    "default_value": "",                      "dtype": str,               "mapped": True,  "widget": "QLineEdit"},
            {"header": "Plus",                   "default_value": "",                      "dtype": str,               "mapped": True,  "widget": "QPlainTextEdit"},
            {"header": "Moins",                  "default_value": "",                      "dtype": str,               "mapped": True,  "widget": "QPlainTextEdit"},
            {"header": "Description",            "default_value": "",                      "dtype": str,               "mapped": True,  "widget": "QPlainTextEdit"}
        ]
    
    house_database = TableDataBase(house_data_schema, house_file_name)

    ###

    apartment_file_name = ".house_hunter_appartement"

    apartment_data_schema = [
            {"header": "Date",                   "default_value": datetime.datetime.now(), "dtype": datetime.datetime, "mapped": False},
            {"header": "Score Lo",               "default_value": int(0),                  "dtype": int,               "mapped": False,  "min_value": 0,  "max_value": 5},
            {"header": "Score Gre",              "default_value": int(0),                  "dtype": int,               "mapped": False,  "min_value": 0,  "max_value": 5},
            {"header": "Prix honoraires inclus", "default_value": int(0),                  "dtype": int,               "mapped": False,  "min_value": 0,  "max_value": 450000},
            {"header": "Surface intérieur",      "default_value": int(0),                  "dtype": int,               "mapped": False,  "min_value": 0,  "max_value": 999},
            {"header": "Surface séjour",         "default_value": int(0),                  "dtype": int,               "mapped": False,  "min_value": 0,  "max_value": 999},
            {"header": "Visité",                 "default_value": False,                   "dtype": bool,              "mapped": False},
            {"header": "Chambres",               "default_value": int(0),                  "dtype": int,               "mapped": False,  "min_value": 0,  "max_value": 9},
            {"header": "SdB",                    "default_value": int(0),                  "dtype": int,               "mapped": False,  "min_value": 0,  "max_value": 9},
            {"header": "WC",                     "default_value": int(0),                  "dtype": int,               "mapped": False,  "min_value": 0,  "max_value": 9},
            {"header": "DPE",                    "default_value": int(0),                  "dtype": int,               "mapped": False,  "min_value": 0,  "max_value": 999},
            {"header": "GES",                    "default_value": int(0),                  "dtype": int,               "mapped": False,  "min_value": 0,  "max_value": 999},
            {"header": "Places parking",         "default_value": int(0),                  "dtype": int,               "mapped": False,  "min_value": 0,  "max_value": 9},
            #{"header": "Étage",                  "default_value": int(0),                  "dtype": int,               "mapped": False,  "min_value": 0,  "max_value": 9},
            #{"header": "Application",  "default_value": False,                   "dtype": bool,              "mapped": False},
            #{"header": "Catégorie",    "default_value": "Entreprise",            "dtype": str,               "mapped": False,  "values": ("Entreprise", "IR/IE", "PostDoc")},
            {"header": "Ville",                  "default_value": "",                      "dtype": str,               "mapped": False},
            {"header": "GPS",                    "default_value": "",                      "dtype": str,               "mapped": True,  "widget": "QLineEdit"},
            {"header": "URL",                    "default_value": "",                      "dtype": str,               "mapped": True,  "widget": "QLineEdit"},
            {"header": "Plus",                   "default_value": "",                      "dtype": str,               "mapped": True,  "widget": "QPlainTextEdit"},
            {"header": "Moins",                  "default_value": "",                      "dtype": str,               "mapped": True,  "widget": "QPlainTextEdit"},
            {"header": "Description",            "default_value": "",                      "dtype": str,               "mapped": True,  "widget": "QPlainTextEdit"}
        ]
    
    apartment_database = TableDataBase(apartment_data_schema, apartment_file_name)

    ###

    websites_file_name = ".house_hunter_websites"

    websites_data_schema = [
        {"header": "Date",            "default_value": datetime.datetime.now(), "dtype": datetime.datetime, "mapped": False,   "hidden": True},
        {"header": "Nom",             "default_value": "",                      "dtype": str,               "mapped": False},
        {"header": "Score",           "default_value": int(0),                  "dtype": int,               "mapped": False,   "min_value": 0,   "max_value": 3},
        {"header": "Catégorie",       "default_value": "Agence",                "dtype": str,               "mapped": False,   "values": ("Agence", "Moteur de recherche", "Particulier à particulier")},
        {"header": "Dernière visite", "default_value": datetime.datetime.now(), "dtype": datetime.datetime, "mapped": False},
        {"header": "Statut du jour",  "default_value": "Non visité",            "dtype": str,               "mapped": False,   "values": ("Non visité", "Visite partielle", "Visite complète")},
        {"header": "Description",     "default_value": "",                      "dtype": str,               "mapped": True,    "widget": "QPlainTextEdit"},
        {"header": "URL",             "default_value": "",                      "dtype": str,               "mapped": True,    "widget": "QLineEdit"}
    ]

    websites_database = TableDataBase(websites_data_schema, websites_file_name)

    ###

    house_data = house_database.load()
    apartment_data = apartment_database.load()
    websites_data = websites_database.load()

    app = QApplication(sys.argv)
    app.setApplicationName(APPLICATION_NAME)

    # Make widgets
    window = MainWindow(house_data, apartment_data, websites_data)

    # The mainloop of the application. The event handling starts from this point.
    # The exec_() method has an underscore. It is because the exec is a Python keyword. And thus, exec_() was used instead.
    exit_code = app.exec_()

    house_database.save(house_data)
    apartment_database.save(apartment_data)
    websites_database.save(websites_data)

    # The sys.exit() method ensures a clean exit.
    # The environment will be informed, how the application ended.
    sys.exit(exit_code)


if __name__ == '__main__':
    main()
