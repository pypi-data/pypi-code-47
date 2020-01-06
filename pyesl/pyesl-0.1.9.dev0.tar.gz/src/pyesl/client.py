# -*- coding: utf-8 -*-
from __future__ import annotations
from typing import List, Tuple, Union, Dict

from elasticsearch import Elasticsearch, TransportError

from pyesl.conf import ElasticsearchConfig
from pyesl.errors import SearchFailedError
from pyesl.parser.response import ResponseParser
from pyesl.response import TsdbResponse
from pyesl.search import ElasticsearchQuery


class SearchClient(object):
    _pool: Dict[str, SearchClient] = {}

    def __init__(self, hosts: List[str], http_auth: Union[None, Tuple[str, str]] = None, **params):
        self._config = ElasticsearchConfig(hosts, http_auth=http_auth, **params)
        self._es = Elasticsearch(**self._config)

    def search(self, query: ElasticsearchQuery, json_loads: List[str] = None) -> TsdbResponse:
        """
        **传入查询结构体，通过client客户端向es发起查询请求并返回结构化的Tsdb格式**

        :param query: 查询语句结构体
        :type query: ElasticsearchQuery
        :param json_loads: 需要json反序列化的fields
        :type json_loads: List[str]
        :return: Tsdb格式的返回结果
        :rtype: TsdbResponse
        :raise: SearchFailedError
        """
        try:
            response = self._es.search(index=query.index, body=query.body, params=query.params)
            return ResponseParser.tsfresp(query, response, json_loads=json_loads)
        except TransportError as ex:
            try:
                raise_err = SearchFailedError(message=ex.info, status=ex.status_code)
            except Exception:
                raise ex
            else:
                raise raise_err

    @classmethod
    def from_pool(
            cls, hosts: List[str], http_auth: Union[None, Tuple[str, str]] = None, **params: dict) -> SearchClient:
        """
        **传入ES配置，返回对应缓存在内存的SearchClient实例，从而使用连接池特性**

        若参数对应的SearchClient实例不存在，则创建并缓存一个

        :param hosts: ES地址列表
        :type hosts: List[str]
        :param http_auth: ES地址对应的auth信息,例如:('username', 'password')
        :type http_auth: Union[None, Tuple[str, str]]
        :param params: 其余的ES客户端初始化参数
        :type params: dict
        :return: 缓存在内存的连接池实例
        :rtype: SearchClient
        """
        _config = ElasticsearchConfig(hosts, http_auth=http_auth, **params)
        if _config.name in cls._pool:
            return cls._pool[_config.name]
        else:
            ret = SearchClient(**_config)
            cls._pool[_config.name] = ret
            return ret

    @classmethod
    def reset_pool(cls, hosts: List[str], http_auth: Union[None, Tuple[str, str]] = None, **params):
        """
        **传入ES配置，生成并在内存缓存的SearchClient实例，从而支持连接池特性**

        若参数对应的SearchClient实例存在，则覆盖

        :param hosts: ES地址列表
        :type hosts: List[str]
        :param http_auth: ES地址对应的auth信息,例如:('username', 'password')
        :type http_auth: Union[None, Tuple[str, str]]
        :param params: 其余的ES客户端初始化参数
        :type params: dict
        """
        _config = ElasticsearchConfig(hosts, http_auth=http_auth, **params)
        cls._pool[_config.name] = SearchClient(**_config)

    @property
    def name(self):
        return self._config.name
