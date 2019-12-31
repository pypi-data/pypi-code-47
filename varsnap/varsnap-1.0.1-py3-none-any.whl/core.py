import base64
import binascii
import collections.abc as collections
import json
import logging
import os
import six
import sys
import threading
import time
import traceback
from typing import Any, Callable, List, Mapping, Optional, Tuple

import dill as pickle
from qualname import qualname
import requests

from .__version__ import __version__

PRODUCE_SNAP_URL = 'https://www.varsnap.com/api/snap/produce/'
CONSUME_SNAP_URL = 'https://www.varsnap.com/api/snap/consume/'
PRODUCE_TRIAL_URL = 'https://www.varsnap.com/api/trial/produce/'
UNPICKLE_ERRORS = [
    binascii.Error,
    ImportError,
    ModuleNotFoundError,
    pickle.UnpicklingError,
]
PICKLE_ERRORS = [
    AttributeError,
    ModuleNotFoundError,
    pickle.PicklingError,
    TypeError,
]

# Names of different environment variables used by varsnap
# See readme for descriptions
ENV_VARSNAP = 'VARSNAP'
ENV_ENV = 'ENV'
ENV_PRODUCER_TOKEN = 'VARSNAP_PRODUCER_TOKEN'
ENV_CONSUMER_TOKEN = 'VARSNAP_CONSUMER_TOKEN'

LOGGER = logging.getLogger(__name__)
LOGGER.setLevel(logging.INFO)
handler = logging.StreamHandler(sys.stdout)
LOGGER.addHandler(handler)

# A list of Varsnap functions for testing and tracing
CONSUMERS = []
PRODUCERS = []


def env_var(env: str) -> str:
    return os.environ.get(env, '').lower()


def get_signature(target_func: Callable) -> str:
    return 'python.%s.%s' % (__version__, qualname(target_func))


def equal(x: Any, y: Any) -> bool:
    if not isinstance(x, y.__class__):
        return False
    if isinstance(x, six.string_types):
        return x == y
    if isinstance(x, collections.Sequence):
        if len(x) != len(y):
            return False
        for v in zip(x, y):
            if not equal(v[0], v[1]):
                return False
        return True
    if isinstance(x, collections.Mapping):
        if len(x) != len(y):
            return False
        for k in x.keys():
            if k not in y:
                return False
            if not equal(x[k], y[k]):
                return False
        return True
    if hasattr(x, '__dict__'):
        return equal(x.__dict__, y.__dict__)
    return x == y


def align_report(report: List[Tuple[str, str]]) -> str:
    # Vertically align report's second column
    key_length = max([len(x[0]) for x in report]) + 2
    report_lines = [
        x[0] + ' '*(key_length - len(x[0])) + str(x[1])
        for x in report
    ]
    log = "\n".join(report_lines)
    return log


def limit_string(x: str) -> str:
    limit = 30
    ellipsis = '...'
    if len(x) <= limit:
        return x
    return x[:limit - len(ellipsis)] + ellipsis


class DeserializeError(ValueError):
    pass


class SerializeError(ValueError):
    pass


class Producer():
    def __init__(self, target_func: Callable) -> None:
        self.target_func = target_func
        PRODUCERS.append(self)

    @staticmethod
    def is_enabled() -> bool:
        if env_var(ENV_VARSNAP) != 'true':
            return False
        if env_var(ENV_ENV) != 'production':
            return False
        if not env_var(ENV_PRODUCER_TOKEN):
            return False
        return True

    @staticmethod
    def serialize(data: Any) -> str:
        try:
            pickle_data = pickle.dumps(data)
        except Exception as e:
            if type(e) in PICKLE_ERRORS:
                raise SerializeError(e)
            raise
        data = base64.b64encode(pickle_data).decode('utf-8')
        return data

    @staticmethod
    def get_globals() -> Mapping[str, Any]:
        global_vars = {}
        for k, v in globals().items():
            if k[:2] == '__':
                continue
            try:
                pickle.dumps(v)
            # Ignore unpickable data
            except Exception as e:
                if type(e) in PICKLE_ERRORS:
                    continue
                raise
            global_vars[k] = v
        return global_vars

    def produce(self, args: Any, kwargs: Any, output: Any) -> None:
        if not Producer.is_enabled():
            return
        LOGGER.info(
            'Varsnap producing call for %s' %
            qualname(self.target_func)
        )
        global_vars = Producer.get_globals()
        inputs = {
            'args': args,
            'kwargs': kwargs,
            'globals': global_vars
        }
        data = {
            'producer_token': env_var(ENV_PRODUCER_TOKEN),
            'signature': get_signature(self.target_func),
        }
        try:
            data['inputs'] = Producer.serialize(inputs)
        except SerializeError as e:
            LOGGER.warn(
                'Varsnap cannot serialize inputs for %s: %s' %
                (qualname(self.target_func), e)
            )
            return
        try:
            data['prod_outputs'] = Producer.serialize(output)
        except SerializeError as e:
            LOGGER.warn(
                'Varsnap cannot serialize outputs for %s: %s' %
                (qualname(self.target_func), e)
            )
            return
        requests.post(PRODUCE_SNAP_URL, data=data)


class Consumer():
    def __init__(self, target_func: Callable) -> None:
        self.target_func = target_func
        self.last_snap_id = None
        CONSUMERS.append(self)

    @staticmethod
    def is_enabled() -> bool:
        if env_var(ENV_VARSNAP) != 'true':
            return False
        if env_var(ENV_ENV) != 'development':
            return False
        if not env_var(ENV_CONSUMER_TOKEN):
            return False
        return True

    @staticmethod
    def deserialize(data: str) -> Any:
        try:
            data = pickle.loads(base64.b64decode(data.encode('utf-8')))
        except Exception as e:
            if type(e) in UNPICKLE_ERRORS:
                raise DeserializeError(e)
            raise
        return data

    def consume_watch(self) -> None:
        if not Consumer.is_enabled():
            return
        LOGGER.info(
            'Varsnap consuming calls to %s' %
            qualname(self.target_func)
        )
        while True:
            self.consume()
            time.sleep(1)

    def consume(self) -> Tuple[bool, str]:
        data = {
            'consumer_token': env_var(ENV_CONSUMER_TOKEN),
            'signature': get_signature(self.target_func),
        }
        response = requests.post(CONSUME_SNAP_URL, data=data)
        try:
            response_data = json.loads(response.content)
        except json.decoder.JSONDecodeError:
            response_data = ''
        if not response_data or response_data['status'] != 'ok':
            return True, ""
        trial_results = []
        for result in response_data['results']:
            trial_result = self.consume_one(result)
            trial_results.append(trial_result)
        all_matches = all([x for x in trial_results if x is not None])
        logs = "\n\n".join([x[1] for x in trial_results])
        return all_matches, logs

    def consume_one(self, snap_data: Mapping) -> Tuple[Optional[bool], str]:
        if snap_data['id'] == self.last_snap_id:
            return None, ''

        self.last_snap_id = snap_data['id']
        LOGGER.info(
            'Receiving call from Varsnap uuid: ' + str(self.last_snap_id)
        )
        try:
            inputs = Consumer.deserialize(snap_data['inputs'])
            prod_outputs = Consumer.deserialize(snap_data['prod_outputs'])
        except DeserializeError:
            return None, ''
        if type(inputs) == list:
            # Backwards compatibility of 0.8.1 to 0.8.0
            inputs = {
                'args': inputs[0],
                'kwargs': inputs[1],
                'globals': inputs[2],
            }
        exception = ''
        for k, v in inputs['globals'].items():
            globals()[k] = v
        try:
            local_outputs = self.target_func(
                *inputs['args'],
                **inputs['kwargs']
            )
        except Exception as e:
            local_outputs = e
            exception = traceback.format_exc()
        if exception:
            matches = equal(prod_outputs, exception)
        else:
            matches = equal(prod_outputs, local_outputs)
        report_lines: List[Tuple[str, str]] = []
        report_lines += self.report_central(
            env_var(ENV_CONSUMER_TOKEN),
            snap_data['id'],
            local_outputs,
            matches,
        )
        report_lines += self.report_log(
            inputs, str(prod_outputs), str(local_outputs), exception, matches
        )
        report = align_report(report_lines)
        if matches:
            LOGGER.info(report)
        else:
            LOGGER.error(report)

        return matches, report

    def report_central(
        self, consumer_token: str, snap_id: str, local_outputs: Any,
        matches: bool,
    ) -> List[Tuple[str, str]]:
        data = {
            'consumer_token': consumer_token,
            'snap_id': snap_id,
            'test_outputs': Producer.serialize(local_outputs),
            'matches': matches,
        }
        response = requests.post(PRODUCE_TRIAL_URL, data=data)
        try:
            response_data = json.loads(response.content)
        except json.decoder.JSONDecodeError:
            response_data = ''
        if response_data['status'] != 'ok':
            return []
        trial_url = response_data.get('trial_url', '')
        report_line = ('Report URL:', trial_url)
        return [report_line]

    def report_log(
        self, inputs: Any, prod_outputs: str, local_outputs: str,
        exception: str, matches: bool,
    ) -> List[Tuple[str, str]]:
        function_name = qualname(self.target_func)
        report = []
        report.append(('Function:', function_name))
        report.append(('Function input args:', limit_string(inputs['args'])))
        report.append((
            'Function input kwargs:', limit_string(inputs['kwargs'])
        ))
        report.append((
            'Production function outputs:', limit_string(prod_outputs)
        ))
        report.append(('Your function outputs:', limit_string(local_outputs)))
        if exception:
            report.append(('Local exception:', limit_string(exception)))
        report.append(('Matching outputs:', matches))
        return report


def varsnap(func: Callable) -> Callable:
    producer = Producer(func)
    Consumer(func)

    def magic(*args, **kwargs):
        try:
            output = func(*args, **kwargs)
        except Exception as e:
            threading.Thread(
                target=producer.produce,
                args=(args, kwargs, e),
            ).start()
            raise
        threading.Thread(
            target=producer.produce,
            args=(args, kwargs, output),
        ).start()
        return output
    LOGGER.info('Varsnap Loaded')
    # Reuse the original function name so it works with flask handlers
    magic.__name__ = func.__name__
    return magic
