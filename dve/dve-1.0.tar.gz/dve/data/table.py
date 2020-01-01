#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class TableDataStructure:

    def __init__(self, data_schema):
        self._data_schema = data_schema
        self._data = []
        self._last_id = 0

    # TODO: redefine [x,y] operator (as in numpy)
    def get_data(self, row_index, column_index):
        return self._data[row_index][column_index]

    # TODO: redefine [x,y] operator (as in numpy)
    def set_data(self, row_index, column_index, value):
        if not isinstance(value, self.dtype[column_index]):
            raise ValueError("Error at row {} column {} with value {}. Expect {} instance. Got {}".format(row_index, column_index, value, self.dtype[column_index], type(value)))

        id_index = self.headers.index("ID")
        if column_index == id_index:
            self._last_id = max(self._last_id, value)

        self._data[row_index][column_index] = value

    def append(self, row):
        row_index = self.num_rows - 1
        self.insert_row(row_index, row=row)

    def insert_row(self, row_index, row=None):
        if row is None:
            row = list(self.default_values)

        self._data.insert(row_index, [None for i in range(self.num_columns)])

        for column_index in range(self.num_columns):
            self.set_data(row_index, column_index, row[column_index])

    def remove_row(self, index):
        if self.num_rows > 0:
            _removed = self._data.pop(index)

    #def describe(self, index):
    #    if index == 0:
    #        return {"header": "ID", "default_value": int(self._last_id + 1), "dtype": int}
    #    else:
    #        return self._data_schema[index]
    
    @property
    def num_rows(self):
        return len(self._data)

    @property
    def num_columns(self):
        return len(self.headers)

    @property
    def shape(self):
        return (self.num_rows, self.num_columns)

    @property
    def headers(self):  # TODO
        return ['ID'] + [row['header'] for row in self._data_schema]

    @property
    def default_values(self):  # TODO
        return [int(self._last_id + 1)] + [row['default_value'] for row in self._data_schema]

    @property
    def dtype(self):  # TODO
        #return [int] + [row['dtype'] if not isinstance(row['dtype'], (tuple, list)) else str for row in self._data_schema]
        return [int] + [row['dtype'] for row in self._data_schema]

    @property
    def schema(self):
        return [{"header": "ID", "default_value": int(self._last_id + 1), "dtype": int}] + self._data_schema