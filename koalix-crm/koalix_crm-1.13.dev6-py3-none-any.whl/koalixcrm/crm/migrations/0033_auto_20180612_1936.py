# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-06-12 19:36
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0032_auto_20180612_1925'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='projectstatus',
            options={'verbose_name': 'Project Status', 'verbose_name_plural': 'Project Status'},
        ),
        migrations.AlterField(
            model_name='task',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crm.Project', verbose_name='Project'),
        ),
    ]
