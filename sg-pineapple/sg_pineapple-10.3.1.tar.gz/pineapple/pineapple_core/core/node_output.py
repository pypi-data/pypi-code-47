# -*- coding: utf-8 -*-
"""This module contains everything that is related to NodeOutputs.
This module contains the NodeOutput class.
"""

import sys
from typing import Any, Dict
from uuid import uuid4

from klotan import match

from pineapple_core.core.exceptions import InvalidNodeOutputTypeError
from pineapple_core.core.types import PineappleType
from pineapple_core.utils.klotan_adapter import (
    type_dict_to_klotan_dict,
    type_list_to_klotan_list,
)


class NodeOutput:
    """
    A class used to represent a single Output of a Node

    Attributes
    ----------
    id: uuid.UUID
        An unique ID generated on the NodeOutput creation
    name: str
        Name of the output
    output_type: type
        Will check if the type of value set on the output
        is equal to output_type
    value: Any
        Can be of any type, it holds the current value of the output
    """

    def __init__(self, node: "Node", name: str, output_type: type):
        self.id = uuid4()
        self.node = node
        self.name = name
        self.output_type = output_type
        self.value = None

    def get(self) -> Any:
        """
        Returns the value contained in the NodeOutput
        """
        return self.value

    def set(self, value: Any):
        """
        Sets the value of the contained value of the NodeOutput
        It will raise an exception if the type of the new value
        is not equal to output_type

        Parameters
        ----------
        value : any
            Value that will be set to the NodeOutput
        """
        if not _type_check(self.output_type, value):
            raise InvalidNodeOutputTypeError(self, value)
        self.value = value

    def __repr__(self) -> str:
        """
        Returns a string representation of a NodeOutput

        Returns
        -------
        str:
            String representation of a NodeOutput
        """
        return f"Output[{self.name}](type={self.output_type}, value={self.value})"

    def dump(self, active: bool = True) -> Dict[str, Any]:
        """
        Dumps a NodeOutput as a dict representation
        (Trivially convertable to a JSON object)

        Parameters
        ----------
        active: bool
            If equal to True, it will return the active
                (instancied) representation of a NodeOutput
            If equal to False, it will return the passive
                (non-instancied) representation of a NodeOutput

        Returns
        -------
        Dict[str, Any]:
            A dictionnary containing all the fields that defines a NodeOutput
        """
        base = {
            "type": "NodeOutput",
            "name": self.name,
            "output_type": str(self.output_type),
        }
        if active:
            base = {
                "id": str(self.id),
                **base,
                "parent": f"{self.node.id}",
                "value": self.value,
            }
        return base

    def copy(self) -> "NodeOutput":
        """Copies the NodeOutput.

        Returns
        =======
        NodeOutput:
            Reference to the newly copied NodeOutput
        """
        node_output_copy = NodeOutput(self.node, self.name, self.output_type)
        node_output_copy.id = self.id
        node_output_copy.value = self.value
        return node_output_copy


def check_pineapple_type(base: PineappleType, value: Any) -> bool:
    if not base.check(value):
        return False
    else:
        return True


def _type_check(base: Any, value: Any) -> bool:
    if isinstance(base, PineappleType):
        if not check_pineapple_type(base, value):
            return False
    elif isinstance(base, (list, tuple, dict)):
        if isinstance(base, (list, tuple)):
            base = type_list_to_klotan_list(base)
        elif isinstance(base, dict):
            base = type_dict_to_klotan_dict(base)
        match_result = match.match(base, value)
        if not match_result.is_valid():
            print(f"Invalid type matching {match_result.to_string()}", file=sys.stderr)
            return False
    elif (
        not type(value) == base
    ):  # Don't change this to isinstance (typing incompatibility)
        result = False
        try:
            result = isinstance(value, base.__args__)
        except AttributeError:
            return False
        return result
    return True
