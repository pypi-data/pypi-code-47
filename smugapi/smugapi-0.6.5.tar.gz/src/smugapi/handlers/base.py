
import json
import os.path
from typing import List, Tuple

from tornado import web

from ..lib.json_utils import json_serialize

Route = Tuple[str, web.RequestHandler]
RouteList = List[Route]


# provides a decorator for our routes
class route:
    _routes = []

    def __init__(self, url:str):
        self._url = url

    def __call__(self, _handler:web.RequestHandler):
        self._routes.append((self._url, _handler))

    @classmethod
    def get_routes(cls, prefix=None) -> List[tuple]:
        if prefix:
            cls._routes = [ (prefix+r,h) for r,h in cls._routes ]
        return cls._routes


# unify our api output through one format point
def apiout(ok=True, msg='', **ka):
    blob = dict(ok=ok, msg=msg, **ka)
    return json.dumps(blob, default=json_serialize)


class BaseHandler(web.RequestHandler):

    def api_ok(self, text='', blocks=[], **ka):
        self.finish(apiout(ok=True, text=text, blocks=blocks, data=ka))

    def api_fail(self, msg='', status=500, **ka):
        self.set_status(status)
        self.finish(apiout(ok=False, msg=msg, **ka))

    def _render_url(self, u):
        if self.application._route_prefix:
            return self.application._route_prefix + u
        return u


class ApiHandler(BaseHandler):
    pass


def make_block(text='', img='', title=''):
    return dict(text=text, img=img, title=title)
