# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-04-29 04:08
from __future__ import unicode_literals

from django.db import migrations, models


def populate_updated_on(apps, schema_editor):
    Matchup = apps.get_model('matchups', 'Matchup')

    for matchup in Matchup.objects.filter(updated_on__isnull=True):
        matchup.updated_on = matchup.created_on
        matchup.save()


class Migration(migrations.Migration):

    dependencies = [
        ('matchups', '0005_matchup_remove_email_add_user'),
    ]

    operations = [
        # Introduce the updated_on field as nullable at first.
        migrations.AddField(
            model_name='matchup',
            name='updated_on',
            field=models.DateTimeField(null=True),
        ),

        # Set updated_on = created_on for existing matchups.
        migrations.RunPython(populate_updated_on),

        # Now add a non-null constraint.
        migrations.AlterField(
            model_name='matchup',
            name='updated_on',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
