from typing import (
    Callable,
    cast,
    ClassVar,
    Dict,
    List,
    Optional,
    Set,
    Tuple,
    Union,
)

from nose.tools import raises

from zuper_ipce.constants import JSONSchema
from zuper_ipce.schema_caching import assert_canonical_schema
from zuper_ipce_tests.test_utils import assert_type_roundtrip
from zuper_typing import dataclass
from zuper_typing.assorted_recursive_type_subst import recursive_type_subst
from zuper_typing.get_patches_ import assert_equivalent_types
from zuper_typing.monkey_patching_typing import MyNamedArg, original_dict_getitem
from zuper_typing.my_dict import make_dict, make_list, make_set


@raises(ValueError)
def test_schema1():
    schema = cast(JSONSchema, {})
    assert_canonical_schema(schema)


def test_rec1():
    @dataclass
    class A:
        a: Dict[int, bool]
        a2: Dict[bool, bool]
        b: Union[float, int]
        b2: Dict[bool, float]
        c: Set[int]
        c2: Set[bool]
        d: List[int]
        d2: List[bool]
        e: Tuple[int, bool]
        e2: Tuple[float, bool]
        f: make_dict(int, int)
        g: make_set(int)
        h: make_list(int)
        h2: make_list(bool)
        i: Optional[int]
        l: Tuple[int, ...]
        m: original_dict_getitem((int, float))
        n: original_dict_getitem((bool, float))

        q: ClassVar[int]
        r: ClassVar[bool]
        s: Callable[[int], int]
        s2: Callable[[bool], int]
        # noinspection PyUnresolvedReferences
        t: Callable[[MyNamedArg(int, "varname")], int]
        # noinspection PyUnresolvedReferences
        t2: Callable[[MyNamedArg(int, "varname")], int]

    T2 = recursive_type_subst(A, swap)

    T3 = recursive_type_subst(T2, swap)
    # logger.info(pretty_dict("A", A.__annotations__))
    # logger.info(pretty_dict("T2", T2.__annotations__))
    # logger.info(pretty_dict("T3", T3.__annotations__))
    assert_equivalent_types(A, T3, set())

    assert_type_roundtrip(A)


def swap(x):
    if x is int:
        return str
    if x is str:
        return int
    return x
