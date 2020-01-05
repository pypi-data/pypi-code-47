from typing import Dict, List, TypeVar

from nose.tools import assert_equal, raises

from zuper_typing import debug_print, logger
from zuper_typing.annotations_tricks import name_for_type_like
from zuper_typing.get_patches_ import assert_equivalent_types
from zuper_typing.my_dict import get_DictLike_args
from zuper_typing.zeneric2 import get_dataclass_info, resolve_types
from zuper_typing_tests.test_utils import my_assert_equal


def test_nested_zuper():
    from zuper_typing import dataclass, Generic

    check_nested(Generic, dataclass)


@raises(Exception)
def test_nested_original():
    from dataclasses import dataclass
    from typing import Generic

    check_nested(Generic, dataclass)


def check_nested(Generic, dataclass):
    X = TypeVar("X")

    @dataclass
    class A(Generic[X]):
        a: X

    logger.info(debug_print(A))

    Ai = get_dataclass_info(A)
    assert_equal(Ai.bindings, {})
    assert_equal(Ai.generic_att, (X,))

    Astr = A[str]
    logger.info(debug_print(Astr))

    Astri = get_dataclass_info(Astr)
    assert_equal(Astri.bindings, {X: str})
    assert_equal(Astri.generic_att, ())

    V = TypeVar("V")

    @dataclass
    class B(A[List[V]]):
        b: int

    logger.info(debug_print(B))
    Bi = get_dataclass_info(B)
    assert_equal(Bi.bindings, {X: List[V]})
    assert_equal(Bi.generic_att, (V,))

    Bfloat = B[float]
    logger.info(debug_print(Bfloat))
    Bfloati = get_dataclass_info(Bfloat)
    assert_equal(Bfloati.bindings, {X: List[float], V: float})
    assert_equal(Bfloati.generic_att, ())

    name = name_for_type_like(Bfloat)

    assert_equal(name, "B[float]")


def test_nested_recursive1():
    from zuper_typing import dataclass

    X = TypeVar("X")

    @dataclass
    class A:
        a: "Dict[str, A]"

    resolve_types(A)


@raises(TypeError)
def test_nested_recursive0():
    """ Note that we need to instantiate """
    from zuper_typing import dataclass, Generic

    X = TypeVar("X")

    @dataclass
    class A(Generic[X]):
        a: "Dict[str, A]"  # <-- BOOM

    resolve_types(A)


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

    # dataclass zuper_typing.zeneric2.B[float] (test_nested_recursive.<locals>.B[float])
    #  field        a : Dict[str,A[float]]
    #
    # but want
    # dataclass zuper_typing.zeneric2.B[float] (test_nested_recursive.<locals>.B[float])
    #  field        a : Dict[str,A[List[float]]]

    # F = Dict[str, A[List[V]]]
    # F2 = replace_typevars(F, bindings={V: float}, symbols={})
    # my_assert_equal(F2, E)
    # F = A[List[V]]
    # logger.info(debug_print({"ALISTV": F}))
    # F2 = replace_typevars(F, bindings={V: float}, symbols={})
    # E = A[List[float]]
    # my_assert_equal(F2, E)
    #
    # F = Dict[str, A[List[V]]]
    # F2 = replace_typevars(F, bindings={V: float}, symbols={})
    # E = Dict[str, A[List[float]]]
    # my_assert_equal(F2, E)

    _, X = get_DictLike_args(Bfloat.__annotations__["a"])
    my_assert_equal(X.__name__, "A[List[float]]")


# but want

#
# name = name_for_type_like(Bfloat)
#
# assert_equal(name, "B[float]")


def test_entity():
    from zuper_typing import dataclass, Generic

    X = TypeVar("X")

    @dataclass
    class Entity(Generic[X]):
        t: X
        a: "Entity[X]"
        b: "Entity[int]"

    EA = Entity[bool]
    logger.info(debug_print(EA))

    assert_equivalent_types(Entity.__annotations__["b"], EA.__annotations__["b"])
