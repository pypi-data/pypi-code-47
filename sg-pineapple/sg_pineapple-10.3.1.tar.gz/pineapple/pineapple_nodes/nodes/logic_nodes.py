from pineapple_core.core.node import node


@node(module="Logic", name="Not", autotrigger=True)
def not_node(a: bool) -> bool:
    return not a


@node(module="Logic", name="And", autotrigger=True)
def and_node(a: bool, b: bool) -> bool:
    return a and b


@node(module="Logic", name="Or", autotrigger=True)
def or_node(a: bool, b: bool) -> bool:
    return a or b


@node(module="Logic", name="Xor", autotrigger=True)
def xor_node(a: bool, b: bool) -> bool:
    return a != b


@node(module="Logic", name="True", autotrigger=True)
def true_node() -> bool:
    return True


@node(module="Logic", name="False", autotrigger=True)
def false_node() -> bool:
    return False
