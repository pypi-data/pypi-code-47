from typing import TypeVar

from zuper_typing import dataclass, Generic


def test_module1():
    @dataclass
    class A:
        a: int

    class B:
        b: int

    X = TypeVar("X")

    @dataclass
    class C(Generic[X]):
        a: int

    D = C[int]

    @dataclass
    class E(D):
        pass

    assert (
        A.__module__ == B.__module__ == C.__module__ == D.__module__ == E.__module__
    ), (A.__module__, B.__module__, C.__module__, D.__module__, E.__module__)
