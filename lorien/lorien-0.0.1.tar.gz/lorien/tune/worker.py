"""
The worker module.
"""
import argparse
import time
from abc import abstractmethod
from typing import Any, Callable, Dict, List, Optional, Set, Tuple, Type

import yaml
from tqdm import tqdm

from tvm import autotvm

from ..configs import append_config_parser
from ..database.util import parse_target
from ..logger import disable_stream_handler, get_logger
from ..workload import Workload
from .rpc import RPCClient
from .tuner import TuneErrorCode, tune

log = get_logger('Worker')
WORKER_TABLE: Dict[str, Type['WorkerBase']] = {}


def register_worker(name: str, format_help: str) -> Callable:
    """Regitster a worker.

    Parameters
    ----------
    name: str
        The worker name.

    format_help: str
        The worker specific config foramt description.

    Returns
    -------
    reg: Callable
        A callable function for registration.
    """
    def _do_reg(worker: Type[WorkerBase]):
        if name in WORKER_TABLE:
            raise RuntimeError('%s has been registered' % name)

        # Register worker
        WORKER_TABLE[name] = worker

        # Register worker config
        cfg_func = lambda: [(['--{}'.format(name)], {
            'default': [],
            'action':
            'append',
            'help':
            'Worker description in YAML format. '
            'Format: "<target> <platform>: {}"'.format(format_help)
        })]
        append_config_parser('top.tune', '{} worker options'.format(name))(cfg_func)
        return worker

    return _do_reg


class WorkerBase():
    """The base class of worker."""
    def __init__(self, idx: int, tvm_target: str, workloads: List[Workload],
                 log_s3: Optional[Tuple[str, str]], configs: argparse.Namespace):
        """Initialize a worker.

        Parameters
        ----------
        idx: int
            The index of this platform.

        tvm_target: str
            The TVM target string (e.g., llvm -cmpu=core-avx2).

        workloads: List[Workload]
            The workload list.

        log_s3: Optional[Tuple[str, str]]
            A pair of a S3 bucket and a folder name to upload the tuning logs. When unset,
            full tuning logs will not be stoed.

        configs: argparse.Namespace
            The system configuration.
        """
        self.idx = idx
        self.tvm_target = tvm_target
        self.workloads = workloads
        self.log_s3 = log_s3
        self.configs = configs
        self.target_workloads: List[Workload] = []

        # Process workload for this platform.
        target, platform = parse_target(tvm_target)
        for workload in workloads:
            # Filter out other targets.
            if workload['target'] != target:
                continue

            # Specify the platform.
            workload['platform'] = platform

            self.target_workloads.append(workload)
        self.total_workloads = len(self.target_workloads)

        if not self.target_workloads:
            raise RuntimeError('Terminate a %s due to no workload for %s' %
                               (self.__class__, tvm_target))

    def num_workloads(self) -> int:
        """Return the total number of workloads should be tuned by this worker."""
        return self.total_workloads

    @abstractmethod
    def desc(self) -> str:
        """Return a description shown at the beginning of progress bar while tuning."""

        raise NotImplementedError

    @abstractmethod
    def tune_impl(self, progress: tqdm) -> Tuple[str, Dict[Workload, Tuple[TuneErrorCode, Any]]]:
        """Workload tuning implementation.

        Parameters
        ----------
        progress: tqdm
            The formulated progress bar to be updated progressively.

        Returns
        -------
        target_n_results: Tuple[str, Dict[Workload, Tuple[TuneErrorCode, Any]]]
            (TVM target string, {workload -> (Error code, result)}).
            The result can be either the absolute performance,
            the speedup over the last performance, or the error message.
        """

        raise NotImplementedError

    def tune(self) -> Tuple[str, Dict[Workload, Tuple[TuneErrorCode, Any]]]:
        """Tune workloads on the servers via RPC.

        Returns
        -------
        target_n_results: Tuple[str, Dict[Workload, Tuple[TuneErrorCode, Any]]]
            (TVM target string, {workload -> (Error code, result)}).
            The result can be either the absolute performance,
            the speedup over the last performance, or the error message.
        """

        progress = tqdm(total=self.num_workloads(),
                        position=self.idx,
                        desc=self.desc(),
                        bar_format='{desc}{percentage:3.0f}%|{bar:50}{r_bar}')

        target_n_results = self.tune_impl(progress)
        print('\n')  # Sometimes tqdm miss the last newline.
        return target_n_results


@register_worker('local', 'no additional config is required')
class LocalWorker(WorkerBase):
    """Local worker class."""
    def __init__(self, idx: int, tvm_target: str, workloads: List[Workload],
                 log_s3: Optional[Tuple[str, str]], configs: argparse.Namespace):
        """Initialize a RPC tuner."""
        super(LocalWorker, self).__init__(idx, tvm_target, workloads, log_s3, configs)

        # Setup database options
        self.db_options = yaml.load(configs.db, Loader=yaml.Loader)

        # Setup AutoTVM tuning options
        measure_option = autotvm.measure_option(builder=autotvm.LocalBuilder(timeout=10),
                                                runner=autotvm.LocalRunner(
                                                    number=configs.test,
                                                    repeat=configs.repeat,
                                                    min_repeat_ms=configs.min))
        self.autotvm_options: Dict[str, Any] = {
            'tuner': configs.tuner,
            'n_trial': configs.ntrial,
            'measure_option': measure_option
        }

        # Setup full log target
        self.bucket_n_dir = log_s3

    def desc(self) -> str:
        return '{0} on the Local worker'.format(self.tvm_target)

    @disable_stream_handler
    def tune_impl(self, progress):
        """Tune workloads with RPC workers.

        Parameters
        ----------
        progress: tqdm
            The formulated progress bar to be updated progressively.

        Returns
        -------
        target_n_results: Tuple[str, Dict[Workload, Tuple[TuneErrorCode, Any]]]
            (TVM target string, {workload -> (Error code, result)}).
            The result can be either the absolute performance,
            the speedup over the last performance, or the error message.
        """

        # Map from workload string to the result.
        results: Dict[Workload, Any] = {}

        # Sequential tuning.
        for workload in self.target_workloads:
            results[workload] = tune(self.autotvm_options, workload, self.bucket_n_dir,
                                     **self.db_options)
            progress.update(1)

        return (self.tvm_target, results)


@register_worker('rpc', '[IP1:port1, IP2:port2, ...]')
class RPCWorker(WorkerBase):
    """RPC Worker class."""
    def __init__(self, idx: int, tvm_target: str, workloads: List[Workload],
                 log_s3: Optional[Tuple[str, str]], configs: argparse.Namespace):
        """Initialize a RPC tuner."""
        super(RPCWorker, self).__init__(idx, tvm_target, workloads, log_s3, configs)

        self.rpc_clients: List[RPCClient] = []

        # Figure out the RPC server list.
        rpc_set: Set[str] = set()
        for val in configs.rpc:
            data = yaml.load(val, Loader=yaml.Loader)
            if len(data) != 1 or not isinstance(list(data.values())[0], list):
                raise RuntimeError('Unrecognized RPC server description: %s' % val)
            if tvm_target != list(data.keys())[0]:
                continue
            rpc_set.update(data[tvm_target])

        # Connect to the RPC servers.
        for server in rpc_set:
            try:
                log.info('Connecting to RPC server %s', server)
                self.rpc_clients.append(RPCClient(server, configs, log_s3))
            except RuntimeError as err:
                log.error(str(err))
                continue

        if not self.rpc_clients:
            raise RuntimeError('No available RPC servers')

    def desc(self) -> str:
        return '{0} on {1} RPC worker(s)'.format(self.tvm_target, len(self.rpc_clients))

    def tune_impl(self, progress):
        """Tune workloads with RPC workers.

        Parameters
        ----------
        progress: tqdm
            The formulated progress bar to be updated progressively.

        Returns
        -------
        target_n_results: Tuple[str, Dict[Workload, Tuple[TuneErrorCode, Any]]]
            (TVM target string, {workload -> (Error code, result)}).
            The result can be either the absolute performance,
            the speedup over the last performance, or the error message.
        """

        # Map from workload string to the result.
        results: Dict[Workload, Any] = {}

        # Map from RPC client ID to the running workload string.
        client_2_workload: Dict[int, Workload] = {}

        # Submit for tuning.
        done_count = 0
        while self.target_workloads or done_count < self.num_workloads():
            new_done_count = 0
            dead_client_count = 0
            for cid, client in enumerate(self.rpc_clients):
                # Check connection
                if not client.is_connected():
                    dead_client_count += 1
                    continue

                # Skip the busy worker.
                if not client.is_ready():
                    continue

                # Fetch the result if someone is waiting for it.
                if cid in client_2_workload:
                    results[client_2_workload[cid]] = client.get_result()
                    new_done_count += 1

                # Submit the next workload.
                if self.target_workloads:
                    curr_workload = self.target_workloads.pop()
                    try:
                        client.submit(curr_workload.to_yaml())
                        client_2_workload[cid] = curr_workload
                    except RuntimeError:
                        # Put the workload back and try the next worker.
                        log.warning('Failed to submit a workload, retrying the next worker')
                        self.target_workloads.append(curr_workload)

            if dead_client_count == len(self.rpc_clients):
                # All clients are dead.
                log.error('All workers are disconnected')
                while self.target_workloads:
                    curr_workload = self.target_workloads.pop()
                    results[curr_workload] = (TuneErrorCode.FAIL_TO_SUBMIT, 'all workers are dead')
                for curr_workload in client_2_workload.values():
                    if curr_workload not in results:
                        results[curr_workload] = (TuneErrorCode.FAIL_TO_SUBMIT,
                                                  'all workers are dead')
                break

            # Update status.
            progress.update(new_done_count)
            done_count += new_done_count
            time.sleep(1)

        return (self.tvm_target, results)
