# -*- coding: utf-8 -*-
"""This module contains everything that is related to exceptions.
Every exception used in Pineapple.Core is defined here.
Every exception should herit from Exception class or another class
that also herits from Exception.
"""

from typing import Any, Callable, Union


class InvalidNodeOutputTypeError(Exception):
    """Exception raised when a NodeOutput emits a value that is
    different than the expected type.
    """

    def __init__(self, node_output: "NodeOutput", value: Any):
        """InvalidNodeOutputTypeError constructor

        Parameters
        ==========
        node_output: NodeOutput
            Reference to the NodeOutput that emits a value with the wrong type
        value: Any
            Reference to the value with the wrong type
        """
        super().__init__(
            f"{node_output.node.full_name()}[{node_output.name}] in Node ({node_output.node}) "
            f"expects values of type {node_output.output_type} "
            f"but got value {value} of type {type(value)}"
        )


class HiddenNodeInputConnectError(Exception):
    """Exception raised when you try to connect a NodeInput with the hidden attribute
    """

    def __init__(self, node_input: "NodeInput"):
        """HiddenNodeInputConnectError

        Parameters
        ==========
        node_input: NodeInput
            Reference to the NodeInput that you tried to connect
        """
        super().__init__(
            f"Can't connect {node_input.node.full_name()}[{node_input.name}]"
            " because it is hidden"
        )


class NotANodeOutputError(Exception):
    """Exception raised when you try to get a NodeOutput but you sent something else
    """

    def __init__(self, output: Union["NodeOutput", "Node"]):
        """NotANodeOutputError constructor

        Parameters
        ==========
        output: Any
            Reference to the value that is not a NodeOuput
        """
        super().__init__(
            f"{output} of type {type(output)} is not a "
            "valid NodeOutput (expected Node['out'] / NodeOutput)"
        )


class AmbiguousNodeOutputError(Exception):
    """Exception raised when there is multiple outputs on a Node and you
    tried to pass the Node as an input.
    The behaviour above works when a Node contains a single output since it
    will replace the Node with its only output but if there is multiple
    outputs, it becomes ambiguous and raises this Exception
    """

    def __init__(self, node: "Node"):
        """AmbiguousNodeOutputError constructor

        Parameters
        ==========
        output: Node
            Node from where you tried to extract a single output
        """
        super().__init__(
            f"Ambiguous extract of NodeOutput from {node.full_name()}"
            f" since it contains multiple outputs ({node.outputs})"
        )


class NoOutputError(Exception):
    def __init__(self, node: "Node"):
        super().__init__(f"The Node {node.full_name()} doesn't contain any output !")


class NodeDoesNotAllowArgsError(Exception):
    """Exception raised when you tried to send values to unnamed
    additional arguments (*args) on a Node that did not accept them
    """

    def __init__(self, node: "Node"):
        """NodeDoesNotAllowArgsError constructor

        Parameters
        ==========
        node: Node
            Reference to the Node you tried to send additional arguments to
        """
        super().__init__(
            f"{node.full_name()} does not allow additional unnamed arguments (*args)"
        )


class NodeDoesNotAllowKwargsError(Exception):
    """Exception raised when you tried to send values to named
    additional arguments (*kwargs) on a Node that did not accept them
    """

    def __init__(self, node: "Node", arg_name: str):
        """NodeDoesNotAllowKwargsError constructor

        Parameters
        ==========
        node: Node
            Reference to the Node you tried to send additional arguments to
        arg_name: str
            Name of the additional named argument
        """
        super().__init__(
            f"{node.full_name()} does not allow additional named arguments (kwargs) : {arg_name}"
        )


class NodeOutputNotFoundError(Exception):
    """Exception raised when you try to retrieve a Node's Output
    that doesn't exist
    """

    def __init__(self, node: "Node", node_output_name: Any):
        """NodeOutputNotFoundError constructor

        Parameters
        ==========
        node: Node
            Reference to the Node you tried to retrieve the NodeOutput from
        node_output_name: Any
            Name of the NodeOutput you tried to retrieve
        """
        super().__init__(
            f"NodeOutput '{node_output_name}' does not exists in Node {node.full_name()}"
        )


class InvalidNodeFunctionReturnTypeError(Exception):
    """Exception raised when the return type of a Node function is not valid
    All valid types are :
    - Any type
    - Any instance of class PineappleType
    - Node
    - A list / tuple
    - A dict
    """

    def __init__(self, node: "Node", node_function: Callable):
        """InvalidNodeFunctionReturnTypeError constructor

        Parameters
        ==========
        node: Node
            Reference to the Node that holds the function with the wrong return type
        node_function: Callable
            Reference to the function with the wrong return type
        """
        output_types = node_function.__annotations__["return"]
        super().__init__(
            f"Invalid return annotation {output_types} for node {node.full_name()}"
        )


class ResultOutputMismatchError(Exception):
    """Exception raised when the amount of values to return (through a wrapped list / dict)
    doesn't match the amount of outputs
    """

    def __init__(self, node: "Node", result: "Any"):
        """ResultOutputMismatchError constructor

        Parameters
        ==========
        node: Node
            Reference to the Node from where the exception was raisen
        result: Any
            Result you tried to affect to multiple outputs
        """
        super().__init__(
            f"Result {result} on Node {node} doesn't match the amount of outputs {node.outputs}"
        )


class InexistantOutputResultError(Exception):
    """Exception raised when a function result doesn't hold any value for one
    of the non-optional NodeOutput
    """

    def __init__(self, node: "Node", output: "NodeOutput", result: "Any"):
        """InexistantOutputResultError constructor

        Parameters
        ==========
        node: Node
            Reference to the Node from where the exception was raisen
        output: NodeOutput
            Reference to the NodeOutput that doesn't have any value from the result
        result: Any
            Result from where the Node could not find a suitable value for the NodeOuput
        """
        super().__init__(
            f"Node {node} doesn't have any result available for NodeOutput "
            f"{output} in result : {result}"
        )


class CallbackManagerNotFoundError(Exception):
    def __init__(self, callback_manager_name):
        super().__init__(
            f"NodeCallbacks does not have any CallbackManager named '{callback_manager_name}'"
        )


class NoCallbacksError(Exception):
    def __init__(self, callback_manager_name):
        super().__init__(
            f"CallbackManager '{callback_manager_name}' does not contain any callbacks !"
        )
