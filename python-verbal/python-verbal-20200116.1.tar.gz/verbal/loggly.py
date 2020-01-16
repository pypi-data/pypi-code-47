from __future__ import absolute_import

import warnings
from urllib.error import URLError
from urllib.request import urlopen

import logging

from datetime import datetime, timedelta
from .mongolog import MongoFormatter

from tornado.ioloop import IOLoop
from json import dumps

class LogglyHandler(logging.Handler):
    def __init__(self, url, level=logging.NOTSET):
        super(LogglyHandler, self).__init__(level=level)
        self.formatter = MongoFormatter()
        self.url = url
        self.enabled = True

    def _callback(self, response):
        if response.error:
            if self.enabled:
                warnings.warn('loggly {} failed, disabling for 1 minute'.format(self.url))
                self.enabled = False
                IOLoop.instance().add_timeout(timedelta(minutes=1), self.reenable)
            response.rethrow()

    def reenable(self):
        warnings.warn('enabling loggly {} again'.format(self.url))
        self.enabled = True

    def emit(self, record):
        if not self.enabled:
            return

        body = self.format(record)
        for key, value in body.items():
            if isinstance(value, datetime):
                body[key] = value.strftime("%Y-%m-%dT%H:%M:%S.%fZ")

        # this will block on loggly, which is bad... we should run everything under tornado
        if not IOLoop.initialized():
            try:
                urlopen(self.url, dumps(body), 5)
            except URLError:
                pass
            return

        from tornado.httpclient import AsyncHTTPClient
        client = AsyncHTTPClient()
        client.fetch(self.url, body=dumps(body), method='POST', callback=self._callback)


