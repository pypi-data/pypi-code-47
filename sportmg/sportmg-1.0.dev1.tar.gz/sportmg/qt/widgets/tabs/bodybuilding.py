#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import webbrowser

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QVBoxLayout

from dve.qt.widgets.tabs.table import TableTab

class BodybuildingTab(TableTab):

    def __init__(self, data, parent=None):
        super().__init__(data=data, parent=parent)

        edition_group_vbox = QVBoxLayout()
        edition_group_vbox.addWidget(self.mapped_widgets[self.data.headers.index("Description")])
        edition_group_vbox.addWidget(self.btn_add_row)
        self.edition_group.setLayout(edition_group_vbox)