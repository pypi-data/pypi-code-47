#!/usr/bin/env python3

import uuid
import json
from dcyd.utils.async_logger import async_logger

logger = async_logger()

def mpm(func):
    """Decorator that logs function inputs and outputs
    """

    def wrapper(*args, **kwargs):
        func_call_uuid = str(uuid.uuid4())
        log_inputs(func, func_call_uuid, *args, **kwargs)
        func_value = func(*args, **kwargs)
        log_outputs(func, func_call_uuid, func_value)

        return func_value

    return wrapper


def log_inputs(func, func_call_uuid, *args, **kwargs):
    logger.info(
        'Arguments',
        {
            'function_name': func.__name__,
            'function_arguments': format_inputs(func, *args, **kwargs),
            'function_call_uuid': func_call_uuid
        }
    )


def log_outputs(func, func_call_uuid, func_value):
    logger.info(
        'Response',
        {
            'function_name': func.__name__,
            'function_value': func_value,
            'function_call_uuid': func_call_uuid
        }
    )


def format_inputs(func, *args, **kwargs):
    import inspect

    # bind arguments
    ba = inspect.signature(func).bind(*args, **kwargs)
    ba.apply_defaults()

    return {
        'args': json.loads(json.dumps(ba.args)),
        'kwargs': json.loads(json.dumps(ba.kwargs))
    }


if __name__ == '__main__':
    @mpm
    def f(*args, qwer=6, **kwargs):
        return 'sassy'

    f(4, 'a', bad="asdf", cool={'a':6})
