#!/usr/bin/env python3

import uuid
import inspect
import json

from dcyd.utils.async_logger import async_logger
from dcyd.utils.async_publisher import async_publisher
from dcyd.utils.utils import (
    get_project_id,
    get_pubsub_topic_name,
    get_account_data,
    get_mpm_client_data,
)

logger = async_logger()
publisher = async_publisher()

def mpm(func):
    """Decorator that logs function inputs and outputs
    """

    def wrapper(*args, **kwargs):
        payload = format_payload(func, *args, **kwargs)

        # Log the request.
        push_request(payload)

        # Call the actual function.
        response = func(*args, **kwargs)

        # Log the response.
        push_response(payload, response)

        return response

    return wrapper


def push_request(payload):

    logger.info('Request', payload)

    publisher.publish(
        publisher.topic_path(
            get_project_id(),
            get_pubsub_topic_name()
        ),
        data=json.dumps(payload).encode('utf-8')
    )


def push_response(payload, response):
    payload.get('request', {}).update({'request_response': response})

    logger.info('Response', payload)

    publisher.publish(
        publisher.topic_path(
            get_project_id(),
            get_pubsub_topic_name()
        ),
        data=json.dumps(payload).encode('utf-8')
    )


def format_payload(func, *args, **kwargs):
    # bind arguments
    ba = inspect.signature(func).bind(*args, **kwargs)
    ba.apply_defaults()

    payload = {
        'function': {
            'function_name': func.__name__,
            'function_sourcefile': inspect.getsourcefile(func),
        },
        'request': {
            'request_id': str(uuid.uuid4()),
            'request_arguments': {
                'args': json.loads(json.dumps(ba.args)),
                'kwargs': json.loads(json.dumps(ba.kwargs))
            },
        },
        'account': get_account_data(),
        'mpm_client': get_mpm_client_data(),
    }

    return payload


if __name__ == '__main__':
    @mpm
    def f(*args, qwer=6, **kwargs):
        return 'sassy'

    f(4, 'a', bad="asdf", cool={'a':6})
