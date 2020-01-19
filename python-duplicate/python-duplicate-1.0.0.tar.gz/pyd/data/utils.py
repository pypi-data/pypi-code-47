# Local import
from .const import DUPLICATE, UNIQUE


class Utils:
    """
    Provides functions to handle search of duplicate or unique item
    inside a list

    :param list lst:    Param to work on.
                        By default its the same list passed to `FromList`_
    """

    def __init__(self, lst: list) -> None:
        self.indexes = {}
        self.lst = lst
        self.item_type = list

    def create_list(self, key: str) -> None:
        """
        Create a list of all item for a given key

        :param str key: Dict key on which to get data
        """
        self.lst = [value.get(key) for value in self.lst]

    def get_type(self) -> None:
        """
        Get the type of the first item
        """
        item = self.lst[0]
        if isinstance(item, (int, float)):
            self.item_type = (int, float)
        elif isinstance(item, str):
            self.item_type = str
        elif isinstance(item, dict):
            self.item_type = dict
        elif isinstance(item, tuple):
            self.item_type = tuple

    def validate_items(self) -> None:
        """
        Check if all items are of the same type

        :raise TypeError: If items are NOT of the same type
        """
        if not all(isinstance(x, self.item_type) for x in self.lst):
            raise TypeError(f'An item has a different type than the others')

    def create_update_feedback(self, index: int, value: any,
                               feedback: bool) -> None:
        """
        Create or update the 'self.indexes' dict to provide feedback
        """
        if feedback:
            str_value = str(value)
            if self.indexes.get(str_value):
                self.indexes[str_value].append(index)
            else:
                self.indexes.update({str_value: [index]})

    def get_indexes(self, index_type: str, feedback: bool = False) -> dict:
        """
        Identify unique or duplicate item and return the index of each of them

        :param str index_type: Param to know what type of item index we want
        :param bool feedback: Param to return more or less information
        :return:    * without feedback::

                        { "all_index": [INDEX(ES)] }

                    * with feedback::

                        {
                            "all_index": [INDEX(ES)],
                            "VALUE_X": [INDEX(ES)],
                            "VALUE_Y": [INDEX(ES)],
                        }
        """
        indexes = []
        for index, value in enumerate(self.lst):
            if index_type == DUPLICATE and self.lst.count(value) >= 2:
                self.create_update_feedback(index, value, feedback)
                indexes.append(index)
            if index_type == UNIQUE and self.lst.count(value) == 1:
                self.create_update_feedback(index, value, feedback)
                indexes.append(index)
        self.indexes['all_index'] = indexes
        return self.indexes

    def create_unique_index(self, feedback: bool = False) -> dict:
        """
        Identify duplicated item and return the index of each of them except for
        the first one (in order to create a list of unique item)

        :param bool feedback: Param to return more or less information
        :return:    * without feedback::

                        { "all_index": [REVERSED_ORDER_INDEX(ES)] }

                    * with feedback::

                        {
                            "all_index": [REVERSED_ORDER_INDEX(ES)],
                            "VALUE_X": [INDEX(ES)],
                            "VALUE_Y": [INDEX(ES)],
                        }
        """
        seen_value = []
        seen_index = []
        for index, value in enumerate(self.lst):
            if self.lst.count(value) >= 2:
                if value not in seen_value:
                    seen_value.append(value)
                else:
                    seen_index.append(index)
                    self.create_update_feedback(index, value, feedback)
        self.indexes['all_index'] = sorted(seen_index, reverse=True)
        return self.indexes
