# -*- coding: utf-8 -*-
# Generated by Django 1.11.18 on 2019-01-05 15:53
from __future__ import unicode_literals

from django.db import migrations
import tendenci.libs.tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('committees', '0002_auto_20180315_0857'),
    ]

    operations = [
        migrations.AddField(
            model_name='committee',
            name='sponsors',
            field=tendenci.libs.tinymce.models.HTMLField(blank=True, default=''),
        ),
    ]
