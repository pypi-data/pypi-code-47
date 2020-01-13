from nose.tools import raises

from zuper_commons.types import ZTypeError
from zuper_typing import dataclass, debug_print
from zuper_typing.subcheck import can_be_used_as2
from . import logger


def test_nominal_no_nominal():
    @dataclass
    class A:
        a: int

    @dataclass
    class C:
        nominal = True

    @dataclass
    class D:
        pass

    assert not can_be_used_as2(A, C)
    assert can_be_used_as2(A, D)


# @raises(TypeError)
def test_nominal_inherit():
    """ this is a limitation of the spec """

    @dataclass
    class A:
        a: int

        nominal = True

    @dataclass
    class B(A):
        b: int


def test_nominal_inherit2():
    @dataclass
    class A:
        a: int

        nominal = True

    logger.info(debug_print(A))

    @dataclass
    class B(A):
        b: int

    logger.info(debug_print(B))

    @dataclass
    class C(B):
        e: int

    logger.info(debug_print(C))


@raises(ZTypeError)
def test_nominal_inherit3():
    @dataclass
    class A:
        a: int
        a0: int = 2

        nominal = True

    logger.info(debug_print(A))

    @dataclass
    class B(A):
        b: int

    logger.info(debug_print(B))
