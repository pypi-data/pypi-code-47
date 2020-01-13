import numpy as np
from numpy.random import RandomState
from randomcsv.Column import Column


class RandomNumberColumn(Column):
    """
    Creates a Column with random float numbers between low (included) and high (excluded)
        If a value for digits is provided, the column values will be rounded to the number of digits

    Example
    -------
    >>> column = RandomNumberColumn('MyRandomNumbers', low=10, high=20, digits=2)
    >>> column.generate_entries(2)
    0    15.89
    1    10.71
    dtype: float64
    """
    def __init__(self, name, low=0, high=1, digits=None, dtype=None, null_ratio=0, null_element=np.NAN,
                 random_state=None):
        """
        Parameters
        ----------
        :param name: Name of the Column
        :param low: Lower bound for the generated values (included, default 0)
        :param high: Upper bound for the generated values (excluded, default 1)
        :param digits: Number of digits to which the values are rounded, if None values are not rounded
        :param dtype: the datatype of the resulting pandas.Series. Per default None (automatically determined by pandas)
        :param null_ratio: ratio of elements, which will be replaced by the null_element (default 0.0). See Column
        :param null_element: value of invalid entries (default numpy's NAN). See Column
        :param random_state: If provided, elements which are replaced by the null_element are deterministic, for testing
                             See Column
        """
        super().__init__(name, dtype=dtype, null_ratio=null_ratio, null_element=null_element, random_state=random_state)
        self.low = low
        self.high = high
        self.digits = digits

    def _create_data(self, count):
        return [self._map_to_range(rnd) for rnd in RandomState(seed=self.random_state).random(count)]

    def _map_to_range(self, rnd):
        value = self.low + (self.high - self.low) * rnd
        if self.digits:
            return round(value, self.digits)
        return value
