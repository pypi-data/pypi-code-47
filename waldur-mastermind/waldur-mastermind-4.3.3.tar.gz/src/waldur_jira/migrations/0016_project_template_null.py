# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-04-26 09:23
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('waldur_jira', '0015_attachment_thumbnail'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='template',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='waldur_jira.ProjectTemplate'),
        ),
    ]
