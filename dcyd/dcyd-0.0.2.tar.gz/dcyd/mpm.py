#!/usr/bin/env python3

import uuid
import inspect
import json

from dcyd.utils.async_logger import async_logger
from dcyd.utils.async_publisher import async_publisher
from dcyd.utils.utils import (
    get_project_id,
    get_pubsub_topic_name
)

logger = async_logger()
publisher = async_publisher()

def mpm(func):
    """Decorator that logs function inputs and outputs
    """

    def wrapper(*args, **kwargs):
        request_data = format_request_data(func, *args, **kwargs)

        # Log the request.
        push_request(request_data)

        # Call the actual function.
        response = func(*args, **kwargs)

        # Log the response.
        push_response(request_data, response)

        return response

    return wrapper


def push_request(request_data):

    logger.info('Request', request_data)

    publisher.publish(
        publisher.topic_path(
            get_project_id(),
            get_pubsub_topic_name()
        ),
        data=json.dumps(request_data).encode('utf-8')
    )


def push_response(request_data, response):
    request_data.update({'response': response})
    logger.info('Response', request_data)

    publisher.publish(
        publisher.topic_path(
            get_project_id(),
            get_pubsub_topic_name()
        ),
        data=json.dumps(request_data).encode('utf-8')
    )


def format_request_data(func, *args, **kwargs):
    # bind arguments
    ba = inspect.signature(func).bind(*args, **kwargs)
    ba.apply_defaults()

    request_data = {
        'function_name': func.__name__,
        'function_sourcefile': inspect.getsourcefile(func),
        'request_arguments': {
            'args': json.loads(json.dumps(ba.args)),
            'kwargs': json.loads(json.dumps(ba.kwargs))
        },
        'request_uuid': str(uuid.uuid4())
    }

    return request_data


if __name__ == '__main__':
    @mpm
    def f(*args, qwer=6, **kwargs):
        return 'sassy'

    f(4, 'a', bad="asdf", cool={'a':6})
