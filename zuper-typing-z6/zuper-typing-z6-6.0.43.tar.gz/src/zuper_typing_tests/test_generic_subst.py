from typing import TypeVar

from nose.tools import assert_equal

from zuper_typing import dataclass, Generic
from zuper_typing.dataclass_info import get_dataclass_info
from zuper_typing.get_patches_ import assert_equivalent_types
from . import logger


def test1():
    X = TypeVar("X")
    Y = TypeVar("Y")

    @dataclass
    class A(Generic[X]):
        value: X

    B = A[Y]

    logger.info(A=A, i=get_dataclass_info(A))
    logger.info(B=B, i=get_dataclass_info(B))

    assert_equal(B.__name__, "A[Y]")
    clsi = get_dataclass_info(B)
    # assert_equal(clsi.extra, ())
    assert_equal(clsi.orig, (Y,))
    # assert_equal(clsi.bindings, {})


def test2():
    X = TypeVar("X")
    Y = TypeVar("Y")

    @dataclass
    class A(Generic[X]):
        value: X

    B = A[Y]
    C = B[X]
    assert_equivalent_types(C, A)
