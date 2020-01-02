# coding=utf-8
__author__ = 'peter gra'
__date__ = '2018/5/23 下午4:44'
import redis
from django.conf import settings


class Rediser(object):
    def __init__(self,
                 host=settings.REDIS.get('default').get('HOST'),
                 port=settings.REDIS.get('default').get('PORT'),
                 password=settings.REDIS.get('default').get('PASSWORD'),
                 decode_responses=True):
        if password:
            self._cache = redis.Redis(host=host, port=port, password=password, decode_responses=decode_responses)
        else:
            self._cache = redis.Redis(host=host, port=port, decode_responses=decode_responses)

    def set(self, key, value, ex=None, px=None, nx=False, xx=False):
        self._cache.set(name=key,
                        value=value,
                        ex=ex,
                        px=px,
                        nx=nx,
                        xx=xx)

    def get(self, key):
        return self._cache.get(key)

    def delete(self, key):
        return self._cache.delete(key)

    def hget(self, key, field_name):
        return self._cache.hget(key, field_name)

    def hset(self, key, field_name, value):
        return self._cache.hset(key, field_name, value)

    def hdel(self, key, field_name):
        return self._cache.hdel(key, field_name)

    def geoadd(self, key, lon, lat, name):
        prefix = settings.REDIS.get('namespace').get('GEO_DICT')
        key = ''.join([prefix, ':', key])
        geo_info = (lon, lat, name)
        return self._cache.geoadd(name=key, *geo_info)

    def geopos(self, key):
        prefix = settings.REDIS.get('namespace').get('GEO_DICT')
        key = ''.join([prefix, ':', key])
        geo_info = ('',)
        return self._cache.geopos(name=key, *geo_info)

    def georadius(self, key, lon, lat, radius=1000, unit='m',
                  withdist=False, withcoord=False, withhash=False,
                  count=None,
                  sort=None, store=None, store_dist=None):
        prefix = settings.REDIS.get('namespace').get('GEO_DICT')
        key = ''.join([prefix, ':', key])
        return self._cache.georadius(name=key,
                                     longitude=lon,
                                     latitude=lat,
                                     radius=radius,
                                     unit=unit,
                                     withdist=withdist,
                                     withcoord=withcoord,
                                     withhash=withhash,
                                     count=count,
                                     sort=sort,
                                     store=store,
                                     store_dist=store_dist)


redis_obj = Rediser()
