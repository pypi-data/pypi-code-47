#! /usr/bin/env python
# -*- coding: utf-8 -*-
import opentracing
from flask_opentracing import FlaskTracing
from jaeger_client import Config
from opentracing_instrumentation.client_hooks import install_all_patches

class Flask():
    def __init__(self, service_name, jaeger_host=None, jaeger_port=None):
        if not jaeger_host:
            jaeger_host = "istio-jaeger-collector.istio-system.svc.cluster.local"
        if not jaeger_port:
            jaeger_port = "14268"
        config = Config(config={'sampler': {'type': 'const', 'param': 1},
                                'logging': True,
                                'propagation': "b3",
                                'local_agent':
                                # Also, provide a hostname of Jaeger instance to send traces to.
                                    {'reporting_host': jaeger_host, "reporting_port": jaeger_port}},
                        # Service name can be arbitrary string describing this particular web service.
                        service_name=service_name)
        jaeger_tracer = config.initialize_tracer()
        self.tracer = FlaskTracing(jaeger_tracer)

        # trace your MySQLdb, SQLAlchemy, Redis ... queries without writing boilerplate code
        install_all_patches()

