
import re
from contextlib import contextmanager
from os import environ, path

import tornado.ioloop
import tornado.web

from .handlers.base import route

template_path = path.join(path.dirname(__file__), "templates")


ENV_PREFIX="SMUG_"


class Configuration:
    def __init__(self, **ka):
        self._vals = ka

    def get(self, key):
        # first look in environ
        envkey = f"{ENV_PREFIX}{key.upper()}"
        evar = environ.get(envkey)
        print("ENV", envkey, evar)
        # return env if set, else whatever we have for a val
        return evar if evar is not None else self._vals.get(key)

    def set(self, key, val):
        # note, the environment will always take precedent
        self._vals[key] = val

    def __call__(self, arg):
        return self.get(arg)


def make_app(debug=False, prefix='', **ka):
    routes = route.get_routes(prefix)
    app = tornado.web.Application(
            routes,
            template_path = template_path,
            autoescape = None,
            debug = debug
            )
    # hang certain items off the app object
    app.configuration = Configuration(
        weatherbit_apikey = ka.get('weatherbit_apikey'),
        worldtradingdata_apikey = ka.get('worldtradingdata_apikey'),
        enable_chartmoji = ka.get('enable_chartmoji'),
        )
    app._route_prefix = prefix
    app._template_path = template_path
    return app


def run(port, addr='127.0.0.1', debug=False, prefix='', **ka):
    app = make_app(debug, prefix, **ka)
    app.listen(port, address=addr)
    tornado.ioloop.IOLoop.current().start()


