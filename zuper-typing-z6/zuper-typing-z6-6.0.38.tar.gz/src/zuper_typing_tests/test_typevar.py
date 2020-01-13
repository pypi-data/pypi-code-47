from typing import TypeVar

from nose.tools import raises

from zuper_typing.annotations_tricks import (
    get_TypeVar_bound,
    get_TypeVar_name,
    is_TypeVar,
)
from zuper_typing.monkey_patching_typing import MyNamedArg


@raises(ValueError)
def test_notallowed():
    MyNamedArg(int, "1")


def test_typevars1():
    X = TypeVar("X")
    assert is_TypeVar(X)
    assert get_TypeVar_name(X) == "X"
    assert get_TypeVar_bound(X) is object


def test_typevars2():
    Y = TypeVar("Y", bound=int)
    assert is_TypeVar(Y)
    assert get_TypeVar_name(Y) == "Y"
    assert get_TypeVar_bound(Y) is int
