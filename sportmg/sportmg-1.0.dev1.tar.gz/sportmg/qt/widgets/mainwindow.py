#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import QMainWindow, QTabWidget

from sportmg.qt.widgets.tabs.running import RunningTab
from sportmg.qt.widgets.tabs.swimming import SwimmingTab
from sportmg.qt.widgets.tabs.bodybuilding import BodybuildingTab


class MainWindow(QMainWindow):

    def __init__(self, running_data, swimming_data, bodybuilding_data):
        super().__init__()

        self.resize(800, 600)
        self.setWindowTitle('Sport-mg')
        self.statusBar().showMessage("Ready", 2000)

        # Make widgets ####################################

        self.tabs = QTabWidget(parent=self)
        self.setCentralWidget(self.tabs)

        # Add tabs
        self.running_tab = RunningTab(running_data, parent=self.tabs)
        self.swimming_tab = SwimmingTab(swimming_data, parent=self.tabs)
        self.bodybuilding_tab = BodybuildingTab(bodybuilding_data, parent=self.tabs)

        self.tabs.addTab(self.running_tab, "Running")
        self.tabs.addTab(self.swimming_tab, "Swimming")
        self.tabs.addTab(self.bodybuilding_tab, "Bodybuilding")

        # Show ############################################

        self.show()
