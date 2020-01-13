from numpy.random import RandomState

from randomcsv.Column import Column


class CategoryColumn(Column):
    """
    A Column with categorical data.

    Example
    ------
    >>> column = CategoryColumn('MyCategory', ['A', 'B', 'C'])
    >>> column.generate_entries(3)
    0   A
    1   A
    2   C
    dtype: category
    """

    def __init__(self, name, categories, dtype='category', null_ratio=0, null_element=None, random_state=None):
        """
        Parameters
        ----------
        :param name: Name of the Column
        :param categories: A List of possible category values
        :param dtype: See randomcsv.Column
        :param null_ratio: See randomcsv.Column
        :param null_element: See randomcsv.Column
        :param random_state: If not None, all random operations are deterministic, for testing. See randomcsv.Column
        """
        super().__init__(name, dtype, null_ratio=null_ratio, null_element=null_element,
                         random_state=random_state)
        self.categories = categories

    def _create_data(self, count):
        return RandomState(seed=self.random_state).choice(self.categories, size=count)
