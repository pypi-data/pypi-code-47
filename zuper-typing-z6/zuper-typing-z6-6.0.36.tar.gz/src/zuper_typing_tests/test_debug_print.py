import numbers
from dataclasses import field, replace
from datetime import datetime
from decimal import Decimal
from typing import (
    Any,
    Callable,
    ClassVar,
    Dict,
    Iterator,
    List,
    Optional,
    Sequence,
    Set,
    Type,
    TypeVar,
    Union,
)

from zuper_typing import dataclass, debug_print
from zuper_typing.debug_print_ import get_default_dpoptions
from zuper_typing.my_dict import make_dict, make_list, make_set, MyBytes
from zuper_typing.my_intersection import make_Intersection
from zuper_typing.uninhabited import make_Uninhabited


def test1():
    @dataclass
    class A:
        a: object

    a = A(2)
    debug_print(a)

    a = A(2.0)
    debug_print(a)

    a = A(b"hello")
    debug_print(a)
    a = A("hello")
    debug_print(a)

    a = A(datetime.now())
    debug_print(a)

    X = TypeVar("X")
    Y = TypeVar("Y", bound=int)
    Z = TypeVar("Z", covariant=True)
    U = TypeVar("U", contravariant=True)

    class SimpleClass:
        pass

    @dataclass
    class Empty:
        pass

    @dataclass
    class WithDunder:
        __with_dunder__: int

    @dataclass
    class WithFactory:
        a: tuple = field(default_factory=lambda: (1,))

    @dataclass
    class WithDefault:
        a: tuple = field(default=(1, 2))

    @dataclass
    class WithClassVar1:
        a: ClassVar[int]

    @dataclass
    class WithClassVar2:
        a: ClassVar[int] = 2

    @dataclass
    class Recursive:
        a: "Optional[Recursive]" = None

    r1 = Recursive(Recursive())

    class MyStr(str):
        pass

    @dataclass
    class WithPrintOrder:
        __print_order__ = ["b", "a"]
        a: int
        b: int

    ts = [
        Empty,
        Union[int, bytes],
        Union[int, bytes, float, bool],  # triggers multi-line
        Optional[int],
        Optional[int],
        make_Intersection((int, bytes)),
        make_Intersection((int, bytes, float, bool)),  # triggers multi-line
        A,
        Callable[[int], bool],
        X,
        Y,
        Z,
        U,
        Iterator[int],
        Sequence[int],
        make_Uninhabited(),
        Any,
        object,
        int,
        float,
        Type[float],
        ClassVar[float],
        make_list(int),
        List[int],
        make_set(int),
        Set[int],
        make_dict(int, int),
        Dict[int, int],
        SimpleClass,
        WithClassVar1,
        WithClassVar2,
        type(None),
        type,
        MyStr,
        WithDunder,
        WithDefault,
        WithFactory,
        WithPrintOrder,
        type(...),
        BaseException,
        numbers.Number,
        Decimal,
        datetime,
        slice,
    ]
    obs = [
        slice(1, 2),
        slice(1, 2, 3),
        slice(1),
        ...,
        Decimal(1),
        WithPrintOrder(1, 2),
        WithDunder(1),
        WithClassVar2(),
        WithClassVar1(),
        WithFactory(),
        WithFactory((1,)),
        MyStr("1"),
        {1: 2},
        {1},
        {},
        r1,
        2,
        2.0,
        b"hello",
        MyBytes(b"hello"),
        "hello",
        "hello\n" * 20,
        "-----BEGIN hey",
        "Qmokdapekpoakdpoek",
        "Traceback",
        "zdpukdapeokpoeakpok",
        ["hellow"] * 20,
        set(["hellow"] * 20),
        set(["hell\now"]),
        tuple(["hellow"] * 20),
        {i: k for i, k in enumerate("hellow" * 20)},
        None,
        (),
        (a,),
        [],
        set([]),
        "\n",
        {"a": "a\nb\nc"},
    ]
    opt0 = get_default_dpoptions()

    def id_gen_null(a: object):
        return None

    def id_gen_exc(a: object):
        raise Exception()

    tryopts = [
        dict(compact=True),
        dict(abbreviate=True),
        dict(max_initial_levels=0),
        dict(id_gen=id),
        dict(id_gen=id, abbreviate=True),
        dict(id_gen=id_gen_null),
        dict(id_gen=id_gen_exc, abbreviate=True),
        dict(omit_type_if_empty=False),
        dict(omit_type_if_short=False),
        dict(obey_print_order=False),
        dict(abbreviate_zuper_lang=True),
        dict(ignore_dunder_dunder=True),
        dict(do_not_display_defaults=False),
    ]
    opts = [replace(opt0, **t) for t in tryopts]
    for t in ts + obs:
        str(t)
        repr(t)
        for opt in opts:
            debug_print(t, opt=opt)
