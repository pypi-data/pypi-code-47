from collections import OrderedDict
from typing import Dict

from django.contrib.contenttypes.models import ContentType
from django.core.exceptions import FieldError, ObjectDoesNotExist
from django.http import Http404
from rest_framework import serializers

from .utils import ORMServices


class ORMServicesSerializer(serializers.Serializer):
    app_label = serializers.CharField(required=False)
    model = serializers.CharField()
    payload = serializers.JSONField()
    fields = serializers.ListField(required=False, default=['__all__'])
    exclude_fields = serializers.ListField(
        required=False,
        default=None,
        allow_null=True,
        allow_empty=True
    )
    relation_data = serializers.JSONField(required=False)

    def __init__(self, *args, **kwargs):
        super(ORMServicesSerializer, self).__init__(*args, **kwargs)
        self.service = None  # type: ORMServices

    def validate(self, attrs: Dict):
        try:
            self.service = ORMServices(
                model=attrs.get('model'),
                payload=attrs.get('payload'),
                fields=attrs.get('fields'),
                exclude_fields=attrs.get('exclude_fields'),
                relation_data=attrs.get('relation_data'),
                app_label=attrs.get('app_label')
            )
        except ContentType.DoesNotExist:
            raise serializers.ValidationError({
                'model': 'Model %s does not exists' % attrs.get('model')
            })
        except ContentType.MultipleObjectsReturned:
            raise serializers.ValidationError({
                'model': 'Multiple Objects Returned,'
                         'please provide app_label '
                         'for specific model' % attrs.get('model')
            })
        return super(ORMServicesSerializer, self).validate(attrs)

    def get_queryset(self):
        try:
            queryset = self.service.get_queryset()
        except ObjectDoesNotExist:
            raise Http404
        except FieldError as err:
            raise serializers.ValidationError({
                "field_error": err.args
            })
        queryset = self.service.serialize_queryset(queryset)
        return queryset


class ORMServicesSaveSerializer(ORMServicesSerializer):

    def get_queryset(self):
        return self.service.get_queryset()


class ModelSerializer(serializers.Serializer):
    map_fields = {
        'AutoField': serializers.IntegerField,
        'CharField': serializers.CharField,
        'IntegerField': serializers.IntegerField,
        'ListField': serializers.ListField,
        'OneToOneField': serializers.IntegerField,
        'ForeignKey': serializers.IntegerField
    }

    def get_fields(self) -> Dict:
        assert hasattr(self, 'Meta'), (
            'Class {serializer_class} missing "Meta" attribute'.format(
                serializer_class=self.__class__.__name__
            )
        )
        assert hasattr(self.Meta, 'model'), (
            'Class {serializer_class} missing "Meta.model" attribute'.format(
                serializer_class=self.__class__.__name__
            )
        )
        assert hasattr(self.Meta, 'fields'), (
            'Class {serializer_class} missing "Meta.fields" attribute'.format(
                serializer_class=self.__class__.__name__
            )
        )
        assert len(self.Meta.fields) > 0, (
            'Are you stupid, you\'re put a blank list on "Meta.fields"'
        )
        ret = super(ModelSerializer, self).get_fields()
        uncreated_fields = set(self.Meta.fields) - set(ret.keys())
        model_info = self.Meta.model.model_info
        model_fields = model_info.get('fields')
        model_related = model_info.get('related_names')
        if uncreated_fields:
            for uncreated_field in uncreated_fields:
                if uncreated_field in model_fields:
                    field = model_fields.get(uncreated_field).get('type')
                elif uncreated_field in model_related:
                    field = 'ListField'
                    if model_related.get(uncreated_field).get('type') == 'OneToOneRel':
                        field = 'IntegerField'
                else:
                    field = 'CharField'
                field_class = self.map_fields.get(field, serializers.CharField)
                ret.update({
                    uncreated_field: field_class()
                })
        for key, value in ret.items():
            value.bind(key, self)
        return ret

    def to_representation(self, instance):
        ret = OrderedDict()
        model_info = self.Meta.model.model_info
        model_fields = model_info.get('fields')
        for field, field_class in self.get_fields().items():
            attr = field_class.source or field
            try:
                if model_fields.get(attr).get('type') in ['ForeignKey', 'OneToOneField']:
                    attr = f"{attr}_id"
            except AttributeError:
                pass
            value = getattr(instance, attr, None)
            if isinstance(value, ORMServices):
                if attr in model_info.get('related_names'):
                    value = instance.reverse_related(attr)
            if field_class.__class__.__name__ == 'SerializerMethodField':
                value = instance
            if value is not None:
                value = field_class.to_representation(value)

            ret[field] = value
        return ret
