"""
The RPC server.
"""
import argparse
from typing import Any, Dict, Tuple

from rpyc import Service
from rpyc.utils.server import ForkingServer

from tvm import autotvm

from ...configs import create_config_parser, register_config_parser
from ...logger import get_logger
from ...util import get_tvm_commit
from ...workload import Workload
from ..tuner import TuneErrorCode, tune

log = get_logger('RPCServer')


class RPCService(Service):
    """The RPC service for tuning AutoTVM tasks."""
    def __init__(self):
        super(RPCService, self).__init__()
        self.autotvm_tune_options: Dict[str, Any] = {}
        self.bucket_n_dir: Optional[Tuple[str, str]] = None

    def check_tvm_commit(self, expected: str) -> bool:
        """Check if the TVM commit on this server matches the one on client.

        Parameters
        ----------
        expected: str
            The expected commit hash.

        Returns
        -------
        match: bool
            Return True if matcheing.
        """
        return get_tvm_commit() == expected

    def set_tune_options(self, autotvm_options: Dict[str, Any]) -> None:
        """Set the AutoTVM tuning options and initialize local builder and runner.

        Parameters
        ----------
        autotvm_options: Dict[str, Any]
            The AutoTVM tuning options.
        """

        for field in ['n_trial', 'tuner', 'measure_option']:
            assert field in autotvm_options, \
                '"{}" is missing in AutoTVM tuning options'.format(field)
        for field in ['number', 'repeat', 'min_repeat_ms']:
            assert field in autotvm_options['measure_option'], \
                '"{}" is missing in measure_option'.format(field)

        self.autotvm_tune_options['n_trial'] = autotvm_options['n_trial']
        self.autotvm_tune_options['tuner'] = autotvm_options['tuner']
        self.autotvm_tune_options['measure_option'] = autotvm.measure_option(
            builder=autotvm.LocalBuilder(timeout=10),
            runner=autotvm.LocalRunner(
                number=autotvm_options['measure_option']['number'],
                repeat=autotvm_options['measure_option']['repeat'],
                min_repeat_ms=autotvm_options['measure_option']['min_repeat_ms']))
        log.info('Tuning options are initialized')

    def set_full_log_target(self, bucket_n_dir: Tuple[str, str]) -> None:
        """Set the target log path to store the full tuning logs.

        Parameters
        ----------
        bucket_n_dir: Tuple[str, str]
            A pair of a S3 bucket and a folder name to upload the tuning logs. When unset,
            full tuning logs will not be stoed.
        """
        self.bucket_n_dir = bucket_n_dir
        log.info('Target S3 log path is set to %s/%s', bucket_n_dir[0], bucket_n_dir[1])

    def remote_tune(self, workload_str: str, **db_kwargs) -> Tuple[TuneErrorCode, Any]:
        """The exposed API for RPC client to submit jobs.
        Note that it will simply ignore the workload and return false if the maximum allowed
        workeres are achieved.

        Parameters
        ----------
        workload_str: str
            The to-be-tuned workload in string format.

        **db_kwargs
            The kwargs of boto3 client. Commonly used: "region_name='us-west-1'"
            or "endpoint_url=http://localhost:8000".

        Returns
        -------
        success: bool
            Return True if the tuning has been done successfully.
        """

        try:
            workload = Workload.from_yaml(workload_str)
        except RuntimeError as err:
            return (TuneErrorCode.FAIL_TO_LOAD_WORKLOAD,
                    'Failed to create a workload {0} from string: {1}'.format(
                        workload_str, str(err)))

        return tune(self.autotvm_tune_options, workload, self.bucket_n_dir, **db_kwargs)


def launch(configs: argparse.Namespace) -> None:
    """Launch the RPC server.
    NOTE: We have to use forking server that uses a child-process to handle incoming requests
    to avoid thread pool confliction, because TVM uses thread pool to build its own RPC server.
    The potential issue is RPyC forking server is POSIX only.

    Parameters
    ----------
    configs: argparse.Namespace
        The system configure for RPC server.
    """
    port = configs.port
    s = ForkingServer(RPCService,
                      port=port,
                      protocol_config={
                          'allow_public_attrs': True,
                          'allow_pickle': True
                      })
    log.info('Launching RPC server at port %d', port)
    s.start()


@register_config_parser('top.rpc-server')
def define_config() -> argparse.ArgumentParser:
    """Define the command line interface for RPC server.

    Returns
    -------
    parser: argparse.ArgumentParser
        The defined argument parser.
    """
    parser = create_config_parser('Launch RPC server on this machine')
    parser.add_argument('-p', '--port', default=18871, type=int, help='The assigned port')
    parser.set_defaults(entry=launch)
    return parser
