# -*- coding: utf-8 -*-
"""This module contains everything that is related to callbacks.
It contains two classes : CallbackManager and NodeCallbacks
CallbackManager is a class that allows you to manage a collection of Callables
NodeCallbacks acts as a static container of CallbackManagers
"""
from typing import Any, Callable

from pineapple_core.core.exceptions import (
    CallbackManagerNotFoundError,
    NoCallbacksError,
)
from pineapple_core.core.flows import Flow
from pineapple_core.core.node_input import NodeInput
from pineapple_core.core.node_output import NodeOutput


class CallbackManager:
    """Class that represents a collection of callbacks for a given event

    Attributes
    ==========
    signature: List[type]
    callbacks: Dict[Callable]
        Dictionnary of callbacks (functions) where the key is equal to the value
    """

    def __init__(self, name: str, *signature: type):
        """CallbackManager constructor

        Parameters
        ==========
        signature: List[type]
            List of types your callback is supposed to receive
            This parameter is not used at the moment
        """
        self.name = name
        self.callbacks = {}
        self.signature = signature

    def add(self, *callbacks: Callable):
        """Adds a new callback for an event
        The key of the callback will be its value

        Parameters
        ==========
        callback: Callable
            Callable to add to the CallbackManager
        """
        for callback in callbacks:
            self.callbacks[callback] = callback

    def remove(self, callback: Callable):
        """Removes an existing callback based on its value

        Parameters
        ==========
        callback: Callable
            Callback to remove from the CallbackManager
        """
        self.callbacks.pop(callback)

    def remove_all(self):
        """Removes all existing callbacks of the CallbackManager
        """
        self.callbacks = {}

    def __call__(self, *args: Any, **kwargs: Any):
        """Special method for when the CallbackManager is called
        It will call all the underlying callbacks and forward them the arguments

        Parameters
        ==========
        *args: Any
            List of unnamed arguments to send to all the callbacks
        **kwargs: Any
            Dict of named arguments to send to all the callbacks
        """
        if len(self.callbacks) > 0:
            for callback in self.callbacks.values():
                callback(*args, **kwargs)
        else:
            raise NoCallbacksError(self.name)

    def __bool__(self) -> bool:
        """Special method for when you want to test whether the CallbackManager contains
        callbacks or not

        It allows you to do this :
            >>> if callback_manager:
            >>>    callback_manager(*args, **kwargs)

        Returns
        =======
        bool:
            True if the CallbackManager contains at least one callback, False otherwise
        """
        return len(self.callbacks) > 0

    def copy(self) -> "CallbackManager":
        """Returns a copy of the CallbackManager
        All functions will keep the same reference but the signature array
        and the callback dictionnary will be created from scratch again.

        Returns
        =======
        CallbackManager:
            A reference to the newly created copy of the CallbackManager
        """
        new_callback_manager = CallbackManager(self.signature)
        new_callback_manager.callbacks = {
            callback_name: callback_function
            for callback_name, callback_function in self.callbacks.items()
        }
        return new_callback_manager


class NodeCallbacks(object):
    """Class that acts as a storage for all Node's CallbackManagers
    """

    Callbacks = [
        "add_output",
        "after_flow",
        "before_flow",
        "connect_flow",
        "connect_input",
        "flow_failure",
        "set_input_value",
        "trigger",
        "trigger_input",
    ]

    def __init__(self):
        from pineapple_core.core.node import Node

        """
        add_output:
            Callback triggered when a NodeOutput is added to the Node using the
            add_output method

        Parameters
        ==========
        node: Node
            Reference to the Node you're adding a NodeOutput to
        output: NodeOutput
            Reference to the newly created NodeOutput
        """
        self.add_output = CallbackManager("add_output", Node, NodeOutput)
        """
        after_flow:
            Callback triggered when a flow has completed its actions

        Parameters
        ==========
        node: Node
            Reference to the Node that triggered the flow
        flow: Flow
            Reference to the flow that was being triggered
        """
        self.after_flow = CallbackManager("after_flow", Node, Flow)
        """
        before_flow:
            Callback triggered before a flow is executed

        Parameters
        ==========
        node: Node
            Reference to the Node that will trigger the flow
        output: NodeOutput
            Reference to the flow that will be triggered
        """
        self.before_flow = CallbackManager("before_flow", Node, Flow)
        """
        connect_flow:
            Callback triggered when a new flow is connected from a Node to another

        Parameters
        ==========
        node: Node
            Reference to the Node you connect a flow from
        flow: Flow
            Reference to the newly created flow
        """
        self.connect_flow = CallbackManager("connect_flow", Node, Flow)
        """
        connect_input:
            Callback triggered when a NodeInput is being connected to a NodeOutput

        Parameters
        ==========
        node: Node
            Reference to the Node which owns the NodeInput
        input: NodeInput
            Reference to the NodeInput being connected to a NodeOutput
        output: NodeOutput
            Reference to the NodeOutput being connected to a NodeInput
        """
        self.connect_input = CallbackManager(
            "connect_input", Node, NodeInput, NodeOutput
        )
        """
        flow_failure:
            Callback triggered when triggering a flow raises an Exception

        Parameters
        ==========
        node: Node
            Reference to the Node that triggered the flow that raised an Exception
        flow: Flow
            Reference to the flow that raised an Exception
        exception: Exception
            Reference to the Exception
        """
        self.flow_failure = CallbackManager("flow_failure", Node, Flow, Exception)
        """
        set_input_value:
            Callback triggered when you set a value to a NodeInput

        Parameters
        ==========
        node: Node
            Reference to the Node which owns the NodeInput
        input: NodeInput
            Reference to the NodeInput you set a value to
        value: Any
            New value of the NodeInput
        """
        self.set_input_value = CallbackManager("set_input_value", Node, NodeInput, Any)
        """
        trigger:
            Callback triggered when a Node is being triggered

        Parameters
        ==========
        node: Node
            Reference to the Node being triggered
        """
        self.trigger = CallbackManager("trigger", Node)
        """
        trigger_input:
            Callback triggered when a Node triggers another Node through the autotrigger mechanism

        Parameters
        ==========
        node: Node
            Reference to the Node that triggers another Node
        input: NodeInput
            Reference to the NodeInput that requires a value
        autotriggered_node: Node
            Reference to the Node that will be triggered
        """
        self.trigger_input = CallbackManager("trigger_input", Node, NodeInput, Node)

    def copy(self) -> "NodeCallbacks":
        """Returns a copy of the NodeCallbacks
        It will copy every contained CallbackManager

        Returns
        =======
        NodeCallbacks:
            A reference to the newly created copy of the NodeCallbacks
        """
        node_callbacks_copy = NodeCallbacks()
        for callback_name in NodeCallbacks.Callbacks:
            callback_copy = getattr(self, callback_name).copy()
            setattr(node_callbacks_copy, callback_name, callback_copy)
        return node_callbacks_copy

    def __setattr__(self, name, value):
        if name in NodeCallbacks.Callbacks:
            if name in self.__dict__ and not isinstance(value, CallbackManager):
                getattr(self, name).remove_all()
                getattr(self, name).add(value)
            else:
                self.__dict__[name] = value
        else:
            raise CallbackManagerNotFoundError(name)
