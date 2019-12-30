# Generated by Django 2.0.1 on 2018-01-30 18:33

from django.db import migrations, models

import enumchoicefield.fields
import enumchoicefield.tests.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ChoiceModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('choice', enumchoicefield.fields.EnumChoiceField(enum_class=enumchoicefield.tests.models.MyEnum, max_length=3)),
            ],
            options={
                'ordering': ('id',),
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='DefaultChoiceModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('choice', enumchoicefield.fields.EnumChoiceField(default=enumchoicefield.tests.models.MyEnum(3), enum_class=enumchoicefield.tests.models.MyEnum, max_length=3)),
            ],
            options={
                'ordering': ('id',),
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='NullableChoiceModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('choice', enumchoicefield.fields.EnumChoiceField(blank=True, enum_class=enumchoicefield.tests.models.MyEnum, max_length=3)),
            ],
            options={
                'ordering': ('id',),
                'abstract': False,
            },
        ),
    ]
