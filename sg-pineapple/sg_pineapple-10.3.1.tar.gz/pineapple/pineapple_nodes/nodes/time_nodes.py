from pineapple_core.core.node import node
import time


@node(module="Time", name="Time", autotrigger=False)
def time_node() -> float:
    return time.time()
