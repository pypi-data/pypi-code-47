from pineapple_core.core.node import node
from pineapple_core.core.types import Any


@node(module="Comparison", name="Equals", autotrigger=True)
def equals_node(a: Any(), b: Any()) -> bool:
    return a == b


@node(module="Comparison", name="Different", autotrigger=True)
def different_node(a: Any(), b: Any()) -> bool:
    return a != b


@node(module="Comparison", name="MoreThan", autotrigger=True)
def more_than_node(a: Any(), b: Any()) -> bool:
    return a > b


@node(module="Comparison", name="LessThan", autotrigger=True)
def less_than_node(a: Any(), b: Any()) -> bool:
    return a < b


@node(module="Comparison", name="MoreOrEqual", autotrigger=True)
def more_or_equal_node(a: Any(), b: Any()) -> bool:
    return a >= b


@node(module="Comparison", name="LessOrEqual", autotrigger=True)
def less_or_equal_node(a: Any(), b: Any()) -> bool:
    return a <= b
