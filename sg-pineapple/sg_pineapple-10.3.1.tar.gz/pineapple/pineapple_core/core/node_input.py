# -*- coding: utf-8 -*-
"""This module contains everything that is related to NodeInputs.
This module contains the NodeInput class.
"""

from copy import deepcopy
from typing import Any, Dict
from uuid import uuid4

from pineapple_core.core.exceptions import HiddenNodeInputConnectError
from pineapple_core.core.node_output import NodeOutput
from pineapple_core.utils.serialization import make_value_serializable


def _process_list(input_list, func, override):
    from pineapple_core.core.node import Node

    for i, value in enumerate(input_list):
        if isinstance(value, (Node, NodeOutput)):
            if override:
                input_list[i] = func(value)
            else:
                func(value)
        if isinstance(value, (list, tuple)):
            _process_list(value, func, override)
        elif isinstance(value, dict):
            _process_dict(value, func, override)


def _process_dict(input_dict, func, override):
    from pineapple_core.core.node import Node

    for key, value in input_dict.items():
        if isinstance(value, (Node, NodeOutput)):
            if override:
                input_dict[key] = func(value)
            else:
                func(value)
        if isinstance(key, (Node, NodeOutput)):
            if override:
                key = func(key)
                input_dict[key] = input_dict.pop(key)
            else:
                func(key)
        if isinstance(value, (list, tuple)):
            _process_list(value, func, override)
        elif isinstance(value, dict):
            _process_dict(value, func, override)


def _process_value(value, func, override=False):
    if override:
        value_copy = deepcopy(value)
    else:
        value_copy = value
    if isinstance(value_copy, dict):
        _process_dict(value_copy, func, override)
        return value_copy
    elif isinstance(value_copy, (list, tuple)):
        _process_list(value_copy, func, override)
        return value_copy
    return value


class NodeInput:
    """
    A class used to represent a single Input of a Node

    Attributes
    ----------
    id : uuid.UUID
        An unique ID generated on the NodeInput creation
    name : str
        Name of the input
    input_type : type
        Excepted type for the connected output
    connected_output : NodeOutput
        Reference to the NodeOuput this NodeInput is connected to
    hidden : bool
        If "hidden" is True, the input can only have a value
        through its fallback value (no connection to an output)
    """

    def __init__(
        self,
        node,
        name: str,
        input_type: type,
        hidden: bool = False,
        optional: bool = False,
    ):
        self.id = uuid4()
        self.name = name
        self.node = node
        self.input_type = input_type
        self.connected_output = None
        self.hidden = hidden
        self.optional = optional
        self.value = None

    def connect(self, output: NodeOutput):
        """
        Connects an input to an existing output
        If the NodeInput is hidden, it will raise an exception

        Parameters
        ----------
        output : NodeOutput
            Reference to an existing NodeOutput instance
        """
        # Should check for output.output_type
        if not self.hidden:
            self.connected_output = output
            if self.node.on.connect_input:
                self.node.on.connect_input(self.node, self, output)
        else:
            raise HiddenNodeInputConnectError(self)

    def set(self, value: Any):
        """Sets the default value of the NodeInput
        This value will be returned if the NodeInput is not connected to a NodeOutput

        Parameters
        ==========
        value: Any
            Default value you want to set for the current NodeInput
        """
        self.value = value
        if self.node.on.set_input_value:
            self.node.on.set_input_value(self.node, self, value)

    def get(self) -> Any:
        """
        Returns a value
        Either the value of the connected output
        Or the fallback value if no output is connected

        Returns
        -------
        Any:
            Value of the NodeInput
        """
        from pineapple_core.core.node import extract_output

        if self.connected_output:
            return self.connected_output.value
        from pineapple_core.core.node import OutputWrapper

        if isinstance(self.value, OutputWrapper):
            return _process_value(
                self.value.underlying_value,
                lambda item: extract_output(item).get(),
                override=True,
            )
        else:
            return self.value

    def backtrigger(self):
        from pineapple_core.core.node import Node, OutputWrapper

        def backtrigger_in_value(item):
            base_node = None
            if isinstance(item, NodeOutput):
                base_node = item.node
            elif isinstance(item, Node):
                base_node = item
            if base_node.autotrigger:
                if self.node.on.trigger_input:
                    self.node.on.trigger_input(self.node, self, base_node)
                base_node.trigger()

        if self.connected_output and self.connected_output.node.autotrigger:
            if self.node.on.trigger_input:
                self.node.on.trigger_input(self.node, self, self.connected_output.node)
            self.connected_output.node.trigger()
        elif isinstance(self.value, OutputWrapper):
            _process_value(self.value.underlying_value, backtrigger_in_value)

    def __repr__(self):
        """
        Returns a string representation of a NodeInput

        Returns
        -------
        str:
            String representation of a NodeInput
        """
        return (
            f"Input[{self.name}]("
            + ", ".join(
                [
                    f"accepts={self.input_type}",
                    f"bind={self.connected_output}",
                    f"hidden={self.hidden}",
                    f"optional={self.optional}",
                    f"value={self.value}",
                ]
            )
        ) + ")"

    def dump(self, active: bool = True) -> Dict[str, Any]:
        """
        Dumps a NodeInput as a dict representation
        (Trivially convertable to a JSON object)

        Parameters
        ----------
        active : bool
            If equal to True, it will return the active
                (instancied) representation of a NodeInput
            If equal to False, it will return the passive
                (non-instancied) representation of a NodeInput

        Returns
        -------
        dict:
            A dictionnary containing all the fields that defines a NodeInput
        """
        base = {
            "type": "NodeInput",
            "name": self.name,
            "input_type": str(self.input_type),
            "hidden": self.hidden,
        }
        if active:
            base = {
                "id": str(self.id),
                **base,
                "parent": f"{self.node.id}",
                "connected_output": str(self.connected_output.id)
                if self.connected_output
                else None,
                "value": make_value_serializable(self.value),
            }
        return base

    def copy(self) -> "NodeInput":
        """Copies the NodeInput.
        The connected_output if there is any will point to the same NodeOutput

        Returns
        =======
        NodeInput:
            Reference to the newly copied NodeInput
        """
        node_input_copy = NodeInput(self.node, self.name, self.input_type, self.hidden)
        node_input_copy.id = self.id
        node_input_copy.value = self.value
        node_input_copy.connected_output = self.connected_output
        return node_input_copy
