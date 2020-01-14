from pineapple_core.core.node import node, wrap
from pineapple_core.core.input_flags import Hidden
from pineapple_core.core.types import Any
from pineapple_core.core.node_output import NodeOutput


@node(module="Value", name="String", autotrigger=True)
def string_node(a: Hidden(str)) -> str:
    return a


@node(module="Value", name="Int", autotrigger=True)
def int_node(a: Hidden(int)) -> int:
    return a


@node(module="Value", name="Bool", autotrigger=True)
def bool_node(a: Hidden(bool)) -> bool:
    return a


@node(module="Value", name="List", autotrigger=True)
def list_node(a: Hidden(list)) -> list:
    return a


@node(module="Value", name="Dict", autotrigger=True)
def dict_node(a: Hidden(dict)) -> dict:
    return a


def convert_native_type_to_node(value):
    if isinstance(value, str):
        return string_node(value)
    elif isinstance(value, bool):
        return bool_node(value)
    elif isinstance(value, int):
        return int_node(value)
    elif isinstance(value, list):
        return list_node(value)
    elif isinstance(value, dict):
        return dict_node(value)
    else:
        return value


def decompose_node_helper(node):
    def on_connect_input(node, input, output):
        for output_name, output_value in output.output_type.items():
            node.add_output(NodeOutput(node, output_name, output_value))

    node.on.connect_input.add(on_connect_input)


@node(
    module="Value",
    name="Decompose",
    autotrigger=True,
    helper_function=decompose_node_helper,
)
def decompose_node(item: Any()):
    return wrap(item)
