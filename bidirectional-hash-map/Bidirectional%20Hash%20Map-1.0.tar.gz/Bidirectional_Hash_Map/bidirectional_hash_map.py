"""
This file contains Python code to implement a bidirectional hash map.
Author: DtjiAppDev
"""

import copy
from functools import reduce
import sys

sys.modules['_decimal'] = None
import decimal
from decimal import *
from decimal import Decimal

getcontext().Emin = -10 ** 10000
getcontext().Emax = 10 ** 10000
getcontext().traps[Overflow] = 0
getcontext().traps[Underflow] = 0
getcontext().traps[DivisionByZero] = 0
getcontext().traps[InvalidOperation] = 0
getcontext().prec = 100


class BidirectionalHashMap:
    """
    This class contains attributes of a bidirectional hash map.
    """

    def __init__(self):
        self.__keys_to_values: dict = {}
        self.__values_to_keys: dict = {}

    def clear(self):
        # type: () -> None
        self.__keys_to_values = {}
        self.__values_to_keys = {}

    def sum_of_keys(self) -> Decimal:
        return sum(Decimal(key) for key in self.keys() if not Decimal(key).is_nan())

    def sum_of_values(self) -> Decimal:
        return sum(Decimal(value) for value in self.values() if not Decimal(value).is_nan())

    def product_of_keys(self) -> Decimal:
        return reduce((lambda x, y: Decimal(x) * Decimal(y) if (not Decimal(x).is_nan() and not Decimal(y).is_nan())
        else Decimal(x) if (not Decimal(x).is_nan()) else Decimal(y) if (not (Decimal(y).is_nan())) else 1),
                      self.keys())

    def product_of_values(self) -> Decimal:
        return reduce((lambda x, y: Decimal(x) * Decimal(y) if (not Decimal(x).is_nan() and not Decimal(y).is_nan())
        else Decimal(x) if (not Decimal(x).is_nan()) else Decimal(y) if (not (Decimal(y).is_nan())) else 1),
                      self.values())

    def contains_key(self, key: object) -> bool:
        return key in self.__keys_to_values

    def contains_value(self, value: object) -> bool:
        return value in self.__values_to_keys

    def get_by_key(self, key: object) -> object:
        return self.__keys_to_values[key]

    def get_by_value(self, value: object) -> object:
        return self.__values_to_keys[value]

    def put(self, key: object, value: object) -> bool:
        if key in self.__keys_to_values.keys() or value in self.__values_to_keys.keys():
            return False
        self.__keys_to_values[key] = value
        self.__values_to_keys[value] = key
        return True

    def remove_by_key(self, key: object) -> bool:
        if key not in self.__keys_to_values.keys():
            return False
        corresponding_value: object = self.__keys_to_values[key]
        self.__keys_to_values.pop(key)
        self.__values_to_keys.pop(corresponding_value)
        return True

    def remove_by_key_and_value(self, key: object, value: object) -> bool:
        if key not in self.__keys_to_values.keys():
            return False
        if self.__keys_to_values[key] != value:
            return False
        self.__keys_to_values.pop(key)
        self.__values_to_keys.pop(value)
        return True

    def size(self) -> int:
        return len(self.__keys_to_values)

    def keys(self) -> list:
        return [i for i in self.__keys_to_values.keys()]

    def get_keys_to_values(self) -> dict:
        return self.__keys_to_values

    def get_values_to_keys(self) -> dict:
        return self.__values_to_keys

    def values(self) -> list:
        return [i for i in self.__values_to_keys.keys()]

    def replace_by_key_and_value(self, key: object, value: object) -> bool:
        if key not in self.__keys_to_values.keys():
            return False
        if value in self.__values_to_keys.keys():
            return False

        corresponding_value: object = self.__keys_to_values[key]
        self.__keys_to_values[key] = value
        self.__values_to_keys.pop(corresponding_value)
        self.__values_to_keys[value] = key
        return True

    def replace_by_key_and_two_values(self, key: object, old_value: object, new_value: object) -> bool:
        if key not in self.__keys_to_values.keys():
            return False

        if self.__keys_to_values[key] != old_value:
            return False

        if new_value in self.__values_to_keys.keys():
            return False

        self.__keys_to_values[key] = new_value
        self.__values_to_keys.pop(old_value)
        self.__values_to_keys[new_value] = key
        return True

    def update(self, other):
        # type: (BidirectionalHashMap) -> BidirectionalHashMap
        for key in other.keys():
            self.__keys_to_values[key] = other.get_by_key(key)

        for value in other.values():
            self.__values_to_keys[value] = other.get_by_value(value)
        return self

    def __str__(self):
        # type: () -> str
        return "Keys to values: " + str(self.__keys_to_values) + "\nValues to keys: " + str(self.__values_to_keys) \
               + "\n"

    def clone(self):
        # type: () -> BidirectionalHashMap
        return copy.deepcopy(self)


def main():
    """
    This function is used to write some tests.
    :return: None
    """

    a: BidirectionalHashMap = BidirectionalHashMap()
    b: BidirectionalHashMap = BidirectionalHashMap()
    a.put(1, 3)
    b.put(2, 4)
    b.put(2, 5)
    assert a.size() == b.size(), "TESTS FAILED"
    assert a.get_by_key(1) == 3, "TESTS FAILED"
    assert b.get_by_key(2) == 4, "TESTS FAILED"
    assert b.get_by_value(4) == 2, "TESTS FAILED"
    assert a.get_by_value(3) == 1, "TESTS FAILED"
    a.put("s", "x")
    assert a.get_by_value("x") == "s", "TESTS FAILED"
    a.put(5, 8)
    b.put(6, 7)
    assert a.product_of_keys() == 5, "TESTS FAILED"
    assert b.product_of_keys() == 12, "TESTS FAILED"
    assert a.product_of_values() == 24, "TESTS FAILED"
    assert b.product_of_values() == 28, "TESTS FAILED"
    a.update(b)
    b.replace_by_key_and_value(2, 9)
    b.replace_by_key_and_two_values(2, 9, 17)
    assert a.size() == 5, "TESTS FAILED"
    assert b.size() == 2, "TESTS FAILED"
    b.remove_by_key_and_value(2, 17)
    b.put(5, 4)
    b.put(17, 19)
    assert b.size() == 3, "TESTS FAILED"
    print("TESTS PASSED")


if __name__ == '__main__':
    main()
