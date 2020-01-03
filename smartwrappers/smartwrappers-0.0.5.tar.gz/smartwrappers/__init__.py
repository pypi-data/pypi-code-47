# -*- coding: utf-8 -*-

"""
SmartWrapper library.
Simple wrappers to deal with immutable objects as mutable
putting them to mutable wrappers that can share their content
to other wrappers or stay unique.

:copyright: (c) 2020 Mavedev
:licence: MIT, see LICENCE for more details.

"""

from typing import Any, List
from smartwrappers import constants

__all__ = [
    'SmartWrapper',
    'SoftSmartWrapper',
    'StrictSmartWrapper',
    'wrap',
    'wrap_list',
    'wrap_strictly',
    'wrap_list_strictly'
]


class SmartWrapper:
    """
    This wrapper can contain value of any type.
    You can get current value from wrapper by just calling it as a functor.
    To put some new value inside, just call the wrapper with an argument.
    Note that you can put only single value inside, if you want to store more
    then you should put your values into array and then wrap it.

    Example
    -----------

    .. code-block:: python3

        x = wrap(5)  # short version, equals x = SmartWrapper(5)
        print(x())  # >>> 5
        x(6)
        print(x())  # >>> 6
        x(x() + 1)
        print(x())  # >>> 7
        x('a')
        print(x())  # >>> a

        def plus_five(x):
            x(x() + 5)

        x = wrap(1)
        plus_five(x)
        print(x)  # 6

        y = wrap(None)
        y.steal(x)
        print(x)  # None
        print(y)  # 6

    Class attributes
    -----------
    _MISSING: object
        A dummy object used to determine if value has been passed.

    Parameters
    -----------
    value: Any
        An object you put inside the wrapper. It must be a single value.
    """
    _MISSING = object()

    def __init__(self, value: Any) -> None:
        self.__value = value

    def __call__(self, value: Any = _MISSING) -> Any:
        """
        If value is not defined returns inner value,
        otherwise wrapper put given value inside replacing
        existing one.
        """
        if value is not SmartWrapper._MISSING:
            self.__value = value
        else:
            return self.__value

    def __str__(self) -> str:
        """String representation of the wrapper."""
        return str(self.__value)

    def __repr__(self) -> str:
        """Exact representation of the wrapper."""
        return repr(self.__value)

    def gettype(self) -> type:
        """Returns the type of the current value."""
        return type(self.__value)

    def hasattr(self, attr: str) -> bool:
        """Delegates hasattr to stored object."""
        return hasattr(self.__value, attr)

    def steal(self, other: 'SmartWrapper') -> None:
        """Move value from other wrapper to this one."""
        self.__value, other.__value = other.__value, None


SoftSmartWrapper = SmartWrapper


class StrictSmartWrapper(SmartWrapper):
    """
    This wrapper can contain value of any type, Trying to put another type
    of data inside results in an error.
    You can get current value from wrapper by just calling it as a functor.
    To put some new value inside, just call the wrapper with an argument.
    Note that you can put only single value inside, if you want to store more
    then you should put your values into array and then wrap it.

    Class attributes
    -----------
    _MISSING: object
        A dummy object used to determine if value has been passed.

    Parameters
    -----------
    value: Any
        An object you put inside the wrapper. It must be a single value.
    """
    _MISSING = object()

    def __init__(self, value: Any, type_: type) -> None:
        super().__init__(value)
        self.__type_ = type_

    def __new__(cls, *args, **kwargs):
        StrictSmartWrapper.__check(*args, **kwargs)
        return super(StrictSmartWrapper, cls).__new__(cls)

    def __call__(self, value: Any = _MISSING) -> Any:
        """
        If value is not defined returns inner value,
        otherwise wrapper put given value inside replacing
        existing one.
        """
        if value is not StrictSmartWrapper._MISSING:
            self.__check(value, self.__type_)
        return super().__call__(value)

    def steal(self, other: 'StrictSmartWrapper') -> None:
        """Move value from other wrapper to this one."""
        if self():
            self.__check(other(), self.__type_)
        super().steal(other)

    @staticmethod
    def __check(value: Any, type_: type) -> None:
        """Raise an error if the type of given value does not match given one."""
        if not isinstance(value, type_):
            raise AssertionError(constants.WRONG_TYPE)


def wrap(value: Any) -> SmartWrapper:
    """Less-code style version of SmartWrapper constructor call."""
    return SmartWrapper(value)


def wrap_list(list_: List[Any], *, dimensions: int = 1) -> List:
    """Wraps values of list using SoftSmartWrapper."""
    if dimensions == 1:
        return [wrap(x) for x in list_]
    if dimensions > 1:
        return [wrap_list(x, dimensions=dimensions - 1) for x in list_]
    raise ValueError(constants.WRONG_DIMENSION)


def wrap_strictly(value: Any, type_: type) -> StrictSmartWrapper:
    """Less-code style version of StrictSmartWrapper constructor call."""
    return StrictSmartWrapper(value, type_)


def wrap_list_strictly(list_: List[Any], type_: type, *, dimensions: int = 1) -> List:
    """Wraps values of list using StrictSmartWrapper."""
    if dimensions == 1:
        return [wrap_strictly(x, type_) for x in list_]
    if dimensions > 1:
        return [wrap_list_strictly(x, type_, dimensions=dimensions - 1) for x in list_]
    raise ValueError(constants.WRONG_DIMENSION)
