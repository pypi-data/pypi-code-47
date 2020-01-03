# -*- coding: utf-8 -*- 
# @Time     : 2019-12-25 16:18
# @Author   : binger

import time
import sys
import traceback
from concurrent import futures
import logging
import grpc
import json
from .proto import route_pb2, route_pb2_grpc

from .utils import new_registry
from . import Message
from .core.app import RequestEvent
from .core.ctx import RequestContext
from .core.globals import _request_ctx_stack
from . import RequestProxy

_TYPES, register = new_registry()


class Router(route_pb2_grpc.RouteServicer, RequestEvent):
    def __init__(self):
        super(Router, self).__init__()

    def handle1(self, request, context):  # 是否做一个回调包装输入和输出
        msg = Message(**json.loads(request.request))
        resp = {'status': 0}

        kls = _TYPES.get(msg.handler)

        assert kls is not None, 'kls not found for {}'.format(msg.handler)

        try:
            resp["content"] = kls(*msg.args, **msg.kwargs)
        except Exception as e:
            exc_type, exc_value, exc_tb = sys.exc_info()
            print(traceback.format_exc())
            resp["exception"] = {"type": exc_type.__name__, "message": e.args}
            resp["status"] = -1
        finally:
            self.logger.debug("Respond: ", resp)
            msg = json.dumps(resp)
            return route_pb2.Response(response=bytes(msg.encode("utf-8")))

    def handle(self, request, context):

        with RequestContext(RequestProxy(request), context):
            try:
                response = self.full_dispatch_request()
            except Exception as e:
                response = self.handle_exception(e)
            except:
                raise
            return self.send_result(response)

    def dispatch_request(self):
        req = Message(**_request_ctx_stack.top.request.json)
        rule = req.handler

        kls = _TYPES.get(rule, None)
        assert kls is not None, 'kls not found for {}'.format(rule)
        return kls(*req.args, **req.kwargs)

    @staticmethod
    def send_result(rv):
        return route_pb2.Response(response=bytes(rv.json.encode("utf-8")))

    def _init(self, host=None, port=5656, max_workers=10):
        address = "{}:{}".format(host or "0.0.0.0", port)
        server = grpc.server(futures.ThreadPoolExecutor(max_workers=max_workers))
        route_pb2_grpc.add_RouteServicer_to_server(self, server)
        server.add_insecure_port(address)
        self.logger.info('grpc server running, listen on {}'.format(address))
        return server

    def run_forever(self, host=None, port=5656, max_workers=10):
        server = self.start(host, port, max_workers)
        try:
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            pass

    def start(self, host=None, port=5656, max_workers=10):
        server = self._init(host, port, max_workers)
        server.start()
        return server

    @staticmethod
    def route(key):
        return register(key)
