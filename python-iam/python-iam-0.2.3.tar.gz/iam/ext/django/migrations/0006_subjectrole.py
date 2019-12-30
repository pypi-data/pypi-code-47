# Generated by Django 2.2.6 on 2019-11-23 12:10

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('iam', '0005_auto_20191115_1348'),
    ]

    operations = [
        migrations.CreateModel(
            name='SubjectRole',
            fields=[
                ('id', models.UUIDField(db_column='id', default=uuid.uuid4, primary_key=True, serialize=False)),
                ('name', models.CharField(db_column='name', max_length=128)),
                ('title', models.CharField(db_column='title', max_length=128)),
                ('description', models.CharField(db_column='description', default='', max_length=1024)),
                ('system', models.BooleanField(db_column='system', default=False)),
                ('isglobal', models.BooleanField(db_column='isglobal', default=False)),
            ],
            options={
                'db_table': 'subjectroles',
                'default_permissions': [],
            },
        ),
    ]
