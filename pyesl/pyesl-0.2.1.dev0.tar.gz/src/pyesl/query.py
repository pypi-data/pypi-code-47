# -*- coding: utf-8 -*-

from __future__ import annotations

from abc import ABC
from copy import deepcopy
from typing import List, Dict, Union

from pyesl.errors import ParamError


class QueryBase(ABC):
    def __init__(self, body: dict):
        self._body = body

    @property
    def body(self) -> dict:
        return self._body
        # return deepcopy(self._body)
        # do not need deep copy


class Query(QueryBase):
    """
    Query object
    """
    BODY_TEMPLATE = {
        "query": {
            "bool": {
                "filter": [
                    {
                        "term": {
                            "metric": "ms_gb_distinct"
                        }
                    },
                    {
                        "range": {
                            "ts": {
                                "gte": "2019-11-16T00:00:00+08:00",
                                "lt": "2019-11-16T07:00:00+08:00"
                            }
                        }
                    }
                ]
            }
        }
    }

    def __init__(self, terms: Terms):
        _body = {
            'query': terms.body
        }
        super().__init__(_body)


class QuerySorts(QueryBase):
    """
    Query Sorts object
    """
    BODY_TEMPLATE = {
        "sort": [
            {
                "field": {
                    "order": "desc"
                }
            }
        ]
    }

    def __init__(self, sort: List[Sort]):
        _body = {
            "sort": [_s.body for _s in sort]
        }
        super().__init__(_body)


class Sort(QueryBase):
    """
    Sorting Base Object
    """
    VALID_OPS = ('asc', 'desc')
    BODY_TEMPLATE = {
        "field": {
            "order": "desc"
        }
    }

    def __init__(self, field: str = 'ts', order: str = 'desc'):
        if order not in self.VALID_OPS:
            raise ParamError('order: {} is not in {}'.format(order, self.VALID_OPS))
        super().__init__({
            field: {
                'order': order
            }
        })


class Condition(QueryBase):
    """
    Condition Base Object of:
    1. Positive Condition like: key='val' or key~'.*val.*'
    2. Negative Condition like: key!='val' or key!='.*val.*'
    3. Range Condition like: key>'val' or key<='val'
    """
    _TYPE = None
    VALID_OPS = ('term', 'regexp', 'gt', 'gte', 'lt', 'lte')
    BODY_TEMPLATE = None

    def __init__(self, op: str = 'term', name: str = 'key', value: str = 'value', **params):
        super().__init__({})
        self._op = op
        self._field_name = name
        self._field_value = value
        self._p = params

    @property
    def type(self) -> int:
        return self._TYPE


class RangeCondition(Condition):
    """
    Condition Object of key>='val' or key<'vall'
    """
    _TYPE = 3
    BODY_TEMPLATE = {
        'range': {
            'field_name': {
                'operator': 'field_value',
                'param_name1': 'param_val1'
            }
        }
    }

    def __init__(self, op: str = 'gte', name: str = 'key', value: str = 'value', **params):
        super().__init__(op, name, value, **params)
        self._body = {
            'range': {
                name: params
            }
        }
        self._body['range'][name][op] = value


class PositiveCondition(Condition):
    """
    Condition Object of key='val' or key~'.*vall.*'
    """
    _TYPE = 1
    BODY_TEMPLATE = {
        'operator': {
            'field_name': {
                'value': 'field_value',
                'param_name1': 'param_val1'
            }
        }
    }

    def __init__(self, op: str = 'term', name: str = 'key', value: str = 'value', **params):
        super().__init__(op, name, value, **params)
        self._body = {
            op: {
                name: params
            }
        }
        self._body[op][name]['value'] = value


class NegativeCondition(Condition):
    """
    Condition Object of key!='val' or key!~'.*vall.*'
    """
    _TYPE = 0
    BODY_TEMPLATE = {
        'bool': {
            'must_not': {
                'operator': {
                    'field_name': {
                        'value': 'field_value',
                        'param_name1': 'param_val1'
                    }
                }
            }
        }
    }

    def __init__(self, op: str = 'term', name: str = 'key', value: str = 'value', **params):
        super().__init__(op, name, value, **params)
        self._body['bool'] = {
            'must_not': {
                op: {
                    name: params
                }
            }
        }
        self._body['bool']['must_not'][op][name]['value'] = value


VALID_RELS = ('should', 'filter')


class ConditionGroup(QueryBase):
    """
    Combination of conditions of
    1. (.. AND .. AND .. AND .. AND ..)
    2. (.. OR .. OR .. OR .. OR .. )

    eg:

    1. OR group of conditions (key!='val' OR key!~'.*vall.*' OR key!~'.*vall.*' OR key!~'.*vall.*')
    2. AND group of conditions (key!='val' AND key!~'.*vall.*' AND key!~'.*vall.*' AND key!~'.*vall.*')
    """

    BODY_TEMPLATE = {
        'relation': []
    }

    def __init__(self, *conditions: Condition, relation: str = 'should'):
        if relation not in VALID_RELS:
            raise ParamError('rel: {} is not in {}'.format(relation, VALID_RELS))
        self._rel = relation
        _body = {
            self._rel: [_cdn.body for _cdn in conditions]
        }
        super().__init__(_body)

    @property
    def relation(self) -> str:
        return self._rel


class Terms(QueryBase):
    """
    **Final query conditions combinations object of ElasticSearch's Query Body, which is a composition of condition and condition groups and terms of syntax: (.. AND .. AND ..) AND (..OR..OR..OR..)**

    :param filter: Condition Group structure that should be place in filter part
    :type filter: Union[ConditionGroup, None]
    :param should: Condition Group structure that should be place in should part
    :type should: Union[ConditionGroup, None]
    :param body: ES Body that already using
    :type body: Union[Dict, None]

    - For case::

        1. condition and condition groups:
            key!='val' AND (key!='val' OR key!~'.*vall.*')

        2. condition and terms groups:
            key!='val' AND ((key!='val' OR key!~'.*vall.*') AND (key!~'.*vall.*' AND key!~'.*vall.*'))

        3. condition groups and terms:
            (key!='val' AND key!~'.*vall.*') AND ((key!='val' OR key!~'.*vall.*') AND (key!~'.*vall.*' AND key!~'.*vall.*'))

    """
    _BODY_TEMPLATE = {
        'bool': {
            'filter': [],
            'should': [],
            'minimum_should_match': 0
        }
    }

    def __init__(
            self, filter: Union[ConditionGroup, None] = None, should: Union[ConditionGroup, None] = None,
            body: Union[Dict, None] = None):
        if body:
            body = self._validate_body(body)
            super().__init__(body)
            if filter:
                self.extend_group(filter)
            if should:
                self.extend_group(should)
        else:
            _body = {
                'bool': {
                    'filter': filter.body['filter'] if filter is not None else [],
                    'should': should.body['should'] if should is not None else [],
                    'minimum_should_match': 1 if should else 0
                }
            }
            super().__init__(_body)

    def _validate_body(self, body: Dict) -> Dict:
        if 'bool' not in body:
            raise ParamError('Invalid ES Body, need "bool": {}'.format(body))
        else:
            _body = deepcopy(body)
            if 'filter' not in _body['bool']:
                _body['bool']['filter'] = []
            if 'should' not in _body['bool']:
                _body['bool']['should'] = []
            _body['bool']['minimum_should_match'] = 1 if len(_body['bool']['should']) > 0 else 0
        return _body

    def update_minimum_should_match(self):
        self._body['bool']['minimum_should_match'] = min(1, len(self._body['bool']['should']))

    def append_condition(self, condition: Condition, relation: str = 'filter') -> Terms:
        """
        Append a condition to one of the condition group eg:

        (key!='val' AND key!='val' ) AND (key!='val' OR key!~'.*vall.*') with key!='val'

        ->

        (key!='val' AND key!='val' ) AND (key!='val' OR key!~'.*vall.*' OR key!='val')


        :param condition:
        :param relation:
        :return:
        """
        if relation not in VALID_RELS:
            raise ParamError('rel: {} is not in {}'.format(relation, VALID_RELS))
        self._body['bool'][relation].append(condition.body)
        self.update_minimum_should_match()
        return self

    def extend_group(self, group: ConditionGroup) -> Terms:
        """
        Extend a group to one of the condition group eg:

        (key!='val' AND key!='val' ) AND (key!='val' OR key!~'.*vall.*') with (key!='val' OR key!~'.*vall.*')


        :param group:
        :return:
        """
        self._body['bool'][group.relation].extend(group.body[group.relation])
        self.update_minimum_should_match()
        return self

    def add_terms(self, other: Terms, relation: str = 'filter') -> Terms:
        """
        Join a terms with a relation to this terms eg:

        (key!='val' AND key!='val' ) AND (key!='val' OR key!~'.*vall.*')                                   <- this terms
        AND
        (key!='val' AND key!='val' ) AND (key!='val' OR key!~'.*vall.*' OR  (key!='val' OR key!~'.*vall.*'))   <- other

        :param other:
        :param relation:
        :return:
        """
        return self.add_termses(other, relation=relation)

    def add_termses(self, *others: Terms, relation: str = 'filter') -> Terms:
        """
        Join a list of terms with a relation to this terms eg:

        (key!='val' AND key!='val' ) AND (key!='val' OR key!~'.*vall.*')                                   <- this terms
        AND
        (key!='val' AND key!='val' ) AND (key!='val' OR key!~'.*vall.*' OR  (key!='val' OR key!~'.*vall.*'))   <- other

        :param others:
        :param relation:
        :return:
        """
        if relation not in VALID_RELS:
            raise ParamError('rel: {} is not in {}'.format(relation, VALID_RELS))
        my_body = self._body
        self._body = deepcopy(self._BODY_TEMPLATE)
        if not my_body == self._BODY_TEMPLATE:
            self._body['bool']['filter'].append(my_body)
        for other in others:
            self._body['bool'][relation].append(other.body)
        self.update_minimum_should_match()
        return self

    def copy(self) -> Terms:
        """
        deep copy of Terms it self
        :return: Copy of Terms structure
        :rtype: Terms
        """
        return Terms(body=self._body)
