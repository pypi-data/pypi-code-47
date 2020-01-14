from pineapple_core.core.node import node
from pineapple_core.core.types import Any


@node(module="IO", name="Input")
def input_node(prompt: str) -> str:
    return input(prompt)


@node(module="IO", name="Print")
def print_node(a: str, *args: Any, **kwargs: Any):
    print(a.format(*args, **kwargs))
