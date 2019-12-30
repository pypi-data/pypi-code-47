# -*- coding: utf-8 -*-
# Generated by Django 1.11.21 on 2019-06-27 08:31
from django.db import migrations, models
import django.db.models.deletion
import waldur_core.core.fields
import waldur_core.core.models
import waldur_core.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('structure', '0009_project_is_removed'),
        ('waldur_vmware', '0003_disk'),
    ]

    operations = [
        migrations.CreateModel(
            name='Template',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(blank=True, max_length=500, verbose_name='description')),
                ('name', models.CharField(max_length=150, validators=[waldur_core.core.validators.validate_name], verbose_name='name')),
                ('uuid', waldur_core.core.fields.UUIDField()),
                ('backend_id', models.CharField(db_index=True, max_length=255)),
                ('guest_os', models.CharField(help_text='Defines the valid guest operating system types used for configuring a virtual machine', max_length=50)),
                ('cores', models.PositiveSmallIntegerField(default=0, help_text='Number of cores in a VM')),
                ('cores_per_socket', models.PositiveSmallIntegerField(default=1, help_text='Number of cores per socket in a VM')),
                ('ram', models.PositiveIntegerField(default=0, help_text='Memory size in MiB', verbose_name='RAM')),
                ('created', models.DateTimeField()),
                ('modified', models.DateTimeField()),
                ('settings', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='structure.ServiceSettings')),
            ],
            options={
                'abstract': False,
            },
            bases=(waldur_core.core.models.BackendModelMixin, models.Model),
        ),
    ]
