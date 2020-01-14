from pineapple_core.core.node import node, Node
from pineapple_core.core.types import Any
from pineapple_core.static_analysis.static_analysis import analyse_scenario
import time


@node(module="Flow", name="If")
def if_node(self: Node, condition: bool):
    if condition:
        if self.get_flow(True):
            self.get_flow(True).enable()
        if self.get_flow(False):
            self.get_flow(False).disable()
    else:
        if self.get_flow(False):
            self.get_flow(False).enable()
        if self.get_flow(True):
            self.get_flow(True).disable()


@node(module="Flow", name="Range")
def range_node(start: int, end: int, step: int = 1) -> int:
    for i in range(start, end, step):
        yield i


class NotANodeError(Exception):
    def __init__(self, name, value):
        super().__init__(
            f"Expected type <Node> for field '{name}'"
            f" but got value '{value}' of type <{type(value)}>"
        )


class NodeContainer(object):
    def __init__(self, parent, node_container_id, node_container_name, disabled=False):
        object.__setattr__(self, "nodes", {})
        object.__setattr__(self, "parent", parent)
        object.__setattr__(self, "container_id", node_container_id)
        object.__setattr__(self, "container_name", node_container_name)
        object.__setattr__(self, "disabled", disabled)
        object.__setattr__(self, "done", False)

    def __setattr__(self, name, value):
        if not isinstance(value, Node):
            raise NotANodeError(name, value)
        value.id = f"{object.__getattribute__(self, 'container_id')}.{name}"
        object.__getattribute__(self, "nodes")[name] = value

    def __getattr__(self, name):
        return object.__getattribute__(self, "nodes")[name]

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        pass

    def __lshift__(self, node):
        ref = object
        node.on.before_flow.add(lambda x, y: ref.__setattr__(self, "done", False))
        object.__getattribute__(self, "parent").connect_flow(
            node,
            object.__getattribute__(self, "container_id"),
            object.__getattribute__(self, "disabled"),
        )
        object.__getattribute__(self, "parent").get_flow(
            object.__getattribute__(self, "container_id")
        ).pretty_name = object.__getattribute__(self, "container_name")

    def __bool__(self):
        return object.__getattribute__(self, "done")

    def validate_step(self):
        object.__setattr__(self, "done", True)


def sequence_helper(self: Node):
    self.__sequence_steps = []

    def find_node_container_from_flow(flow):
        if flow.name in [step.container_id for step in self.__sequence_steps]:
            node_container = next(
                filter(
                    lambda step: step.container_id == flow.name, self.__sequence_steps
                )
            )
            return node_container
        return None

    def on_flow_failure(self, flow, exception):
        for flow in self.flows:
            flow.disable()
        if self.get_flow("failure_step"):
            self.get_flow("failure_step").enable()

    def on_before_flow(self, flow):
        node_container = find_node_container_from_flow(flow)
        if node_container is not None:
            flow_index = self.__sequence_steps.index(node_container)
            print(
                f"[Step {flow_index + 1}/{len(self.__sequence_steps)}] =>",
                flow.pretty_name,
            )
        else:
            print(f"[Special Step] =>", flow.name)

    def on_after_flow(self, flow):
        node_container = find_node_container_from_flow(flow)
        if node_container is not None:
            node_container.validate_step()

    def global_nodes():
        self.__global_nodes_container = NodeContainer(self, "global_nodes", "Global Nodes")
        return self.__global_nodes_container

    def step(step_id, step_pretty_name=None):
        new_container = NodeContainer(
            self, step_id, step_pretty_name if step_pretty_name is not None else step_id
        )
        self.__sequence_steps.append(new_container)
        return new_container

    def failure_step(func=None):
        # TODO: Add a Node to store exception
        self.__failure_node_container = NodeContainer(
            self, "failure_step", "Failure Step", True
        )
        if func and callable(func):
            self.__failure_node_container.failure = node(
                module="Flow", name=f"FailureStep_{func.__module__}.{func.__name__}"
            )(func)()
            self.__failure_node_container << self.__failure_node_container.failure
            return self.__failure_node_container.failure
        else:
            self.on.flow_failure.add(on_flow_failure)
            return self.__failure_node_container

    def on_trigger(self):
        analyse_scenario(self)

    self.on.before_flow.add(on_before_flow)
    self.on.trigger.add(on_trigger)
    self.on.after_flow.add(on_after_flow)
    self.on.flow_failure.add(on_flow_failure)
    self.global_nodes = global_nodes
    self.failure_step = failure_step
    self.step = step


@node(module="Flow", name="Sequence", helper_function=sequence_helper)
def sequence_node():
    pass


@node(module="Flow", name="Sleep")
def sleep_node(delay: float):
    time.sleep(delay)


class SwitchNodeDefault:
    @staticmethod
    def __static_repr__():
        return "__SWITCH_DEFAULT__"


@node(module="Flow", name="Switch")
def switch_node(self: Node, branch: Any(), *args, **kwargs):
    found_route = False
    for flow in self.flows:
        if flow.name == branch:
            flow.enable()
            found_route = True
        else:
            flow.disable()
    if not found_route:
        if self.get_flow(SwitchNodeDefault):
            self.get_flow(SwitchNodeDefault).enable()


def wait_until_helper(node, *args, **kwargs):
    node.connect_flow(node, False)

    def on_connect_flow(node, flow):
        if flow.name is True:
            flow.disable()

    node.on.connect_flow.add(on_connect_flow)


@node(module="Flow", name="WaitUntil", helper_function=wait_until_helper)
def wait_until_node(self: Node, condition: bool, delay: float):
    if condition:
        self.get_flow(False).disable()
    else:
        time.sleep(delay)


@node(module="Flow", name="Null")
def null_node():
    pass


@node(module="Flow", name="Exception")
def exception_node(exception_type: Exception, *args: Any(), **kwargs: Any()):
    raise exception_type(*args, **kwargs)


@node(module="Flow", name="StringException")
def format_exception_node(
    exception_name: str, string: str, *args: Any(), **kwargs: Any()
):
    raise type(exception_name, (Exception,), {})(string.format(*args, **kwargs))
