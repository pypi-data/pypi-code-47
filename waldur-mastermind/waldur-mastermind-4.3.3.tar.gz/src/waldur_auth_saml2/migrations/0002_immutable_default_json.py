# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-07-03 17:02
from django.db import migrations
import waldur_core.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('waldur_auth_saml2', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='identityprovider',
            name='metadata',
            field=waldur_core.core.fields.JSONField(default=dict),
        ),
    ]
