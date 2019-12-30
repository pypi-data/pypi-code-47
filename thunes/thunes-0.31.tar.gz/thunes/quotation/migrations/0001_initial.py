# Generated by Django 2.2.6 on 2019-12-30 07:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Destination',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('currency', models.CharField(max_length=10, verbose_name='Source currency in ISO 4217 format')),
                ('amount', models.IntegerField(blank=True, null=True, verbose_name='Source amount')),
            ],
        ),
        migrations.CreateModel(
            name='Source',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country_iso_code', models.CharField(max_length=10, verbose_name='Country code in ISO 3166-1 alpha-3 format')),
                ('currency', models.CharField(max_length=10, verbose_name='Source currency in ISO 4217 format')),
                ('amount', models.IntegerField(blank=True, verbose_name='Source amount')),
            ],
        ),
        migrations.CreateModel(
            name='Quotation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quotation_id', models.CharField(max_length=50, verbose_name='Quotation reference ID')),
                ('external_id', models.CharField(max_length=50, verbose_name='External reference ID')),
                ('payer_id', models.CharField(max_length=50, verbose_name='Payer ID')),
                ('mode', models.CharField(choices=[('SOURCE_AMOUNT', 'Quotation created by specifying desired source'), ('DESTINATION_AMOUNT', 'Quotation created by specifying desired destination')], default='SOURCE_AMOUNT', max_length=50, verbose_name='Quotation mode')),
                ('destination', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='destinationEntity', to='quotation.Destination', verbose_name='Destination information')),
                ('source', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='sourceEntity', to='quotation.Source', verbose_name='Source information')),
            ],
            options={
                'verbose_name': 'quotation',
                'db_table': 'quotation',
            },
        ),
    ]
