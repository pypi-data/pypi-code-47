# Generated by Django 2.1.2 on 2019-11-10 15:20

import django.contrib.postgres.fields.jsonb
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('djpaypal', '0009_shipping_address_null'),
    ]

    operations = [
        migrations.AddField(
            model_name='sale',
            name='payment_hold_reasons',
            field=django.contrib.postgres.fields.jsonb.JSONField(blank=True, editable=False, null=True),
        ),
        migrations.AddField(
            model_name='sale',
            name='payment_hold_status',
            field=models.CharField(choices=[('HELD', 'Held'), ('RELEASED', 'Released')], editable=False, max_length=8, null=True),
        ),
    ]
