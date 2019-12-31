#! /usr/bin/env python
# -*- coding: utf-8 -*-
from django_opentracing import DjangoTracing
from jaeger_client import Config
from opentracing_instrumentation.client_hooks import install_all_patches
from django_opentracing import middleware
from django.conf import settings

class Django():
    # default tracer is opentracing.Tracer(), which does nothing
    settings.OPENTRACING_TRACING = DjangoTracing()

    # default is False
    settings.OPENTRACING_TRACE_ALL = True

    # default is []
    settings.OPENTRACING_TRACED_ATTRIBUTES = ['META']

    OpenTracingMiddleware = middleware.OpenTracingMiddleware

    def __init__(self, service_name, jaeger_host=None, jaeger_port=None):

        if getattr(settings, 'OPENTRACING_JAEGER_HOST', None) is not None:
            # Backwards compatibility.
            jaeger_host = settings.OPENTRACING_JAEGER_HOST
        else:
            jaeger_host = "istio-jaeger-collector.istio-system.svc.cluster.local"
        if getattr(settings, 'OPENTRACING_JAEGER_PORT', None) is not None:
            jaeger_port = settings.OPENTRACING_JAEGER_PORT
        else:
            jaeger_port = "14268"
        if getattr(settings, 'OPENTRACING_SERVER_NAME', None) is not None:
            service_name = settings.OPENTRACING_SERVER_NAME
        else:
            service_name = None


        config = Config(config={'sampler': {'type': 'const', 'param': 1},
                                'logging': True,
                                'propagation': "b3",
                                'local_agent':
                                # Also, provide a hostname of Jaeger instance to send traces to.
                                    {'reporting_host': jaeger_host, "reporting_port": jaeger_port}},
                        # Service name can be arbitrary string describing this particular web service.
                        service_name=service_name)
        jaeger_tracer = config.initialize_tracer()
        self.OPENTRACING_TRACING = DjangoTracing(jaeger_tracer)

        # trace your MySQLdb, SQLAlchemy, Redis ... queries without writing boilerplate code
        install_all_patches()
