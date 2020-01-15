import numpy as np
import torch
import torch.nn as nn

from typing import Any, Callable, Dict, List


class OperationGraph(dict):
    def __getitem__(self, index) -> torch.Tensor:
        item = super().__getitem__(index)
        if callable(item):
            return item(self)
        if isinstance(item, np.ndarray):
            return torch.from_numpy(item)
        return item


class Model(nn.Module):
    def __init__(
        self,
        operation_graph: Dict[str, Callable[[OperationGraph], Any]],
        parameter_map: Dict[str, np.ndarray],
        inputs: List[str],
        outputs: List[str],
    ):
        super().__init__()
        self.operation_graph = operation_graph
        self.parameter_map = parameter_map
        self.inputs = inputs
        self.outputs = outputs

    def forward(self, *x):
        if len(x) != len(self.inputs):
            raise ValueError("Incorrect number of inputs")
        op_graph = OperationGraph()
        op_graph.update(self.operation_graph)
        op_graph.update(self.parameter_map)
        for name, x_ in zip(self.inputs, x):
            op_graph[name] = x_
        outputs = tuple(op_graph[output] for output in self.outputs)
        return outputs
