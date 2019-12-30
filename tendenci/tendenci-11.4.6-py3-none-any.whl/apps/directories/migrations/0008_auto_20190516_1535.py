# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-05-16 15:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('directories', '0007_auto_20180315_1839'),
    ]

    operations = [
        migrations.AddField(
            model_name='directory',
            name='facebook',
            field=models.URLField(blank=True, default='', verbose_name='Facebook'),
        ),
        migrations.AddField(
            model_name='directory',
            name='instagram',
            field=models.URLField(blank=True, default='', verbose_name='Instagram'),
        ),
        migrations.AddField(
            model_name='directory',
            name='linkedin',
            field=models.URLField(blank=True, default='', verbose_name='LinkedIn'),
        ),
        migrations.AddField(
            model_name='directory',
            name='twitter',
            field=models.URLField(blank=True, default='', verbose_name='Twitter'),
        ),
        migrations.AddField(
            model_name='directory',
            name='youtube',
            field=models.URLField(blank=True, default='', verbose_name='YouTube'),
        ),
    ]
