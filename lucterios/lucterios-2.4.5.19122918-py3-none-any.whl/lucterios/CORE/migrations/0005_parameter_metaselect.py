# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-03-01 18:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CORE', '0004_printmodel_is_default'),
    ]

    operations = [
        migrations.AddField(
            model_name='parameter',
            name='metaselect',
            field=models.TextField(blank=True, verbose_name='meta'),
        ),
    ]
