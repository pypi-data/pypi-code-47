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
import os

class XLSX(SourceBase):

    def __init__(self, *args, **kwargs):
        self._iterator = None
        super().__init__(*args, **kwargs)

    def open_stream(self):
        import openpyxl
        self.workbook = openpyxl.load_workbook(os.path.expanduser(self.filename), read_only=True, data_only=True)
        self._worksheets = self.workbook.sheetnames
        if self.worksheet:
            self.xlsheet = self.workbook[self.worksheet]
        else:
            self.xlsheet = self.workbook.worksheets[0] ### this could be self.workbook.active, but that has given weird results
            self.worksheet = self.xlsheet.title
        self._iterator = iter(self.xlsheet.rows)

    @property
    def iterator(self):
        if not self._iterator:
            self.open()
        return(self._iterator)

    @property
    def worksheet(self): return(self._worksheet)

    @worksheet.setter
    def worksheet(self, worksheet):
        self._worksheet = worksheet
        self.xlsheet = self.workbook[worksheet]

    def skip_rows(self, count):
        skipped = []
        for i in range(count):
            row = next(self.iterator)
            skipped.append(list(map(lambda cell: cell.value, row)))
        return(skipped)

    def next_row(self):
        hasText = False
        while True:
            try:
                rowcontainer = next(self.iterator)
            except StopIteration:
                self.workbook.close()
                raise(StopIteration)

            row = []
            cellcount = 0
            for cell in rowcontainer:
                cellcount += 1
                v = cell.value
                if type(v) is str:
                    if self.nonemptyre.search(v):
                        hasText = cellcount
                    else:
                        v = None
                elif v is not None:
                    hasText = cellcount
                else:
                    v = None
                # add the cell value to the row
                row.append(v)
            if hasText is not False:
                return(row[:hasText])
