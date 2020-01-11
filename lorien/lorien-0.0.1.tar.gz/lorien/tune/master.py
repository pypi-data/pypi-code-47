"""
The tuning master.
"""
import argparse
import time
from concurrent.futures import Future, ProcessPoolExecutor, as_completed
from typing import Any, Callable, Dict, Generator, List, Optional, Tuple, Type

import boto3
import yaml

from ..configs import create_config_parser, register_config_parser
from ..database.table import create_table, list_tables
from ..database.util import parse_target
from ..logger import get_logger
from ..workload import Workload
from .tuner import TuneErrorCode
from .worker import WORKER_TABLE, WorkerBase

log = get_logger('Master')


def run_worker(
        worker_cls: Type[WorkerBase], worker_idx: int,
        packed_args: Dict[str, Any]) -> Tuple[str, Dict[Workload, Tuple[TuneErrorCode, Any]]]:
    """Tune workloads on the servers via RPC.

    Parameters
    ----------
    worker_cls: Type[TunerBase]
        The worker class.

    worker_idx: int
        The worker index.

    packed_args: Dict[str, Any]
        The packed worker arguments.

    Returns
    -------
    target_n_results: Tuple[str, Dict[Workload, Tuple[TuneErrorCode, Any]]]
        (TVM target string, {workload -> (Error code, result)}).
        The result can be either the performance or error message.
    """

    try:
        worker = worker_cls(worker_idx, **packed_args)  # type: ignore
    except RuntimeError as err:
        log.error(str(err))
        return ('', {})

    return worker.tune()


def visit_worker_configs(configs: argparse.Namespace, action: Callable) -> Generator:
    """Visit workers in the configuration and take a given action.

    Parameters
    ----------
    configs: argparse.Namespace
        The system configurations.

    action: Callable
        The action function for each worker config.

    Returns
    -------
    item: Generator
        A generator for outputs of the action.
    """

    for worker_name, worker_cls in WORKER_TABLE.items():
        assert hasattr(configs, worker_name), \
            'Worker {} has not registered the same name config'.format(worker_name)

        # Process worker arguments
        for val in getattr(configs, worker_name):
            data = yaml.load(val, Loader=yaml.Loader)
            yield action(worker_cls, data)


def get_target_list(configs: argparse.Namespace) -> List[str]:
    """Parse worker info and get a unique list of targets for creating table and S3 buckets.

    Parameters
    ----------
    configs: argparse.Namespace
        The system configurations.

    Returns
    -------
    targets: List[str]
        A list of target (e.g., llvm, cuda, etc).
    """
    def _action(_: Any, data: Any) -> str:
        if isinstance(data, dict):
            tvm_target = list(data.keys())[0]
        elif isinstance(data, str):
            tvm_target = data
        else:
            raise RuntimeError('Worker config is expected in dict or str, but got %s' % type(data))
        target, _ = parse_target(tvm_target)
        return target

    return list(set(visit_worker_configs(configs, _action)))


def create_target_tables(configs: argparse.Namespace, targets: List[str]):
    """Create tables in DB if it has not yet been created.

    Parameters
    ----------
    configs: argparse.Namespace
        The system configurations.

    targets: List[str]
        The unique target list.
    """

    db_options = yaml.load(configs.db, Loader=yaml.Loader)

    exist_tables = list_tables('topi', **db_options)

    for target in targets:
        table_name = 'topi-{}'.format(target)
        if table_name not in exist_tables:
            create_table('topi', target, **db_options)


def create_s3_log_dir(configs: argparse.Namespace,
                      targets: List[str]) -> Dict[str, Optional[Tuple[str, str]]]:
    """Create a directory in the S3 bucket for uploading tuning logs.

    Parameters
    ----------
    targets: List[str]
        The unique target list.

    Returns
    -------
    target_2_log_target: Dict[str, Optional[Tuple[str, str]]]
        Map from the target to a pair of (S3 bucket, dir name), or None if we do not want to
        keep full tuning logs.
    """

    curr_time = time.gmtime()
    bucket_name_suffix = '{y:04d}{M:02d}{d:02d}-{h:02d}{m:02d}'.format(y=curr_time.tm_year,
                                                                       M=curr_time.tm_mon,
                                                                       d=curr_time.tm_mday,
                                                                       h=curr_time.tm_hour,
                                                                       m=curr_time.tm_min)
    target_2_log_target: Dict[str, Optional[Tuple[str, str]]] = {}
    for target in targets:
        # Create a folder for tuning logs.
        if configs.log_s3_bucket:
            dir_name = 'topi-{target}-{suffix}'.format(target=target, suffix=bucket_name_suffix)
            try:
                client = boto3.client('s3')
                client.put_object(Bucket=configs.log_s3_bucket, Key=('{}/'.format(dir_name)))
            except Exception as err:  # pylint: disable=broad-except
                log.error('Failed to create a folder in S3 bucket %s: %s', configs.log_s3_bucket,
                          str(err))
                return {}
            log.info('s3://%s/%s is created for tuning logs', configs.log_s3_bucket, dir_name)
            target_2_log_target[target] = (configs.log_s3_bucket, dir_name)
        else:
            target_2_log_target[target] = None

    if not configs.log_s3_bucket:
        log.info('Tuning logs will not be stored because target log path is unset')

    return target_2_log_target


def parse_worker_info(configs: argparse.Namespace, log_map: Dict[str, Optional[Tuple[str, str]]],
                      workloads: List[Workload]) -> List[Tuple[Type[WorkerBase], Dict[str, Any]]]:
    """Parse and formulate worker info.

    Parameters
    ----------
    configs: argparse.Namespace
        The system configurations.

    workloads: List[Workload]
        A complete list of workloads to be tuned.

    log_map: Dict[str, Optional[Tuple[str, str]]]
        Map from the target to the log target path, or None if we do not want to
        keep full tuning logs.

    Returns
    -------
    worker_info: List[Tuple[Type[WorkerBase], Dict[str, Any]]]
        A list of (worker class, worker info).
    """
    def _action(worker_cls: Type[WorkerBase],
                data: Any) -> Tuple[Type[WorkerBase], Dict[str, Any]]:
        if isinstance(data, dict):
            tvm_target = list(data.keys())[0]
        elif isinstance(data, str):
            tvm_target = data
        else:
            raise RuntimeError('Worker config is expected in dict or str, but got %s' % type(data))
        target, _ = parse_target(tvm_target)
        return (worker_cls, {
            'tvm_target': tvm_target,
            'workloads': workloads,
            'log_s3': log_map[target],
            'configs': configs
        })

    return list(visit_worker_configs(configs, _action))


def run(configs: argparse.Namespace) -> Dict[str, Dict[Workload, Tuple[TuneErrorCode, Any]]]:
    """Distribute workloads to workers and track the progress.

    Parameteres
    -----------
    configs: argparse.Namespace
        The system configuration of tuner.

    Returns
    -------
    results: Dict[str, Dict[Workload, Tuple[TuneErrorCode, Any]]]
        Map from TVM target string to results (workload -> tuning result).
    """

    results: Dict[str, Dict[Workload, Tuple[TuneErrorCode, Any]]] = {}

    # Load workloads
    workloads: List[Workload] = list({Workload.from_yaml(data) for data in configs.workload})
    log.info('Loaded %d workloads', len(workloads))

    targets = get_target_list(configs)

    # Create tables in DB if needed.
    try:
        create_target_tables(configs, targets)
    except RuntimeError as err:
        log.error(str(err))
        return {}

    # Create S3 buckets if needed.
    target_2_log_target: Dict[str, Optional[Tuple[str, str]]] = create_s3_log_dir(configs, targets)
    if not target_2_log_target:
        return results

    # Process workers
    worker_info: List[Tuple[Type[WorkerBase], Dict[str, Any]]] = \
        parse_worker_info(configs, target_2_log_target, workloads)
    if not worker_info:
        log.warning('Skip tuning due to no worker specified')
        return results

    # Run workers
    futures: List[Future] = []
    with ProcessPoolExecutor(max_workers=len(worker_info)) as pool:
        futures += [
            pool.submit(run_worker, worker_cls, idx, info)
            for idx, (worker_cls, info) in enumerate(worker_info)
        ]
        for future in as_completed(futures):
            tvm_target, result = future.result()
            results[tvm_target] = result

    log.info('Finished tuning')
    return results


@register_config_parser('top.tune')
def define_config() -> argparse.ArgumentParser:
    """Define the command line interface for tuning.

    Returns
    -------
    parser: argparse.ArgumentParser
        The defined argument parser.
    """
    parser = create_config_parser('Distributed Tuning')
    parser.add_argument('--workload',
                        action='append',
                        default=[],
                        required=True,
                        help='A workload in YAML format. It is recommanded to list workload in '
                        'a YAML file and use @workloads.yaml to specify them')
    parser.add_argument('--db',
                        default='endpoint_url: http://localhost:10020',
                        help='DynamoDB client options in YAML format')
    parser.add_argument('--log-s3-bucket',
                        default=None,
                        help='The S3 bucket to upload the tuning logs. '
                        'When unset, full tuning logs will not be stoed.')
    parser.add_argument('--no-txt-rpt',
                        default=False,
                        action='store_true',
                        help='Do not generate a plain text report')
    parser.add_argument('--no-html-rpt',
                        default=False,
                        action='store_true',
                        help='Do not generate a HTML report')
    options = parser.add_argument_group('AutoTVM tuning options')
    options.add_argument('-t',
                         '--tuner',
                         default='ga',
                         choices=['random', 'ga', 'xgb', 'gridsearch'],
                         help='AutoTVM tuning algorithm')
    options.add_argument('-n',
                         '--ntrial',
                         default=3000,
                         type=int,
                         help='Number of tuning trials for each workload')
    measure = parser.add_argument_group('AutoTVM measure options')
    measure.add_argument('--test', default=5, type=int, help='Number of tests in one measurement')
    measure.add_argument('--repeat',
                         default=1,
                         type=int,
                         help='Number of measurements for one config')
    measure.add_argument('--min', default=1000, type=int, help='Minimum repeat time (ms)')
    parser.set_defaults(entry=run)
    return parser
