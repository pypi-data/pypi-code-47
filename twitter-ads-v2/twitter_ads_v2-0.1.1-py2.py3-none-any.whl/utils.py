"""Container for all helpers and utilities used throughout the Ads API SDK."""

import datetime
import json
import warnings
warnings.simplefilter('default', DeprecationWarning)
from email.utils import formatdate
from time import mktime
from functools import wraps

from twitter_ads_v2 import VERSION
from twitter_ads_v2.enum import GRANULARITY
from twitter_ads_v2.resources import RESOURCE_TABLE


def get_version():
    """Returns a string representation of the current SDK version."""
    if isinstance(VERSION[-1], str):
        return '.'.join(map(str, VERSION[:-1])) + VERSION[-1]
    return '.'.join(map(str, VERSION))


def remove_minutes(time):
    """Sets the minutes, seconds, and microseconds to zero."""
    return time.replace(minute=0, second=0, microsecond=0)


def remove_hours(time):
    """Sets the hours, minutes, seconds, and microseconds to zero."""
    return time.replace(hour=0, minute=0, second=0, microsecond=0)


def to_time(time, granularity):
    """Returns a truncated and rounded time string based on the specified granularity."""
    if not granularity:
        if type(time) is datetime.date:
            return format_date(time)
        else:
            return format_time(time)
    if granularity == GRANULARITY.HOUR:
        return format_time(remove_minutes(time))
    elif granularity == GRANULARITY.DAY:
        return format_date(remove_hours(time))
    else:
        return format_time(time)


def format_time(time):
    """Formats a datetime as an ISO 8601 compliant string."""
    return time.strftime('%Y-%m-%dT%H:%M:%SZ')


def format_date(time):
    """Formats a datetime as an ISO 8601 compliant string, dropping time."""
    return time.strftime('%Y-%m-%d')


def http_time(time):
    """Formats a datetime as an RFC 1123 compliant string."""
    return formatdate(timeval=mktime(time.timetuple()), localtime=False, usegmt=True)


def validate_whole_hours(time):
    if type(time) is datetime.date:
        pass
    else:
        # Times must be expressed in whole hours
        if time.minute > 0 or time.second > 0:
            raise ValueError("'start_time' and 'end_time' must be expressed in whole hours.")


def split_list(list_, n):
    """Splits a list by a given number (n) and returns a generator object."""
    list_size = len(list_)
    for sp in range(0, list_size, n):
        yield list_[sp:min(sp + n, list_size)]


def _validate_endpoint_type(method, resource, operation):
    if operation not in RESOURCE_TABLE[resource]['endpoint_types']:
        raise NotImplementedError(
            'Detected unsupported endpoint_types. {method} only supports {endpoint_types}'.format(
                method=method,
                endpoint_types=RESOURCE_TABLE[resource]['endpoint_types']
            )
        )


class CustomDecorators(object):

    @staticmethod
    def deprecated(message):
        def wrapper(decorated):
            @wraps(decorated)
            def executer(*args, **kwargs):
                method = str(decorated.__qualname__)
                warnings.warn(
                    "{} => {}".format(method, message),
                    DeprecationWarning,
                    stacklevel=2
                )
                return decorated(*args, **kwargs)
            return executer
        return wrapper

    @staticmethod
    def flatten_params(decorated):
        @wraps(decorated)
        def wrapper(*args, **kwargs):
            # skip batch request
            if ('batch' in args) or (kwargs.get('endpoint_type') == 'batch'):
                return decorated(*args, **kwargs)

            params = {k: v for k, v in kwargs.items() if v is not None}
            for i in params:
                if isinstance(params[i], list):
                    params[i] = ','.join(map(str, params[i]))
                elif isinstance(params[i], bool):
                    params[i] = str(params[i]).lower()
            return decorated(*args, **params)
        return wrapper

    @staticmethod
    def resource_controller(*deco_args, **deco_kwargs):
        def wrapper(decorated):
            @wraps(decorated)
            def controller(*args, **kwargs):
                resource = deco_args[0]
                default_operation = deco_kwargs.get('default_operation')

                params = kwargs.copy()
                instance = args[0]
                account_id = instance.account_id
                operation_types = ['all', 'load', 'update', 'create', 'batch', 'delete']

                if default_operation:
                    if (len(args) > 1 and args[1] in operation_types) or\
                       (params.get('endpoint_type') is not None):
                        operation = params.get('endpoint_type') or args[1]
                    else:
                        operation = default_operation
                        params['endpoint_type'] = operation
                else:
                    try:
                        operation = params.get('endpoint_type') or args[1]
                    except IndexError:
                        raise ValueError(
                            '{} is missing the first argument (endpoint_type).'
                            .format(str(decorated.__qualname__))
                        ) from None

                method = str(decorated.__qualname__)
                _validate_endpoint_type(method, resource, operation)

                if operation in ['all', 'create']:
                    base = RESOURCE_TABLE[resource]['RESOURCE_COLLECTION']
                    resource = base.format(account_id=account_id)
                elif operation in ['load', 'delete', 'update']:
                    base = RESOURCE_TABLE[resource]['RESOURCE']
                    resource = base.format(
                        account_id=account_id,
                        id=params.get('id', None)
                    )
                elif operation == 'batch':
                    params['data'] = json.dumps(params.get('data', []))
                    headers = {'content-type': 'application/json'}
                    base = RESOURCE_TABLE[resource]['BATCH']
                    resource = base.format(account_id=account_id)
                    return decorated(*args, _resource=resource, _headers=headers, **params)

                return decorated(*args, _resource=resource, **params)
            return controller
        return wrapper
