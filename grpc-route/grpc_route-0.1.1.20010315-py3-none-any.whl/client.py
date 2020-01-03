# -*- coding: utf-8 -*- 
# @Time     : 2019-12-27 11:43
# @Author   : binger
import grpc
import json
from .proto import route_pb2, route_pb2_grpc
from .utils import apply_repeat_run
from grpc._channel import _InactiveRpcError
from grpc import StatusCode
from . import Message
import logging

logger = logging.getLogger("grpc")


def re_connect_cb(e):
    if isinstance(e, _InactiveRpcError) and e.args[0].code == StatusCode.UNAVAILABLE:
        return True
    else:
        return False


class RouteClient(object):
    def __init__(self, servers):
        self.pool = {}
        self.addr_list = [servers] if not isinstance(servers, (tuple, list)) else servers
        self._tries = 3

    def get_connect(self, address, restart=False):
        """
        get server stub
        :param address:
        :param restart:
        :return:
        """

        conn = self.pool.get(address)
        if not conn or restart:
            conn = self.pool[address] = self._connect(address)

        return conn

    @classmethod
    def _connect(cls, address):
        return route_pb2_grpc.RouteStub(grpc.insecure_channel(address))

    def connect(self):
        """
        load grpc server list
        :return:
        """

        for addr in self.addr_list:
            self.pool[addr.addr] = self._connect(addr.addr)

    def send(self, msg, to_addr, serialize=3):

        re_connect = lambda: self.get_connect(to_addr.addr, restart=True)

        # TODO: 连接失败时，抛出专有异常
        @apply_repeat_run(re_connect, at_exception_cb=re_connect_cb)
        def _send(msg, to_addr, serialize=3):
            res = route_pb2.Request(request=bytes(msg.encode("utf-8")), serialize=serialize)
            response = self.get_connect(to_addr.addr).handle(res)
            return response.response

        request_json = json.dumps(msg)
        result = _send(request_json, to_addr, serialize)
        return json.loads(result)

    def register(self, handler, to_addr, serialize=3):
        """
        grpc service define
        :param handler: server name
        :param to_addr: server name
        :param serialize: serialize type, default 3 : json
        :return:
        """

        def decorator(func):
            def wrapper(*args, **kwargs):
                msg = Message(handler=handler, args=args, kwargs=kwargs)
                resp = self.send(msg.to_dict(), to_addr, serialize)
                return resp

            return wrapper

        return decorator
