# -*- coding: utf-8 -*-

import json
from datetime import datetime as dt
from functools import partial
from typing import Union, Tuple, List, Iterator, Dict

from deprecated import deprecated

from pyesl.aggs import TopKType
from pyesl.errors import SearchFailedError
from pyesl.response import TsdbResponse, Series, TopKFilter, SingleSeries
from pyesl.search import ElasticsearchQuery


class ResponseParser(object):

    @staticmethod
    def tsfresp(query: ElasticsearchQuery, response: dict, json_loads: Union[List[str], None] = None) -> TsdbResponse:
        """
        **Get TsdbResponse From Elasticsearch Search API Response**

        This function allows users to get tsdb type response from the Elasticsearch search API return object.

        :param query: 本次查询结果的查询对象
        :type query: ElasticsearchQuery
        :param response: Elasticsearch的search的API返回结果
        :type response: dict
        :param json_loads: 需要json反序列化的fields字段列表
        :type json_loads: List[str]
        :return: 返回时序格式结构对象
        :rtype: TsdbResponse

        - Example::

              es_query = TestParser().test_10_where_filters_aggs()
              cli = SearchClient(**es_conf.es_conf)
              res = cli.search(es_query)
              for _s in res.series:
                  print(_s.name) # using name
                  print(_s.legends) # using legends
                  for _dp in _s.data: # using datapoint
                      print(_dp.ts)
                      print(_dp.value)

        - Expected Success Response::

              self.assertEqual(res.series[0].name, 'agg#gameid=g66#url=/g66/gb/sauth')
              self.assertEqual(len(res.series[0].data), 7)
              self.assertEqual(res.series[0].data[0].value, 47022.28388131516)
              self.assertEqual(res.series[0].data[0].ts, 1573833600000)
              self.assertEqual(res.series[0].data[6].value, 26883.47335553705)
              self.assertEqual(res.series[0].data[6].ts, 1573855200000)
              self.assertEqual(res.series[-1].name, 'agg#gameid=lh2#url=/lh2/gb/sauth')
        """

        if response['_shards'][
            'failed'] and query.aggregations and query.aggregations.topk_type != TopKType.TOPK_FIELD.value:
            # failed and handler error
            raise SearchFailedError(u'Search Failed Error: {}'.format(response['_shards']['failures'][0]))
        else:
            # success
            _series = []
            if query.aggregations:
                # 聚合查询
                _topk_filter = TopKFilter(topk=query.aggregations.topk) if query.aggregations.topk else None
                if query.aggregations.topk_type == TopKType.TOPK_FIELD.value:
                    for series in ResponseParser._walk_through_bucket(
                            response.get('aggregations', {}), query.aggregations.result_path,
                            Series('agg', topk_filter=_topk_filter), {}, in_hits=True):
                        _series.append(series)
                else:
                    for series in ResponseParser._walk_through_bucket(
                            response.get('aggregations', {}), query.aggregations.result_path,
                            Series('agg', topk_filter=_topk_filter), {}):
                        _series.append(series)
            else:
                # 一般查询
                _series = ResponseParser._walk_through_hits(
                    response.get('hits', {}).get('hits', []), json_loads=json_loads)
        return TsdbResponse(_series, response)

    @staticmethod
    def _add_tag(tag_name: str, tag_value: str, datapoint: dict):
        datapoint['tag'][tag_name] = tag_value

    @staticmethod
    def _add_ts_metric(tag_name: str, tag_value: Union[str, int], datapoint: dict):
        datapoint[tag_name] = tag_value

    _DEFAULT_VALUE = {
        'value': None
    }

    @classmethod
    def _add_datapoint(
            cls, series: Series, ts: Union[int, float, str], field_name: Union[List[str], Tuple[str], str],
            result_bucket: dict, filter_out_null: bool = True):
        """
        **将数据节点从es的bucket中抽取放入Series数据结构当中**

        :param series: 用于存放解析得到的数据的数据队列结构
        :type series: Series
        :param ts: 时间信息
        :type ts: Union[int, float, str]
        :param field_name: 数据字段的获取路径(数组方式传入)/名字(字符串方式传入)
        :type field_name: Union[List[str], Tuple[str], str]
        :param result_bucket: 数据字段所在的ES结果bucket
        :type result_bucket: dict
        :param filter_out_null: 获取结果的时候是否过滤掉为null的数据点
        :type filter_out_null: bool
        :return: 无
        """
        if isinstance(field_name, (list, tuple)):
            # 多个运算结果
            for field_path in field_name:
                _cur = result_bucket
                if isinstance(field_path, (list, tuple)):
                    _field_name = field_path[0]
                    for _path in field_path:
                        _cur = _cur.get(_path, cls._DEFAULT_VALUE)
                else:
                    _field_name = field_path
                    _cur = result_bucket.get(field_path, cls._DEFAULT_VALUE)
                _val = _cur['value']
                if filter_out_null and _val is None:
                    continue
                else:
                    # 过滤掉为null的结果
                    series.add_datapoint(_cur['value'], ts)
        else:
            series.add_datapoint(result_bucket[field_name]['value'], ts)

    @staticmethod
    def _walk_through_bucket(
            groupby_result: Dict[str, dict], result_path: Union[tuple, list],
            base_series: Series,
            series_results: Dict[str, Series], ts: Union[int, float, str, None] = None,
            in_hits: bool = False) -> Iterator[Series]:
        """
        **返回结构化聚合数据**
        :param groupby_result:
        :type groupby_result:
        :param result_path:
        :type result_path:
        :param base_series: 用于生成新Series的base series
        :type base_series: Series
        :param series_results: 用于保存生成数据的Series
        :type series_results: Dict[str, Series]
        :param ts: 传入的时间戳
        :type ts: Union[int, float, str, None]
        :param in_hits: 结果是否在最终的in_hits队列中
        :type in_hits: bool
        :return:
        :rtype: Iterator[Series]
        """
        this_tagname = result_path[0]
        next_layer = result_path[1:]
        if this_tagname == 'ts':
            if len(next_layer) == 1:
                # 到达了统计边界（ts）next_layer就是field_name了
                if base_series.name in series_results:
                    # 已有的series_name
                    _s = series_results[base_series.name]
                else:
                    # 没有series_name
                    _s = base_series.copy()
                    series_results[base_series.name] = _s
                for bucket in groupby_result.get(this_tagname, {}).get('buckets', []):
                    _ts = bucket['key']
                    if in_hits:
                        ResponseParser._add_datapoint_in_hits(series_results, _ts, next_layer[0], bucket)
                    else:
                        ResponseParser._add_datapoint(_s, _ts, next_layer[0], bucket)
                if in_hits:
                    for _ret in series_results.values():
                        yield _ret
                else:
                    yield _s
            else:
                # 没有到达时序边界，向下还有一层，但需要记录时间节点
                for bucket in groupby_result.get(this_tagname, {}).get('buckets', []):
                    _ts = bucket['key']
                    for ret in ResponseParser._walk_through_bucket(
                            bucket, next_layer, base_series, series_results, ts=_ts, in_hits=in_hits):
                        yield ret
        elif this_tagname == 'metric':
            # metric
            for bucket in groupby_result.get(this_tagname, {}).get('buckets', []):
                metric_value = bucket['key']
                _s = base_series.add_copy('metric', metric_value)
                for ret in ResponseParser._walk_through_bucket(
                        bucket, next_layer, _s, series_results, ts=ts, in_hits=in_hits):
                    yield ret
        else:
            # tagkey
            if isinstance(this_tagname, (list, tuple)):
                # 到达了统计边界，获取多个数据点
                # 生成时间
                if ts:
                    _ts = ts
                else:
                    _ts = dt.now().timestamp() * 1000
                # 检查是否存在series
                if base_series.name in series_results:
                    # 已有的series_name，直接使用
                    _s = series_results[base_series.name]
                else:
                    # 否则新建一个以后添加
                    _s = base_series.copy()
                    series_results[base_series.name] = _s
                if in_hits:
                    ResponseParser._add_datapoint_in_hits(series_results, _ts, this_tagname, groupby_result)
                    for _ret in series_results.values():
                        yield _ret
                else:
                    ResponseParser._add_datapoint(_s, _ts, this_tagname, groupby_result)
                    yield _s
            else:
                # 还可以往下深入探索
                for bucket in groupby_result.get(this_tagname, {}).get('buckets', []):
                    this_tagvalue = bucket['key']
                    _s = base_series.add_copy(this_tagname, this_tagvalue)
                    for ret in ResponseParser._walk_through_bucket(
                            bucket, next_layer, _s, series_results, ts=ts, in_hits=in_hits):
                        yield ret

    @classmethod
    def _add_datapoint_in_hits(
            cls, series: Dict[str, Series], ts: Union[int, float, str], field_name: Union[List[str], Tuple[str], str],
            result_bucket: dict):
        """
        **将数据节点从es的bucket中抽取放入Series数据结构当中**

        :param series: 用于存放解析得到的数据的数据队列结构
        :type series: Series
        :param ts: 时间信息
        :type ts: Union[int, float, str]
        :param field_name: 数据字段的获取路径(数组方式传入)/名字(字符串方式传入)
        :type field_name: Union[List[str], Tuple[str], str]
        :param result_bucket: 数据字段所在的ES结果bucket
        :type result_bucket: dict
        :return: 无
        """
        if isinstance(field_name, (list, tuple)):
            # 多个运算结果
            for field_path in field_name:
                _cur = result_bucket
                if isinstance(field_path, (list, tuple)):
                    _field_name = field_path[0]
                    for _path in field_path:
                        _cur = _cur.get(_path, cls._DEFAULT_VALUE)
                else:
                    _field_name = field_path
                    _cur = result_bucket.get(field_path, cls._DEFAULT_VALUE)
                ResponseParser._walk_through_hits(_cur['hits']['hits'], series=series, ts=ts)
        else:
            ResponseParser._walk_through_hits(result_bucket['hits']['hits'], ts=ts)

    @staticmethod
    def _walk_through_hits(
            query_result: List[dict], json_loads: Union[List[str], None] = None,
            series: Union[Dict[str, Series], None] = None, ts: Union[int, float, str, None] = None) -> List[Series]:
        """
        **返回结构化查询数据**
        :param query_result: 查询结果
        :type query_result: List[dict]
        :param json_loads: 需要使用json序列化的字段列表
        :type json_loads: Union[List[str], None]
        :return:
        """
        s_dict = series or {}
        for _res in query_result:
            for _s in ResponseParser._parse_es_data(_res, json_loads=json_loads, ts=ts):
                series = s_dict.get(_s.name, Series(_s.name, legends=_s.legends))
                series.add_datapoint(*_s.data)
                s_dict[_s.name] = series
        return list(s_dict.values())

    @staticmethod
    def _parse_es_data(
            res: dict, json_loads: Union[List[str], None] = None, ts: Union[int, float, str, None] = None,
            series_name_pattern: str = 'query#{metric}#{tags}#{field}') -> Iterator[SingleSeries]:
        """
        **从es查询返回结果中抽取有效数据格式化成时序数据格式**
        :param res:
        :param json_loads:
        :param ts:
        :type ts: 给定时间格式
        :param series_name_pattern:
        :type series_name_pattern:
        :return:
        :rtype Iterator[SingleSeries]
        """
        _source = res['_source']
        if 'ts' in _source:
            _ts = _source['ts']
        else:
            _ts = res['fields'].pop('ts', [ts])[0]
        if 'metric' in _source:
            _metric = _source['metric']
        else:
            _metric = res['fields'].pop('metric')[0]
        tags_arr = []
        legend_dict = {
            'tag': _source.pop('tag', {})
        }
        for key in sorted(legend_dict['tag'].keys()):
            val = legend_dict['tag'][key]
            tags_arr.append('{}={}'.format(key, val))
        legend_dict['metric'] = _metric
        tags = '#'.join(tags_arr)
        script_fields = {
            field_name: field_value[0] for field_name, field_value in res.get('fields', {}).items()
        }
        fields = _source.get('field', {})
        if json_loads:
            for key in json_loads:
                value = fields.pop(key, None)
                if value:
                    fields.update(json.loads(value))
        fields.update(script_fields)
        for field_name, field_value in fields.items():
            s_name = series_name_pattern.format(metric=_metric, tags=tags, field=field_name)
            legend_dict['field'] = field_name
            _s = SingleSeries(s_name, field_value, _ts, legend_dict)
            yield _s

    @staticmethod
    def _iter_through_hits(
            query_result: List[dict], json_loads: Union[List[str], None] = None,
            ts: Union[int, float, str, None] = None) -> Iterator[SingleSeries]:
        """
        **迭代器方式返回结构化查询数据**

        :param query_result: 查询结果
        :type query_result: List[dict]
        :param json_loads: 需要使用json序列化的字段列表
        :type json_loads: Union[List[str], None]
        :param ts: 给定时间
        :type ts: Union[int, float, str, None]
        :return:
        :rtype: Iterator[SingleSeries]
        """
        for _res in query_result:
            for _s in ResponseParser._parse_es_data(_res, json_loads=json_loads, ts=ts):
                yield _s

    @staticmethod
    @deprecated(version='0.0.6', reason="This method is deprecated")
    def _walk_iter_bucket(groupby_result: dict, result_path: Union[tuple, list]) -> dict:
        if len(result_path) == 1:
            # 最底层
            field_name = result_path[0]
            datapoint = None
            if isinstance(field_name, (list, tuple)):
                # 多个运算结果
                for field_path in field_name:
                    _cur = groupby_result
                    if isinstance(field_path, (list, tuple)):
                        _field_name = field_path[0]
                        for _path in field_path:
                            _cur = _cur[_path]
                    else:
                        _field_name = field_path
                        _cur = groupby_result[field_path]
                    if datapoint is None:
                        datapoint = _cur
                        datapoint['field'] = {
                            _field_name: datapoint.pop('value')
                        }
                    else:
                        datapoint['field'][_field_name] = _cur['value']
            else:
                datapoint = groupby_result[field_name]
                datapoint['field'] = {
                    field_name: datapoint.pop('value')
                }
            datapoint['tag'] = {}
            datapoint['ts'] = 0
            yield datapoint
        else:
            this_tagname = result_path[0]
            next_layer = result_path[1:]
            if this_tagname == 'ts':
                add_tag = partial(ResponseParser._add_ts_metric, tag_name=this_tagname)
            elif this_tagname == 'metric':
                add_tag = partial(ResponseParser._add_ts_metric, tag_name=this_tagname)
            else:
                add_tag = partial(ResponseParser._add_tag, tag_name=this_tagname.split('.')[1])
            for bucket in groupby_result[this_tagname]['buckets']:
                this_tagvalue = bucket['key']
                for datapoint in ResponseParser._walk_iter_bucket(bucket, next_layer):
                    add_tag(tag_value=this_tagvalue, datapoint=datapoint)
                    yield datapoint

    @staticmethod
    @deprecated(version='0.0.6', reason="This method is deprecated")
    def _listmydoc(aggr, ignore_keys=('key_as_string',)) -> list:
        """

        :param aggr:
        :param ignore_keys:
        :return:
        """
        rets = []
        for _keyname in aggr.keys():
            for bucket in aggr[_keyname]['buckets']:
                _keyval = bucket.pop('key')
                _fieldval = bucket.pop('doc_count')
                for key in ignore_keys:
                    bucket.pop(key, None)
                if not bucket or ResponseParser._is_value_bucket(bucket):
                    # final bucket
                    if ResponseParser._is_value_bucket(bucket):
                        # bucket like:
                        # {"_fieldname": {"value": "_fieldval"}}
                        _fieldname = list(bucket.keys())[0]
                        _fieldval = bucket.pop(_fieldname)['value']
                        bucket[_fieldname] = _fieldval
                    else:
                        bucket['count'] = _fieldval
                    bucket[_keyname] = _keyval
                    rets.append(bucket)
                else:
                    # maybe son bucket
                    son_aggr = {}
                    _mid = {
                        _keyname: _keyval
                    }
                    for son_k in list(bucket.keys()):
                        if isinstance(bucket[son_k], dict) and 'buckets' in bucket[son_k]:
                            # son bucket
                            son_aggr[son_k] = bucket.pop(son_k)
                        elif isinstance(bucket[son_k], dict) and 'value' in bucket[son_k]:
                            # metric bucket
                            # {"_fieldname": {"value": "_fieldval"}}
                            ret = bucket.pop(son_k)
                            # ret[_keyname] = _keyval
                            _mid[son_k] = ret.pop('value')
                            # rets.append(ret)
                        else:
                            del bucket[son_k]
                    if son_aggr:
                        for son_doc in ResponseParser._listmydoc(son_aggr):
                            son_doc.update(_mid)
                            rets.append(son_doc)
                    else:
                        rets.append(_mid)
        return rets

    @staticmethod
    @deprecated(version='0.0.6', reason="This method is deprecated")
    def _is_value_bucket(bucket):
        """
        Check if bucket is value bucket like:
        {
            "summary": {
                "value": 2323
            }
        }
        :param bucket:
        :return:
        """
        if len(bucket) == 1:
            val_bucket = bucket[list(bucket.keys())[0]]
            if 'value' in val_bucket and len(val_bucket) == 1:
                return True
            else:
                return False
        else:
            return False

    @staticmethod
    def iterfresp(
            query: ElasticsearchQuery, response: dict, json_loads: Union[List[str], None] = None) -> Iterator[
        SingleSeries]:
        """
        **Iter SingleSeries From Elasticsearch Search API Response**

        This function allows users to iter single series type response from the Elasticsearch scroll API return object.

        :param query: 本次查询结果的查询对象
        :type query: ElasticsearchQuery
        :param response: Elasticsearch的search的API返回结果
        :type response: dict
        :param json_loads: 需要json反序列化的fields字段列表
        :type json_loads: List[str]
        :return: 返回时序格式结构对象
        :rtype: Iterator[SingleSeries]

        - Example::

            terms = TestParser().test_03_term_filter()
            script_fields = TestParser().test_04_field_script_02()
            return_size = 6000
            es_query = QueryParser.where_filters(
                ['ms_gb_distinct', 'cpu'], terms, index='tsdb_alias', script_fields=script_fields, offset=2,
                size=return_size)
            self.assertEqual(es_query.body.get('aggs', None), None)
            self.assertEqual(es_query.body['size'], 5000)
            # print(json.dumps(es_query.body))
            cli = SearchClient(**es_conf.es_conf)
            a = []
            query_size = 30000
            for _s in cli.scroll(es_query, query_size=query_size, fetch_size=5000, sync=True):
                a.append(_s)
            self.assertEqual(es_query.body['size'], 5000)
            self.assertEqual(len(a), query_size)
            print(a[0].data)pyesl.response.SingleSeries.data:
            print(a[-1].data)
        """

        if response['_shards'][
            'failed'] and query.aggregations and query.aggregations.topk_type != TopKType.TOPK_FIELD.value:
            # failed and handler error
            raise SearchFailedError(u'Search Failed Error: {}'.format(response['_shards']['failures'][0]))
        else:
            # 一般查询
            for _s in ResponseParser._iter_through_hits(
                    response.get('hits', {}).get('hits', []), json_loads=json_loads):
                yield _s
