from pineapple_nodes.nodes.assertion_nodes import assert_equals_node, assert_in_list_node


def build_list_check(list_input, key, value_to_find):
    list_check_node = assert_in_list_node()
    list_check_node.connect_input(
        list_input=list_input,
        key=key,
        value=value_to_find
    )
    return list_check_node


def build_int_equals_check(a: int, b: int, message: str):
    equals_check_node = assert_equals_node()
    equals_check_node.connect_input(
        a=a,
        b=b,
        message=message
    )
    return equals_check_node
