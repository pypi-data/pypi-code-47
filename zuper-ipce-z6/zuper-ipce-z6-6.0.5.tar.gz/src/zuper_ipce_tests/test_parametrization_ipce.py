from typing import TypeVar, Dict, List

from zuper_ipce import logger
from zuper_ipce_tests.test_utils import assert_type_roundtrip
from zuper_typing import debug_print
from zuper_typing.zeneric2 import resolve_types, get_dataclass_info
from zuper_typing_tests.test_utils import my_assert_equal


def test_nested_recursive():
    """
    creation        name given      csi.gen csi.orig bindings
    A(Generic[X])   A[X]            (X,)    (X,)     {}
    U = A[List[V]]  A[List[V]]      (V,)    (X,)     X=List[float]
    W = U[float]    A[List[float]]  ()      (X,)     X=List[float] V=float
    B(A(List[V]))   B[V]            (V,)    (V,)     X=List[float]
    B[float]        V[floatt]       ()      (V,)     X=List[float] V=float

    """
    from zuper_typing import dataclass, Generic

    X = TypeVar("X")

    V = TypeVar("V")

    @dataclass
    class A(Generic[X]):
        a: "Dict[str, A[X]]"
        x: X

    resolve_types(A)
    logger.info(debug_print(A))
    #
    Ai = get_dataclass_info(A)
    my_assert_equal(Ai.bindings, {})
    my_assert_equal(Ai.generic_att, (X,))
    my_assert_equal(Ai.orig, (X,))
    my_assert_equal(A.__name__, "A[X]")

    U = A[List[V]]
    Ui = get_dataclass_info(U)
    my_assert_equal(Ui.bindings, {X: List[V]})
    my_assert_equal(Ui.generic_att, (V,))
    my_assert_equal(Ui.orig, (X,))
    my_assert_equal(U.__name__, "A[List[V]]")

    W = U[float]
    Wi = get_dataclass_info(W)
    my_assert_equal(Wi.bindings, {X: List[float], V: float})
    my_assert_equal(Wi.generic_att, ())
    my_assert_equal(Wi.orig, (X,))
    my_assert_equal(W.__name__, "A[List[float]]")

    Astr = A[str]
    logger.info(debug_print(Astr))
    #
    Astri = get_dataclass_info(Astr)
    my_assert_equal(Astri.bindings, {X: str})
    my_assert_equal(Astri.generic_att, ())
    my_assert_equal(Astr.__name__, "A[str]")

    @dataclass
    class B(A[List[V]]):
        b: int
        b2: "List[B[V]]"

    logger.info(debug_print(B))

    Bi = get_dataclass_info(B)
    my_assert_equal(Bi.bindings, {X: List[V]})
    my_assert_equal(Bi.generic_att, (V,))
    my_assert_equal(Bi.orig, (V,))
    my_assert_equal(B.__name__, "B[V]")

    #
    Bfloat = B[float]
    logger.info(debug_print(Bfloat))
    Bfloati = get_dataclass_info(Bfloat)
    my_assert_equal(Bfloati.bindings, {X: List[float], V: float})
    my_assert_equal(Bfloati.generic_att, ())
    my_assert_equal(Bfloati.orig, (V,))
    my_assert_equal(Bfloat.__name__, "B[float]")

    assert_type_roundtrip(A)
    assert_type_roundtrip(U)
    assert_type_roundtrip(W)
    assert_type_roundtrip(B)
    assert_type_roundtrip(Bfloat)
