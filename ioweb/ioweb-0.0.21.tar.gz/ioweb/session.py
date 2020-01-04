from pprint import pprint

from .response import Response
from .request import Request
from .transport import Urllib3Transport
from .error import NetworkError


class Session(object):
    def __init__(self):
        self.transport = Urllib3Transport()

    def request(self, url=None, **kwargs):
        req = Request(url=url, **kwargs)
        res = Response()
        self.transport.prepare_request(req, res)
        self.transport.request(req, res)
        self.transport.prepare_response(req, res, None)
        return res


def request(*args, **kwargs):
    sess = Session()
    return sess.request(*args, **kwargs)
