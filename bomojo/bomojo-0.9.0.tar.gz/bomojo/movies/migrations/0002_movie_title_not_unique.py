# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-05-02 11:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='title',
            field=models.CharField(db_index=True, max_length=1024),
        ),
    ]
