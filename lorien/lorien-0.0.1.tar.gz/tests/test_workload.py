"""
The unit test module for the workload generation.
"""

import pytest

from lorien.workload import Workload


def test_workload():
    #pylint:disable=missing-docstring, redefined-outer-name

    workload = Workload()
    workload['lib'] = 'topi'
    workload['target'] = 'cuda'

    # Test invalid arguments caused task creation failure
    workload['args'] = [[1, 3, 224, 224], [32, 3, 3, 3]]
    with pytest.raises(RuntimeError):
        workload.to_task()

    workload['args'] = [['TENSOR', [1, 3, 224, 224], 'float32'],
                        ['TENSOR', [32, 3, 3, 3], 'float32']]

    # Test missing task definition
    with pytest.raises(RuntimeError):
        workload.to_task()

    workload['task_name'] = 'topi_nn_conv2d'
    workload['template_key'] = 'winograd'

    # Test invalid workload for the TOPI schedule. conv2d winograd on CUDA only accepts NCHW layout.
    workload['args'] += [[1, 1], [1, 1], [1, 1], 'HWCN', 'float32']
    with pytest.raises(RuntimeError):
        workload.to_task()

    workload['args'][-2] = 'NCHW'
    task = workload.to_task()

    # Test load from task
    workload_from_task = Workload.from_task(task)
    assert workload == workload_from_task

    # Test dump and load from YAML
    workload_str = workload.to_yaml()
    assert workload == Workload.from_yaml(workload_str)

    # Test loading invalid workload
    del workload._data['task_name']
    workload_str = workload.to_yaml()
    with pytest.raises(RuntimeError):
        Workload.from_yaml(workload_str)
