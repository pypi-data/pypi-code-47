#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import datetime
import json
import os

from dve.data.table import TableDataStructure
from dve.io.lock import lock_path, unlock_path

PY_DATE_TIME_FORMAT = "%Y-%m-%d %H:%M:%S"  # TODO

ID_COLUMN_LABEL = "ID"    # TODO

class TableDataBase:

    def __init__(self, data_schema, file_name):
        self._data_schema = data_schema
        self._file_name = file_name
        lock_path(self.path)


    def __del__(self):
        unlock_path(self.path)


    def load(self):
        """Load the JSON database."""

        json_data_dict = {}

        try:
            with open(self.path, "r") as fd:
                json_data_dict = json.load(fd)
        except FileNotFoundError:
            pass

        data = TableDataStructure(self._data_schema)

        for item_id, item_dict in json_data_dict.items():
            item_list = []

            for col_label, dtype in zip(data.headers, data.dtype):
                if col_label == ID_COLUMN_LABEL:
                    value = int(item_id)
                #elif col_label == "Score":   # Temporary uncomment this line to introduce new fields in existing data
                #    value = 0                # Temporary uncomment this line to introduce new fields in existing data
                else:
                    value = item_dict[col_label]

                    if dtype == datetime.datetime:
                        value = datetime.datetime.strptime(value, PY_DATE_TIME_FORMAT)

                item_list.append(value)

            data.append(item_list)

        return data


    def save(self, data):
        """Save the JSON database."""

        # Use a dict structure to have items sorted by ID automatically by the JSON parser (for some strange reason, the first and the last items are switched when a list is used)
        json_data_dict = {}

        for row_index in range(data.num_rows):
            row_dict = {}

            for col_label, dtype, col_index in zip(data.headers, data.dtype, range(data.num_columns)):
                value = data.get_data(row_index=row_index, column_index=col_index)

                if dtype == datetime.datetime:
                    value = value.strftime(format=PY_DATE_TIME_FORMAT)

                row_dict[col_label] = value

            row_id = row_dict.pop(ID_COLUMN_LABEL)
            json_data_dict[row_id] = row_dict

        with open(self.path, "w") as fd:
            json.dump(json_data_dict, fd, sort_keys=True, indent=4)


    @property
    def path(self):
        home_path = os.path.expanduser("~")                 # TODO: does it work on Unix only ?
        file_path = os.path.join(home_path, self._file_name)
        return file_path
