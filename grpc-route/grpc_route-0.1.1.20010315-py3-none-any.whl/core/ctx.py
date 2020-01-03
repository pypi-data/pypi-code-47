# -*- coding: utf-8 -*- 
# @Time     : 2020-01-02 13:58
# @Author   : binger

from .globals import _request_ctx_stack
import json


class RequestProxy(object):
    def __init__(self, request):
        self._request_ = request
        self._json = None

    def __getattr__(self, item):
        return getattr(self._request_, item)

    def __setattr__(self, key, value):
        if key.startswith("_"):
            super().__setattr__(key, value)
        else:
            setattr(self._request_, key, value)

    @property
    def json(self):
        self._json = self._json or json.loads(self.data)
        return self._json

    @property
    def data(self):
        return self._request_.request

    def __delattr__(self, item):
        if item.startswith('_'):
            super().__delattr__(item)
        else:
            delattr(self._request_, item)


class RequestContext(object):
    def __init__(self, request, context):
        self.request = request
        self.context = context

        self.preserved = False
        self._preserved_exc = None

    def push(self):
        top = _request_ctx_stack.top
        if top is not None and top.preserved:
            top.pop(top._preserved_exc)

        _request_ctx_stack.push(self)

    def pop(self):
        rv = _request_ctx_stack.pop()

    def __enter__(self):
        self.push()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.pop()
