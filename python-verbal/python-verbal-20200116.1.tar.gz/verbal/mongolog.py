from __future__ import absolute_import

import logging
import getpass
import socket
import os
import os.path
import sys
import urllib.parse as urlparse
import re
import traceback

from datetime import datetime, timedelta
from pymongo import MongoClient
from pymongo.collection import Collection
from pymongo.errors import InvalidDocument


def _redact(url):
    if '=' in url:
        return '='.join([_redact(v) for v in url.split('=')])

    url = urlparse.urlparse(url)
    if url.password:
        password = url.password
        url = list(url)
        url[1] = url[1].replace(password, '****')
        return urlparse.urlunparse(url)
    else:
        return url.geturl()


def _full_process_info():
    """
    add more complete process into to a record
    """
    import pkg_resources
    return dict(
        sys={
            k: getattr(sys, k, None) for k in [
                'argv', 'prefix', 'real_prefix', 'version', 'platform', 'winver', 'path'
            ]
        },
        working_set=[
            {k: getattr(d, k, None) for k in [
                'project_name',
                'version',
                'platform',
                'location',
                'py_version'
            ]}
            for d in pkg_resources.working_set
        ],
        environ=dict(os.environ)
    )


def excepthook(uri, type, value, tb):
    try:
        record = logging.LogRecord(
            name='excepthook',
            level=logging.CRITICAL,
            pathname=tb.tb_frame.f_code.co_filename,
            msg=(''.join(traceback.format_exception_only(type, value)))[:-1],
            args=(),
            lineno=tb.tb_lineno,
            exc_info=(type, value, tb),
        )

        MongoHandler(uri).emit(record)
    except:
        sys.__excepthook__(*sys.exc_info())


# shoudl this be a filter?
class MongoFormatter(logging.Formatter):
    def __init__(self):
        main = sys.modules['__main__']

        self.info = dict(
            username=getpass.getuser(),
            host=socket.getfqdn(),
            requires=getattr(main, '__requires__', None),
            prefix=sys.prefix
        )

        try:
            import psutil
            self.info['process_create_time'] = datetime.fromtimestamp(
                psutil.Process(os.getpid()).create_time()
            )
        except:
            sys.__excepthook__(*sys.exc_info())
            self.info['process_create_time'] = None

        if hasattr(main, '__file__'):
            file = os.path.basename(main.__file__)
            self.info['entrypoint'] = re.sub("-script.pyc?$", "", file)

    def format(self, record):
        data = record.__dict__.copy()

        try:
            # format message with args, and forget them
            data['message'] = str(record.getMessage())

            data.pop('msg')
            data.pop('args')

            data['message_time'] = datetime.now()
            if 'exc_info' in data and data['exc_info']:
                data['exc_text'] = self.formatException(data.pop('exc_info')).split('\n')

            data.update(self.info)
        except:
            sys.__excepthook__(*sys.exc_info())

        return data


class MongoHandler(logging.Handler):
    """ Custom log handler

    Logs all messages to a mongo collection. This  handler is
    designed to be used with the standard python logging mechanism.
    """

    def __init__(self, uri, collection='log', level=logging.NOTSET):
        """ Init log handler and store the collection handle """
        logging.Handler.__init__(self, level)
        if isinstance(collection, str):
            self.collection = MongoClient(uri).get_default_database()[collection]
        elif isinstance(collection, Collection):
            self.collection = collection
        else:
            raise TypeError('collection must be an instance of basestring or '
                            'Collection')
        self.formatter = MongoFormatter()

    def emit(self, record):
        """ Store the record to the collection. Async insert """
        try:
            self.collection.insert_one(self.format(record))
        except InvalidDocument as e:
            logging.error("Unable to save log record: %s", e,
                          exc_info=True)


def tail(mongolog_uri=None, collection='log', pause=0.1):
    from time import sleep
    from datetime import datetime, time

    log = logging.getLogger('')

    collection = MongoClient(mongolog_uri).get_default_database()[collection]

    d = datetime.now() - timedelta(minutes=10)
    log.info("tailing from {collection}, from {d}".format(**locals()))

    cursor = collection.find({
        'message_time': {'$gte': d}
    }, tailable=True, await_data=True)

    root = logging.getLogger('')

    while cursor.alive:
        try:
            msg = cursor.next()
            record = logging.LogRecord(
                msg.get('name', ''),
                msg.get('levelno', logging.NOTSET),
                msg.get('pathname', ''),
                msg.get('lineno', ''),
                msg.get('message', ''),
                args=(),
                exc_info=(),
                func=msg.get('funcName', ''),
            )

            for k, v in msg.items():
                if not hasattr(record, k):
                    setattr(record, k, v)

            logger = logging.getLogger(record.name)
            if logger.isEnabledFor(record.levelno):
                logger.handle(record)
        except StopIteration:
            sleep(pause)


def main():
    from verbal.argh import ArghParser
    argh = ArghParser()
    argh.add_commands([tail])
    argh.dispatch()
