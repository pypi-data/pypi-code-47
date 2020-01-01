#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import QMainWindow, QTabWidget

from jhunt.qt.widgets.tabs.adverts import AdvertsTab
from jhunt.qt.widgets.tabs.stats import StatsTab
from jhunt.qt.widgets.tabs.websites import WebsitesTab


class MainWindow(QMainWindow):

    def __init__(self, adverts_data, websites_data):
        super().__init__()

        self.resize(800, 600)
        self.setWindowTitle('Job Hunter')
        self.statusBar().showMessage("Ready", 2000)

        # Make widgets ####################################

        self.tabs = QTabWidget(parent=self)
        self.setCentralWidget(self.tabs)

        # Add tabs
        self.adverts_tab = AdvertsTab(adverts_data, parent=self.tabs)
        self.websites_tab = WebsitesTab(websites_data, parent=self.tabs)
        self.stats_tab = StatsTab(adverts_data, parent=self.tabs)

        self.tabs.addTab(self.adverts_tab, "Job Adverts")
        self.tabs.addTab(self.websites_tab, "Search")
        self.tabs.addTab(self.stats_tab, "Stats")

        # Show ############################################

        self.show()
