# Generated by Django 2.2.7 on 2019-12-27 10:29

import django.contrib.postgres.fields.jsonb
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('waldur_rancher', '0007_cluster_tenant_settings'),
    ]

    operations = [
        migrations.AddField(
            model_name='node',
            name='annotations',
            field=django.contrib.postgres.fields.jsonb.JSONField(blank=True, default=dict),
        ),
        migrations.AddField(
            model_name='node',
            name='cpu_allocated',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='node',
            name='cpu_total',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='node',
            name='docker_version',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='node',
            name='k8s_version',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='node',
            name='labels',
            field=django.contrib.postgres.fields.jsonb.JSONField(blank=True, default=dict),
        ),
        migrations.AddField(
            model_name='node',
            name='pods_allocated',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='node',
            name='pods_total',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='node',
            name='ram_allocated',
            field=models.IntegerField(blank=True, null=True, help_text='Allocated RAM in Mi.'),
        ),
        migrations.AddField(
            model_name='node',
            name='ram_total',
            field=models.IntegerField(blank=True, null=True, help_text='Total RAM in Mi.'),
        ),
    ]
