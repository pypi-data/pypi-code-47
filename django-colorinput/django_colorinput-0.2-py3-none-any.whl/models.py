# -*- coding: utf-8 -*-
from django.db import models

from . import forms


class ColorField(models.CharField):
    description = ("A simple field to store a color's RGB values "
                   "in triple HEX format")

    def __init__(self, *args, **kwargs):
        kwargs['max_length'] = 6
        super().__init__(*args, **kwargs)

    def deconstruct(self):
        name, path, args, kwargs = super().deconstruct()
        del kwargs['max_length']
        return name, path, args, kwargs

    def formfield(self, **kwargs):
        kwargs['form_class'] = forms.ColorField
        return super().formfield(**kwargs)
