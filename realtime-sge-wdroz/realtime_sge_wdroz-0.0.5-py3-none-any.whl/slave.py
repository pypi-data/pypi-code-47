""" Slave module that take order from master
"""
import psutil
import socket
import time
from uuid import uuid4
from concurrent import futures
import grpc
from threading import Thread
from realtime_sge.protos import services_pb2_grpc
from realtime_sge.protos.messages_pb2 import Empty, Status, Worker, Command, Action


class Slave(services_pb2_grpc.SlaveServicer):
    def __init__(self, server):
        self._slave_id = "{}-{}".format(socket.gethostname(), str(uuid4()))
        self._server = server
        self._send = True

    def register(self, host, port, server_host="localhost", server_port=1234):
        with grpc.insecure_channel("{}:{}".format(server_host, server_port)) as channel:
            stub = services_pb2_grpc.MasterStub(channel)
            worker = Worker(id=self._slave_id, host=host, port=port)
            stub.Register(worker)

    def GetStatus(self, request, context):
        self._send = True
        while self._send:
            time.sleep(1)
            ram_usage = psutil.virtual_memory().percent
            cpu_usage = psutil.cpu_percent()
            status = Status(id=self._slave_id, ram_usage=ram_usage, cpu_usage=cpu_usage)
            yield status

    def stop_soon(self):
        def stop():
            time.sleep(2)
            self._server.stop(grace=0)
            exit(0)

        self._send = False
        t = Thread(target=stop)
        t.start()

    def DoCommand(self, request, context):
        if request.action == Action.QUIT:
            self.stop_soon()
        return Empty()

    def DoTask(self, request, context):
        pass


def serve(server_host, server_port, slave, server, host=None, port=0):
    services_pb2_grpc.add_SlaveServicer_to_server(slave, server)
    if host is None:
        host = socket.gethostname()
    port = server.add_insecure_port("[::]:{}".format(port))
    server.start()
    slave.register(host, port, server_host=server_host, server_port=server_port)
    server.wait_for_termination()


if __name__ == "__main__":
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=100))
    slave = Slave(server)
    serve("localhost", 1234, slave, server)
