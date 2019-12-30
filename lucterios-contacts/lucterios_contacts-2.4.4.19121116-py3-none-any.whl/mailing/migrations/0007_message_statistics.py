# Generated by Django 2.1.8 on 2019-05-18 15:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mailing', '0006_message_doc_in_link'),
    ]

    operations = [
        migrations.AddField(
            model_name='emailsent',
            name='last_open_date',
            field=models.DateTimeField(default=None, null=True, verbose_name='last open date'),
        ),
        migrations.AddField(
            model_name='emailsent',
            name='nb_open',
            field=models.IntegerField(default=0, verbose_name='number open'),
        ),
    ]
