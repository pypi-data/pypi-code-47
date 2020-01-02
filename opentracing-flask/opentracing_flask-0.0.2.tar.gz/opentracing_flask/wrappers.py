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
        logging.info("Tracing function: tracer:{}, span:{}, name:{}".format(current_tracer,
                                                                            current_span, func.__name__))
        span = kwargs.get("span")
        if span:
            with global_tracer().scope_manager.activate(span, finish_on_close=False):
                with current_tracer.start_active_span(func.__name__, child_of=span):
                    result = func(*args, **kwargs)
        else:
            with current_tracer.start_active_span(func.__name__, child_of=get_current_span()):
                result = func(*args, **kwargs)
        return result

    return _wrappper


def http_call_wrapper(func):
    @wraps(func)
    def _wrappper(*args, **kwargs):
        http_url = kwargs.get("url", args[1])
        http_method = kwargs.get("method", args[0])
        current_tracer = global_tracer()
        current_span = get_current_span()
        logging.info("Tracing request: tracer:{}, span:{}, http_url:{}, http_method:{}".format(
            current_tracer, current_span, http_url, http_method))

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

        span = kwargs.get("span")
        if span:
            with current_tracer.scope_manager.activate(span, finish_on_close=False):
                request_result = start_child_span(parent_span=span)
        else:
            request_result = start_child_span(parent_span=current_span)
        return request_result

    return _wrappper