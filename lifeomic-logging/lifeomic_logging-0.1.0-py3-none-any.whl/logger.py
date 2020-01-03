import socket
import os
import datetime
import threading
import uuid
from collections import OrderedDict
from logging import Formatter, Filter, StreamHandler, getLogger, INFO
from json import loads, dumps
from contextlib import contextmanager

thread_local_storage = threading.local()

RESERVED_ATTRS = (
    "args",
    "asctime",
    "created",
    "exc_info",
    "exc_text",
    "filename",
    "funcName",
    "levelname",
    "levelno",
    "lineno",
    "module",
    "msecs",
    "message",
    "msg",
    "name",
    "pathname",
    "process",
    "processName",
    "relativeCreated",
    "stack_info",
    "thread",
    "threadName",
)


def _logger(name, handler, level=INFO):
    log = getLogger(name)
    textformatter = JSONFormatter()
    handler.setFormatter(textformatter)
    log.addHandler(handler)
    log.addFilter(LoggingContextFilter())
    log.setLevel(level)
    return log


@contextmanager
def scoped_logger(logname, normal_context=None, error_context=None, level=INFO):
    try:
        LoggingContextFilter.push_context(
            normal_context, LoggingContextFilter.tls_normal_context_field_name
        )
        LoggingContextFilter.push_context(
            error_context, LoggingContextFilter.tls_error_context_field_name
        )

        yield _logger(logname, StreamHandler(), level)
    finally:
        LoggingContextFilter.pop_context(
            LoggingContextFilter.tls_normal_context_field_name
        )
        LoggingContextFilter.pop_context(
            LoggingContextFilter.tls_error_context_field_name
        )


def get_request_context(lambda_context):
    """
    Helper method to retrieve our most pertinent header information. These are stored from the passed in lambda_context
    object. Please see https://docs.aws.amazon.com/lambda/latest/dg/python-logging.html for the structure.
    :param lambda_context - The lambda context.
    """
    if lambda_context is None:
        return None

    client_context = getattr(lambda_context, "client_context", None)
    if not client_context:
        return None

    custom = getattr(client_context, "custom", {})
    if not custom:
        return None

    request_user = custom.get("lifeomic-user", "(unknown user)")
    request_account = custom.get("lifeomic-account", "(unknown account)")
    request_correlation_id = custom.get("lifeomic-correlation-id", str(uuid.uuid4()))
    request_id = custom.get("lifeomic-request-id", request_correlation_id)

    return {
        "account": request_account,
        "correlationId": request_correlation_id,
        "requestId": request_id,
        "user": request_user,
    }


class LoggingContextFilter(Filter):

    """
    Provides logging context helper utilizing thread local storage (TLS) to store pertinent information for tracing.
    """

    logger_context_field_name = "context"
    tls_normal_context_field_name = "normal_request_context"
    tls_error_context_field_name = "error_request_context"

    def __init__(self):
        super(LoggingContextFilter, self).__init__()

    def filter(self, record):
        """
        Overloaded filter method. The method loads from TLS context for info and non info based tracing. All context
        will be written in JSON format.
        :param record - Record in question
        """

        normal_request_context = LoggingContextFilter.merge_context(
            self.tls_normal_context_field_name
        )
        error_request_context = LoggingContextFilter.merge_context(
            self.tls_error_context_field_name
        )

        log_context = normal_request_context.copy()
        if record.levelname != "INFO":
            log_context.update(error_request_context)

        record.__dict__.update(log_context)
        return True

    @staticmethod
    def push_context(context, context_name):
        """
        Pushed a new context into the context stack. This allows subsequent pertinent information to get accumulated
        as the thread stack grows. All context in the stack will be merged upon tracing.
        :param context - The new context to store.
        :param context_name - The string to which the context will be stored.
        """
        existing_context = getattr(thread_local_storage, context_name, [])
        existing_context.append(context if context else {})
        setattr(thread_local_storage, context_name, existing_context)

    @staticmethod
    def merge_context(context_name):
        """
        Helper method to merge array of dictionaries into a single one. Note that if any keys are duplicated, they will
        get overwritten.
        :param context_name - The string of which the context to be merged.
        """
        contexts = getattr(thread_local_storage, context_name, None)
        if contexts is None:
            return {}
        merged_context = {}
        for context in contexts:
            merged_context.update(context)
        return merged_context

    @staticmethod
    def pop_context(context_name):
        """
        Pop the context stack as the thread stack unwinds.
        :param context_name - The string whose context will be popped.
        """
        existing_context = getattr(thread_local_storage, context_name, [])
        if len(existing_context) > 0:
            existing_context.pop()


class JSONFormatter(Formatter):
    def _getjsondata(self, record):
        fields = []
        fields.append(("name", record.name))
        if isinstance(record.msg, dict):
            for key, value in record.msg.items():
                fields.append((key, value))
        else:
            fields.append(("msg", str(record.msg)))
        fields.append(("severity", record.levelname))
        fields.append(("level", record.levelno))
        fields.append(("time", datetime.datetime.utcnow().isoformat()))

        if record.exc_info:
            fields.append(
                (
                    "err",
                    {
                        "message": self.formatException(record.exc_info),
                        "stack": self.formatStack(record.stack_info)
                        if record.stack_info
                        else None,
                    },
                )
            )

        fields.append(("hostname", socket.gethostname()))
        fields.append(("pid", os.getpid()))

        for key, value in record.__dict__.items():
            if key not in RESERVED_ATTRS and not (
                hasattr(key, "startswith") and key.startswith("_")
            ):
                fields.append((key, value))

        return OrderedDict(fields)

    def format(self, record):
        jsondata = self._getjsondata(record)
        formattedjson = dumps(jsondata)
        return formattedjson
