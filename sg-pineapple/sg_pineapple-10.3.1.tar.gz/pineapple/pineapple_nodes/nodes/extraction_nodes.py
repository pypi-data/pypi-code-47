from pineapple_core.core.node import node, wrap, Node
from pineapple_core.core.types import Any
from pineapple_core.core.input_flags import Optional
from pineapple_core.core.node_output import NodeOutput

from nq import nested_query


def extract_from_list_node_helper(node):
    def on_connect_input(node, input, output):
        if input.input_type == list:
            if isinstance(output.output_type[0], dict):
                for output_name, output_value in output.output_type[0].items():
                    node.add_output(NodeOutput(node, output_name, output_value))
            else:
                node.add_output(NodeOutput(node, output.name, output.output_type))
            del node.outputs["out"]

    node.on.connect_input.add(on_connect_input)


@node(
    module="Extraction",
    name="ExtractFromList",
    autotrigger=True,
    helper_function=extract_from_list_node_helper,
)
def extract_from_list_node(
    list_input: list, index: int, error_message: Optional(str)
) -> Any():
    try:
        return wrap(list_input[index])
    except Exception as e:
        if error_message is not None:
            raise Exception(error_message.format(e))
        else:
            raise e


@node(
    module="Extraction",
    name="ExtractWithFilter",
    autotrigger=True,
    helper_function=extract_from_list_node_helper,
)
def extract_item_with_filter_node(list_input: list, key: str, to_match: Any()) -> Any():
    for item in list_input:
        try:
            if item[key] == to_match:
                return wrap(item)
        except Exception:
            raise Exception(f"List {list_input} does not contain requested key {key}")
    raise Exception(
        f"List {list_input} does not contain item with {key} equal to {to_match}"
    )


def _common_iterable(obj):
    if isinstance(obj, dict):
        return obj.items()
    else:
        return (index for index, value in enumerate(obj))


def smart_extract_helper(self, *args, **kwargs):
    self._sen_path_parts = args


@node(
    module="Extraction",
    name="SmartExtract",
    autotrigger=True,
    helper_function=smart_extract_helper,
)
def smart_extract_node(self: Node, iterable: Any(), flags: Any()) -> Any():
    result = nested_query(iterable, *self._sen_path_parts, flags=flags)
    return result
