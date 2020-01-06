# -*- coding: utf-8 -*-

from typing import Dict, Any

from pyesl.aggs import Aggregations
from pyesl.errors import ParamError
from pyesl.field import SourceFields, ScriptFields
from pyesl.query import QuerySorts, Query


class ElasticsearchQuery(object):
    BODY_TEMPLATE = {
        'query': {
            'bool': {
                'filter': [],
                'should': [],
            }
        },
        '_source': {
            'include': []
        },
        'script_fields': {},
        'aggs': {},
        'sort': {
            'FIELD': {
                'order': 'desc'
            }
        },
        'from': 0,
        'size': 1
    }

    def __init__(
            self, query: Query = None, source_fields: SourceFields = None, script_fields: ScriptFields = None,
            aggregations: Aggregations = None, query_sorts: QuerySorts = None,
            offset: int = 0, size: int = 10, index: str = 'tsdb_alias', **params):
        self._body = {}
        self._index = index
        self.query = query
        self.source_fields = source_fields
        self.script_fields = script_fields
        self.aggregations = aggregations
        self.offset = offset
        self.size = size
        self.query_sorts = query_sorts
        self._params = params

    @property
    def offset(self) -> int:
        return self._offset

    @offset.setter
    def offset(self, offset: int):
        if offset < 0:
            raise ParamError('offset: {} < 0'.format(offset))
        self._offset = offset
        self._body['from'] = offset

    @property
    def size(self) -> int:
        return self._size

    @size.setter
    def size(self, size: int):
        if size < 0:
            raise ParamError('size: {} < 0'.format(size))
        self._size = size
        self._body['size'] = size

    @property
    def query(self) -> Query:
        return self._query

    @query.setter
    def query(self, query: Query):
        self._query = query
        if self._query:
            self._body['query'] = query.body['query']

    @property
    def query_sorts(self) -> QuerySorts:
        return self._query_sorts

    @query_sorts.setter
    def query_sorts(self, query_sorts: QuerySorts):
        self._query_sorts = query_sorts
        if self._query_sorts:
            self._body['sort'] = query_sorts.body['sort']

    @property
    def aggregations(self) -> Aggregations:
        return self._aggregations

    @aggregations.setter
    def aggregations(self, aggs: Aggregations):
        self._aggregations = aggs
        if self._aggregations:
            self._body['aggs'] = aggs.body['aggs']

    @property
    def source_fields(self) -> SourceFields:
        return self._source_fields

    @source_fields.setter
    def source_fields(self, source_fields: SourceFields):
        self._source_fields = source_fields
        if self._source_fields:
            self._body['_source'] = source_fields.body['_source']

    @property
    def script_fields(self) -> ScriptFields:
        return self._script_fields

    @script_fields.setter
    def script_fields(self, script_fields: ScriptFields):
        self._script_fields = script_fields
        if self._script_fields:
            self._body['script_fields'] = script_fields.body['script_fields']

    @property
    def params(self) -> Dict:
        return self._params

    def set_param(self, param_name: str, param_value: Any):
        self._params[param_name] = param_value

    @property
    def body(self) -> dict:
        return self._body

    @property
    def index(self) -> str:
        return self._index

    @index.setter
    def index(self, value: str):
        self._index = value
