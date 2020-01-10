import json
from typing import Dict
from urllib.parse import urljoin

import requests
from django.conf import settings

from .related_descriptors import create_reverse_many_to_one

# NOTE: All models info will be stored here.
# contains fields and related_names,
# keep note don't redefine the MODELS variable
# for keeping the reactivity. If you want to
# change the value, just clear or append it.
MODELS = []

service_settings = getattr(settings, 'ORM_SERVICE', {
    "url": "",
    "auth_header": ""
})
ORM_SERVICE_URL = service_settings.get("url")
ORM_SERVICE_AUTH_HEADER = service_settings.get("auth_header")


class VirtualModel(object):
    def __init__(
            self,
            model: str,
            payload: dict,
            value=None,
            model_info=None
    ):
        self._payload = payload
        app_label = None
        if len(model.split('.')) == 2:
            app_label, model = model.split('.')
        self.__model = model
        self._app_label = app_label
        self._attrs = {}
        if not model_info:
            model_info = get_model(model, app_label)
        if not app_label:
            self._app_label = model_info.get('app_label')
        self._class_name = model_info.get('class_name')
        self._fields = model_info.get('fields')  # type: Dict
        self._related_names = model_info.get('related_names')  # type: Dict
        if value:
            self._set_value(value)

    def __repr__(self):
        key = self._attrs.get(
            '__str__',
            (self._attrs.get('id') or
             self._attrs.get(
                 next(iter(self._attrs))
             ))
        )
        return f"<{self._class_name}: {key}>"

    def __setattr__(self, key, value):
        try:
            super(VirtualModel, self).__setattr__(key, value)
            if key in self._fields or key in self._related_names:
                if isinstance(value, dict):
                    info = self._fields.get(key, self._related_names.get(key))
                    related_model = info.get('related_model')
                    model = f"{related_model.get('app_label')}.{related_model.get('name')}"
                    value = self.__class__(model, self._payload, value=value)
                    super(VirtualModel, self).__setattr__(key, value)
                self._attrs.update({
                    key: value
                })

        except Exception:
            pass

    def _set_attr_single_instance(self, key, value):
        from .connector import ORM88

        if hasattr(self, key):
            return None

        attr_value = None
        if self._attrs.get(f"{key}_id"):
            related_model = value.get('related_model')
            model = f"{related_model.get('app_label')}.{related_model.get('name')}"
            attr_value = ORM88(model)
        setattr(self, key, attr_value)

    def set_many_to_one_or_many(self, key, value, related_field):
        from .connector import ORM88
        related_model = value.get('related_model')
        model = f"{related_model.get('app_label')}.{related_model.get('name')}"
        if hasattr(self, key):
            _value = getattr(self, key)
            if isinstance(_value, self.__class__):
                return None
            elif isinstance(_value, list):
                attr_value = create_reverse_many_to_one(model, {
                    'filter': {
                        'args': [],
                        'kwargs': {
                            related_field: self.id
                        }
                    }
                })()
                attr_value._bind(data=_value)
                attr_value._prefetch_done = True
            elif isinstance(_value, dict):
                attr_value = self.__class__(model, self._payload, value=_value)
            else:
                attr_value = ORM88(model)
        else:
            attr_value = ORM88(model)
            type_field = self._fields.get(
                key,
                self._related_names.get(key, {})
            ).get('type')
            payload = {}
            if type_field in ['OneToOneField', 'OneToOneRel']:
                payload.update({
                    'get': {
                        'args': [],
                        'kwargs': {
                            related_field: self.id
                        }
                    }
                })
            else:
                payload.update({
                    'filter': {
                        'args': [],
                        'kwargs': {
                            related_field: self.id
                        }
                    }
                })
            attr_value._payload.update(payload)
        setattr(self, key, attr_value)

    def _set_related_attributes(self):

        for key, value in self._fields.items():
            type_field = value.get('type')
            if type_field in ['ForeignKey', 'OneToOneField']:
                self._set_attr_single_instance(key, value)
            elif type_field == 'ManyToManyField':
                related_model = value.get('related_model')
                self.set_many_to_one_or_many(key, value,
                                             related_model.get('related_query_name'))

        for key, value in self._related_names.items():
            related_model = value.get('related_model')
            self.set_many_to_one_or_many(key, value, related_model.get('related_field'))

    def _set_value(self, attrs: Dict):
        self._attrs.update(attrs)
        for key, value in attrs.items():
            setattr(self, key, value)
        self._set_related_attributes()

    def _get_related(self, name):
        from .connector import ORM88

        attr = getattr(self, name)
        if isinstance(attr, ORM88):
            if name in self._fields:
                field = self._fields.get(name)
                if field.get('type') in ['ForeignKey', 'OneToOneField']:
                    attr = attr.get(id=self._attrs.get(f"{name}_id"))
                    setattr(self, name, attr)
                    return attr
                elif field.get('type') == 'ManyToManyField':
                    return attr
        return attr

    def _reverse_related(self, related_name):
        from .connector import ORM88
        try:
            orm = getattr(self, related_name)  # type: ORM88
        except AttributeError:
            raise AttributeError(f'{self.__model} has no related {related_name}')
        else:
            if isinstance(orm, ORM88):
                rel = self._related_names.get(related_name)
                related_model = rel.get('related_model')
                filter_kwargs = {
                    related_model.get('related_field'): self.id
                }
                if rel.get('type') == 'OneToOneRel':
                    orm = orm.get(**filter_kwargs)
                    setattr(self, related_name, orm)
                    return orm
            return orm

    def rel(self, name):
        if name in self._fields:
            return self._get_related(name)
        return self._reverse_related(name)

    def has_rel(self, name):
        try:
            return bool(self.rel(name))
        except Exception:
            return False

    def refresh_from_db(self):
        from .connector import ORM88

        instance = ORM88(
            model=self.__model,
            fields=list(self._attrs)
        )
        url = urljoin(ORM_SERVICE_URL, "/api/v1/orm_services/get_queryset")
        attrs = instance._ORM88__request_get(
            url=url,
            payload=self._payload
        )
        if isinstance(attrs, dict):
            for key, value in attrs:
                setattr(self, key, value)

    def save(self):
        from .connector import ORM88

        instance = ORM88(
            model=self.__model,
            fields=list(self._attrs)
        )
        payload = self._payload.copy()
        model_fields = {}
        for field in self._fields:
            model_fields.update({
                field: self._attrs.get(field)
            })
        payload.get("payload").update({
            "save": model_fields
        })
        return instance._save(payload)


class ModelNotFound(Exception):
    pass


class MultipleModelsReturned(Exception):
    pass


def initialize_models(force=False):
    global MODELS
    if not MODELS or force:
        url = urljoin(ORM_SERVICE_URL, "/api/v1/orm_services/get_models")
        response = requests.get(url, headers={
            "content-type": "application/json",
            'Authorization': ORM_SERVICE_AUTH_HEADER
        })
        if response.status_code == 400:
            raise Exception(response.text)
        try:
            response = response.json()
        except json.decoder.JSONDecodeError:
            if response.text:
                raise Exception(response.text)
        else:
            MODELS.clear()
            MODELS += response


def get_model(name: str, app_label=None) -> Dict:
    initialize_models()
    name = name.lower()
    result = list(filter(
        lambda model: model.get('model') == name,
        MODELS
    ))
    if app_label:
        result = list(filter(
            lambda model: model.get('app_label') == app_label,
            result
        ))
    if not result:
        msg = f"Cannot find model {name}"
        if app_label:
            msg = f"{msg} with app_label {app_label}"
        raise ModelNotFound(msg)
    if len(result) > 1:
        multiple = list(map(lambda x: x.get('app_label'), result))
        raise MultipleModelsReturned(f"Please provide app_label: {multiple}")
    return result[0]
