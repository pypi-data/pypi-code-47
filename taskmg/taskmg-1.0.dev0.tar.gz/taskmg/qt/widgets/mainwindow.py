#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import QMainWindow, QTabWidget

from taskmg.qt.widgets.tabs.task import TaskTab
from taskmg.qt.widgets.tabs.tracker import TrackerTab


class MainWindow(QMainWindow):

    def __init__(self, task_data, tracker_data):
        super().__init__()

        self.resize(800, 600)
        self.setWindowTitle('Task-Mg')
        self.statusBar().showMessage("Ready", 2000)

        # Make widgets ####################################

        self.tabs = QTabWidget(parent=self)
        self.setCentralWidget(self.tabs)

        # Add tabs
        self.task_tab = TaskTab(task_data, parent=self.tabs)
        self.tracker_tab = TrackerTab(tracker_data, parent=self.tabs)

        self.tabs.addTab(self.task_tab, "Tasks")
        self.tabs.addTab(self.tracker_tab, "Time Tracker")

        # Show ############################################

        self.show()
