# file matrixb/source/__init__.py

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
#from .matrix import Matrix
from .resident import Resident
from .csv import CSV
from .googlesheet import GoogleSheet
from .xls import XLS
from .xlsx import XLSX


import re
import os
def factory(source, *args, **kwargs):
    """A function to allow for the generic import of any file-based source. 

    Args:
        source: A key that determines the source. The following are recognized. For any other source type, instantiate the source object directly:
            1. filename with a known extension (csv, ods, xls, xlsx)
            2. matrix (list of lists)
            3. A Google Spreadsheet ID. It is assumed that an alphanumeric character string of >10 characters that matches \w{10,} is such a sheet.
        All other parameters are delegated to the matrix source class without validation. It is assumed that the source class or subclass will handle them.
    
    Returns: 
        An object that is the appropriate descendant of SourceBase.
    """

    if type(source) is list:
        if type(source[0]) is list:
            return Resident(source, **kwargs)
        else:
            raise Exception("Cannot auto-identify the source for a single-dimenson list")

    if type(source) is not str:
        raise Exception("Expecting the type provided to the matrix source to be a matrix or a string")

    extmatch = re.search(r'\.(\w+)$', source)
    if not extmatch:
        # check for google sheet
        if re.match(r'\w{10,}', source):
            return(GoogleSheet(source, *args, **kwargs))
        else:
            raise Exception("Cannot identify an extension or valid source for " + str(source))

    extension = extmatch.group(1).upper()
    if extension not in globals():
        raise Exception("Cannot find a built-in matrix source class to handle extension " + extension.lower())
    source_class = globals()[extension]
    return(source_class(source, *args, **kwargs))

class Importer():
    """ Kept to maintain legacy code """
    def __new__(cls, *args, **kwargs):
        source = factory(*args, **kwargs)
        return(source)
