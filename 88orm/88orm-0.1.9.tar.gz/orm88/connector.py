# -*- coding: utf-8 -*-
# Created at 01/02/2019

__author__ = "Rimba Prayoga"
__copyright__ = "Copyright 2019, 88Spares"
__credits__ = ["88 Tech"]

__maintainer__ = "Rimba Prayoga"
__email__ = "rimba47prayoga@gmail.com"
__status__ = "Development"

import json
from typing import List
from urllib.parse import urljoin

import requests
from django.conf import settings
from django.db import models
from django.db.models import Q, ObjectDoesNotExist
from django.utils.functional import cached_property

from .models import initialize_models, get_model, VirtualModel

initialize_models()

service_settings = getattr(settings, 'ORM_SERVICE', {
    "url": "",
    "auth_header": "",
    "communication": {
        "method": "rest"
    }
})
ORM_SERVICE_URL = service_settings.get("url")
ORM_SERVICE_AUTH_HEADER = service_settings.get("auth_header")
ORM_SERVICE_COMMUNICATION = service_settings.get("communication", {})

if ORM_SERVICE_COMMUNICATION.get("method") == "rpc":
    try:
        from nameko.standalone.rpc import ClusterRpcProxy
    except ImportError:
        raise Exception('Nameko is required for using rpc.')


class ORM88(object):
    """
    ORM Services Connector.
    because you are familiar with Django ORM.
    Use it like Django ORM :D
    """

    def __init__(self, model: str, fields=None, **kwargs):
        initialize_models()
        app_label = None
        if len(model.split('.')) == 2:
            app_label, model = model.split('.')

        if isinstance(model, str):
            self._model_name = model
        elif isinstance(model, type) and isinstance(model(), models.Model):
            self._model_name = model._meta.model_name.lower()
        else:
            raise TypeError('unsupported type "%s" for model.' % type(model))

        self._app_label = app_label
        self._payload = {}
        if fields is None:
            fields = ['__all__']
        self._fields = fields
        self._exclude_fields = kwargs.get('exclude_fields', None)
        self._result_cache = {}
        self._CHUNK_SIZE = 20
        self._prefetch_done = False
        self.model_info = get_model(model, app_label)

    ########################
    # PYTHON MAGIC METHODS #
    ########################

    def __repr__(self):
        if self._payload:
            _slice = self._payload.get('slice')
            if _slice:
                start = _slice.get('start')
                stop = _slice.get('stop')
                step = _slice.get('step')
                data = list(self[start:stop:step])
            else:
                data = list(self[:self._CHUNK_SIZE])
            if len(data) >= self._CHUNK_SIZE:
                data[-1] = '...(remaining elements truncated)...'
            return f"<Virtual Queryset {data}>"
        return super(ORM88, self).__repr__()

    def __iter__(self):
        data = self._result_cache.get('result')
        if not self._payload:
            data = []
        if data is None:
            self._bind()
            data = self._result_cache.get('result')
        return iter(data)

    def __len__(self):
        count = self._result_cache.get("count", 0)
        if not count and self.__last_query:
            self._bind()
            count = self._result_cache.get("count", 0)
        return count

    def __bool__(self):
        return bool(len(self))

    def __getitem__(self, item):
        result_cache = self._result_cache.get('result')
        if result_cache or self._prefetch_done:
            return result_cache[item]
        if isinstance(item, slice):
            clone = self._clone()
            clone._payload.update({
                "slice": {
                    "start": item.start,
                    "stop": item.stop,
                    "step": item.step
                }
            })
            return clone
        _self = self._bind()
        if _self == self:
            result_cache = self._result_cache.get('result')
            return result_cache[item]
        return _self

    @cached_property
    def __exclude_params(self):
        return [
            "all",
            "exists",
            "count",
            "first",
            "last",
            "latest",
            "values",
            "save",
            "distinct"
        ]

    @cached_property
    def __is_model_instance(self):
        for method in ["first", "last", "latest"]:
            if self._payload.get(method):
                return True
        return False

    @property
    def __payload_request(self):
        payload = {
            "model": self._model_name,
            "payload": self._payload,
            "fields": self._fields,
            "exclude_fields": self._exclude_fields
        }
        if self._app_label:
            payload.update({
                "app_label": self._app_label
            })
        return payload

    @property
    def __last_query(self) -> str:
        """
        :return: last query
        """
        queries = list(self._payload.keys()).copy()
        if 'slice' in queries:
            queries.pop(queries.index('slice'))
        try:
            return queries[-1]
        except IndexError:
            return ''

    @property
    def __is_return_different_object(self) -> bool:
        return self.__last_query in [
            'first', 'last', 'get', 'latest',
            'exists', 'count', 'create'
        ]

    @property
    def __is_return_instance(self) -> bool:
        return self.__last_query in ['first', 'last', 'get', 'latest', 'create']

    def __update_payload(self, name, data) -> None:
        try:
            existed = self._payload.get(name).copy()  # type: Dict
        except AttributeError:
            pass
        else:
            existed = existed.copy()
            existed.update({
                "args": [*existed.get("args", []), *data.get("args", [])],
                "kwargs": {
                    **existed.get("kwargs"),
                    **data.get("kwargs")
                }
            })
            data = existed
        self._payload.update({
            name: data
        })

    # --- expressions
    def __resolve_q(self, args: Q) -> List:
        """
        Resolve expression Q. e.g: Q(a=b) | Q(c=d).
        :param params:
        :param result:
        :param extra_params:
        :return:
        """
        _, params, connector = args.deconstruct()
        params = list(params)
        for index, param in enumerate(params.copy()):
            if isinstance(param, Q):
                params[index] = self.__resolve_q(param)
            elif isinstance(param, tuple):
                params[index] = list(param)
        return ['Q', params, connector]

    def __resolve_expression(self, expr):
        expression_handlers = {
            "Q": self.__resolve_q
        }
        return expression_handlers.get(expr)

    def __do_query(self, name, *args, **kwargs):
        assert self._payload.get('slice') is None, \
            "Cannot filter a query once a slice has been taken."
        _args = list(args).copy()
        for index, arg in enumerate(_args):
            if isinstance(arg, Q):
                _args[index] = self.__resolve_q(arg)
        clone = self._clone()
        for key, value in kwargs.copy().items():
            if isinstance(value, VirtualModel):
                related = self._get_related_field(key)
                if related.get('type') in ['ForeignKey', 'OneToOneField']:
                    foreign_field = related.get('foreign_related_fields')
                    kwargs.update({
                        key: getattr(value, foreign_field)
                    })
            elif isinstance(value, ORM88):
                kwargs.update({
                    key: value.__payload_request
                })
        payload = {
            "args": _args,
            "kwargs": kwargs
        }
        clone.__update_payload(name, data=payload)
        if clone.__is_return_different_object:
            if clone.__is_return_instance:
                return clone._bind()
            return clone.fetch()
        return clone

    def _get_related_field(self, name):
        return (self.model_info.get('fields').get(name) or
                self.model_info.get('related_names').get(name))

    def _clone(self):
        """
        :return: clone of current class
        """
        exclude_fields = self._exclude_fields
        if isinstance(exclude_fields, (dict, list)):
            exclude_fields = self._exclude_fields.copy()
        model_name = self._model_name
        if self._app_label:
            model_name = f'{self._app_label}.{model_name}'
        clone = self.__class__(
            model=model_name,
            fields=self._fields.copy(),
            exclude_fields=exclude_fields
        )
        clone._payload = self._payload.copy()
        return clone

    def __clear_query(self, name=None):
        if name is not None:
            try:
                del self._payload[name]
            except KeyError:
                pass
        else:
            self._payload = {}

    def _bind(self, model=None, data=None):
        if data is None:
            data = self.fetch()

        if isinstance(data, dict):
            _model = model
            if _model is None:
                _model = self._model_name
            vi = VirtualModel(
                model=_model,
                payload=self.__payload_request,
                value=data,
                model_info=self.model_info
            )
            return vi
        vi = {
            "result": [],
            "count": 0
        }
        if isinstance(data, list):
            if {'values', 'values_list'} & set(self._payload.keys()):
                vi.update({
                    "result": data,
                    "count": len(data)
                })
            else:
                for i in data:
                    _vi = VirtualModel(
                        model=self._model_name,
                        payload=self.__payload_request,
                        value=i,
                        model_info=self.model_info
                    )
                    vi.get('result').append(_vi)
                    vi.update({
                        "count": vi.get("count") + 1
                    })
            self._result_cache = vi
            return self

    # for custom method
    def call_manager_method(self, name, *args, **kwargs):

        return self.__do_query(name, *args, **kwargs)

    # --- fetch data from orm services
    def __request_get(self, url, payload, params=None):
        if ORM_SERVICE_COMMUNICATION.get("method") == "rpc":
            with ClusterRpcProxy(ORM_SERVICE_COMMUNICATION.get("conf")) as rpc:
                return rpc.orm_service.query(payload)
        response = requests.get(url, data=json.dumps(payload), headers={
            "content-type": "application/json",
            'Authorization': ORM_SERVICE_AUTH_HEADER
        }, params=params)
        if response.status_code == 400:
            raise Exception(response.text)
        elif response.status_code == 404:
            raise self.DoesNotExist(
                "%s matching query does not exist." % self._model_name.capitalize())
        try:
            return response.json()
        except json.decoder.JSONDecodeError:
            if response.text:
                raise Exception(response.text)

    def __request_post(self, url, payload):
        if ORM_SERVICE_COMMUNICATION.get("method") == "rpc":
            with ClusterRpcProxy(ORM_SERVICE_COMMUNICATION.get("conf")) as rpc:
                return rpc.orm_service.query(payload)
        response = requests.post(url, data=json.dumps(payload), headers={
            "content-type": "application/json",
            'Authorization': ORM_SERVICE_AUTH_HEADER
        })
        try:
            return response.json()
        except json.decoder.JSONDecodeError:
            raise Exception(response.text)

    def fetch(self):
        url = urljoin(ORM_SERVICE_URL, "/api/v1/orm_services/get_queryset")
        return self.__request_get(
            url=url,
            payload=self.__payload_request
        )

    def fetch_with_relation(self, relation_data):
        """
        fetch data with relation object
        :param relation_data: -- e.g:
        ORM88(model='partitem').all()
            .fetch_with_relation({'member':[{'user': ['id', 'email']}]})
        :return: -- response:
        [{'member': {'user': {'id': 556, 'email': 'cobacoba@gmail.com'}}},]
        """
        payload = self.__payload_request.copy()
        payload.update({
            "relation_data": relation_data
        })
        url = urljoin(ORM_SERVICE_URL, "/api/v1/orm_services/get_queryset")
        return self.__request_get(
            url=url,
            payload=payload
        )

    def get_property(self, property_name):
        payload = self.__payload_request.copy()
        payload.update({
            "property_name": property_name
        })
        url = urljoin(ORM_SERVICE_URL, "/api/v1/orm_services/get_property")
        return self.__request_get(url=url, payload=payload)

    def call_property(self, property_name):
        payload = self.__payload_request.copy()
        payload.update({
            "property_name": property_name
        })
        url = urljoin(ORM_SERVICE_URL, "/api/v1/orm_services/call_property")
        return self.__request_get(url=url, payload=payload)

    # --- querying

    def get_queryset(self, *args, **kwargs):
        return self.__do_query('all', *args, **kwargs)

    def all(self):
        return self.get_queryset()

    def exists(self) -> bool:
        return self.__do_query('exists')

    def get(self, *args, **kwargs) -> VirtualModel:
        return self.__do_query('get', *args, **kwargs)

    def filter(self, *args, **kwargs):
        return self.__do_query('filter', *args, **kwargs)

    def exclude(self, *args, **kwargs):
        return self.__do_query('exclude', *args, **kwargs)

    def values(self, *args, **kwargs):
        return self.__do_query('values', *args, **kwargs)

    def values_list(self, *args, **kwargs):
        return self.__do_query('values_list', *args, **kwargs)

    def count(self, *args, **kwargs) -> int:
        return self.__do_query('count', *args, **kwargs)

    def first(self, *args, **kwargs) -> VirtualModel:
        return self.__do_query('first', *args, **kwargs)

    def last(self, *args, **kwargs) -> VirtualModel:
        return self.__do_query('last', *args, **kwargs)

    def latest(self, *args, **kwargs) -> VirtualModel:
        return self.__do_query('latest', *args, **kwargs)

    def order_by(self, *args, **kwargs):
        return self.__do_query('order_by', *args, **kwargs)

    def select_related(self, *args, **kwargs):
        return self.__do_query('select_related', *args, **kwargs)

    def prefetch_related(self, *args, **kwargs):
        return self.__do_query('prefetch_related', *args, **kwargs)

    def distinct(self, *args, **kwargs):
        return self.__do_query('distinct', *args, **kwargs)

    def only(self, *args, **kwargs):
        return self.__do_query('only', *args, **kwargs)

    def defer(self, *args, **kwargs):
        return self.__do_query('defer', *args, **kwargs)

    def create(self, *args, **kwargs):
        return self.__do_query('create', *args, **kwargs)

    def update(self, **kwargs):
        self.__update_payload('update', data={
            'args': [],
            'kwargs': kwargs
        })
        return self.fetch()

    def delete(self):
        self.__update_payload('delete', data={
            'args': [],
            'kwargs': {}
        })
        return self.fetch()

    def get_or_create(self, *args, **kwargs):
        try:
            return self.get(*args, **kwargs), False
        except self.DoesNotExist:
            return self.create(**kwargs), True

    def custom(self, name, **kwargs):
        return self.__do_query(name, *(), **kwargs)

    def filter_offline(self, **kwargs):
        def _filter(item):
            if isinstance(item, VirtualModel):
                ret = []
                for key, value in kwargs.items():
                    ret.append(getattr(item, key) == value)
                return all(ret)
            return False

        return list(filter(_filter, self._result_cache.get('result', [])))

    @classmethod
    def execute_many(cls, payloads: List):
        payload_requests = list(
            map(lambda orm: orm._ORM88__payload_request, payloads))
        url = urljoin(ORM_SERVICE_URL, "/api/v1/orm_services/execute_many")
        response = requests.get(url, data=json.dumps(payload_requests), headers={
            "content-type": "application/json",
            'Authorization': ORM_SERVICE_AUTH_HEADER
        })
        try:
            response = response.json()
        except Exception:
            raise Exception(response.content)
        else:
            result = []
            for index, orm_service in enumerate(payloads):
                result.append(orm_service._bind(data=response[index]))
            return result

    def _save(self, payload, *args, **kwargs):
        self.__do_query('save', *args, **kwargs)
        url = urljoin(ORM_SERVICE_URL, "/api/v1/orm_services/save")
        return self.__request_post(
            url=url,
            payload=payload
        )

    class DoesNotExist(ObjectDoesNotExist):
        pass
