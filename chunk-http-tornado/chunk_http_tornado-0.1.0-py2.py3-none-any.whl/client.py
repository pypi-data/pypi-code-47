# coding: utf-8
import typing
from tornado import httpclient
from tornado import gen
from tornado.ioloop import IOLoop


@gen.coroutine
def send_chunks(url: str, producer: typing.Callable, task_id: str, request_timeout=3600) -> typing.Awaitable:
    """
    :param url:
    :param producer: A function that accepts one argument `write`
    :param task_id: Id to identify this request
    :param request_timeout: Timeout for entire request in seconds

    :return: A tornado `future`
    """
    client = httpclient.AsyncHTTPClient()
    resp = yield client.fetch(
        url,
        method='POST',
        body_producer=producer,
        headers={'task_id': task_id},
        request_timeout=request_timeout
    )
    return resp


def send_chunks_sync(*args, **kwargs):
    """ Run send chunks """

    IOLoop.current().run_sync(lambda: send_chunks(*args, **kwargs))


@gen.coroutine
def example_producer(write):
    for i in range(300):
        yield write(str(i).encode())
        yield gen.sleep(1)



