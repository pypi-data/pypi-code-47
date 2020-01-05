# -*- coding: utf-8 -*- 
# @Time     : 2019-12-25 16:18
# @Author   : binger
"""
    原始仅仅 grpc 通讯，不包含服务器上下文处理
"""
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

_TYPES, register = new_registry()

logger = logging.getLogger("rpc")


class RouteServer(route_pb2_grpc.RouteServicer):

    def handle(self, request, context):  # 是否做一个回调包装输入和输出
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
            logger.debug("Respond: ", resp)
            msg = json.dumps(resp)
            return route_pb2.Response(response=bytes(msg.encode("utf-8")))


class Router(object):
    def __init__(self):
        pass

    @classmethod
    def _init(cls, host=None, port=5656, max_workers=10):
        address = "{}:{}".format(host or "0.0.0.0", port)
        server = grpc.server(futures.ThreadPoolExecutor(max_workers=max_workers))
        route_pb2_grpc.add_RouteServicer_to_server(RouteServer(), server)
        server.add_insecure_port(address)
        logger.info('grpc server running, listen on ' + address)
        return server

    @classmethod
    def run_forever(cls, host=None, port=5656, max_workers=10):
        server = cls.start(host, port, max_workers)
        try:
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            pass

    @classmethod
    def start(cls, host=None, port=5656, max_workers=10):
        server = cls._init(host, port, max_workers)
        server.start()
        return server

    @staticmethod
    def route(key):
        return register(key)
