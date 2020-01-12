# -*- coding: utf-8 -*-
from __future__ import annotations
import uuid
from abc import ABC
from collections import OrderedDict
from enum import Enum
from typing import List, Dict, Union, Any

from pyesl.errors import ParamError, QueryBodyError
from pyesl.query import Terms


class AggsBase(ABC):
    def __init__(self, body: dict, name: str):
        self._body = body
        self._name = self._format_name(name)
        self._result_path = []

    @property
    def body(self) -> dict:
        return self._body

    @property
    def name(self) -> str:
        return self._name

    def _format_name(self, value: str) -> str:
        return value.replace('[', '(').replace(']', ')').replace('>', '=')

    @property
    def result_path(self) -> tuple:
        return tuple(self._result_path)


class Groupby(AggsBase):
    """
    Group by condition object of tags eg:

    1. sql like: group by keyA
    2. pql like: by (keyA)
    """

    BODY_TEMPLATE = {
        'agg_name': {
            'terms': {
                'field': 'key',
                'size': 1024,
                'param_name1': 'param_val1'
            }
        }
    }

    def __init__(self, field: str = 'key', name: str = None, size: int = 1024, **params):
        self._field = field
        _name = self._format_name(name or field)
        _body = {
            _name: {
                'terms': params
            }
        }
        _body[_name]['terms']['field'] = field
        _body[_name]['terms']['size'] = size
        super().__init__(_body, _name)

    @property
    def field(self):
        return self._field


class Step(AggsBase):
    """
    Group by condition object of time steps eg:

    1. sql like: group by DATE_FORMAT(ts, '%Y-%d-%h %H')
    2. pql like: step_s = 3600
    """

    BODY_TEMPLATE = {
        'agg_name': {
            'date_histogram': {
                'field': 'key',
                'interval': '3600s',  # < 7.4 "interval"
                'size': 4096
            }
        }
    }

    def __init__(self, field: str = 'ts', name: str = 'ts', step_s=3600, **params):
        self._field = field
        _name = self._format_name(name or field)
        self._step_s = step_s
        _body = {
            _name: {
                'date_histogram': params
            }
        }
        _body[_name]['date_histogram']['field'] = field
        _body[_name]['date_histogram']['interval'] = '{}s'.format(step_s)
        super().__init__(_body, _name)

    @property
    def field(self):
        return self._field

    @property
    def step_s(self):
        return self._step_s


class Calculation(AggsBase):
    """
    **Base Calculation of field**

    :param fields: 用于计算的字段名字和别名
    :type fields: Dict[str, str]
    :param expr: 用于字段之间计算的表达式
    :type expr: Union[str, None]
    :param func: 计算字段的算子,例如('sum', 'avg', 'max', 'min', 'value_count')
    :type func: str
    :param field_format: 提取字段使用的格式
    :type field_format: str
    :param expr_params: 用于字段之间计算的表达式使用到的参数
    :type expr_params: Union[Dict[str, float], None]
    :param param_format: 提取参数使用的格式
    :type param_format: str
    :param offset:
    :type offset:
    :param size:
    :type size:
    :param order:
    :type order:
    :param params: 其余参数
    :type params: dict
    """

    _VALID_FUNC = ('sum', 'avg', 'max', 'min', 'value_count', 'top_hits', 'bucket_script')
    _FUNC_TYPE = ('aggs', 'topk')

    def __init__(
            self, fields: Dict[str, str], expr: Union[str, None] = None, func: str = 'sum',
            field_format: str = "doc['field.{field}'].value",
            expr_params: Union[Dict[str, float], None] = None,
            param_format: str = "params.{param}",
            offset: int = 0, size: int = 1, order: str = 'desc',
            **params: Any):
        if func not in self._VALID_FUNC:
            raise ParamError('func: {} is not in {}'.format(func, self._VALID_FUNC))
        self._func = func
        self._fields = fields
        self._is_script = True if expr else False
        self._expr = expr
        if len(fields) > 1 and not self._is_script:
            raise ParamError('To use script when more than one field: {}'.format(fields))
        self._expr_formatted = None
        self._fields_formatted = dict()
        for key, field in self._fields.items():
            self._fields_formatted[key] = field_format.format(field=field)
        _name = str(uuid.uuid1())
        if self._is_script:
            self._expr_params_formatted = {}
            self._expr_params_value = {}
            if expr_params:
                id_gap = 0
                for idx, org_param_name in enumerate(sorted(expr_params.keys()), 1):
                    param_value = expr_params[org_param_name]
                    # 统一化处理，避免过多的script语句产生
                    new_param_name = 'param{id}'.format(id=idx + id_gap)
                    while new_param_name in self._fields_formatted or new_param_name in self._expr_params_value:
                        id_gap += 1
                        new_param_name = 'param{id}'.format(id=idx + id_gap)
                    self._expr_params_formatted[org_param_name] = param_format.format(param=new_param_name)
                    self._expr_params_value[new_param_name] = param_value
                self._expr_formatted = self._expr.format(**self._fields_formatted, **self._expr_params_formatted)

            else:
                self._expr_formatted = self._expr.format(**self._fields_formatted)
        else:
            self._expr_params_formatted = None
            self._expr_params_value = None
            self._expr_formatted = None
        if func == 'top_hits':
            self._func_type = FuncType.FUNC_TOPK.value
            _body = self._init_topk(
                name=_name, offset=offset, size=size, order=order, **params)
        else:
            self._func_type = FuncType.FUNC_AGG
            _body = self._init_aggs(name=_name, **params)
        super().__init__(_body, _name)
        self._result_path.append(_name)

    def _init_aggs(
            self, name: str, **params: Any):
        _body = {
            name: {
                self._func: params
            }
        }
        if not self._is_script:
            if self._fields_formatted:
                _body[name][self._func]['field'] = list(self._fields_formatted.values())[0]
            else:
                pass
        else:
            _body[name][self._func]['script'] = {
                'source': self._expr_formatted,
                'params': self._expr_params_value
            }
        return _body

    def _init_topk(
            self, name: str, offset: int = 0, size: int = 1, order: str = 'desc',
            **params: Any):
        params['from'] = offset
        params['size'] = size
        params['script_fields'] = {
            'ts': {
                "script": {
                    "source": "doc['ts'].value"
                }
            },
            'metric': {
                "script": {
                    "source": "doc['metric'].value"
                }
            },
        }
        params['_source'] = {
            'includes': ['tag'],
            'excludes': ['metric', 'ts', 'field', 'meta']
        }
        _body = {
            name: {
                self._func: params
            }
        }
        if self._is_script:
            _body[name][self._func]['sort'] = [{
                "_script": {
                    "type": "number",
                    "script": {
                        "inline": self._expr_formatted,
                        "params": self._expr_params_value
                    },
                    "order": order
                }
            }]
            _body[name][self._func]['script_fields'][self._expr_formatted] = {
                "script": {
                    "source": self._expr_formatted,
                    "params": self._expr_params_value
                }
            }
        else:
            _body[name][self._func]['sort'] = []
            for _field_key, _field_name in self._fields_formatted.items():
                _body[name][self._func]['sort'].append({
                    _field_name: {
                        'order': order
                    }
                })
                _body[name][self._func]['script_fields'][_field_name] = {
                    "script": {
                        "source": 'doc["{}"].value'.format(_field_name)
                    }
                }
        return _body

    @property
    def is_script(self) -> bool:
        return self._is_script

    @property
    def func_type(self) -> FuncType:
        return self._func_type


class FieldCalculation(Calculation):
    """
    **Calculation of field**

    :param fields: 用于计算的字段名字和别名
    :type fields: Dict[str, str]
    :param expr: 用于字段之间计算的表达式
    :type expr: Union[str, None]
    :param func: 计算字段的算子,例如('sum', 'avg', 'max', 'min', 'value_count')
    :type func: str
    :param field_format: 提取字段使用的格式
    :type field_format: str
    :param expr_params: 用于字段之间计算的表达式使用到的参数
    :type expr_params: Union[Dict[str, float], None]
    :param param_format: 提取参数使用的格式
    :type param_format: str
    :param params: 其余参数
    :type params: Any

    - For case::

        1. sql like: sum(a)
        2. pql like: sum_over_time(abc.value)
        3. aql like: sum(abc.field1 + abc.field2 / 2)

    """

    _BODY_TEMPLATE = {
        'cal_name': {
            'func': {
                'field': 'field_name',
                'param_name1': 'param_val1'
            }
        }
    }

    _VALID_FUNC = ('sum', 'avg', 'max', 'min', 'value_count')

    def __init__(
            self, fields: Dict[str, str], expr: Union[str, None] = None, func: str = 'sum',
            field_format: str = "doc['field.{field}'].value",
            expr_params: Union[Dict[str, float], None] = None,
            param_format: str = "params.{param}",
            **params: Any):
        super().__init__(
            fields=fields, expr=expr, func=func, field_format=field_format, expr_params=expr_params,
            param_format=param_format, **params)


class ResultCalculation(FieldCalculation):
    """
    **Calculation of FieldCalculation or QueryCalculation**

    :param calculation: 算子对象列表
    :type calculation: Dict[str, Calculation]
    :param expr: 算子表达式
    :type expr: str
    :param expr_params: 算子参数
    :type expr_params: Union[Dict[str, float], None]
    :param params: 剩余的参数
    :type params: dict

    - For case::

        1. sql like: sum(abc.field1 + abc.field2, a='b', b='c')
        2. pql like: sum_over_time(abc.value) + sum_over_time(abc.value)
        3. aql like: sum(abc.field1 + abc.field2 / 2, a='b', b='c') / sum(abc.field1 + abc.field2 / 2, a='b', b='c')
            group by a, b, c within

    """

    _BODY_TEMPLATE = {
        "cal_name": {
            "bucket_script": {
                "buckets_path": {
                    "name1": "_ignore_agg_name1>cal_name",
                    "name2": "_ignore_agg_name2"
                },
                "script": {
                    "source": "params.name1 / params.name2 + params.param1 / params.param2",
                    "params": {
                        "param1": 2,
                        "param2": 10
                    }
                },
            }
        },
        '_ignore_agg_name1': {
            "filter": {
                "bool": {
                    "filter": [
                        {
                            "term": {
                                "metric": "cpu"
                            }
                        }
                    ],
                    "must_not": [
                        {
                            "term": {
                                "tag.gameid": "g18"
                            }
                        }
                    ]
                }
            },
            "aggs": {
                'cal_name': {
                    'func': {
                        'field': 'field_name',
                        'param_name1': 'param_val1'
                    }
                }
            }
        },
        '_ignore_agg_name2': {
            'func': {
                'field': 'field_name',
                'param_name1': 'param_val1'
            }
        }
    }

    _VALID_FUNC = ('bucket_script',)

    def __init__(
            self, calculation: Dict[str, Calculation], expr: str,
            expr_params: Union[Dict[str, float], None] = None, **params):
        self._buckets_path = {}
        self._calname_formatted = {}
        for name, _cal in calculation.items():
            if isinstance(_cal, FieldTopKSort) or _cal.func_type == FuncType.FUNC_TOPK.value:
                raise ParamError(u'Topk calculation can not be used to script')
            self._buckets_path[name] = '>'.join(_cal.result_path)
            self._calname_formatted[name] = 'params.{}'.format(name)
        self._expr = expr
        super().__init__(
            fields=self._calname_formatted, expr=expr, func='bucket_script', field_format='{field}',
            buckets_path=self._buckets_path, expr_params=expr_params, **params)


class QueryCalculation(Calculation):
    """
    **Calculation with query terms**


    :param fields: 用于计算的字段名字和别名
    :param expr: 用于字段之间计算的表达式
    :type expr: Union[str, None]
    :param func: 计算字段的算子,例如('sum', 'avg', 'max', 'min', 'value_count')
    :type func: str
    :param field_format: 提取字段使用的格式
    :type field_format: str
    :param expr_params: 用于字段之间计算的表达式使用到的参数
    :type expr_params: Union[Dict[str, float], None]
    :param param_format: 提取参数使用的格式
    :type param_format: str
    :param params: 其余参数
    :type params: dict

    - For case::

        1. pql like: sum_over_time(abc.value, a='b', c='d', e='a') by (a, b, c)
        2. aql like: sum(abc.field1 + abc.field2 / 2, a='bc', c='a', fas='fs') groupby (c, d, e, f)

    """

    _BODY_TEMPLATE = {
        'agg_name': {
            "filter": {
                "bool": {
                    "filter": [
                        {
                            "term": {
                                "metric": "cpu"
                            }
                        }
                    ],
                    "must_not": [
                        {
                            "term": {
                                "tag.gameid": "g18"
                            }
                        }
                    ]
                }
            },
            "aggs": {
                'cal_name': {
                    'func': {
                        'field': 'field_name',
                        'param_name1': 'param_val1'
                    }
                }
            }
        }
    }

    def __init__(
            self, terms: Terms, fields: dict, expr: str = None, func: str = 'sum',
            field_format: str = "doc['field.{field}'].value",
            expr_params: Union[Dict[str, float], None] = None, param_format: str = "params.{param}",
            offset: int = 0, size: int = 1, order: str = 'desc', **params):
        if not expr:
            field_format = 'field.{field}'
        super().__init__(
            fields, expr=expr, func=func, field_format=field_format, expr_params=expr_params, param_format=param_format,
            offset=offset, size=size, order=order,
            **params)
        self._name = 'filter_{}'.format(self._name)
        self._result_path.insert(0, self._name)
        _body = {
            self._name: {
                'aggs': self._body
            }

        }
        _body[self._name]['filter'] = terms.body
        self._body = _body
        self._terms = terms

    @property
    def terms(self) -> Terms:
        return self._terms


class Calculations(AggsBase):
    """
    **Calculations combination of all kind of calculations**

    :param calculations: 需要组合使用的聚合计算
    :type calculations: Calculation
    :param return_calculation_name: 最终返回结果的聚合方法名,多个聚合运算必须指定其中一个作为最终唯一返回结果
    :type return_calculation_name: Union[str, None]

    """

    _BODY_TEMPLATE = {
        'aggs': {
            'agg_name1': {
                "filter": {
                    "bool": {
                        "filter": [
                            {
                                "term": {
                                    "metric": "cpu"
                                }
                            }
                        ],
                        "must_not": [
                            {
                                "term": {
                                    "tag.gameid": "g18"
                                }
                            }
                        ]
                    }
                },
                "aggs": {
                    'cal_name': {
                        'func': {
                            'field': 'field_name',
                            'param_name1': 'param_val1'
                        }
                    }
                }
            },
            'agg_name2': {
                "filter": {
                    "bool": {
                        "filter": [
                            {
                                "term": {
                                    "metric": "cpu"
                                }
                            }
                        ],
                        "must_not": [
                            {
                                "term": {
                                    "tag.gameid": "g18"
                                }
                            }
                        ]
                    }
                },
                "aggs": {
                    'cal_name': {
                        'func': {
                            'field': 'field_name',
                            'param_name1': 'param_val1'
                        }
                    }
                }
            }
        }
    }

    def __init__(self, *calculations: Calculation, return_calculation_name: Union[str, None] = None):

        self._should_filters = []
        self._calculations = {}
        _body = {
            'aggs': {

            }
        }
        _cal_paths = []
        _names = []
        if len(calculations) == 1:
            return_calculation_name = calculations[0].name
        elif return_calculation_name is None:
            raise QueryBodyError('Choose One of Calculation Result to Return: {}'.format(
                [_cal.name for _cal in calculations]))
        else:
            # calculation name supported
            pass
        self._result_calculation = None
        for _cal in calculations:
            if isinstance(_cal, QueryCalculation):
                if _cal.terms:
                    self._should_filters.append(_cal.terms)
            _body['aggs'][_cal.name] = _cal.body[_cal.name]
            _names.append(_cal.name)
            if _cal.name == return_calculation_name:
                _cal_paths.append(_cal.result_path)
                self._result_calculation = _cal
            else:
                pass
            self._calculations[_cal.name] = _cal
        if self._result_calculation is None:
            raise QueryBodyError('Choose One of Calculation Result to Return: {}'.format(
                [_cal.name for _cal in calculations]))
        super().__init__(_body, 'cal_{}'.format('#'.join(_names)))
        self._result_path = [_cal_paths]

    @property
    def should_filters(self) -> List[Terms]:
        return self._should_filters

    def calculation_names(self) -> List[str]:
        return list(self._calculations.keys())

    def get_calculation(self, name: str) -> Calculation:
        return self._calculations[name]

    def list_calculations(self) -> List[Calculation]:
        return list(self._calculations.values())

    @property
    def result_calculation(self) -> Union[Calculation, None]:
        return self._result_calculation


class TopKType(Enum):
    NONE = -1  # 没有topk
    TOPK_GROUPBY = 1  # 有groupby条件的简单聚合计算的topk
    TOPK_MOV = 2  # 滑动窗口的topk
    TOPK_FIELD = 3  # 没有groupby条件只有within的topk


class Aggregations(AggsBase):
    """
    **Aggregation combination of calculation(with filter), group by**

    :param calculations: Calculations structure
    :type calculations: Calculations
    :param groupby: Groupby structure list
    :type groupby: Union[List[Groupby], None]
    :param step: Step structure
    :type step: Union[Step, None]
    :param topk: Topk filter, if valid, last bucket should be terms bucket
    :type topk: Union[int, None]
    :param topk_type: if topk sort in es or not, if True agg by ts first then temrs
    :type topk_type: bool

    - For case::

        1. pql like: sum(a, b, c) by (A, B, C) interval = 3600
        2. aql like: sum(cpu.a + cpu.b, kk=1 and bb=1) group by 3600 within 10s

    """

    _BODY_TEMPLATE = {
        'aggs': {
            'agg_key': {
                'term': {
                    'field': 'key',
                    'size': 1024
                },
                'aggs': {
                    'agg_ts': {
                        'date_histogram': {
                            'field': 'ts',
                            'interval': '3600s',  # < 7.4 "interval"
                            'size': 4096
                        },
                        "aggs": {
                            'agg_name': {
                                "filter": {
                                    "bool": {
                                        "must_not": [
                                            {
                                                "term": {
                                                    "tag.gameid": "g18"
                                                }
                                            }
                                        ]
                                    }
                                },
                                'aggs': {
                                    'cal_field': {
                                        'sum': 'field.field_name'
                                    }
                                }
                            }

                        }
                    }
                }
            }
        }
    }

    def __init__(
            self, calculations: Calculations, groupby: Union[List[Groupby], None] = None,
            step: Union[Step, None] = None, topk: Union[int, None] = None, topk_type: TopKType = TopKType.NONE.value):
        _groupby = OrderedDict()
        self._step = step
        self._topk = topk
        self._topk_type = topk_type
        _body = {}
        _cu = _body
        _result_path = []
        # deal with topk bucket situation
        if self._topk is not None and self._topk > 0:
            if self._topk_type == TopKType.TOPK_GROUPBY.value:
                # 普通groupby聚合计算的TOPK
                groupby_count = len(groupby)
                if groupby_count == 0:
                    # such as aql like topk(5, sum(field.field_value))
                    raise ParamError('topk({}) aggregation with no groupby'.format(topk))
                else:
                    before_step_groupbys = None
                    after_step_groupby = groupby
            elif self._topk_type == TopKType.TOPK_FIELD.value:
                # 取每个时间段间隔的TOPK值
                # such as aql like topk(5, field.field_value) within 1m
                if self._step is None:
                    raise ParamError('topk({}) select with no within'.format(topk))
                before_step_groupbys = None
                after_step_groupby = None
            elif self._topk_type == TopKType.TOPK_MOV.value:
                # 滑动窗口计算的TopK
                before_step_groupbys = groupby
                after_step_groupby = None
            else:
                raise ParamError('topk_type({}) error with topk({})'.format(self._topk_type, self._topk))
        else:
            # 普通聚合查询
            before_step_groupbys = groupby
            after_step_groupby = None
        self._groupby = groupby or []
        # before step agg
        if before_step_groupbys:
            for _g in before_step_groupbys:
                _groupby[_g.name] = _g
                _result_path.append(_g.name)
                _cu['aggs'] = _g.body
                _cu = _cu['aggs'][_g.name]
        else:
            pass
        if self._step:
            _cu['aggs'] = self._step.body
            _result_path.append(self._step.name)
            _cu = _cu['aggs'][self._step.name]
            _name = 'agg_{}_{}'.format('#'.join(_groupby.keys()), step.name)
        else:
            _name = 'agg_{}'.format('#'.join(_groupby.keys()))
        # after step agg
        if after_step_groupby:
            for _g in after_step_groupby:
                _groupby[_g.name] = _g
                _result_path.append(_g.name)
                _cu['aggs'] = _g.body
                _cu = _cu['aggs'][_g.name]
        else:
            pass
        super().__init__(_body, _name)
        _cu['aggs'] = calculations.body['aggs']
        _result_path.extend(calculations.result_path)

        self._step = step
        self._calculations = calculations
        self._result_path = _result_path

    @property
    def groupby(self) -> List[Groupby]:
        return self._groupby

    @property
    def step(self) -> Union[Step, None]:
        return self._step

    @property
    def calculations(self) -> Calculations:
        return self._calculations

    @property
    def topk(self) -> Union[int, None]:
        return self._topk if self._topk is not None and self._topk > 0 else None

    @property
    def topk_type(self) -> TopKType:
        return self._topk_type


class QueryCalculationFilter(Calculation):
    """
    **Result Filter of FieldCalculation or QueryCalculation**

    Filter for the calculation result

    - For case::

        sum(ms_gb_distinct.distinctcount)/avg(ms_gas2gb_distinct.count) groupby ip, gameid within 10m

        when sum(ms_gb_distinct.distinctcount) group by ip, gameid within 10m
        and avg(ms_gas2gb_distinct.count) group by ip, gameid within 10m's
        result vector of the same moment are like:

        {'sum_res': 10, 'gameid': 'yoyo', 'ip': 'myhost', 'ts': 10000}
        {'avg_res': 10, 'gameid': 'mama', 'ip': 'yourhost', 'ts': 10000}

        result of sum(ms_gb_distinct.distinctcount)/avg(ms_gas2gb_distinct.count) groupby ip, gameid within 10m
        should be filter out and not return as one of the calculation result, neither 0 or null

    - Example::

        sa = QueryParser.single_aggs({
            'ms_gb_distinct.distinctcount': 'ms_gb_distinct.distinctcount'},
            func='sum', metric='ms_gb_distinct')
        av = QueryParser.single_aggs({
            'ms_gas2gb_distinct.count': 'ms_gas2gb_distinct.count'},
            func='value_count', metric='ms_gas2gb_distinct')
        calculations = [sa, av]
        expr = ' && '.join(['params.{} > 0'.format(_single.name) for _single in calculations])
        calculation_value_extractor = {_cal.name: '{}._count'.format(_cal.name) for _cal in calculations}
        filter = QueryCalculationFilter(
            calculation=calculations, calculation_value_extractor=calculation_value_extractor, expr=expr)

    """

    _BODY_TEMPLATE = {
        "result_filter": {
            "bucket_selector": {
                "buckets_path": {
                    "my_var1": "_ignore_agg_name1._count",
                    "my_var2": "_ignore_agg_name1._count"
                },
                "script": "params.my_var1 > 0 && params.my_var2 > 0"
            }
        },
        '_ignore_agg_name1': {
            "filter": {
                "bool": {
                    "filter": [
                        {
                            "term": {
                                "metric": "cpu"
                            }
                        }
                    ],
                    "must_not": [
                        {
                            "term": {
                                "tag.gameid": "g18"
                            }
                        }
                    ]
                }
            },
            "aggs": {
                'cal_name': {
                    'func': {
                        'field': 'field_name',
                        'param_name1': 'param_val1'
                    }
                }
            }
        },
        '_ignore_agg_name2': {
            'func': {
                'field': 'field_name',
                'param_name1': 'param_val1'
            }
        }
    }

    _VALID_FUNC = ('bucket_selector',)

    def __init__(
            self, calculation: Dict[str, QueryCalculation], calculation_value_extractor: Dict[str, str], expr: str,
            **params):
        self._buckets_path = {}
        self._calname_formatted = {}
        for name, _cal in calculation.items():
            self._buckets_path[name] = calculation_value_extractor[name]
            self._calname_formatted[name] = 'params.{}'.format(name)
        self._expr = expr
        super().__init__(
            fields=self._calname_formatted, expr=expr, func='bucket_selector', field_format='{field}',
            buckets_path=self._buckets_path, **params)


class QueryCalculationSorter(Calculation):
    """
    **Result Sorter of FieldCalculation or QueryCalculation**

    Sorter for the calculation result

    :param calculation: 用于排序的统计算子聚合结构
    :type calculation: Dict[str, QueryCalculation]
    :param calculation_value_extractor: 统计算子结果的抽取方法
    :type calculation_value_extractor: Dict[str, str]
    :param calculation_order: 统计算子结果的排序方向
    :type calculation_order: Dict[str, str]
    :param offset: 从第几位开始排序
    :type offset: int
    :param size: topk
    :type size: int
    :param params: 其他参数
    :type params: Any

    - For case::

        * 1. topk(5, sum(ms_gb_distinct.distinctcount))
          return top 5 of sum value, total 5 points

        * 2. topk(5 sum(ms_gb_distinct.distinctcount) group by url, gameid, tag)
          return top 5 of sum value of group url, gameid, tag, total 5 * 3 points

        * 3. topk(5 sum(ms_gb_distinct.distinctcount) group by a, b, c within 1h))
          return top 5 of sum value of group url, gameid, tag and 1h ts bucket, total 5 * 3 * ts_bucket_count

    - Example::

        sa = QueryParser.single_aggs({
            'ms_gb_distinct.distinctcount': 'ms_gb_distinct.distinctcount'},
            func='sum', metric='ms_gb_distinct')
        av = QueryParser.single_aggs({
            'ms_gas2gb_distinct.count': 'ms_gas2gb_distinct.count'},
            func='value_count', metric='ms_gas2gb_distinct')
        calculations = {sa.name: sa, av.name: av}
        calculation_value_extractor = {_cal.name: '.'.join(_cal.result_path) for _cal in calculations.values()}
        calculation_order = {_cal.name: 'desc' for _cal in calculations.values()}
        filter = QueryCalculationSorter(
            calculation=calculations, calculation_value_extractor=calculation_value_extractor,
            calculation_order=calculation_order, offset=offset, size=size)

    """

    _BODY_TEMPLATE = {
        "result_sorter": {
            "bucket_sort": {
                "sort": [
                    {
                        "ignore_filter_name.cal_name": {
                            "order": "desc"
                        }
                    }
                ],
                "from": 0,
                "size": 3
            }
        },
        'ignore_filter_name': {
            "filter": {
                "bool": {
                    "filter": [
                        {
                            "term": {
                                "metric": "cpu"
                            }
                        }
                    ],
                    "must_not": [
                        {
                            "term": {
                                "tag.gameid": "g18"
                            }
                        }
                    ]
                }
            },
            "aggs": {
                'cal_name': {
                    'func': {
                        'field': 'field_name',
                        'param_name1': 'param_val1'
                    }
                }
            }
        }
    }

    _VALID_FUNC = ('bucket_sort',)

    def __init__(
            self, calculation: Dict[str, Calculation], calculation_value_extractor: Dict[str, str],
            calculation_order: Dict[str, str], offset: int = 0, size: int = 1, **params: Any):
        self._sorts = []
        for name, _cal in calculation.items():
            if isinstance(_cal, FieldTopKSort) or _cal.func_type == FuncType.FUNC_TOPK.value:
                raise ParamError(u'Topk calculation can not be used to script')
            self._sorts.append({calculation_value_extractor[name]: {"order": calculation_order[name]}})
        params['sort'] = self._sorts
        params['from'] = offset
        params['size'] = size
        super().__init__(fields={}, func='bucket_sort', **params)


class FieldTopKSort(Calculation):
    """
    **Topk sort of field**

    :param fields: 用于计算的字段名字和别名
    :type fields: Dict[str, str]
    :param expr: 用于字段之间计算的表达式
    :type expr: Union[str, None]
    :param func: 计算字段的算子,例如('sum', 'avg', 'max', 'min', 'value_count')
    :type func: str
    :param field_format: 提取字段使用的格式
    :type field_format: str
    :param expr_params: 用于字段之间计算的表达式使用到的参数
    :type expr_params: Union[Dict[str, float], None]
    :param param_format: 提取参数使用的格式
    :type param_format: str
    :param offset: 排序的位移
    :type offset: int
    :param size: 截取topk返回
    :type size: int
    :param order: 排序方向
    :type order: str
    :param params: 其余参数
    :type params: Any

    - For case::

        1. pql like: topk(5, abc.value)
            which equals to topk(5, abc.value) within 1m
        2. aql like: topk(5, abc.field1 + abc.field2 / 2)
            which equals to topk(5, abc.field1 + abc.field2 / 2) within 1m

    """

    _BODY_TEMPLATE = {
        'cal_name': {
            'func': {
                'sort': [
                    {
                        "_script": {
                            "type": "number",
                            "script": {
                                "lang": "painless",
                                "inline": "((doc['field.distinctcount'].value)-params.search_altitude)/10",
                                "params": {
                                    "search_altitude": 200
                                }
                            },
                            "order": "order_direction"
                        }
                    },
                    {
                        'field_name': {
                            'order': 'order_direction'
                        }
                    }

                ],
                '_source': {
                    'includes': ['tag'],
                    'excludes': ['metric', 'ts', 'field', 'meta']
                },
                "script_fields": {
                    'ts': {
                        "script": {
                            "source": "doc['ts'].value"
                        }
                    },
                    'metric': {
                        "script": {
                            "source": "doc['metric'].value"
                        }
                    },
                    'field_name': {
                        'script': {
                            'source': 'doc["field_name"].value'
                        }
                    }
                },
                'from': 0,
                'size': 1
            }
        }
    }

    _VALID_FUNC = ('top_hits',)

    def __init__(
            self, fields: Dict[str, str], expr: Union[str, None] = None, func: str = 'top_hits',
            field_format: str = "doc['field.{field}'].value",
            expr_params: Union[Dict[str, float], None] = None,
            param_format: str = "params.{param}",
            offset: int = 0, size: int = 1, order: str = 'desc', **params: Any):
        super().__init__(
            fields=fields, expr=expr, func=func, field_format=field_format, expr_params=expr_params,
            param_format=param_format, order=order, offset=offset, size=size, **params)


class FuncType(Enum):
    FUNC_AGG = 1
    FUNC_TOPK = 2
    FUNC_MOV = 3
