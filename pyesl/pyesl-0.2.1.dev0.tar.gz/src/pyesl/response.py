# -*- coding: utf-8 -*-
from __future__ import annotations

import heapq
from collections import defaultdict, OrderedDict
from copy import deepcopy
from typing import Union, List, Dict, Tuple, Any

from dateutil.parser import parse


class DataPoint(object):
    def __init__(self, ts: Union[float, int, str], value: float):
        if isinstance(ts, str):
            self._ts = parse(ts).timestamp() * 1000
        elif isinstance(ts, float):
            point_size = len(str(ts).split('.')[1])
            self._ts = int(ts * (10 ** point_size))
        else:
            self._ts = ts
        # 1574925204228
        ts_str = str(self._ts)
        if len(ts_str) > 13:
            self._ts = int(str(ts_str)[:13])
        elif len(ts_str) < 13:
            self._ts = int(ts_str.ljust(13, '0'))
        self._val = float(value)
        self._datapoint = (self._val, self._ts)

    @property
    def ts(self) -> int:
        """
        **Millseconds since 1970**
        :return: Millseconds
        :rtype: int
        """
        return self._ts

    @property
    def value(self) -> float:
        return self._val

    @property
    def datapoint(self) -> Tuple[float, int]:
        return self._datapoint


class Legend(dict):
    """
    **Legend of Series**

    - Example::

        _legend = Legend(metric='ms_gb_distinct', tag={'host':'192.168.127.1', 'url':'www.baidu.com'}, field='count')

    :param kwargs:
    :type kwargs: Any
    """

    def __init__(self, **kwargs: Any):
        kwargs['tag'] = kwargs.get("tag", {})
        super().__init__(**kwargs)

    def set_tag(self, tag_name: str, tag_val: str):
        self['tag'][tag_name] = tag_val

    def set_metric(self, metric_val: str):
        self['metric'] = metric_val

    def set_field(self, field_name: str):
        self['field'] = field_name


class Series(object):
    """
    **Series structure of ts datapoint**

    :param name:
    :param legends:
    :param data:
    """

    def __init__(
            self, name: str, legends: Dict[str, Union[Dict[str, str], str]] = None, data: List[DataPoint] = None,
            topk_filter: TopKFilter = None):

        self._name = name
        self._legends = Legend(**legends) if legends else Legend()
        self._data = OrderedDict()
        for _d in data or []:
            self._data[_d.ts] = _d
        self._topk_filter = topk_filter

    def __lt__(self, other):
        return self.name < other.name

    @property
    def name(self) -> str:
        return self._name

    @property
    def legends(self) -> Legend:
        return self._legends

    @property
    def data(self) -> List[Tuple[float, int]]:
        """
        **Return list of data point with data type as a tuple of (value, ts)**
        :return:
        :rtype List[Tuple[float, int]]
        """
        return [_data.datapoint for _data in self._data.values()]

    @property
    def size(self) -> int:
        return len(self._data)

    def add_legend(self, tagname: str, tagvalue: str):
        """
        **Add legend tag name and tag value**

        if '.' in tagname, like 'tag.field.name', legend will be {'tag': {'field': {'name': 'value'}}}

        :param tagname: tag name
        :type tagname: str
        :param tagvalue: tag value
        :type tagvalue: str
        :return:
        """
        if "." not in tagname:
            self._legends[tagname] = tagvalue
        else:
            cur = self._legends
            tag_arr = tagname.split('.')
            for _tag in tag_arr[:-1]:
                if _tag in cur:
                    cur = cur[_tag]
                else:
                    cur[_tag] = {}
                    cur = cur[_tag]
            cur[tag_arr[-1]] = tagvalue

    def add_datapoint(self, value: float, ts: Union[int, float, str]) -> DataPoint:
        if self._topk_filter:
            _d = self._topk_filter.add_datapoint(self, value, ts)
            return _d
        else:
            _d = DataPoint(ts, value)
            self._data[_d.ts] = _d
            return _d

    @staticmethod
    def new_datapoint(value: float, ts: Union[int, float, str]) -> DataPoint:
        return DataPoint(ts, value)

    def set_datapoint(self, datapoint: DataPoint):
        self._data[datapoint.ts] = datapoint

    def pop_datapoint(self, ts: int) -> DataPoint:
        return self._data.pop(ts)

    def add_copy(self, tag_name: str, tag_value: str) -> Series:
        new_s = Series(
            self._new_series_name(tag_name, tag_value), deepcopy(self._legends), topk_filter=self._topk_filter)
        new_s.add_legend(tag_name, tag_value)
        return new_s

    def copy(self) -> Series:
        new_s = Series(
            self.name, deepcopy(self._legends), topk_filter=self._topk_filter)
        return new_s

    def _new_series_name(self, tagname: str, tagvalue: str) -> str:
        return '{}#{}={}'.format(self._name, tagname, tagvalue)


class TsdbResponse(object):
    def __init__(self, series: List[Series], response: dict):
        self._series = series
        self._response = response

    @property
    def series(self) -> List[Series]:
        return self._series

    @property
    def response(self) -> dict:
        return self._response


class TopKFilter(object):
    def __init__(self, topk: int = 2):
        self._topk = topk
        self._ts_series: Dict[int, List[Tuple[float, Series]]] = defaultdict(list)

    def add_datapoint(self, series: Series, value: float, ts: Union[int, float, str]) -> DataPoint:
        _d = series.new_datapoint(value, ts)
        if _d.ts not in self._ts_series:
            series.set_datapoint(_d)
            self._ts_series[_d.ts].append((_d.value, series))
            return _d
        else:
            _topk_series = self._ts_series[_d.ts]
            if len(_topk_series) < self._topk:
                series.set_datapoint(_d)
                self._ts_series[_d.ts].append((_d.value, series))
                return _d
            else:
                series.set_datapoint(_d)
                _, _s = heapq.heappushpop(_topk_series, (_d.value, series))
                return _s.pop_datapoint(_d.ts)


class SingleSeries(object):
    """
    **Series structure of ts datapoint**

    :param value:
    :param ts:
    :param legends:
    """

    def __init__(
            self, name: str, value: float, ts: Union[int, float, str],
            legends: Dict[str, Union[Dict[str, str], str]] = None):
        self._name = name
        self._legends = Legend(**legends) if legends else Legend()
        self._data = DataPoint(ts=ts, value=value)

    @property
    def name(self) -> str:
        return self._name

    @property
    def legends(self) -> Legend:
        return self._legends

    @property
    def data(self) -> Tuple[float, int]:
        """
        **Return data point with data type as a tuple of (value, ts)**
        :return:
        :rtype Tuple[float, int]

        """
        return self._data.datapoint
