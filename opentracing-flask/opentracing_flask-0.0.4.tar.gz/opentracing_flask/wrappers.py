# -*- coding: utf-8 -*-
from functools import wraps
from opentracing import global_tracer, Format
from opentracing_instrumentation import get_current_span
import logging


def func_call_wrapper(func):
    """Tracing internal function calls
    :param func:
    :return:
    """

    @wraps(func)
    def _wrappper(*args, **kwargs):
        current_tracer = global_tracer()
        current_span = get_current_span()
        parent_greenlet_span = kwargs.pop("parent_greenlet_span", None)
        if parent_greenlet_span:
            with global_tracer().scope_manager.activate(parent_greenlet_span, finish_on_close=False):
                with current_tracer.start_active_span(func.__name__, child_of=parent_greenlet_span):
                    result = func(*args, **kwargs)
        else:
            with current_tracer.start_active_span(func.__name__, child_of=current_span):
                result = func(*args, **kwargs)
        logging.debug("Tracing function: tracer:{}, span:{}, name:{}".format(
            current_tracer, parent_greenlet_span if not current_span else current_span, func.__name__))
        return result

    return _wrappper


def http_call_wrapper(func):
    @wraps(func)
    def _wrappper(*args, **kwargs):
        if len(args) == 0:
            http_url = kwargs.get("url")
            http_method = kwargs.get("method")
        elif len(args) == 1:
            http_url = kwargs.get("url")
            http_method = args[0]
        elif len(args) == 2:
            http_url = args[1]
            http_method = args[0]
        else:
            http_url = ""
            http_method = "POST"
        current_tracer = global_tracer()
        current_span = get_current_span()

        def start_child_span(parent_span):
            with current_tracer.start_active_span(http_url.split("/")[-1], child_of=parent_span) as scope:
                trace_headers = {}
                current_tracer.inject(scope.span.context, Format.HTTP_HEADERS, trace_headers)
                headers = kwargs.get("headers")
                if not headers:
                    headers = trace_headers
                else:
                    for k, v in trace_headers.items():
                        headers[k] = v
                kwargs["headers"] = headers
                scope.span.set_tag("http.url", http_url)
                scope.span.set_tag("http.method", http_method)
                result = func(*args, **kwargs)
                if not result:
                    scope.span.set_tag("http.status_code", 499)
                else:
                    scope.span.set_tag("http.status_code", result.status_code)
            return result

        parent_greenlet_span = kwargs.pop("parent_greenlet_span", None)
        if parent_greenlet_span:
            with current_tracer.scope_manager.activate(parent_greenlet_span, finish_on_close=False):
                request_result = start_child_span(parent_span=parent_greenlet_span)
        else:
            request_result = start_child_span(parent_span=current_span)
        logging.debug("Tracing request: tracer:{}, span:{}, http_url:{}, http_method:{}".format(
            current_tracer, parent_greenlet_span if not current_span else current_span, http_url, http_method))
        return request_result

    return _wrappper