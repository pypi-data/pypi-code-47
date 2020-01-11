"""
RPC client.
"""
import argparse
from typing import Any, Dict, Optional, Tuple

import rpyc
import yaml

from ...logger import get_logger
from ...util import get_tvm_commit
from ..tuner import TuneErrorCode

log = get_logger('RPCClient')


class RPCClient:
    """The RPC client."""
    def __init__(self, server: str, configs: argparse.Namespace, log_s3: Optional[Tuple[str,
                                                                                        str]]):
        """Connect to the RPC server and initialzie the tuning options.

        Parameters
        ----------
        server: str
            The remote server with an optional port (e.g., localhost:8888).
            The default port is 18871 if no specified.

        configs: argparse.Namespace
            The system configuration of RPC tuner.

        log_s3: Optional[Tuple[str, str]]
            A pair of a S3 bucket and a folder name to upload the tuning logs. When unset,
            full tuning logs will not be stoed.
        """
        # Client config.
        self.server = server
        self.curr_job_idx = 0
        self.db_options = yaml.load(configs.db, Loader=yaml.Loader)

        # Status tracking for the running job.
        self.async_client: Optional[rpyc.utils.helpers._Async] = None
        self.running_job: Optional[rpyc.core.async_.AsyncResult] = None

        if server.find(':') != -1:
            try:
                port = int(server[server.find(':') + 1:])
            except ValueError:
                raise RuntimeError('Invalid port: %s' % server[server.find(':') + 1:])
            server_name = server[:server.find(':')]
        else:
            server_name = server
            port = 18871

        try:
            conn = rpyc.connect(server_name, port, config={'sync_request_timeout': None})
            log.info('%s connected', self.server)
        except ConnectionRefusedError as err:
            raise RuntimeError('Failed to connect to %s: %s' % (server, str(err)))

        # Check TVM version and disconnect if the requirement doesn't meet.
        if not conn.root.check_tvm_commit(get_tvm_commit()):
            raise RuntimeError('TVM commits between client and server are mismatching')

        # Set the AutoTVM tuning options and async wrapper.
        autotvm_options: Dict[str, Any] = {
            'tuner': configs.tuner,
            'n_trial': configs.ntrial,
            'measure_option': {
                'number': configs.test,
                'repeat': configs.repeat,
                'min_repeat_ms': configs.min
            }
        }
        conn.root.set_tune_options(autotvm_options)
        if log_s3 is not None:
            conn.root.set_full_log_target(log_s3)
        self.async_client = rpyc.async_(conn.root.remote_tune)

    def is_connected(self) -> bool:
        """Indicate if the RPC client is connected to the server.

        Returns
        -------
        connected: bool
            Return True if connected
        """
        return self.async_client is not None

    def submit(self, workload_str: str) -> None:
        """Submit a workload to the RPC server.

        Parameters
        ----------
        workload_str: str
            The to-be-submitted workload in string format.
        """

        if self.async_client is None:
            raise RuntimeError('Failed to submit workload: Not connected to the RPC server')

        # The other job is running or the result is not fetched yet.
        if self.running_job is not None:
            raise RuntimeError('The other job is still running or the result is not fetched yet')

        self.running_job = self.async_client(workload_str, **self.db_options)

    def get_result(self) -> Optional[Tuple[TuneErrorCode, Any]]:
        """Fetch the result of the finished job and remove the job from status.

        Returns
        -------
        ret: Optional[Tuple[TuneErrorCode, Any]]
            A tuple of error code and the result, or None if no result is available.
        """

        if not self.is_ready() or self.running_job is None:
            return None

        try:
            result = self.running_job.value
        except Exception as err:  # pylint:disable=broad-except
            result = (TuneErrorCode.FAIL_TO_GET_RESULT, str(err))

        self.running_job = None
        return result

    def is_ready(self) -> bool:
        """Check the running job status.

        Returns
        -------
        ready: bool
            Return True if no job is running or the running job is done.
        """
        return self.running_job is None or self.running_job.ready
