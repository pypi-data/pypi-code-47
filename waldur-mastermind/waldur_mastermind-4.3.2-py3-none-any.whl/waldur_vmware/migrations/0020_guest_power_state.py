# -*- coding: utf-8 -*-
# Generated by Django 1.11.21 on 2019-08-01 07:23
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('waldur_vmware', '0019_port_service_project_link'),
    ]

    operations = [
        migrations.AddField(
            model_name='virtualmachine',
            name='guest_power_enabled',
            field=models.BooleanField(default=False, help_text='Flag indicating if the virtual machine is ready to process soft power operations.'),
        ),
        migrations.AddField(
            model_name='virtualmachine',
            name='guest_power_state',
            field=models.CharField(blank=True, choices=[('RUNNING', 'Running'), ('SHUTTING_DOWN', 'Shutting down'), ('RESETTING', 'Resetting'), ('STANDBY', 'Standby'), ('NOT_RUNNING', 'Not running'), ('UNAVAILABLE', 'Unavailable')], max_length=150, verbose_name='The power state of the guest operating system.'),
        ),
    ]
