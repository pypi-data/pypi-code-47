# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-06-12 19:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0030_auto_20180611_1930'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='short_description',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Short Description'),
        ),
    ]
