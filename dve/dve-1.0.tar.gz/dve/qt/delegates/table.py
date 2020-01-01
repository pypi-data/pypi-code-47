#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import datetime

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QStyledItemDelegate, QDateTimeEdit, QSpinBox, QComboBox

QT_DATE_TIME_FORMAT = "yyyy-MM-dd HH:mm:ss"   # MUST BE CONSISTENT WITH QT_DATE_TIME_FORMAT
PY_DATE_TIME_FORMAT = "%Y-%m-%d %H:%M:%S"     # MUST BE CONSISTENT WITH PY_DATE_TIME_FORMAT

class TableDelegate(QStyledItemDelegate):

    def __init__(self, data):
        super().__init__()

        self.data = data

    def createEditor(self, parent, option, index):
        if self.data.dtype[index.column()] == datetime.datetime:
            editor = QDateTimeEdit(parent=parent)

            #editor.setMinimumDate(datetime.datetime(year=2018, month=1, day=1, hour=0, minute=0))
            #editor.setMaximumDate(datetime.datetime(year=2020, month=9, day=1, hour=18, minute=30))
            editor.setDisplayFormat(QT_DATE_TIME_FORMAT)
            #editor.setCalendarPopup(True)

            # setFrame(): tell whether the line edit draws itself with a frame.
            # If enabled (the default) the line edit draws itself inside a frame, otherwise the line edit draws itself without any frame.
            editor.setFrame(False)

            return editor
        elif self.data.dtype[index.column()] == int:
            editor = QSpinBox(parent=parent)

            # setFrame(): tell whether the line edit draws itself with a frame.
            # If enabled (the default) the line edit draws itself inside a frame, otherwise the line edit draws itself without any frame.
            editor.setFrame(False)

            if ("min_value" in self.data.schema[index.column()]) and ("max_value" in self.data.schema[index.column()]):
                min_value = self.data.schema[index.column()]["min_value"]
                max_value = self.data.schema[index.column()]["max_value"]
                editor.setRange(min_value, max_value)

            return editor
        elif (self.data.dtype[index.column()] == str) and ("values" in self.data.schema[index.column()]):
            editor = QComboBox(parent=parent)

            values_list = self.data.schema[index.column()]['values']
            editor.addItems(values_list)

            # setFrame(): tell whether the line edit draws itself with a frame.
            # If enabled (the default) the line edit draws itself inside a frame, otherwise the line edit draws itself without any frame.
            editor.setFrame(False)

            return editor
        else:
            return QStyledItemDelegate.createEditor(self, parent, option, index)

    def setEditorData(self, editor, index):
        if self.data.dtype[index.column()] == datetime.datetime:
            value = index.model().data(index, Qt.EditRole)
            editor.setDateTime(value)     # value cannot be a string, it have to be a datetime...
        elif self.data.dtype[index.column()] == int:
            value = int(index.model().data(index, Qt.EditRole))
            editor.setValue(value)
        elif (self.data.dtype[index.column()] == str) and ("values" in self.data.schema[index.column()]):
            value = index.model().data(index, Qt.EditRole)
            editor.setCurrentText(value)
        else:
            return QStyledItemDelegate.setEditorData(self, editor, index)

    def setModelData(self, editor, model, index):
        if self.data.dtype[index.column()] == datetime.datetime:
            editor.interpretText()
            str_value = editor.text()
            dt_value = datetime.datetime.strptime(str_value, PY_DATE_TIME_FORMAT)
            model.setData(index, dt_value, Qt.EditRole)
        elif self.data.dtype[index.column()] == int:
            editor.interpretText()
            value = editor.value()
            model.setData(index, value, Qt.EditRole)
        elif (self.data.dtype[index.column()] == str) and ("values" in self.data.schema[index.column()]):
            value = editor.currentText()
            model.setData(index, value, Qt.EditRole)
        else:
            return QStyledItemDelegate.setModelData(self, editor, model, index)

    def updateEditorGeometry(self, editor, option, index):
        if (self.data.dtype[index.column()] in (datetime.datetime, int)) or ("values" in self.data.schema[index.column()]):
            editor.setGeometry(option.rect)
        else:
            return QStyledItemDelegate.updateEditorGeometry(self, editor, option, index)
