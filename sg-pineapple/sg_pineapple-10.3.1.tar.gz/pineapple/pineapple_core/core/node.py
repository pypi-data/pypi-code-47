# -*- coding: utf-8 -*-
"""This module contains everything that is related to Nodes.
This module contains the Node class and several helper functions.
"""

import time
from inspect import getfullargspec
from typing import Any, Callable, Dict, List, Tuple, Union
from uuid import UUID, uuid4

from klotan.match import OptionalKey

from pineapple_core.core.callbacks import NodeCallbacks
from pineapple_core.core.exceptions import (
    AmbiguousNodeOutputError,
    InexistantOutputResultError,
    InvalidNodeFunctionReturnTypeError,
    NodeDoesNotAllowArgsError,
    NodeDoesNotAllowKwargsError,
    NodeOutputNotFoundError,
    NotANodeOutputError,
    ResultOutputMismatchError,
    NoOutputError,
)
from pineapple_core.core.flows import Flow
from pineapple_core.core.input_flags import Hidden, Optional, InputFlag, contains_flag
from pineapple_core.core.node_input import NodeInput
from pineapple_core.core.node_output import NodeOutput
from pineapple_core.core.store import model_store, node_store
from pineapple_core.core.types import PineappleType


class Node:
    """
    A class used to represent an object that contains a function and several attributes
    A Node can have multiple inputs and outputs that can be used to connect the node to other ones
    The inputs are the internal function parameters and the outputs are the function's results

    Attributes
    ----------
    function: Callable
        The function that is contained in the Node
        All the inputs / outputs of the function should be annotated as the Node
        uses those annotations to determine inputs / outputs types
    module: str
        The module of the node, it is simply a category where the Node fits
        For example "Math" nodes or "Logic" nodes
    name: str
        Name of the Node
    autotrigger: bool
        Whether the Node can be triggered automatically through its outputs when a connected
        node needs the result of self node
    """

    def __init__(self, function: Callable, module: str, name: str, autotrigger: bool):
        self.id = uuid4()
        self.function = function
        self.module = module
        self.name = name
        self.flows = []
        self.autotrigger = autotrigger
        self.function_arg_spec = getfullargspec(self.function)
        self.on = NodeCallbacks()
        function_inputs = self._find_input_arguments(function)
        self.inputs = {}
        for (input_name, input_value) in function_inputs.items():
            self.inputs[input_name] = self._build_node_input(input_name, input_value)

        self.args_inputs, self.kwargs_inputs = [], {}
        self.allow_args = self.function_arg_spec.varargs is not None
        self.allow_kwargs = self.function_arg_spec.varkw is not None
        self.outputs = {
            key: NodeOutput(self, key, output_type)
            for key, output_type in self._build_return_types().items()
        }
        self.is_aware = False
        self.origin = self
        if "self" in self.inputs:
            self.is_aware = True
        self.delay = 0
        self.retries = 0
        self.trigger_log = {"success": 0, "failure": 0, "trigger": 0}

    def set_retries(self, retries: int, delay: float = 0) -> "Node":
        """Set the amount of retries a Node can call its function and
        catching the Exception without failing

        Parameters
        ==========
        retries: int
            Amount of retries a Node can call its function and catching the
            Exception without failing
        delay: float [0]
            Optional delay in seconds between each retry
        """
        self.delay = delay
        self.retries = retries

    def get_connected_nodes(self) -> List["Node"]:
        """Returns all Nodes connected to the current Node

        Returns
        =======
        List[Node]:
            List of Nodes connected to the current Node
        """
        flow_nodes = [flow.node for flow in self.flows]
        input_nodes = [
            input.connected_output.node
            for input in (
                list(self.inputs.values())
                + self.args_inputs
                + list(self.kwargs_inputs.values())
            )
            if input.connected_output
        ]
        connected_nodes = flow_nodes + input_nodes
        return list(set(connected_nodes))

    def copy(self):
        """Copies a Node.
        It will recursively call copy() for all inputs, outputs and flows.

        Returns
        =======
        Node:
            Reference to the newly copied Node
        """
        node_copy = Node(self.function, self.module, self.name, self.autotrigger)
        node_copy.id = self.id
        node_copy.inputs = {key: value.copy() for key, value in self.inputs.items()}
        node_copy.outputs = {key: value.copy() for key, value in self.outputs.items()}
        node_copy.allow_args, node_copy.allow_args = self.allow_args, self.allow_kwargs
        node_copy.on = self.on.copy()
        node_copy.flows = [flow.copy() for flow in self.flows]
        node_copy.args_inputs = [arg_input.copy() for arg_input in self.args_inputs]
        node_copy.kwargs_inputs = {
            key: value.copy() for key, value in self.kwargs_inputs.items()
        }
        node_copy.is_aware = self.is_aware
        node_copy.origin = self.origin
        node_copy.retries = self.retries
        node_copy.delay = self.delay
        node_copy.trigger_log = {key: value for key, value in self.trigger_log.items()}
        return node_copy

    def update_references(self, scenario_state: Dict[UUID, "Node"]):
        """Update all references within the Node (to other Nodes) based
        on a Dictionnary containing all the new Node references.

        Parameters
        ==========
        scenario_state: Dict[UUID, Node]
            All Nodes the current Node can use to update its internal references.
        """

        def find_output(search_output):
            for current_node in scenario_state.values():
                for output in current_node.outputs.values():
                    if search_output.id == output.id:
                        return output
            return None

        for node_input in self.inputs.values():
            if node_input.node:
                node_input.node = scenario_state[node_input.node.id]
            if node_input.connected_output:
                node_input.connected_output = find_output(node_input.connected_output)
        for output in self.outputs.values():
            if output.node:
                output.node = scenario_state[output.node.id]
        for flow in self.flows:
            flow.node = scenario_state[flow.node.id]
        for node_input in self.args_inputs:
            node_input.node = scenario_state[node_input.node.id]
        for node_input in self.kwargs_inputs.values():
            node_input.node = scenario_state[node_input.node.id]

    def _build_return_types(self) -> Dict[Any, Any]:
        return_types = (
            self.function.__annotations__["return"]
            if "return" in self.function.__annotations__
            else None
        )
        if isinstance(return_types, (list, tuple)):
            return_types = {key: value for key, value in enumerate(return_types)}
        elif isinstance(return_types, (PineappleType, type)):
            return_types = {"out": return_types}
        elif return_types is None:
            return_types = {}
        elif not isinstance(return_types, dict):
            raise InvalidNodeFunctionReturnTypeError(self, self.function)
        return return_types

    def _build_node_input(self, name: str, value: Any) -> NodeInput:
        input_type = value.underlying_type if isinstance(value, InputFlag) else value
        optional = contains_flag(value, Optional)
        hidden = contains_flag(value, Hidden)
        return NodeInput(self, name, input_type, hidden, optional)

    def _find_input_arguments(self, function: Callable) -> Dict[str, Any]:
        temp_inputs = {}
        for name, value in function.__annotations__.items():
            if name not in [
                "return",
                self.function_arg_spec.varargs,
                self.function_arg_spec.varkw,
            ]:
                temp_inputs[name] = value
        return temp_inputs

    def _args_keys_to_index(self, values: Dict[str, Any]) -> List[Any]:
        """
        Function for internal use only
        It will transform a dictionnary of values to an array of values
        The array index of the value is determined with the order of the output names

        Parameters
        ----------
        values : Dict[str, Any]
            Dictionnary of values

        Returns
        -------
        list[Any]
            A list of values
        """
        args = []
        for arg in self.function_arg_spec.args:
            if arg in values:
                args.append(values[arg])
        return args

    def full_name(self) -> str:
        """
        Returns a string that represents the full name of a Node
        self is composed of module.name(id)

        Returns
        -------
            A string that is composed of module.name(id)
        """
        return f"{self.module}.{self.name}({self.id})"

    def get_flow(self, name: Any) -> Flow:
        """Gets the Flow by its name.
        If the Flow does not exists, it will return None.

        Parameters
        ==========
        name: Any
            Name of the Flow you want to get

        Returns
        =======
        Flow:
            Reference to the Flow you retrieved.
        """
        for flow in self.flows:
            if flow.name == name:
                return flow
        return None

    def add_output(self, output: NodeOutput):
        """
        Adds a new output to the Node

        Parameters
        ----------
        output : NodeOutput
            NodeOutput to add to the Node
        """
        self.outputs[output.name] = output
        if self.on.add_output:
            self.on.add_output(self, output)

    def connect_input(self, *args: Any, **kwargs: Any) -> "Node":
        """
        Connects an input of the Node to an existing NodeOutput
        If the input is
            - not named
            - not already existing in the Node
        but the Node allow dynamic args, the input will be dynamically created
        If the Node doesn't allow dynamic args, an exception will be raised
        The same behaviour applies for kwargs (named input)
        If the input is named and exists in the Node, it will try to connect the NodeOutput
        to the corresponding NodeInput, self action might fail for various reasons (see NodeInput)

        Parameters
        ----------
        *args: Any
            List of NodeOutput to connect to unnamed NodeInput (will be dynamically created)
        *kwargs: Any
            Dict of NodeOuput to connect to existing or non-existing named NodeInput

        Returns
        =======
        Node:
            Returns itself
        """
        for arg_name, arg_value in kwargs.items():
            if arg_name in self.inputs.keys():
                _connect_or_set_input(self.inputs[arg_name], arg_value)
            elif self.allow_kwargs:
                self.kwargs_inputs[arg_name] = NodeInput(
                    self, arg_name, _get_output_value_type(arg_value)
                )
                _connect_or_set_input(self.kwargs_inputs[arg_name], arg_value)
            else:
                raise NodeDoesNotAllowKwargsError(self, arg_name)

        if len(args) > 0 and not self.allow_args:
            if self._can_handle_args(len(args), kwargs):
                self._set_args(args, kwargs)
            else:
                raise NodeDoesNotAllowArgsError(self)

        if self.allow_args:
            args_left = self._set_args(args, kwargs)
            for arg in args_left:
                self.args_inputs.append(
                    NodeInput(
                        self, str(len(self.args_inputs)), _get_output_value_type(arg)
                    )
                )
                _connect_or_set_input(self.args_inputs[-1], arg)

        return self

    def _can_handle_args(self, nb_args, kwargs):
        count = 0
        for arg_name, arg_value in kwargs.items():
            if arg_name in self.inputs.keys():
                count += 1
        if nb_args == len(self.inputs) - count:
            return True

        return False

    def _set_args(self, args, kwargs):
        index_arg = 0
        for input_name, input_value in self.inputs.items():
            if input_name not in kwargs and not (
                self.is_aware and input_name == "self"
            ):
                _connect_or_set_input(self.inputs[input_name], args[index_arg])
                index_arg += 1
        return args[index_arg:]

    def connect_flow(
        self, next_node: "Node", name: Any = None, disabled: bool = False
    ) -> "Node":
        """
        Connects a Node to another one
        flow is a reference to a Node that will be triggered after the current one

        Parameters
        ----------
        next_node: Node
            Reference to the Node you want to trigger after the current one
        name: Any
            Name you want to give to the Flow (can be of any type)
        disabled: bool
            Whether the Flow is disabled by default or not

        Returns
        =======
        Node:
            Returns itself
        """
        if name is None:
            name = len(self.flows)
            while [flow for flow in self.flows if flow.name == name]:
                name += 1
        for flow in self.flows:
            flow.priority += 1
        self.flows.append(Flow(next_node, name, (-1 if disabled else 1)))
        if self.on.connect_flow:
            self.on.connect_flow(self, self.flows[-1])
        return self

    def _find_all_possible_inputs(self) -> Tuple[NodeInput]:
        return (
            list(self.inputs.values())
            + self.args_inputs
            + list(self.kwargs_inputs.values())
        )

    def _execute_function(self):
        positional_inputs = {inp.name: inp.get() for inp in self.inputs.values()}
        if self.is_aware:
            positional_inputs["self"] = self
        positional_args = self._args_keys_to_index(positional_inputs)
        result = self.function(
            *positional_args,
            *[inp.get() for inp in self.args_inputs],
            **{inp.name: inp.get() for inp in self.kwargs_inputs.values()},
        )
        if isinstance(result, OutputWrapper):
            result = result()
            if isinstance(result, (list, tuple)):
                result = dict((i, v) for i, v in enumerate(result))
            if len(self.outputs) == 1 and not isinstance(result, dict):
                result = {list(self.outputs.keys())[0]: result}
        elif len(self.outputs) > 1:
            raise ResultOutputMismatchError(self, result)
        elif len(self.outputs) == 1:
            result = {list(self.outputs.keys())[0]: result}

        for key, output in self.outputs.items():
            if key in result:
                output.set(result[key])
            elif not isinstance(key, OptionalKey):
                raise InexistantOutputResultError(self, output, result)

    def trigger(self):
        """
        Triggers the Node, it will do the following actions
        - Check if it needs to trigger previous nodes to get values in input
        - Call the contained function of the Node injecting the values of the inputs as parameters
        - Inject the result of the function call to the outputs
        - Call the next node using the flow
        If the result of the function is a list or a dictionnary,
        it can be bound to multiple outputs
        """
        self.trigger_log["trigger"] += 1
        flows_backup = [flow for flow in self.flows]
        self.flows = [Flow.from_reference(flow) for flow in self.flows]
        if self.on.trigger:
            self.on.trigger(self)
        for inp in self._find_all_possible_inputs():
            inp.backtrigger()
        self._execute_with_retries()
        self.trigger_log["success"] += 1
        for flow in self.get_next_flow():
            if flow.priority >= 0:
                if self.on.before_flow:
                    self.on.before_flow(self, flow)
                try:
                    flow.node.trigger()
                except Exception as exception:
                    if self.on.flow_failure:
                        self.on.flow_failure(self, flow, exception)
                    else:
                        raise exception
                if self.on.after_flow:
                    self.on.after_flow(self, flow)
        self.flows = [flow for flow in flows_backup]

    def get_next_flow(self):
        executed_flows = []

        def get_sorted_flows():
            return sorted(
                [
                    flow
                    for flow in self.flows
                    if (flow not in executed_flows and flow.priority > 0)
                ],
                key=lambda x: x.priority,
                reverse=True,
            )

        while True:
            sorted_flows = get_sorted_flows()
            if len(sorted_flows) > 0:
                next_flow = sorted_flows[0]
                executed_flows.append(next_flow)
                yield next_flow
            else:
                break

    def _execute_with_retries(self):
        for x in range(self.retries + 1):
            try:
                self._execute_function()
                break
            except Exception as e:
                time.sleep(self.delay)
                if x == self.retries:
                    self.trigger_log["failure"] += 1
                    raise e

    def dump(self, active: bool = True) -> Dict[str, Any]:
        """
        Dumps a Node as a dict representation
        (Trivially convertable to a JSON object)

        Parameters
        ----------
        active : bool
            If equal to True, it will return the active
                (instancied) representation of a Node
            If equal to False, it will return the passive
                (non-instancied) representation of a Node

        Returns
        -------
        dict:
            A dictionnary containing all the fields that defines a Node
        """
        base = {
            "type": "Node",
            "module": self.module,
            "name": self.name,
            "autotrigger": self.autotrigger,
            "inputs": {key: value.dump(active) for key, value in self.inputs.items()},
            "outputs": {key: value.dump(active) for key, value in self.outputs.items()},
        }
        if active:
            base = {
                "id": str(self.id),
                **base,
                "args_inputs": [value.dump(active) for value in self.args_inputs],
                "kwargs_inputs": {
                    key: value.dump(active) for key, value in self.kwargs_inputs
                },
                "flows": [flow.dump() for flow in self.flows],
            }
        return base

    def result(self) -> Dict[Any, Any]:
        """Returns a dictionnary containing all values contained in the Node's outputs

        Returns
        =======
        Dict[Any, Any]:
            A dictionnary of values of any type with the key being the name of the NodeOutput
            and the value being the value of the corresponding NodeOutput.
            If the NodeOutput contained no value, the dictionnary entry value will be None.
        """
        return {key: value.get() for key, value in self.outputs.items()}

    def __getitem__(self, output_name: str) -> NodeOutput:
        """
        __getitem__ : Brackets operator overloading
        Get a NodeOutput of the Node
        self function raises a NodeOutputNotFoundError if the NodeOutput doesn't exists

        Parameters
        ----------
        output_name : str
            Name of the NodeOutput you want to retrieve

        Returns
        -------
        NodeOutput
            Reference to the NodeOutput if found
        """
        for key, output in self.outputs.items():
            if isinstance(key, OptionalKey):
                key = key.key
            if key == output_name:
                return output
        raise NodeOutputNotFoundError(self, output_name)

    def __str__(self) -> str:
        return self.full_name()

    def __repr__(self) -> str:
        return self.full_name()


def node(
    module: str,
    name: str,
    autotrigger: bool = False,
    helper_function: Callable = None,
    **decorator_kwargs: Any,
) -> Node:
    """
    Decorator used to convert a function to a Node object

    Parameters
    ==========
    module: str
        Module of the Node, it should be a human readable string that
        says what kind of category the Node belongs to
    name: str
        Name of the Node, it should be a human readable string that
        says what kind of action the Node does
    autotrigger: bool [False]
        See autotrigger attribute on Node class
    helper_function: Callable
        Function to call before creating a Node instance, the Node and all
        additional *args and **kwargs passed on the Node creation will be
        forwarded to the helper_function

    Returns
    =======
    Node:
        Reference to the newly created Node
    """

    def node_wrapper(node_function: Callable) -> Node:
        """Wrapper for the Node decorator, takes a function in argument

        Parameters
        ==========
        node_function: Callable
            Function you want to decorate

        Returns
        =======
        Node:
            Reference to the newly created Node
        """
        model_store[f"{module}.{name}"] = Node(
            node_function, module, name, autotrigger
        )  # TODO: make real model

        def node_sub_wrapper(*args: Any, **kwargs: Any) -> Node:
            """Wrapper for the Node decorator wrapper, takes the variadic arguments
            used for the helper_function

            *args: Any
                Unnamed variadic arguments that will be forwarded to the helper_function
            **kwargs: Any
                Named variadic arguments that will be forwarded to the helper_function

            Returns
            =======
            Node:
                Reference to the newly created Node
            """
            new_node = Node(node_function, module, name, autotrigger)
            node_store[str(new_node.id)] = new_node
            if helper_function is not None:
                helper_function(new_node, *args, **kwargs)
            for kwarg_key, kwarg_value in decorator_kwargs.items():
                setattr(new_node, kwarg_key, kwarg_value)
            return new_node

        return node_sub_wrapper

    return node_wrapper


class OutputWrapper:
    """Class that allows you to wrap a value in an OutputWrapper.
    It acts like a tag that a Node will recognize.
    The Node will get the underlying value and will try to unzip
    the value to the corresponding outputs
    """

    def __init__(self, underlying_value: Any):
        """OutputWrapper constructor

        Parameters
        ==========
        underlying_value: Any
            Value that you want to wrap, can be anything
        """
        self.underlying_value = underlying_value

    def __call__(self) -> Any:
        """Special method __call__
        Gets the underlying value in the OutputWrapper
        """
        return self.underlying_value


def wrap(underlying_value: Any) -> OutputWrapper:
    """Helper function to build an OutputWrapper

    Parameters
    ==========
    underlying_value: Any
        Value you want to wrap inside an OutputWrapper

    Returns
    =======
    OutputWrapper
        Reference to the newly created OutputWrapper
    """
    return OutputWrapper(underlying_value)


def _connect_or_set_input(node_input: NodeInput, item: Union[NodeOutput, Node, Any]):
    """Connects the <node_input> to <item> if item is a NodeOutput
    or a Node with a default output, sets value of the <node_input> to <item> otherwise

    Parameters
    ==========
    node_input: NodeInput
        Reference to the NodeInput you want to connect / set the value to
    item: NodeOutput / Node / Any
        Reference to the NodeOutput or Node with a default output or a value you want
        to set to the NodeInput
    """
    if isinstance(item, (Node, NodeOutput)):
        node_input.connect(extract_output(item))
    else:
        node_input.set(item)


def _get_output_value_type(item: Union[NodeOutput, Any]) -> type:
    """Tries to get the type of the value contained in the item (if it is a NodeOutput)
    or the type of the item if it fails

    Parameters
    ==========
    item: NodeOutput / Any
        Reference to the NodeOutput or value you want to get the type of

    Returns
    =======
    type:
        Type of the value contained in the NodeOutput or the type of the item
    """
    try:
        return extract_output(item).output_type
    except NotANodeOutputError:
        return type(item)


def extract_output(output: Union["Node", NodeOutput]) -> NodeOutput:
    """
    Function for internal use only
    It abstracts what can be connected to a NodeInput
    Either you can send a NodeOutput directly
    Or you can also send a Node and it will try to extract the single output of the Node
    If the Node contains more than one input, in the previous case it will raise an Exception
    self function also raises an Exception if the output is neither a Node or a NodeOutput

    Parameters
    ----------
    output : Node / NodeOutput
        Reference to the object you want to extract / forward the NodeOutput from

    Returns
    -------
    NodeOutput
        A reference to the NodeOutput extracted from the Node sent in parameter or
        directly the value you sent returned if it was already a NodeOutput
    """
    if isinstance(output, Node):
        if len(output.outputs) == 1:
            for value in output.outputs.values():
                return value
        elif len(output.outputs) == 0:
            raise NoOutputError(output)
        else:
            raise AmbiguousNodeOutputError(output)
    elif isinstance(output, NodeOutput):
        return output
    else:
        raise NotANodeOutputError(output)


def get_whole_scenario(starting_node: Node):
    """Get all Nodes included in a scenario

    Parameters
    ==========
    starting_node: Node
        Node from where you want to get the whole scenario.
        Any Node from the Scenario is fine since it will recursively get all
        connected nodes.

    Returns
    =======
    List[Node]:
        Reference to all Nodes in the scenario
    """
    connected_nodes = starting_node.get_connected_nodes() + [starting_node]
    for connected_node in connected_nodes:
        connected_nodes += [
            node
            for node in connected_node.get_connected_nodes()
            if node not in connected_nodes
        ]
    return connected_nodes


def copy_scenario_state(starting_node: Node):
    """Copies a whole scenario.

    Parameters
    ==========
    starting_node: Node
        Node from where you want to copy the scenario.
        Any Node from the Scenario is fine since it will recursively get all
        connected nodes.

    Returns
    =======
    Node:
        Reference to the equivalent of <starting_node> in your copied scenario
    """
    connected_nodes = get_whole_scenario(starting_node)
    scenario_state = {node.id: node.copy() for node in connected_nodes}
    for current_node in scenario_state.values():
        current_node.update_references(scenario_state)
    return scenario_state[starting_node.id]
