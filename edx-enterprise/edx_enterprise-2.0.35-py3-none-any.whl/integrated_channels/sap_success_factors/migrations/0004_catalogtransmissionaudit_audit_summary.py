# -*- coding: utf-8 -*-
# Generated by Django 1.9.12 on 2017-03-29 20:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sap_success_factors', '0003_auto_20170317_1402'),
    ]

    operations = [
        migrations.AddField(
            model_name='catalogtransmissionaudit',
            name='audit_summary',
            field=models.TextField(default='{}'),
        ),
    ]
