from typing import TypeVar

from zuper_typing import dataclass, Generic
from zuper_typing.get_patches_ import assert_equivalent_types
from . import logger

assert logger

X = TypeVar("X")
Y = TypeVar("Y")


def test_subst_id():
    X = TypeVar("X")

    @dataclass
    class C(Generic[X]):
        a: X

    CX = C[X]
    assert_equivalent_types(CX, C)


def test_right_subst():
    @dataclass
    class A(Generic[X]):
        v: X

    Aint = A[int]

    AY = A[Y]
    logger.info(
        "", A=A, typeA=type(A), AY=AY, typeAY=type(AY), Aint=Aint, typeAint=type(Aint)
    )

    AYint = AY[int]

    assert_equivalent_types(Aint, AYint)
