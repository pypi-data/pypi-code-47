"""
The unit test module for the workload generation and mutation.
"""
import argparse
import os

import mock
import yaml
from testfixtures import TempDirectory

from lorien.generate import generator
from lorien.generate.extract.gcv import extract_from_gcv
from lorien.generate.extract.tf import extract_from_tf
from lorien.generate.mutate.modelzoo import mutate_from_model_zoo
from lorien.workload import Workload
from tvm.autotvm.task.task import Task


def test_gen():
    #pylint:disable=missing-docstring, redefined-outer-name

    # Fake workloads
    workload1 = Workload()
    workload1['lib'] = 'topi'
    workload1['target'] = 'llvm'
    workload1.to_task = mock.MagicMock()
    workload1.to_task.return_value = Task('topi_nn_conv2d', [])
    workload2 = Workload()

    workload2['lib'] = 'topi'
    workload2['target'] = 'cuda'
    workload2.to_task = mock.MagicMock()
    workload2.to_task.return_value = Task('topi_nn_conv2d', [])

    def mock_generator(_):
        return [workload1, workload2]

    # Get the generator.
    _gen = generator.gen(mock_generator)

    with TempDirectory() as temp_dir:
        workload_file = '{}/workloads.yaml'.format(temp_dir.path)
        configs = argparse.Namespace(output=workload_file)
        _gen(configs)

        # Check workload file
        assert os.path.exists(workload_file)
        line_count = 0
        with open(workload_file, 'r') as filep:
            for _ in filep:
                line_count += 1

        # The first line is "workload:"
        assert line_count == 3


def test_mutate_model_zoo():
    #pylint:disable=missing-docstring, redefined-outer-name

    rules = {"topi": {"conv2d": {"kernel_size": [[3, 3], [5, 5], [7, 7]]}}}

    with TempDirectory() as temp_dir:
        rules_file = '{}/rules.yaml'.format(temp_dir.path)
        with open(rules_file, 'w') as filep:
            filep.write(yaml.dump(rules))

        configs = argparse.Namespace(rules=rules_file,
                                     model=['alexnet: { data: [1, 3, 224, 224]}'],
                                     target=['llvm'],
                                     skip_validate=False)
        workloads = mutate_from_model_zoo(configs)

    # GluonCV AlexNet has 5 conv2d and 3 dense:
    # 4 conv2d with 3 possible kernel sizes = 12
    # 1 conv2d is 11 x 11, plus 3 possible sizes = 4
    # 3 dense with no mutation = 3
    assert len(workloads) == 19


def test_extract_from_gcv():
    #pylint:disable=missing-docstring, redefined-outer-name

    configs = argparse.Namespace(model=['alexnet', 'alexnet: { data: [1, 3, 224, 224]}'],
                                 target=['llvm'])
    workloads = extract_from_gcv(configs)
    assert len(workloads) == 8


def test_extract_from_tf(mocker):
    #pylint:disable=missing-docstring, redefined-outer-name

    # Mock TensorFlow parser and assume it's always working.
    mocker.patch('lorien.generate.extract.tf.TFParser').return_value.parse.return_value = 'FakeNet'
    mocker.patch('lorien.generate.extract.tf.relay.frontend.from_tensorflow').return_value = (
        'mod', 'params')

    # Mock the model extraction because it has been tested in test_extract_from_gcv.
    mocker.patch('lorien.generate.extract.tf.extract_from_model').return_value = [
        Workload() for _ in range(8)
    ]

    configs = argparse.Namespace(model=['alexnet', 'alexnet: { data: [1, 3, 224, 224]}'],
                                 target=['llvm'])
    workloads = extract_from_tf(configs)
    assert len(workloads) == 8
