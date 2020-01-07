import time
from concurrent import futures
from typing import Any, Optional

import daemon
import grpc
from daemon import pidfile


class GrpcServer(object):
    _ONE_DAY_IN_SECONDS = 60 * 60 * 24

    def __init__(self, stdout_file: str, stderr_file: str, pidfile_path: str, execution_task: Any,
                 max_workers: int, max_rpcs_requests: Optional[str],
                 port: int, add_servicer_method: Any, task_api_class: Any):
        self.stdout_file = stdout_file
        self.stderr_file = stderr_file
        self.pidfile_path = pidfile_path
        self.execution_task = execution_task
        self.max_workers = max_workers
        self.max_rpcs_requests = max_rpcs_requests
        self.port = port
        self.add_servicer_to_server = add_servicer_method
        self.task_api_class = task_api_class

    def run(self):
        """
        Run gRPC server with new daemon process.
        """
        pid_lock_file = pidfile.PIDLockFile(self.pidfile_path)
        with daemon.DaemonContext(stdout=self.stdout_file,
                                  stderr=self.stderr_file,
                                  pidfile=pid_lock_file,
                                  detach_process=True):
            self.serve()

    def serve(self):
        if self.max_rpcs_requests:
            max_requests = int(self.max_rpcs_requests)
        else:
            max_requests = None
        server = grpc.server(futures.ThreadPoolExecutor(max_workers=int(self.max_workers)), maximum_concurrent_rpcs=max_requests)
        self.add_servicer_to_server(self.task_api_class(self.execution_task), server)
        server.add_insecure_port('[::]:' + str(self.port))

        server.start()
        print("[{}] gRPC server is listening to port: '[::]:{}'".format(
            time.strftime("%Y-%m-%d %H:%m:%S"), self.port))
        try:
            while True:
                time.sleep(self._ONE_DAY_IN_SECONDS)
        except KeyboardInterrupt:
            server.stop(0)
