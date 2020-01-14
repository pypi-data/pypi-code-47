from pineapple_core.core.node import node


@node(module="String", name="ToInt", autotrigger=True)
def string_to_int_node(a: str) -> int:
    return int(a)
