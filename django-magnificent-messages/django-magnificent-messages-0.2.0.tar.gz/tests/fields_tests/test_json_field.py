"""
Tests for `django-magnificent-messages` models module.
"""
import datetime

from django.core import checks, serializers
from django.core.exceptions import ValidationError
from django.core.serializers.base import DeserializationError
from django.db import connection
from django.test import TestCase

from django_magnificent_messages.fields import JSONField
from tests import models


class TestJsonField(TestCase):
    def _test_default(self, value):
        j = models.JSONFieldDefaultModel(id=1, field=value)
        j.save()
        json = models.JSONFieldDefaultModel.objects.get(id=1)

        self.assertEqual(value, json.field)
        self.assertEqual(type(value), type(json.field))

    def test_none(self):
        self._test_default(None)

    def test_integer(self):
        self._test_default(1)

    def test_str(self):
        self._test_default("aaaa")

    def test_float(self):
        self._test_default(1.5)

    def test_list(self):
        self._test_default([1, 2, 3])

    def test_dict(self):
        self._test_default({"aaa": 1, "bbb": "ccc"})

    def test_date(self):
        with self.assertRaises(ValidationError):
            self._test_default(datetime.date.today())

    def test_encode_check(self):
        class Model(models.models.Model):
            f = JSONField(encode=10)
        errors = Model.check()
        self.assertEqual('django_magnificent_messages.E101', errors[0].id)
        self.assertEqual('Parameter `encode` of `JSONField` should be callable', errors[0].msg)

    def test_decode_check(self):
        class Model(models.models.Model):
            f = JSONField(decode=10)
        errors = Model.check()
        self.assertEqual('django_magnificent_messages.E102', errors[0].id)
        self.assertEqual('Parameter `decode` of `JSONField` should be callable', errors[0].msg)

    def test_valid_config(self):
        class Model(models.models.Model):
            f = JSONField(encode=models.custom_encode, decode=models.custom_decode)
        errors = Model.check()
        self.assertEqual(0, len(errors))

    def test_filter(self):
        r1 = models.JSONFieldDefaultModel(id=1, field=[1, 2])
        r1.save()

        r2 = models.JSONFieldDefaultModel(id=2, field=[3, 4])
        r2.save()

        r = models.JSONFieldDefaultModel.objects.filter(field=[1, 2])
        self.assertEqual(1, r.count())
        self.assertIn(r1, r)
        self.assertNotIn(r2, r)

    def test_bad_json(self):
        with connection.cursor() as cursor:
            cursor.execute("insert into \"default\"(id, field) values (1, '{{');")
        with self.assertRaises(ValidationError):
            models.JSONFieldDefaultModel.objects.get(id=1)

    def test_db_null(self):
        with connection.cursor() as cursor:
            cursor.execute("insert into \"default\"(id, field) values (1, null);")

        t = models.JSONFieldDefaultModel.objects.get(id=1)
        self.assertEqual(None, t.field)

    def test_custom_encoding(self):
        c = models.CustomClass(10, "aaa")
        models.JSONFieldCustomModel.objects.create(id=1, field=c)
        m = models.JSONFieldCustomModel.objects.get(id=1)

        self.assertEqual(c, m.field)
        self.assertEqual(type(c), type(m.field))

    def test_serialization(self):
        models.JSONFieldDefaultModel.objects.create(id=1, field=[10, "aaa"])
        data = serializers.serialize("json", models.JSONFieldDefaultModel.objects.all())

        self.assertEqual(
            '[{"model": "tests.jsonfielddefaultmodel", "pk": 1, "fields": {"field": "[10, \\"aaa\\"]"}}]',
            data
        )

    def test_deserialization(self):
        data = '[{"model": "tests.jsonfielddefaultmodel", "pk": 2, "fields": {"field": "[20, \\"bbb\\"]"}}]'
        for deserialized_object in serializers.deserialize("json", data):
            deserialized_object.save()

        t = models.JSONFieldDefaultModel.objects.get(id=2)

        self.assertEqual(t.field, [20, "bbb"])

    def test_bad_deserialization(self):
        data = '[{"model": "tests.jsonfielddefaultmodel", "pk": 2, "fields": {"field": "[[[]"}}]'
        with self.assertRaises(DeserializationError):
            for deserialized_object in serializers.deserialize("json", data):
                deserialized_object.save()

