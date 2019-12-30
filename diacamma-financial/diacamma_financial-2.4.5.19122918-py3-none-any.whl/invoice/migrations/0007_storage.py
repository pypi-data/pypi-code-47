# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-05-15 13:49
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
from django_fsm import FSMIntegerField
from lucterios.framework.models import LucteriosDecimalField


class Migration(migrations.Migration):

    dependencies = [
        ('accounting', '0007_costaccounting_year'),
        ('invoice', '0006_storagearea'),
    ]

    operations = [
        migrations.CreateModel(
            name='StorageDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', LucteriosDecimalField(decimal_places=3, default=0.0, max_digits=10, validators=[
                 django.core.validators.MinValueValidator(0.0), django.core.validators.MaxValueValidator(9999999.999)], verbose_name='buying price')),
                ('quantity', models.DecimalField(decimal_places=2, default=1.0, max_digits=10, validators=[
                 django.core.validators.MinValueValidator(0.0), django.core.validators.MaxValueValidator(9999999.99)], verbose_name='quantity')),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='invoice.Article', verbose_name='article')),
            ],
            options={
                'default_permissions': [],
                'verbose_name': 'storage detail',
                'verbose_name_plural': 'storage details',
            },
        ),
        migrations.CreateModel(
            name='StorageSheet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sheet_type', models.IntegerField(choices=[(0, 'stock receipt'), (1, 'stock exit'), (2, 'stock transfer')], db_index=True, default=0, verbose_name='sheet type')),
                ('status', FSMIntegerField(choices=[(0, 'building'), (1, 'valid')], db_index=True, default=0, verbose_name='status')),
                ('date', models.DateField(verbose_name='date')),
                ('comment', models.TextField(verbose_name='comment')),
                ('bill_reference', models.CharField(blank=True, max_length=50, verbose_name='bill reference')),
                ('bill_date', models.DateField(null=True, verbose_name='bill date')),
                ('provider', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.PROTECT, to='accounting.Third', verbose_name='provider')),
                ('storagearea', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='invoice.StorageArea', verbose_name='storage area')),
            ],
            options={
                'verbose_name': 'storage sheet',
                'verbose_name_plural': 'storage sheets',
                'ordering': ['-date', 'status'],
            },
        ),
        migrations.AddField(
            model_name='storagedetail',
            name='storagesheet',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='invoice.StorageSheet', verbose_name='storage sheet'),
        ),
        migrations.AddField(
            model_name='detail',
            name='storagearea',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.PROTECT, to='invoice.StorageArea', verbose_name='storage area'),
        ),
    ]
