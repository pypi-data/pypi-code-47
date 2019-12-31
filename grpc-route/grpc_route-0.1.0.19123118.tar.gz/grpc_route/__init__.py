# -*- coding: utf-8 -*- 
# @Time     : 2019-12-31 15:55
# @Author   : binger
import attr
import json

name = "grpc_route"
version_info = (0, 1, 0, 19123118)
__version__ = ".".join([str(v) for v in version_info])
__description__ = 'Python gRPC 回调方式实现CS通讯'

__all__ = ["Message", "AddrConf"]


@attr.s(frozen=True, slots=True)
class Message(object):
    handler = attr.ib(validator=attr.validators.instance_of(str))
    args = attr.ib(default=attr.Factory(list))
    kwargs = attr.ib(default=attr.Factory(dict))

    def to_json(self):
        return json.dumps(self.to_dict())

    def to_dict(self):
        return attr.asdict(self)


@attr.s(slots=True)
class AddrConf(object):
    addr = attr.ib(init=False)
    _host = attr.ib(default="0.0.0.0")
    _port = attr.ib(default=5656)

    def __attrs_post_init__(self):
        self.addr = "{}:{}".format(self._host, self._port)
