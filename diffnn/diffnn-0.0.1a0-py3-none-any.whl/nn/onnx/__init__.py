import numpy as np
import onnx

from google.protobuf.message import DecodeError
from pathlib import Path
from typing import Any, Callable, Dict, Set

from ... import logging
from ..errors import NetworkLoadError
from .pytorch import Model, OperationGraph, build_operation
from .utils import ONNX_TO_NUMPY_DTYPE, as_numpy


def load(path: Path) -> Model:
    logger = logging.getLogger(__name__)
    try:
        onnx_model = onnx.load(str(path))
    except DecodeError as e:
        raise NetworkLoadError("Incorrect network format.")

    node_map = {}
    operation_map = {}  # type: Dict[str, Callable[[OperationGraph], Any]]
    parameter_map = {}  # type: Dict[str, np.ndarray]
    for node in onnx_model.graph.node:
        if node.op_type in ["Constant"]:
            assert len(node.output) == 1
            parameter_map[node.output[0]] = as_numpy(node)
        else:
            for output_name in node.output:
                node_map[output_name] = node
    for initializer in onnx_model.graph.initializer:
        parameter_map[initializer.name] = as_numpy(initializer)
    input_operations = []
    for input_info in onnx_model.graph.input:
        if input_info.name not in parameter_map:
            input_operations.append(input_info.name)
    output_operations = []
    for output_info in onnx_model.graph.output:
        output_operations.append(output_info.name)

    operations = []
    visited = set()  # type: Set[int]

    def topo_sort(node):
        if id(node) in visited:
            return
        visited.add(id(node))
        inputs = []
        for name in node.input:
            if name in node_map:
                topo_sort(node_map[name])
            inputs.append(name)
        operation = build_operation(node)
        if len(node.output) > 1:
            raise NotImplementedError("Multiple node outputs not currently supported")
        else:
            operation_map[node.output[0]] = operation
        operations.append(operation)

    for node in node_map.values():
        topo_sort(node)

    for i, operation in enumerate(operations, 1):
        logger.debug(
            "%3d: %-24s %-24s %-24s",
            i,
            operation.func.__name__,
            operation.args[0].input,
            operation.args[0].output,
        )

    return Model(operation_map, parameter_map, input_operations, output_operations)

