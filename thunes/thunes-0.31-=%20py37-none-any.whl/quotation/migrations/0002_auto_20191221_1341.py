# Generated by Django 2.2.6 on 2019-12-21 05:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quotation', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='destination',
            name='amount',
            field=models.IntegerField(blank=True, max_length=10, verbose_name='Source amount'),
        ),
        migrations.AlterField(
            model_name='source',
            name='amount',
            field=models.IntegerField(blank=True, verbose_name='Source amount'),
        ),
    ]
