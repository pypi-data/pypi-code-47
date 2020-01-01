#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import webbrowser

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QVBoxLayout

from dve.qt.widgets.tabs.table import TableTab

class WebsitesTab(TableTab):

    def __init__(self, data, parent=None):
        super().__init__(data=data, parent=parent)

        edition_group_vbox = QVBoxLayout()
        edition_group_vbox.addWidget(self.mapped_widgets[self.data.headers.index("URL")])
        edition_group_vbox.addWidget(self.mapped_widgets[self.data.headers.index("Description")])
        edition_group_vbox.addWidget(self.btn_add_row)
        self.edition_group.setLayout(edition_group_vbox)

    def row_action_callback(self):
        model_index_list = self.table_view.selectionModel().selectedRows()

        for model_index in model_index_list:
            row_index = model_index.row()
            column_index = self.data.headers.index("URL")

            # https://wiki.python.org/moin/PyQt/Reading%20selections%20from%20a%20selection%20model
            model_index = self.table_view.model().index(row_index, column_index)
            url = self.table_view.model().data(model_index, role=Qt.DisplayRole)

            webbrowser.open_new_tab(url) # Open the URL in a browser
