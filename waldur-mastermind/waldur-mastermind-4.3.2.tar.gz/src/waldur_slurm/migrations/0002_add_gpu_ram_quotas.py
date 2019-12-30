# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-09-12 15:22
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('waldur_slurm', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='allocation',
            name='gpu_limit',
            field=models.IntegerField(default=-1),
        ),
        migrations.AddField(
            model_name='allocation',
            name='gpu_usage',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='allocation',
            name='ram_limit',
            field=models.IntegerField(default=-1),
        ),
        migrations.AddField(
            model_name='allocation',
            name='ram_usage',
            field=models.IntegerField(default=0),
        ),
    ]
