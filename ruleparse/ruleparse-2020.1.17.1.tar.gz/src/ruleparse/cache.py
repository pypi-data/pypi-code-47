#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Time    : 2019/12/19 17:31
# @Author  : Niyoufa
import json
import base64
from pymemcache.client.base import Client

from ruleparse.utils import md5
from ruleparse.rules import Rule
from ruleparse.slots import Slot

import logging
logger = logging.getLogger(__file__)


class CacheProxy(object):

    def get(self, key):
        """
        查询缓存
        :param key:
        :return:
        """
        raise NotImplementedError

    def set(self, key, value):
        """
        添加缓存
        :param key:
        :param value:
        :return:
        """
        raise NotImplementedError


class MemCacheProxy(CacheProxy):

    def __init__(self, host, port):
        self.client = Client((host, port), serializer=self.json_serializer,
                    deserializer=self.json_deserializer)

    def json_serializer(self, _, value):
        if type(value) == str:
            value = base64.b64encode(value.encode()), 1
        else:
            value = base64.b64encode(json.dumps(value).encode()), 2
        return value

    def json_deserializer(self, _, value, flags):
        if flags == 1:
            return base64.b64decode(value)
        if flags == 2:
            return json.loads(base64.b64decode(value))
        raise Exception("Unknown serialization format")

    def get(self, key):
        md5_key = md5(key)
        value = self.client.get(md5_key)
        logger.debug("{} {} {}".format(key, md5_key, value))
        return value

    def set(self, key, value):
        md5_key = md5(key)
        logger.debug("{} {}".format(key, md5_key))
        self.client.set(md5_key, value)


class EXRECache(object):

    def __init__(self, cacheProxy):
        self.cacheProxy = cacheProxy

    def get_rule(self, rule_name):
        return self.cacheProxy.get("rule_{}".format(rule_name))

    def set_rule(self, *args):
        for rule in args:
            if not rule.name:
                continue
            self.cacheProxy.set("rule_{}".format(rule.name),
                       {"name":rule.name, "content": rule.content})

    def get_slot(self, slot_name):
        return self.cacheProxy.get("slot_{}".format(slot_name))

    def set_slot(self, *args):
        for slot in args:
            self.cacheProxy.set("slot_{}".format(slot.name), repr(slot))

    def set(self, *args):
        for obj in args:
            if isinstance(obj, Rule):
                self.set_rule(obj)
            elif isinstance(obj, Slot):
                self.set_slot(obj)
            else:
                raise Exception("缓存对象类型错误")