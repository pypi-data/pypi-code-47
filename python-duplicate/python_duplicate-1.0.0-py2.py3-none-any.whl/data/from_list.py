# Native import
from copy import deepcopy

# Local import
from .const import UNIQUE, DUPLICATE, CREATE_UNIQUE
from .utils import Utils


class FromList(Utils):
    """
    Handle search of duplicate or unique item inside a list

    :param list lst: Param to work on
    :param str key: Param to work in a list of dict if you need it
    """

    def __init__(self, lst: list, key: str = None) -> None:
        self.copied_lst = deepcopy(lst)
        Utils.__init__(self, self.copied_lst)
        if key:
            self.create_list(key)
        self.get_type()
        self.validate_items()

    def analyze(self, analyze_type: str, feedback: bool = True) -> dict:
        """
        Analyze the list to get the items and their indexes
        (depending on the analyze_type)

        :param str analyze_type: Param to determine what type of analyse to do
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

        if analyze_type == UNIQUE:
            return self.get_indexes(UNIQUE, feedback)
        if analyze_type == DUPLICATE:
            return self.get_indexes(DUPLICATE, feedback)
        if analyze_type == CREATE_UNIQUE:
            return self.create_unique_index(feedback)

    def create_unique(self) -> list:
        """

        :return: Unique items (by deleting duplicate items)
        """
        indexes = self.create_unique_index()

        for index in indexes['all_index']:
            del self.copied_lst[index]

        return self.copied_lst

    def get_unique(self) -> list:
        """

        :return: Only unique items
        """
        indexes = self.get_indexes(UNIQUE)

        return [self.copied_lst[index] for index in indexes['all_index']]

    def get_duplicate(self) -> list:
        """

        :return: Only all duplicate items
        """
        indexes = self.get_indexes(DUPLICATE)

        return [self.copied_lst[index] for index in indexes['all_index']]
