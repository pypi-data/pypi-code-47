from typing import TypeVar

from nose.tools import assert_equal

from zuper_typing import dataclass, Generic
from zuper_typing.dataclass_info import get_dataclass_info
from . import logger


def test1():
    from zuper_typing import debug_print

    assert debug_print
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
    assert_equal(clsi.extra, ())
    assert_equal(clsi.orig, (Y,))
    assert_equal(clsi.bindings, {})
