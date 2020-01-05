# -*- coding: utf-8 -*- 
# @Time     : 2019-12-27 11:43
# @Author   : binger
import grpc
import json
from .proto import route_pb2, route_pb2_grpc
from .utils import apply_repeat_run
from .core.app import RequestEvent
from .core.globals import _request_ctx_stack
from . import RequestProxy
from functools import wraps
from .wrap import re_connect_cb, update_rgpc_e


class Request(object):
    __slots__ = ['request', 'to_server', 'caller', 'json', 'serialize']

    def __init__(self, request, to_server, caller, serialize=3):
        self.request = json.dumps(request)
        self.to_server = to_server
        self.caller = caller
        self.json = request
        self.serialize = serialize


class RouteClient(RequestEvent):
    def __init__(self, servers):
        super(RouteClient, self).__init__("client")
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

        return _send(msg, to_addr, serialize)

    def handle_wrap_exception(self, e):
        return update_rgpc_e(e)

    def dispatch_request(self):
        req = _request_ctx_stack.top.request
        rv = self.send(msg=req.request, to_addr=req.to_server)
        return self.response_class(**json.loads(rv))

    def process_wrapper(self, request, context):
        with self.request_context(request, context):
            try:
                response = self.full_dispatch_request()
            except Exception as e:
                response = self.handle_exception(e)
            except:
                raise
            return response

    def register(self, handler, to_addr, serialize=3):
        """
        grpc service define
        :param handler: server name
        :param to_addr: server name
        :param serialize: serialize type, default 3 : json
        :return:
        """

        def decorator(func):
            @wraps(func)
            def wrapper(*args, **kwargs):
                info = dict(handler=handler, args=args, kwargs=kwargs)
                request = RequestProxy(Request(info, to_addr, func, serialize))
                return self.process_wrapper(request, context=None)

            return wrapper

        return decorator
