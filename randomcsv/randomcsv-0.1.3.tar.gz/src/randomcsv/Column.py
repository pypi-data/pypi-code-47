from abc import ABC, abstractmethod

from numpy.random import RandomState
from pandas import Series


class Column(ABC):
    """
    Abstract parent class for Columns.

    Custom Column Classes only need to overwrite the abstract method _create_data(count).
    The Parent then handles conversion to the specified dtype and replacing the given fraction
    of elements with null_elements, representing invalid data.
    """

    def __init__(self, name, dtype=None, null_ratio=0, null_element=None, random_state=None):
        """
        Parameters
        ----------
        :param name: Name of the column
        :param dtype: Datatype (see pandas DataFrame/ Series)
        :param null_ratio: Ratio of elements, which will be replaced by the null_element.
                           The value should be between 0 and 1, default is 0
        :param null_element: Element representing invalid data. A fraction of elements, specified by
                             null_ratio is replaced with this element.
        :param random_state: The seed value for numpys RandomState.
                             If not None, the output of all random operations will not change for multiple executions
        """
        self.name = name
        self.dtype = dtype
        self.null_ratio = null_ratio
        self.null_element = null_element
        self.random_state = random_state

    def generate_entries(self, count):
        """
        Generates a pandas Series with <count> rows.

        Uses the Columns <null_ratio> and <null_element> values to replace a given fraction of elements.
        Used by CsvGenerator to generate the Column values.
        :param count: Number of rows, which will be generated.
        :return: A pandas.Series containing <count> values.
        """
        series = Series(self._create_data_with_null_elements(count))
        if self.dtype:
            return series.astype(self.dtype)
        return series

    def _create_data_with_null_elements(self, count):
        data = []
        values = self._create_data(count)
        if self.null_ratio == 0:
            return values
        random_score = RandomState(self.random_state).random(count)
        for value, score in zip(values, random_score):
            data.append(value if score > self.null_ratio else self.null_element)
        return data

    @abstractmethod
    def _create_data(self, count):
        pass
