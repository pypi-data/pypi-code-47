#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import QMainWindow, QTabWidget

from hhunt.qt.widgets.tabs.house import HouseTab
from hhunt.qt.widgets.tabs.apartment import ApartmentTab
from hhunt.qt.widgets.tabs.websites import WebsitesTab


class MainWindow(QMainWindow):

    def __init__(self, house_data, apartment_data, websites_data):
        super().__init__()

        self.resize(800, 600)
        self.setWindowTitle('House Hunter')
        self.statusBar().showMessage("Ready", 2000)

        # Make widgets ####################################

        self.tabs = QTabWidget(parent=self)
        self.setCentralWidget(self.tabs)

        # Add tabs
        self.house_tab = HouseTab(house_data, parent=self.tabs)
        self.apartment_tab = ApartmentTab(apartment_data, parent=self.tabs)
        self.websites_tab = WebsitesTab(websites_data, parent=self.tabs)

        self.tabs.addTab(self.house_tab, "Maison")
        self.tabs.addTab(self.apartment_tab, "Appartement")
        self.tabs.addTab(self.websites_tab, "Recherche")

        # Show ############################################

        self.show()
