import numpy as np
from randomcsv.Column import Column


class IntColumn(Column):
    """
    A Column with incrementing Integers.
    The default dtype is None because Errors might be raised if null_elements are used.
    A fraction of the elements, determined by null_ratio, will be replaced by the null_element, representing invalid
    entries.

    Example
    -------
    >>> column = IntColumn('MyInts', start=100)
    >>> column.generate_entries(2)
    0    100
    1    101
    dtype: int64
    """
    def __init__(self, name, start=0, dtype=None, null_ratio=0, null_element=np.NAN, random_state=None):
        """
        Parameters
        ----------
        :param start: start value of the column (included, default 0)
        :param dtype: the datatype of the resulting pandas.Series. Per default None (automatically determined by pandas)
        :param null_ratio: ratio of elements, which will be replaced by the null_element (default 0.0). See Column
        :param null_element: value of invalid entries (default numpy's NAN). See Column
        :param random_state: If provided, elements which are replaced by the null_element are deterministic, for testing
                             See Column
        """
        super().__init__(name, dtype=dtype, null_ratio=null_ratio, null_element=null_element, random_state=random_state)
        self.start = start

    def _create_data(self, count):
        return range(self.start, self.start + count)
