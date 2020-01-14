from pineapple_core.core.node import node, wrap
from pineapple_core.core.types import Any


report_result = {"passed": bool, "report": str}


@node(module="Comparison", name="Report", autotrigger=True)
def report_node(*args: Any) -> report_result:
    report = ""
    success = True
    for assertion_result in args:
        message = assertion_result["message"]
        result = assertion_result["result"]
        report += f"{message}: {result}\n"
        if not assertion_result["result"]:
            success = False
    report = f"Passed: {success}\n{report}"
    return wrap({"passed": success, "report": report})
