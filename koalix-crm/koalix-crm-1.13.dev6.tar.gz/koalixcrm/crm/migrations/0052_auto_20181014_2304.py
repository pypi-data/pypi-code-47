# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-10-12 20:56
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


def reverse_func(apps, schema_editor):
    return 1


def restore_from_backup(apps, schema_editor):
    Position = apps.get_model("crm", "Position")
    ProductType = apps.get_model("crm", "ProductType")
    CustomerGroupTransform = apps.get_model("crm", "CustomerGroupTransform")
    Price = apps.get_model("crm", "Price")
    ProductPrice = apps.get_model("crm", "ProductPrice")
    UnitTransform = apps.get_model("crm", "UnitTransform")
    db_alias = schema_editor.connection.alias
    all_positions = Position.objects.using(db_alias).all()
    for position in all_positions:
        product_type = ProductType.objects.using(db_alias).get(id=position.product_backup)
        position.product_type = product_type
        position.save()
    all_customer_group_transforms = CustomerGroupTransform.objects.using(db_alias).all()
    for customer_group_transform in all_customer_group_transforms:
        product_type = ProductType.objects.using(db_alias).get(id=customer_group_transform.product_backup)
        customer_group_transform.product_type = product_type
        customer_group_transform.save()
    all_prices = Price.objects.using(db_alias).all()
    for price in all_prices:
        product_type = ProductType.objects.using(db_alias).get(id=price.product_backup)
        new_product_price = ProductPrice.objects.using(db_alias).create(unit=price.unit,
                                                                        currency=price.currency,
                                                                        customer_group=price.customer_group,
                                                                        price=price.price,
                                                                        valid_from=price.valid_from,
                                                                        valid_until=price.valid_until,
                                                                        product_type=product_type)
        new_product_price.save()
        price.delete()
    all_unit_transforms = UnitTransform.objects.using(db_alias).all()
    for unit_transform in all_unit_transforms:
        product_type = ProductType.objects.using(db_alias).get(id=unit_transform.product_backup)
        unit_transform.product_type = product_type
        unit_transform.save()


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0051_auto_20181014_2302'),
    ]

    operations = [
        migrations.RunPython(restore_from_backup, reverse_func),
    ]
