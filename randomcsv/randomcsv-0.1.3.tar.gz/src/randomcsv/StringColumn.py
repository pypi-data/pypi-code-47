import os

from pkg_resources import resource_filename
from randomcsv.Column import Column
from randomcsv.FileUtils import read_line_looping

DICTIONARY_DIR = resource_filename('randomcsv.resources.dictionaries', '')


class StringColumn(Column):
    """
    A Column with text values.

    Per default, will be filled with first names from a dictionary.
    Up to about 500 different values, non-latin characters.

    Example
    ------
    >>> column = StringColumn('MyStrings')
    >>> column.generate_entries(2)
    0     Hannes
    1    Charlos
    dtype: object
    """

    def __init__(self, name, dictionary='firstNames.txt', dtype='object', null_ratio=0, null_element='',
                 random_state=None):
        super().__init__(name, dtype=dtype, null_ratio=null_ratio, null_element=null_element, random_state=random_state)
        self.dictionary = os.path.join(DICTIONARY_DIR, dictionary)

    def _create_data(self, count):
        return read_line_looping(self.dictionary, count)
