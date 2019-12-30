# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import ast
from django.db import models
from django import forms
from django.conf import settings
from django.template import loader
from django.forms import Field

# model field
class DictField(models.TextField):
    description = "DictField"

    def __init__(self, *args, **kwargs):
        super(DictField, self).__init__(*args, **kwargs)


    def to_dict(self,value):
        if isinstance(value, dict):
            return value
        return ast.literal_eval(value)


    # 把数据库数据转成python数据
    def to_python(self, value):
        if not value:
            value = {}
        return self.to_dict(value)

    def from_db_value(self, value, expression, connection, context):
        if not value:
            value = {}
        return self.to_dict(value)

        # text_list=[]
        # for key in _dict:
        #     text_list.append(key+u"："+str(_dict[key]))
        # return "，".join(text_list)


    # 把python数据压缩准备存入数据库
    def get_prep_value(self, value):
        if value is None:
            return value
        return str(value)

    # 指定过滤的条件
    def get_prep_lookup(self, lookup_type, value):
        if lookup_type == 'exact':
            return value
        elif lookup_type == 'in':
            return [self.get_prep_value(v) for v in value]
        else:
            return TypeError('lookup type %r not supported' % lookup_type)

    # 数据序列化
    def value_to_string(self, obj):
        return 'aaa'
        value = self.value_from_object(obj)
        return self.get_prep_value(value)




    # def deconstruct(self):
    #     name, path, args, kwargs = super(JSONField, self).deconstruct()
    #     return name, path, args, kwargs

    # 为模型字段指定表单字段
    def formfield(self, **kwargs):
        # This is a fairly standard way to set up some defaults
        # while letting the caller override them.
        # defaults = {'form_class': RichTextFormField, "image_max_size": self.image_max_size}
        defaults = {"widget": forms.Textarea()}
        defaults.update(kwargs)
        return super(DictField, self).formfield(**defaults)


    def text(self,a=','):
        text_list = []
        _dict = self.to_dict(self)
        for key in _dict:
            text_list.append(_dict[key])
        return a.join(text_list)


# form field widget
# class DictWidget(forms.Textarea):
#     template_name = 'bee_django_object_field/widgets/dict.html'

# model field
class ListField(models.TextField):
    description = "ListField"
    def __init__(self, *args, **kwargs):
        super(ListField, self).__init__(*args, **kwargs)

    # 把数据库数据转成python数据
    def to_python(self, value):
        if not value:
            value = []
        if isinstance(value, list):
            return value
        return ast.literal_eval(value)

    # 把python数据压缩准备存入数据库
    def get_prep_value(self, value):
        if value is None:
            return value
        return str(value)

    # 指定过滤的条件
    def get_prep_lookup(self, lookup_type, value):
        if lookup_type == 'exact':
            return value
        elif lookup_type == 'in':
            return [self.get_prep_value(v) for v in value]
        else:
            return TypeError('lookup type %r not supported' % lookup_type)

    # 数据序列化
    def value_to_string(self, obj):
        value = self._get_val_from_obj(obj)
        return self.get_db_prep_value(value)
    # def deconstruct(self):
    #     name, path, args, kwargs = super(JSONField, self).deconstruct()
    #     return name, path, args, kwargs

    # 为模型字段指定表单字段
    def formfield(self, **kwargs):
        # This is a fairly standard way to set up some defaults
        # while letting the caller override them.
        # defaults = {'form_class': RichTextFormField, "image_max_size": self.image_max_size}
        defaults = {"widget": forms.Textarea()}
        defaults.update(kwargs)
        return super(ListField, self).formfield(**defaults)

#
# # form field
# class JSONFormField(forms.CharField):
#     def __init__(self, *args, **kwargs):
#         defaults = {"widget": forms.Textarea()}
#         defaults.update(kwargs)
#         super(JSONFormField, self).__init__(*args, **kwargs)

    # def to_python(self, value):
    #     "Returns a Unicode object."
    #     if value in self.empty_values:
    #         return self.empty_value
    #     value = force_text(value)
    #     if self.strip:
    #         value = value.strip()
    #     return value

    # def widget_attrs(self, widget):
    #     attrs = super(JSONFormField, self).widget_attrs(widget)
    #     return attrs

