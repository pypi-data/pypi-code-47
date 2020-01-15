import onnx
import torch
import torch.nn as nn
import torch.nn.functional as F

from .base import OperationGraph
from ..utils import as_numpy


def conv(node: onnx.NodeProto, op_graph: OperationGraph) -> torch.Tensor:
    attributes = {a.name: as_numpy(a) for a in node.attribute}
    dilation = tuple(attributes.get("dilations", (1, 1)))
    groups = attributes.get("group", 1)
    padding = tuple(attributes.get("pads", ()))
    strides = tuple(attributes.get("strides", 1))

    x = op_graph[node.input[0]]
    w = op_graph[node.input[1]]
    b = None
    if len(node.input) > 2:
        b = op_graph[node.input[2]]

    pads = []
    for p1, p2 in zip(padding, padding[int(len(padding) / 2) :]):
        pads.append(p1)
        pads.append(p2)
    x_ = F.pad(x, pads)
    return F.conv2d(x_, w, b, strides, padding=0, dilation=dilation, groups=groups)


def gemm(node: onnx.NodeProto, op_graph: OperationGraph) -> torch.Tensor:
    attributes = {a.name: as_numpy(a) for a in node.attribute}
    alpha = attributes.get("alpha", 1.0)
    beta = attributes.get("beta", 1.0)
    transA = bool(attributes.get("transA", False))
    transB = bool(attributes.get("transB", False))

    a = op_graph[node.input[0]]
    b = op_graph[node.input[1]]
    c = op_graph[node.input[2]]

    a_ = a.T if transA else a
    b_ = b.T if transB else b

    return alpha * torch.matmul(a_, b_) + beta * c


def relu(node: onnx.NodeProto, op_graph: OperationGraph) -> torch.Tensor:
    x = op_graph[node.input[0]]
    return F.relu(x)


def reshape(node: onnx.NodeProto, op_graph: OperationGraph) -> torch.Tensor:
    x = op_graph[node.input[0]]
    shape = op_graph[node.input[1]]
    assert len(shape.shape) == 1
    return x.reshape(tuple(shape.numpy()))


def transpose(node: onnx.NodeProto, op_graph: OperationGraph) -> torch.Tensor:
    x = op_graph[node.input[0]]
    attributes = {a.name: as_numpy(a) for a in node.attribute}
    perm = tuple(attributes.get("perm", range(x.dim())))
    return x.permute(perm)
