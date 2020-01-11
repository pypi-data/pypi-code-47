# file matrixb/rowmap.py

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

from .iterator import MatrixIterator

class MatrixRowmap(MatrixIterator):
    """ Defines a subclass of the MatrixIterator when the rowmap is called instead of a strict matrix iteration. """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # we
        self._columns = self.matrix.columns

    def __next__(self):
        cols = self.matrix.columns
        row = super().__next__()
        return({cols[i]:row[i] for i in range(len(cols))})

    def top(self):
        cols = self.matrix.columns
        row = super().top()
        return({cols[i]:row[i] for i in range(len(cols))})
