from enum import Enum


class ListOrder(Enum):
    """Enum for list's order

    ListOrder.ASCENDING: sort by ascending
    ListOrder.DESCENDING: sort by descending
    """
    ASCENDING = 1
    DESCENDING = 2


class SearchOrder(Enum):
    """Enum for search's order

    SearchOrder.SCORE: sort by score
    SearchOrder.NUMBER: sort by number ascending
    """
    SCORE = 1
    NUMBER = 2
