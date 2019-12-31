#! /usr/bin/env python
# -*- coding: utf-8 -*-

from opentracing_instrumentation.client_hooks import install_all_patches

def get_forward_headers(raw_headers):
    """Get forward headers for danlu_tracing.

    :param raw_headers:
        Dict type. the headers request contains.
    :return:
        Dict type. the headers should be forward to next request.
    """
    headers = {}

    incoming_headers = ['x-request-id', 'x-datadog-trace-id', 'x-datadog-parent-id', 'x-datadog-sampled',
                        "x-b3-traceid", "x-b3-spanid", "x-b3-parentspanid", "x-b3-sampled", "x-b3-flags"]
    for ihdr in incoming_headers:
        val = raw_headers.get(ihdr)
        if val is not None:
            headers[ihdr] = val

    return headers


# def trace_all_patches():
#     """boto3.install_patches()
#     celery.install_patches()
#     mysqldb.install_patches()
#     psycopg2.install_patches()
#     strict_redis.install_patches()
#     sqlalchemy.install_patches()
#     tornado_http.install_patches()
#     urllib.install_patches()
#     urllib2.install_patches()
#     requests.install_patches()"""
#     install_all_patches()
