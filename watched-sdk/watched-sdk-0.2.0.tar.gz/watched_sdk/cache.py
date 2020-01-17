import hashlib
import os
import time

from .common import logger


def wait_key(cache, key, timeout, delete, sleep):
    t = time.time()
    while True:
        result = cache.get(key)
        if result:
            if delete:
                cache.delete(key)
            return result
        if time.time() - t > timeout:
            raise ValueError('Remote request timed out')
        time.sleep(sleep)


class BaseCache(object):
    def get(self, key):
        raise NotImplementedError()

    def set(self, key, value, ttl=3600):
        raise NotImplementedError()

    def delete(self, key):
        raise NotImplementedError()

    def cleanup(self):
        """Cleanup the expired cache entries. This
        function is currently never called and just
        a plan.
        """
        pass

    def wait_key(self, key, timeout=30, delete=True):
        raise NotImplementedError()


class LocalCache(BaseCache):
    def __init__(self):
        self.data = {}

    def get(self, key):
        d = self.data.get(key, None)
        if d:
            if d[0] <= time.time():
                return d[1]
            self.data.pop(key)
        return None

    def set(self, key, value, ttl=3600):
        self.data[key] = [time.time()+ttl, value]
        return value

    def delete(self, key):
        self.data.pop(key)

    def cleanup(self):
        for key in self.data:
            d = self.data.get(key, None)
            if d and d[0] > time.time():
                self.data.pop(key)

    def wait_key(self, key, timeout=30, delete=True):
        return wait_key(self, key, timeout, delete, 0.1)


class FileCache(BaseCache):
    def __init__(self, path):
        import diskcache
        self.cache = diskcache.Cache(path)

    def _key(self, key):
        h = hashlib.sha1()
        h.update(repr(key).encode('utf-8'))
        return h.hexdigest()

    def get(self, key):
        return self.cache.get(self._key(key))

    def set(self, key, value, ttl=3600):
        self.cache.set(self._key(key), value, expire=ttl)
        return value

    def delete(self, key):
        self.cache.delete(self._key(key))

    def wait_key(self, key, timeout=30, delete=True):
        return wait_key(self, key, timeout, delete, 0.5)


class RedisCache(BaseCache):
    def __init__(self, url):
        import redis
        self.db = redis.Redis.from_url(url)

    def get(self, key):
        return self.db.get(key)

    def set(self, key, value, ttl=3600):
        self.db.setex(key, ttl, value)
        return value

    def delete(self, key):
        self.db.delete(key)

    def wait_key(self, key, timeout=30, delete=True):
        return wait_key(self, key, timeout, delete, 0.5)


if 'FILE_CACHE' in os.environ:
    cache = FileCache(os.environ['FILE_CACHE'])
elif 'REDIS_CACHE' in os.environ:
    cache = RedisCache(os.environ['REDIS_CACHE'])
else:
    logger.warning(
        'Using LocalCache, use this only when you use one process!')
    cache = LocalCache()


def get_cache():
    return cache


def set_cache(cache):
    """Set the caching options. It is recommended to
    set it via environment variables.

    Use a shared directory:
    `FILE_CACHE=/path/to/cache`

    Use redis:
    `REDIS_CACHE=redis://example.com:6379`

    Default is that a local cache will be used. This
    local cache is not distributed, so use it only it
    in environments where you use one process!
    """
    globals['cache'] = cache
