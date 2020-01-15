import onnx

from functools import partial

from . import operations
from .base import Model, OperationGraph


def build_operation(node: onnx.NodeProto):
    op_type = node.op_type.lower()
    op_func = operations.__dict__.get(op_type, None)
    if op_func is None:
        raise NotImplementedError(f"Unimplemented operation type: {op_type}")
    return partial(op_func, node)

