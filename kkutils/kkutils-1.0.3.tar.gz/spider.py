#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Author: zhangkai
Email: zhangkai@cmcm.com
Last modified: 2018-01-05 17:21:17
'''
import asyncio
import collections
import copy
import hashlib
import inspect
import pickle
import sys
import urllib.parse
from asyncio import Queue
from asyncio.locks import Lock
from concurrent.futures._base import CancelledError
from functools import partial
from importlib import import_module
from signal import SIGINT
from signal import SIGTERM

import uvloop
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from utils import AioPika
from utils import AioRedis
from utils import Config
from utils import Logger
from utils import Redis
from utils import Request

asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())


def sched(trigger, **trigger_kwargs):
    def wrapper(func):
        func._trigger = trigger
        func._trigger_kwargs = trigger_kwargs
        return func
    return wrapper


class BaseChecker:

    def __init__(self, prefix, retries=3):
        self.retries = retries
        self.lock = Lock()

    def __getattr__(self, key):
        def func(*args, **kwargs):
            return False
        return func

    async def __call__(self, key):
        with await self.lock:
            if self.check('succeed', key) or self.check('failed', key) or self.check('running', key):
                return False
            if self.incr(key) < self.retries:
                self.add('running', key)
                return True
            else:
                self.add('failed', key)
                return False


class MemoryChecker(BaseChecker):

    def __init__(self, prefix, retries=3):
        super().__init__(prefix, retries)
        self.cache = collections.defaultdict(int)
        self.storage = collections.defaultdict(set)

    def incr(self, key):
        self.cache[key] += 1
        return self.cache[key]

    def add(self, name, key):
        self.storage[name].add(key)

    def remove(self, name, key):
        if key in self.storage[name]:
            self.storage[name].remove(key)

    def check(self, name, key):
        return key in self.storage[name]


class RedisChecker(BaseChecker):

    def __init__(self, prefix, retries=3):
        super().__init__(prefix, retries)
        self.prefix = prefix
        self.rd = Redis()

    def incr(self, key):
        return self.rd.hincrby(f'{self.prefix}_count', key, 1)

    def add(self, name, key):
        self.rd.sadd(f'{self.prefix}_{name}', key)

    def remove(self, name, key):
        self.rd.srem(f'{self.prefix}_{name}', key)

    def check(self, name, key):
        return self.rd.sismember(f'{self.prefix}_{name}', key)


class QueueBroker:

    def __init__(self, prefix):
        self.queue = Queue()

    async def get(self):
        return await self.queue.get()

    async def ack(self):
        self.queue.task_done()

    async def put(self, msg):
        return await self.queue.put(msg)

    async def size(self):
        return self.queue.qsize()

    async def join(self):
        await self.queue.join()

    async def finish(self):
        while not self.queue.empty():
            await self.queue.get()


class RedisBroker:

    def __init__(self, prefix):
        self.prefix = prefix
        self.rd = AioRedis(decode_responses=False)

    async def get(self):
        return await self.rd.brpoplpush(self.prefix, f'{self.prefix}_tmp')

    async def ack(self):
        await self.rd.lpop(f'{self.prefix}_tmp')

    async def put(self, msg):
        await self.rd.lpush(self.prefix, msg)

    async def size(self):
        return await self.rd.llen(self.prefix) + await self.rd.llen(f'{self.prefix}_tmp')

    async def join(self):
        while await self.size():
            await asyncio.sleep(1)

    async def finish(self):
        pass


class AmqpBroker:

    def __init__(self, prefix):
        self.prefix = prefix
        self.mq = AioPika(queue=prefix)

    async def get(self):
        return await self.mq.get()

    async def size(self):
        return await self.mq.size()

    async def ack(self):
        pass

    async def put(self, msg):
        await self.mq.publish(msg)

    async def join(self):
        while await self.size():
            await asyncio.sleep(1)

    async def finish(self):
        pass


class SpiderMeta(type):

    def __new__(cls, name, bases, attrs):
        sched_jobs = []
        for job in attrs.values():
            if inspect.isfunction(job) and getattr(job, '_trigger', None):
                sched_jobs.append(job)
        newcls = type.__new__(cls, name, bases, attrs)
        newcls._sched_jobs = sched_jobs
        return newcls


class Spider(metaclass=SpiderMeta):

    urls = [f'https://www.baidu.com']

    def __init__(self,
                 workers=10,
                 timeout=30,
                 retries=3,
                 prefix='spider',
                 checker='MemoryChecker',
                 broker='QueueBroker',
                 roles=['producer', 'consumer'],
                 splash=None,
                 **kwargs):
        ''' splash: http://localhost:8050/render.html
            broker: redis://localhost:6379
        '''
        self.workers = workers
        self.splash = splash
        self.roles = roles
        self.prefix = prefix
        self.logger = Logger(name='tornado.application')
        self.http = Request(lib='tornado', retry=3, max_clients=workers, timeout=timeout)
        module = sys.modules[__name__]
        self.broker = getattr(module, broker)(prefix)
        self.checker = getattr(module, checker)(prefix, retries)
        self.sched = AsyncIOScheduler()
        self.loop = asyncio.get_event_loop()
        if hasattr(self, 'init'):
            ret = self.init()
            if inspect.isawaitable(ret):
                self.loop.run_until_complete(ret)
        for key, value in kwargs.items():
            setattr(self, key, value)

    async def crawl(self, url, callback, *args, **kwargs):
        msg = pickle.dumps((url, callback.__name__, args, kwargs))
        key = hashlib.md5(msg).hexdigest()
        if await self.checker(key):
            await self.broker.put(msg)

    async def parse(self, resp):
        self.logger.info(f'{resp.code}: {resp.url}')

    # @sched('interval', seconds=3)
    async def producer(self):
        for url in self.urls:
            await self.crawl(url, self.parse)

    async def process(self, msg):
        url, callback, args, kwargs = pickle.loads(msg)
        callback = getattr(self, callback)
        key = hashlib.md5(msg).hexdigest()
        if self.splash:
            data = copy.deepcopy(kwargs)
            data['url'] = url
            data.setdefault('http_method', data.pop('method', 'GET'))
            data.setdefault('wait', 1)
            if 'lua_source' in data:
                ret = urllib.parse.urlparse(self.splash)
                splash_url = f'{ret.scheme}://{ret.netloc}/execute'
                resp = await self.http.post(splash_url, data=data, json=True)
            else:
                resp = await self.http.post(self.splash, data=data, json=True)
        else:
            resp = await self.http.request(url, **kwargs)

        size = await self.broker.size()
        message = f'queue: {size}, url: {url} {resp.code} {resp.reason}'
        if 200 <= resp.code < 300:
            self.logger.info(message)
        else:
            self.logger.warning(message)
        self.checker.remove('running', key)

        codes = kwargs.get('codes', [])
        if (codes and resp.code in codes) or (not codes and 200 <= resp.code < 300):
            try:
                doc = callback(resp, *args)
                if inspect.isawaitable(doc):
                    doc = await doc
                self.checker.add('succeed', key)
            except Exception as e:
                self.logger.exception(e)
                await self.crawl(url, callback, *args, **kwargs)
        else:
            await self.crawl(url, callback, *args, **kwargs)

    async def consumer(self):
        while True:
            try:
                msg = await self.broker.get()
                await self.process(msg)
                await self.broker.ack()
            except CancelledError:
                return self.logger.error(f'Cancelled consumer')
            except Exception as e:
                self.logger.exception(e)
                self.broker.ack()

    async def shutdown(self, sig):
        self.logger.warning('caught {0}'.format(sig.name))
        await self.broker.finish()
        tasks = list(filter(lambda task: task is not asyncio.tasks.Task.current_task(),
                            asyncio.Task.all_tasks()))
        self.logger.info(f'finished awaiting cancelled tasks: {len(tasks)}')
        list(map(lambda task: task.cancel(), tasks))
        # await asyncio.gather(*tasks, return_exceptions=True)
        self.loop.stop()

    def start(self):
        if 'consumer' in self.roles:
            for _ in range(self.workers):
                self.loop.create_task(self.consumer())

        for sig in (SIGINT, SIGTERM):
            self.loop.add_signal_handler(sig, partial(self.loop.create_task, self.shutdown(sig)))

        if self._sched_jobs:
            self.checker = BaseChecker()
            self.logger.info(self._sched_jobs)
            for func in self._sched_jobs:
                function = func.__get__(self, self.__class__)
                self.sched.add_job(function, func._trigger, **func._trigger_kwargs)
            self.sched.start()
            self.loop.run_forever()
        else:
            if 'producer' in self.roles:
                self.loop.run_until_complete(self.producer())
            if 'consumer' in self.roles:
                self.loop.run_until_complete(self.broker.join())
            if hasattr(self, 'finish'):
                ret = self.finish()
                if inspect.isawaitable(ret):
                    self.loop.run_until_complete(ret)


def main():
    opt = Config(dict(
        workers=10,
        timeout=30,
        retries=3,
        prefix='spider',
        checker='MemoryChecker',
        broker='QueueBroker',
        roles=['producer', 'consumer'],
        splash=None,
    ))
    module_name, app_name = sys.argv[1].split('.')
    module = import_module(module_name)
    app = getattr(module, app_name)(**opt)
    app.start()


if __name__ == '__main__':
    main()
