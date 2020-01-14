from pineapple_core.core.node import node
from typing import List


@node(module="List", name="Length", autotrigger=True)
def len_node(list: List) -> int:
    return len(list)
