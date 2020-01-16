from django.core import serializers
from django.db import models
from django.contrib.postgres.fields import JSONField
import json
import dictdiffer


class AuditLog(models.Model):
    object_type = models.CharField(max_length=100)
    object_id = models.BigIntegerField()
    state_delta = models.TextField()

    @classmethod
    def get_prev_versions(cls, object, limit=1):
        current_db_state_of_objects = object.__class__.objects.get(id=object.id)
        second = json.loads(serializers.serialize('json', [current_db_state_of_objects]))[0]
        previous_versions = []
        queryset = cls.objects.filter(object_type=second["model"], object_id=second["pk"]).order_by("-id")[:limit]
        for audit_log in queryset:
            diff = json.loads(audit_log.state_delta)
            first = dictdiffer.revert(diff, second)
            if first == {}:
                break
            previous_versions.append(first)
            second = first
        previous_version_objects = []
        for version in serializers.deserialize('json', json.dumps(previous_versions)):
            previous_version_objects.append(version.object)
        return previous_version_objects


def save_with_history(save, *args, **kwargs):
    def wrapper(*args, **kwargs):
        # Normal notify functionality
        obj = args[0]
        if not obj.id:
            db_state = {}
        else:
            db_obj = obj.__class__.objects.filter(id=obj.id).first()
            db_state = json.loads(serializers.serialize('json', [db_obj]))[0]
        rt = save(*args, **kwargs)
        new_state = json.loads(serializers.serialize('json', [args[0]]))[0]
        model_name = new_state["model"]
        AuditLog(object_type=model_name, object_id=new_state.get("pk"),
                 state_delta=json.dumps(list(dictdiffer.diff(db_state, new_state)))).save()
        return rt

    # Return the composite function
    return wrapper


class ModelHistoryMeta(models.base.ModelBase):
    def __new__(cls, name, bases, attrs, **kwargs):
        # if 'audited' in attrs and attrs.get('audited') is True:
        attrs['save'] = save_with_history(attrs.get('save', models.Model.save))
        instance = super(ModelHistoryMeta, cls).__new__(cls, name, bases, attrs, **kwargs)
        return instance
