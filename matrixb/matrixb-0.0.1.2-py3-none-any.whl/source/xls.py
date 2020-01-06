# Copyright (c) 2019-2020 Kevin Crouse
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# @license: http://www.apache.org/licenses/LICENSE-2.0
# @author: Kevin Crouse (krcrouse@gmail.com)

from .base import SourceBase
class XLS(SourceBase):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._row_tracker

    def open_stream(self):
        import xlrd
        self.workbook = xlrd.open_workbook(os.path.expanduser(self.filename))
        self._worksheets = self.workbook.sheet_names()
        if self.worksheet:
            self.xlsheet = self.workbook.sheet_by_name(self.worksheet)
        else:
            self.xlsheet = self.workbook.sheet_by_index(0)
            self.worksheet = self.xlsheet.name
        self._row_tracker = 0

    @property
    def worksheet(self): return(self._worksheet)

    @worksheet.setter
    def worksheet(self, worksheet):
        self._worksheet = worksheet
        self.xlsheet = self.workbook.sheet_by_name(worksheet)


    def skip_rows(self, count):
        if self._row_tracker + count > self.xlsheet.nrows:
            raise IndexError("Asked to skip " + str(count) + " rows from current row ("+
                             str(self._row_tracker)+"), but there are not that many rows in the worksheet")
        skipped = []
        for row in range(count):
            skipped.append(list(map(lambda col: self.xlsheet.cell(self._row_tracker,col).value,
                                    range(self.xlsheet.ncols))))
            self._row_tracker += 1
        return(skipped)

    def next_row(self):
        while self._row_tracker < self.xlsheet.nrows:
            hasText = False
            row = []
            for i_col in range(self.xlsheet.ncols):
                v = self.xlsheet.cell(self._row_tracker, i_col).value
                if type(v) is str:
                    if self.nonemptyre.search(v):
                        hasText = i_col+1
                    else:
                        v = None
                elif type(v) is not None:
                    hasText = i_col+1
                else:
                    v = None
                # add the cell value to the row
                row.append(v)

            self._row_tracker += 1

            if hasText:
                return(row[:hasText])

        # if we get here, we are at EOF
        raise StopIteration
