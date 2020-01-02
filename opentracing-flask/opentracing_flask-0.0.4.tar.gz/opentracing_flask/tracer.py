# -*- coding: utf-8 -*-
from jaeger_client import Config
from flask_opentracing import FlaskTracing
import logging
from opentracing import global_tracer
from opentracing_instrumentation import get_current_span


def create_tracer(service_name, flask_app, jaeger_host="localhost", sample_type="const", sample_param=1):
    """Create global flask trace instance
    :param service_name: current service name
    :param flask_app: flask app instance
    :param jaeger_host: jaeger agent host, default localhost
    :param sample_type: work with sample param
           reference: https://www.jaegertracing.io/docs/1.15/sampling/
    :param sample_param:
    :return:
    """
    config = Config(config={'sampler': {'type': sample_type, 'param': sample_param},
                            'local_agent': {'reporting_host': jaeger_host}},
                    service_name=service_name,
                    validate=True)
    jaeger_tracer = config.initialize_tracer()
    tracer = FlaskTracing(jaeger_tracer, True, flask_app)
    logging.info("Create trace {} on flask_app {} as service_name {}".format(tracer, flask_app, service_name))
    return tracer


def get_global_tracer():
    return global_tracer()


def get_global_span():
    return get_current_span()
