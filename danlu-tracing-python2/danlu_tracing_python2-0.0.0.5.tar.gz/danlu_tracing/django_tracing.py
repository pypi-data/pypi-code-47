#! /usr/bin/env python
# -*- coding: utf-8 -*-
import django_opentracing
from jaeger_client import Config
from opentracing_instrumentation.client_hooks import install_all_patches
from django.conf import settings


class Django:

    def tracer(self, service_name, jaeger_host=None, jaeger_port=None):
        if not jaeger_host:
            jaeger_host = "istio-jaeger-collector.istio-system.svc.cluster.local"
        # Tracing info cannot be collected when jaeger_port is set to '14268'
        # if not jaeger_port:
        #     jaeger_port = "14268"

        config = Config(
            config={'sampler': {'type': 'const', 'param': 1},
                    'logging': True,
                    'propagation': "b3",
                    'local_agent': {'reporting_host': jaeger_host}},  # , 'reporting_port': "14268"
            service_name=service_name)
        return config.initialize_tracer()

    def __init__(self, service_name, jaeger_host=None, jaeger_port=None):
        # default tracer is opentracing.Tracer(), which does nothing
        settings.OPENTRACING_TRACING = django_opentracing.DjangoTracing(
            tracer=self.tracer(service_name=service_name, jaeger_host=jaeger_host, jaeger_port=jaeger_port))
        # default is False
        settings.OPENTRACING_TRACE_ALL = True
        # default is []
        settings.OPENTRACING_TRACED_ATTRIBUTES = ['META']

        settings.MIDDLEWARE.append('django_opentracing.OpenTracingMiddleware')

        settings.INSTALLED_APPS.append('django_opentracing')

        install_all_patches()