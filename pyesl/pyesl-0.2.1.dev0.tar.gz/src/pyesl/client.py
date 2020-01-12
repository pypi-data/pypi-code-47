# -*- coding: utf-8 -*-
from __future__ import annotations

import asyncio
from concurrent.futures.thread import ThreadPoolExecutor
from functools import partial
from typing import List, Tuple, Union, Dict, Iterable

from elasticsearch import Elasticsearch, TransportError

from pyesl.conf import ElasticsearchConfig
from pyesl.errors import SearchFailedError
from pyesl.parser.response import ResponseParser
from pyesl.response import TsdbResponse, SingleSeries
from pyesl.search import ElasticsearchQuery


class SearchClient(object):
    _pool: Dict[str, SearchClient] = {}

    def __init__(self, hosts: List[str], http_auth: Union[None, Tuple[str, str]] = None, **params):
        self._config = ElasticsearchConfig(hosts, http_auth=http_auth, **params)
        self._es = Elasticsearch(**self._config)

    def search(self, query: ElasticsearchQuery, json_loads: Union[List[str], None] = None) -> TsdbResponse:
        """
        **传入查询结构体，通过client客户端向es发起查询请求并返回结构化的Tsdb格式**

        :param query: 查询语句结构体
        :type query: ElasticsearchQuery
        :param json_loads: 需要json序列化的fields字段列表
        :type json_loads: Union[List[str], None]
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

    def scroll(
            self, query: ElasticsearchQuery, json_loads: Union[List[str], None] = None, query_size: int = -1,
            fetch_size: int = 100, fetch_timeout_s: int = 60, sync: bool = True) -> Iterable[SingleSeries]:
        """
        **传入查询结构体，通过client客户端向es发起查询请求并游标形式返回结构化的Tsdb格式数据**

        :param query: 查询语句结构体
        :type query: ElasticsearchQuery
        :param json_loads: 需要json序列化的fields字段列表
        :type json_loads: Union[List[str], None]
        :param fetch_size: 分批获取数据的数量,最多5000
        :type fetch_size: int
        :param query_size: 数据查询总条目数量,-1, 没有限制
        :type query_size: int
        :param fetch_timeout_s: 分批获取数据的超时时间,单位s
        :type fetch_timeout_s:
        :return: Tsdb格式的返回结果
        :param sync: 是否已同步的方式访问，若使用异步方式访问，则在上一批数据处理的时候，下一次数据获取将提前执行
        :type sync: bool
        :rtype: Iterable[SingleSeries]
        :raise: SearchFailedError
        """
        scroll_body = query.body
        scroll_params = query.params
        scroll_params.pop('track_total_hits', None)
        scroll_params.pop('request_cache', None)
        scroll_params.pop('pre_filter_shard_size', None)
        timeout = '{}s'.format(fetch_timeout_s)
        fetch_size = min(fetch_size, 5000)
        scroll_body['size'] = fetch_size
        scroll_body.pop('from', None)
        scroll_params['scroll'] = timeout
        scroll_params.pop('routing', None)
        response = self._es.search(
            index=query.index, body=scroll_body, params=scroll_params)
        scroll_id = response.pop('_scroll_id')
        return_size = 0
        if response['hits'].get('hits', None):
            total = response['hits'].get('total', 0)
            if isinstance(total, dict):
                total = total.get('value', 0)
            else:
                pass
        else:
            total = 0
        return_limit = total if query_size < 0 else min(query_size, total)
        try:
            if response['hits'].get('hits', None):
                if not sync:
                    loop = asyncio.get_event_loop()
                    next_tasks = self.async_get_response(scroll_id, scroll_params)
                    next_done, _ = loop.run_until_complete(asyncio.wait([next_tasks]))
                    for _single_series in ResponseParser.iterfresp(query, response, json_loads=json_loads):
                        return_size += 1
                        yield _single_series
                        if return_size >= return_limit:
                            break
                    response = next_done.pop().result()
                    while return_size < return_limit and response['hits'].get('hits', None):
                        next_tasks = self.async_get_response(scroll_id, scroll_params)
                        next_done, _ = loop.run_until_complete(asyncio.wait([next_tasks]))
                        for _single_series in ResponseParser.iterfresp(query, response, json_loads=json_loads):
                            return_size += 1
                            yield _single_series
                            if return_size >= return_limit:
                                break
                        if return_size >= return_limit:
                            break
                        response = next_done.pop().result()
                    loop.close()
                else:
                    for _single_series in ResponseParser.iterfresp(query, response, json_loads=json_loads):
                        return_size += 1
                        yield _single_series
                        if return_size >= return_limit:
                            break
                    while return_size < return_limit and response['hits'].get('hits', None):
                        response = self._es.scroll(scroll_id=scroll_id, params=scroll_params)
                        for _single_series in ResponseParser.iterfresp(query, response, json_loads=json_loads):
                            return_size += 1
                            yield _single_series
                            if return_size >= return_limit:
                                break
        except Exception as ex:
            raise ex
        finally:
            pass
            self._es.clear_scroll(scroll_id=scroll_id)

    async def async_get_response(
            self, scroll_id: str, params: dict, executor: ThreadPoolExecutor = ThreadPoolExecutor(1)):
        _response = await asyncio.get_event_loop().run_in_executor(
            executor, partial(self._es.scroll, scroll_id=scroll_id, params=params))
        return _response

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
