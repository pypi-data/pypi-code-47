"""
The unit test for tune.
"""
import argparse

import boto3
import mock
import pytest
import yaml
from moto import mock_s3

from lorien.tune.master import (create_s3_log_dir, create_target_tables, get_target_list,
                                parse_worker_info, run)
from lorien.tune.rpc.server import RPCService
from lorien.tune.tuner import TuneErrorCode, create_autotvm_tuner, tune
from lorien.tune.worker import LocalWorker, RPCWorker
from lorien.workload import Workload
from tvm.autotvm.measure import MeasureInput, MeasureResult
from tvm.autotvm.task.space import ConfigEntity


@pytest.fixture
def fixture_workload():
    #pylint:disable=missing-docstring

    workload = Workload()
    workload['task_name'] = 'topi_nn_dense'
    workload['template_key'] = 'direct'
    workload['args'] = [["TENSOR", [1, 9216], "float32"], ["TENSOR", [4096, 9216], "float32"],
                        None, "float32"]
    workload['lib'] = 'topi'
    workload['target'] = 'llvm'
    return workload


def test_create_autotvm_tuner(fixture_workload):
    #pylint:disable=missing-docstring, redefined-outer-name

    task = fixture_workload.to_task()

    create_autotvm_tuner('xgb', task)
    create_autotvm_tuner('ga', task)
    create_autotvm_tuner('random', task)
    create_autotvm_tuner('gridsearch', task)

    with pytest.raises(RuntimeError):
        create_autotvm_tuner('wrong-tuner', task)


@mock_s3
def test_tune(mocker, fixture_workload):
    #pylint:disable=missing-docstring, redefined-outer-name

    client = boto3.client('s3')
    client.create_bucket(Bucket='unit-test-bucket',
                         CreateBucketConfiguration={'LocationConstraint': 'us-west-2'})
    client.put_object(Bucket='unit-test-bucket', Key=('topi-llvm-0000/'))

    def mock_create_autotvm_tuner(_, task):
        class MockAutoTVMTuner():
            #pylint:disable=missing-docstring

            def __init__(self, task):
                self.task = task
                self.best_flops = 0

            def tune(self, n_trial, early_stopping, measure_option, callbacks):
                #pylint:disable=missing-docstring, unused-argument

                inp = MeasureInput('llvm', self.task, ConfigEntity(0, '', 'direct', {}, []))
                ret = MeasureResult([10], 0, 20, 0)
                for callback in callbacks:
                    callback(self, [inp], [ret])

        return MockAutoTVMTuner(task)

    def mock_list_tables(table_name):
        #pylint:disable=missing-docstring, unused-argument
        return ['test_table.db']

    def mock_query(tasks, table_name):
        #pylint:disable=missing-docstring, unused-argument
        return [[{'thrpt': 0.007550156, 'latency': 0.01}]]

    with mocker.patch('lorien.tune.tuner.create_autotvm_tuner',
                      side_effect=mock_create_autotvm_tuner), \
         mocker.patch('lorien.tune.tuner.list_tables',
                      side_effect=mock_list_tables), \
         mocker.patch('lorien.tune.tuner.query_result_by_tasks',
                      side_effect=mock_query), \
         mocker.patch('lorien.tune.tuner.commit_tuning_log'):
        result = tune({
            'tuner': 'random',
            'n_trial': 10,
            'measure_option': {}
        }, fixture_workload, ('unit-test-bucket', 'topi-llvm-0000'))
        assert result[0] == TuneErrorCode.NORMAL
        assert abs((result[1][0] / result[1][1]) - 1) < 1e-5


def test_get_target_list():
    #pylint:disable=missing-docstring, redefined-outer-name

    rpc_list = [
        yaml.dump({'cuda -model=v100': ['localhost:18871']}),
        yaml.dump({'cuda -model=1080ti': ['localhost:18871']}),
        yaml.dump({'llvm -mcpu=core-avx2': ['localhost:18871']}),
        yaml.dump({'llvm -mcpu=skylake-avx512': ['localhost:18871']})
    ]
    configs = argparse.Namespace(rpc=rpc_list, local=['mali'])

    targets = get_target_list(configs)
    assert len(targets) == 3
    assert 'cuda' in targets
    assert 'llvm' in targets
    assert 'mali' in targets


def test_create_target_table():
    #pylint:disable=missing-docstring, redefined-outer-name

    configs = argparse.Namespace(db='endpoint_url: http://localhost:10020')
    targets = ['llvm', 'cuda']

    def mock_list_tables(table_name, **kwargs):
        #pylint:disable=missing-docstring, unused-argument
        return []

    with mock.patch('lorien.tune.master.list_tables', side_effect=mock_list_tables), \
         mock.patch('lorien.tune.master.create_table'):
        create_target_tables(configs, targets)


@mock_s3
def test_create_log_buckets(mocker):
    #pylint:disable=missing-docstring, redefined-outer-name

    # Virtual S3 bucket for mocking.
    conn = boto3.resource('s3', region_name='us-west-2')
    conn.create_bucket(Bucket='unit-test-bucket')

    # Not specified.
    configs = argparse.Namespace(log_s3_bucket=None)
    assert create_s3_log_dir(configs, ['llvm'])['llvm'] is None

    # Invalid S3 bucket.
    configs = argparse.Namespace(log_s3_bucket='invalid-bucket')
    assert not create_s3_log_dir(configs, ['llvm'])

    def mock_raise_runtime_error(*args, **kwargs):
        raise RuntimeError('random error')

    configs.log_s3_bucket = 'unit-test-bucket'
    result = create_s3_log_dir(configs, ['llvm'])
    assert len(result) == 1
    assert 'llvm' in result
    assert result['llvm'][0] == 'unit-test-bucket'
    assert result['llvm'][1].startswith('topi-llvm')


def test_parse_worker_info():
    #pylint:disable=missing-docstring, redefined-outer-name

    configs = argparse.Namespace(db='mock_db',
                                 rpc=[yaml.dump({'cuda -model=v100': ['localhost:18871']})],
                                 local=['llvm -mcpu=skylake-avx512'])
    workers_info = parse_worker_info(configs, {
        'cuda': ('unit-test-bucket', 'topi-cuda-0000'),
        'llvm': ('unit-test-bucket', 'topi-llvm-0000')
    }, [])
    assert len(workers_info) == 2
    assert workers_info[0][0] == LocalWorker
    assert workers_info[0][1]['tvm_target'] == 'llvm -mcpu=skylake-avx512'
    assert workers_info[0][1]['log_s3'] == ('unit-test-bucket', 'topi-llvm-0000')
    assert workers_info[1][0] == RPCWorker
    assert workers_info[1][1]['tvm_target'] == 'cuda -model=v100'
    assert workers_info[1][1]['log_s3'] == ('unit-test-bucket', 'topi-cuda-0000')


def test_run(mocker, fixture_workload):
    #pylint:disable=missing-docstring, redefined-outer-name

    # Failed to load workloads
    with pytest.raises(RuntimeError):
        configs = argparse.Namespace(workload=['not/exist/path/a.json'])
        run(configs)

    # Mock process executor
    mock_pool = mock.Mock()
    mock_pool.submit.return_value = mock.Mock()
    mock_pool.submit.return_value.result = mock.Mock()
    workload = Workload()
    workload['lib'] = 'myLib'
    mock_pool.submit.return_value.result.return_value = ('localhost', {workload: 'myResult'})
    mocker.patch(
        'lorien.tune.master.ProcessPoolExecutor').return_value.__enter__.return_value = mock_pool
    mocker.patch('lorien.tune.master.as_completed').side_effect = lambda x: x

    configs = argparse.Namespace(workload=[fixture_workload.to_yaml()])

    # Mock other functions we have tested
    mocker.patch('lorien.tune.master.get_target_list').return_value = ['cuda']
    mocker.patch('lorien.tune.master.create_target_tables').return_value = None
    mocker.patch('lorien.tune.master.create_s3_log_dir').return_value = {
        'cuda': ('unit-test-bucket', 'topi-cuda-0000')
    }
    mocker.patch('lorien.tune.master.parse_worker_info').return_value = [(RPCWorker, {
        'tvm_target':
        'cuda -model=v100',
        'workloads': [],
        'log_s3': ('unit-test-bucket', 'topi-cuda-0000'),
        'configs':
        configs,
    })]

    results = run(configs)
    assert 'localhost' in results
    workload2 = Workload()
    workload2['lib'] = 'myLib'
    assert workload2 in results['localhost']
    assert 'myResult' in results['localhost'][workload2]


def test_local_worker():
    #pylint:disable=missing-docstring, redefined-outer-name, invalid-name

    # Make a config.
    configs = argparse.Namespace(local=['llvm -mcpu=core-avx2'],
                                 db='endpoint_url: http://localhost:10020',
                                 test=5,
                                 repeat=1,
                                 min=1000,
                                 tuner='random',
                                 ntrial=10,
                                 log_s3=None)

    # Make workloads
    w1 = Workload()
    w1['target'] = 'llvm'
    w1['task_name'] = 'op1'
    w2 = Workload()
    w2['target'] = 'llvm'
    w2['task_name'] = 'op2'

    worker = LocalWorker(idx=0,
                         tvm_target='llvm -mcpu=core-avx2',
                         workloads=[w1, w2],
                         log_s3=('unit-test-bucket', 'topi-llvm-0000'),
                         configs=configs)
    assert worker.num_workloads() == 2

    with mock.patch('lorien.tune.worker.tune', return_value=(TuneErrorCode.NORMAL, 1.0)):
        platform_n_results = worker.tune()
        assert platform_n_results[0] == 'llvm -mcpu=core-avx2'

    # 2 workload should be tuned.
    assert len(platform_n_results[1]) == 2
    assert sum([code == TuneErrorCode.NORMAL for code, _ in platform_n_results[1].values()]) == 2


def test_rpc_worker(mocker):
    #pylint:disable=missing-docstring, redefined-outer-name, invalid-name

    # Make a config.
    # Set 3 workers with one unavailable (1.1.1.1) to test connection failure.
    configs = argparse.Namespace(
        rpc=[yaml.dump({'llvm -mcpu=core-avx2': ['localhost:1', 'localhost:2', '1.1.1.1:3']})])

    # Make workloads
    # The normal one to the first worker.
    w1 = Workload()
    w1['target'] = 'llvm'
    w1['task_name'] = 'op1#direct'

    # The normal one to the second worker.
    w2 = Workload()
    w2['target'] = 'llvm'
    w2['task_name'] = 'op2#direct'

    # The normal one to the first worker.
    w3 = Workload()
    w3['target'] = 'llvm'
    w3['task_name'] = 'op3#direct'

    # The normal one to the second worker.
    w4 = Workload()
    w4['target'] = 'llvm'
    w4['task_name'] = 'op4#direct'

    # The normal one but cannot be submitted due to disconnection.
    w5 = Workload()
    w5['target'] = 'llvm'
    w5['task_name'] = 'op5#direct'

    # To be skipped.
    w6 = Workload()
    w6['target'] = 'cuda'

    workloads = [w1, w2, w3, w4, w5, w6]

    # Make a fake RPC client.
    # Control the behaviors of is_connect and is_ready to test all situations.
    class MockRPCClient():
        def __init__(self, server, configs, log_s3_bucket):
            if server.find('localhost') == -1:
                raise RuntimeError
            self.check_connect_count = 0
            self.check_ready_count = 0

        def is_connected(self):
            self.check_connect_count += 1
            return self.check_connect_count < 4

        def is_ready(self):
            self.check_ready_count += 1
            return self.check_ready_count % 2 == 1

        def submit(self, _):
            return

        def get_result(self):
            return (TuneErrorCode.NORMAL, 1.0)

    mocker.patch('lorien.tune.worker.RPCClient').side_effect = MockRPCClient
    mocker.patch('lorien.tune.worker.time.sleep')
    worker = RPCWorker(idx=0,
                       tvm_target='llvm -mcpu=core-avx2',
                       workloads=workloads,
                       log_s3=('unit-test-bucket', 'topi-llvm-0000'),
                       configs=configs)
    assert worker.num_workloads() == 5
    assert worker.desc() == 'llvm -mcpu=core-avx2 on 2 RPC worker(s)'
    platform_n_results = worker.tune()
    assert platform_n_results[0] == 'llvm -mcpu=core-avx2'

    # 5 workload except for w6 (wrong target) should be tuned.
    assert len(platform_n_results[1]) == 5

    # w1 and w1 should be done normally.
    # w3 and w4 should be submitted but failed to get results due to disconnection.
    # w5 failed to be submitted due to disconnection.
    assert sum([code == TuneErrorCode.NORMAL for code, _ in platform_n_results[1].values()]) == 2


def test_rpc_service(mocker, fixture_workload):
    #pylint:disable=missing-docstring, redefined-outer-name

    tuning_options = {
        'n_trial': 10,
        'tuner': 'random',
        'measure_option': {
            'number': 5,
            'repeat': 1,
            'min_repeat_ms': 1000
        }
    }

    rpc_service = RPCService()
    rpc_service.set_tune_options(tuning_options)
    assert rpc_service.autotvm_tune_options

    result = rpc_service.remote_tune('invalid-workload')
    assert result[0] == TuneErrorCode.FAIL_TO_LOAD_WORKLOAD
    assert isinstance(result[1], str)

    mocker.patch('lorien.tune.rpc.server.tune').return_value = (TuneErrorCode.NORMAL, 1.1)
    result = rpc_service.remote_tune(fixture_workload.to_yaml())
    assert result[0] == TuneErrorCode.NORMAL
    assert result[1] == 1.1
