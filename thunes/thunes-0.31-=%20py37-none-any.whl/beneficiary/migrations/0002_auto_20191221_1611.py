# Generated by Django 2.2.6 on 2019-12-21 08:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('beneficiary', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='beneficiary',
            old_name='data_of_birth',
            new_name='date_of_birth',
        ),
    ]
