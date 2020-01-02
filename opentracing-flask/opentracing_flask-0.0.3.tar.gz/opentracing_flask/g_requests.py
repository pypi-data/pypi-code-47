# -*- coding: utf-8 -*-
import grequests
from requests import Session
from functools import partial

from .wrappers import http_call_wrapper

g_session = Session()


@http_call_wrapper
def request(method, url, **kwargs):
    timeout = kwargs.get('timeout', 2)
    if not kwargs.get("session"):
        kwargs["session"] = g_session
    req_list = [grequests.request(method=method, url=url, **kwargs)]
    ret_list = grequests.map(req_list, gtimeout=timeout)
    ret = ret_list[0]
    return ret


get = partial(request, 'GET')
options = partial(request, 'OPTIONS')
head = partial(request, 'HEAD')
post = partial(request, 'POST')
put = partial(request, 'PUT')
patch = partial(request, 'PATCH')
delete = partial(request, 'DELETE')
