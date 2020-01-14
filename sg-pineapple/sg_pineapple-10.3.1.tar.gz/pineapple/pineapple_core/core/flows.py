# -*- coding: utf-8 -*-
"""This module contains everything that is related to flows.
This module contains one class : Flow.
"""

from typing import Any, Dict

from pineapple_core.utils.serialization import make_value_serializable


class Flow:
    """Class that represents a flow

    Attributes
    ==========
    name: Any
        Name of the Flow, it can be of any type
    priority: int
        Number that defines the order of execution of the flow in a set of flows
        It the number is positive, the flow is enabled, otherwise it's disabled
    node: Node
        The next node to execute with this flow
    """

    @staticmethod
    def from_reference(flow: "Flow"):
        """Creates a fake exact copy of a Flow by usurpating its hash

        Parameters
        ==========
        flow: Flow
            Reference to the flow you want to create an exact copy of
        """
        new_flow = flow.copy()
        new_flow.inject_reference(flow)
        return new_flow

    def __init__(self, node: "Node", name: Any, priority: int):
        """Flow constructor

        Parameters
        ==========
        node: Node
            Node that the flow will trigger
        name: Any
            Name of the flow
        priority: int
            Priority of the flow
        """
        self.node = node
        self.priority = priority
        self.name = name
        self.pretty_name = name
        self._ref = None

    def toggle(self):
        """Toggle a flow (enables it if it was disabled, disables it otherwise)
        """
        self.priority *= -1

    def disable(self):
        """Disables a flow (make its priority negative)
        """
        if self.priority > 0:
            self.toggle()

    def enable(self):
        """Enables a flow (gives an absolute priority to the flow)
        """
        self.priority = abs(self.priority)

    def increase_priority(self):
        """Increases the priority of the flow with the given name
        """
        self.priority += 1

    def decrease_priority(self):
        """Decreases the priority of the flow with the given name
        """
        self.priority -= 1

    def inject_reference(self, ref: "Flow"):
        """Stores a reference of the Flow to usurp

        Parameters
        ==========
        ref: Flow
            Reference to the Flow you want to usurp
        """
        self._ref = ref

    def __eq__(self, other) -> bool:
        return self.__hash__() == other.__hash__()

    def __hash__(self) -> int:
        """Implement of special method __hash__
        It allows a Flow to usurpate another one by giving its underlying _ref __hash__
        with _ref being the Flow you want to usurp

        Returns
        =======
        int:
            Hash of the Flow object
        """
        if not self._ref:
            return super().__hash__()
        return self._ref.__hash__()

    def copy(self) -> "Flow":
        """Copies a Flow, name and priority will be copied while
        the Node inside the flow will be the same reference

        Returns
        =======
        Flow:
            Reference to the newly copied Flow
        """
        flow_copy = Flow(self.node, self.name, self.priority)
        flow_copy.pretty_name = self.pretty_name
        return flow_copy

    def dump(self) -> Dict[str, Any]:
        """Dumps a flow

        Returns
        =======
        dict:
            A dictionnary of attributes representing its state
        """
        return {
            "name": make_value_serializable(self.name),
            "node": str(self.node.id),
            "priority": self.priority,
        }

    def __repr__(self):
        return f"Flow(name='{self.name}', priority={self.priority}, node={self.node})"
