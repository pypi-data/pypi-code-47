# -*- coding: utf-8 -*-
# Generated by Django 1.9.12 on 2017-02-24 15:08
from __future__ import unicode_literals

import django.utils.timezone
from django.db import migrations, models

import model_utils.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EnterpriseIntegratedChannel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('name', models.CharField(help_text='Third Party name.', max_length=255)),
                ('data_type', models.CharField(help_text='Data Type', max_length=100)),
            ],
            options={
                'verbose_name': 'Enterprise Integrated Channel',
                'verbose_name_plural': 'Enterprise Integrated Channels',
            },
        ),
        migrations.AlterUniqueTogether(
            name='enterpriseintegratedchannel',
            unique_together=set([('name', 'data_type')]),
        ),
    ]
