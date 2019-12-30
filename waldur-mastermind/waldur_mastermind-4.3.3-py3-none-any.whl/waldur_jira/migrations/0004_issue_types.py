# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-19 13:04
from django.db import migrations, models
import django.db.models.deletion
import waldur_core.core.fields
import waldur_core.core.models
import waldur_core.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('structure', '0001_squashed_0054'),
        ('waldur_jira', '0003_project_template'),
    ]

    operations = [
        migrations.CreateModel(
            name='IssueType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(blank=True, max_length=500, verbose_name='description')),
                ('name', models.CharField(max_length=150, validators=[waldur_core.core.validators.validate_name], verbose_name='name')),
                ('icon_url', models.URLField(blank=True, verbose_name='icon url')),
                ('uuid', waldur_core.core.fields.UUIDField()),
                ('backend_id', models.CharField(db_index=True, max_length=255)),
            ],
            options={
                'abstract': False,
                'verbose_name': 'Issue type',
                'verbose_name_plural': 'Issue types',
            },
            bases=(waldur_core.core.models.BackendModelMixin, models.Model),
        ),
        migrations.RemoveField(
            model_name='project',
            name='default_issue_type',
        ),
        migrations.AlterField(
            model_name='issue',
            name='type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='waldur_jira.IssueType'),
        ),
        migrations.AddField(
            model_name='issuetype',
            name='projects',
            field=models.ManyToManyField(related_name='issue_types', to='waldur_jira.Project'),
        ),
        migrations.AddField(
            model_name='issuetype',
            name='settings',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='structure.ServiceSettings'),
        ),
    ]
