# coding=utf-8
__author__ = 'peter gra'
__date__ = '2019-12-16 16:02'
import requests
import logging

from django.conf import settings
from elasticsearch import Elasticsearch


class ESIndex(object):
    idle = 'idle'
    user = 'user'
    department = 'department'
    topic = 'topic'


class ESHandler(object):
    def __init__(self, host=settings.SERVICE_DOMAIN + ':' + str(settings.ELASTICSEARCH_PORT)):
        try:
            result = requests.get(host).json()
            if result.get('version'):
                self._es = Elasticsearch(hosts=[host])
            else:
                logging.exception('ES模块失效: 初始化失败')
        except Exception as exce:
            logging.exception('ES模块失效', str(exce))

    def search(self, index=None, body=None):
        try:
            return self._es.search(index=index, body=body)
        except Exception as exce:
            logging.exception('ES模块失效', str(exce))
            return None

    def create(self, index, id, body):
        try:
            return self._es.create(index=index, id=id, body=body)
        except Exception as exce:
            logging.exception('ES模块失效', str(exce))
            return None

    def update(self, index, id, body):
        try:
            return self._es.update(index=index, id=id, body=body)
        except Exception as exce:
            logging.exception('ES模块失效', str(exce))
            return None

    def delete(self, index, id):
        try:
            return self._es.delete(index=index, id=id)
        except Exception as exce:
            logging.exception('ES模块失效', str(exce))
            return None

    def exists(self, index, id):
        try:
            return self._es.exists(index=index, id=id)
        except Exception as exce:
            logging.exception('ES模块失效', str(exce))
            return None


es_obj = ESHandler()
