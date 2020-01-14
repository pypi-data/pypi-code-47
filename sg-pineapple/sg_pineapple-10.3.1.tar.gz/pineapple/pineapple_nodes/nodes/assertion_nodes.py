from pineapple_core.core.node import node
from pineapple_core.core.types import Any
from pineapple_core.core.input_flags import Optional


equals_result = {"out": {"result": bool, "message": str}}


@node(module="Comparison", name="AssertEquals", autotrigger=True)
def assert_equals_node(a: Any(), b: Any(), message: Optional(str)) -> equals_result:
    result = a == b
    return {"result": result, "message": message.format(str(a), str(b))}


list_compare_result = {"out": {"result": bool, "message": str}}


@node(module="Comparison", name="AssertInList", autotrigger=True)
def assert_in_list_node(
    list_input: list, key: str, value: Any()
) -> list_compare_result:
    in_list = False
    for item in list_input:
        if key:
            if item[key] == value:
                in_list = True
        else:
            if item == value:
                in_list = True
    return {
        "result": in_list,
        "message": "Does {}:{} appear in {}".format(key, str(value), str(list_input)),
    }


@node(module="Comparison", name="AssertNotInList", autotrigger=True)
def assert_not_in_list_node(
    list_input: list, key: str, value: Any()
) -> list_compare_result:
    in_list = False
    for item in list_input:
        if item[key] == value:
            in_list = True
    return {
        "result": not in_list,
        "message": "Does {}:{} not appear in {}".format(
            key, str(value), str(list_input)
        ),
    }


def check_http_code(node_to_check: node, http_code: int) -> assert_equals_node:
    equals_check_node = assert_equals_node()
    equals_check_node.connect_input(
        a=node_to_check["_HttpCode"],
        b=http_code,
        message="Http Code for " + node_to_check.name + ": {}, is equal to {}",
    )
    return equals_check_node
