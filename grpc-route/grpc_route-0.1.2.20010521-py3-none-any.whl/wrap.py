# -*- coding: utf-8 -*- 
# @Time     : 2019-12-31 11:30
# @Author   : binger
from .core.error import ServerError, GrpcCode
from grpc._channel import _InactiveRpcError
from grpc import StatusCode


def update_rgpc_e(e):
    if isinstance(e, _InactiveRpcError):
        if e.args[0].code == StatusCode.UNAVAILABLE:
            return ServerError, ServerError(GrpcCode.UNAVAILABLE, e.args[0].details)
        else:
            return ServerError, ServerError(GrpcCode.RGPCIO_ERROR, "{}:{}".format(e.args[0].code.value, e.args[0].details))

    return None, None


def re_connect_cb(e):
    if isinstance(e, _InactiveRpcError) and e.args[0].code == StatusCode.UNAVAILABLE:
        return True
    else:
        return False


if __name__ == "__main__":
    pass
