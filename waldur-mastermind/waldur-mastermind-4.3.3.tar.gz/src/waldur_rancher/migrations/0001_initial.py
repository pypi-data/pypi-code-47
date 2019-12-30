# -*- coding: utf-8 -*-
# Generated by Django 1.11.24 on 2019-09-19 08:14
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import django_fsm
import model_utils.fields
import waldur_core.core.shims
import waldur_core.core.fields
import waldur_core.core.models
import waldur_core.core.validators
import waldur_core.logging.loggers
import waldur_core.structure.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('structure', '0009_project_is_removed'),
        ('contenttypes', '0002_remove_content_type_name'),
        ('taggit', '0002_auto_20150616_2121'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cluster',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('description', models.CharField(blank=True, max_length=500, verbose_name='description')),
                ('name', models.CharField(max_length=150, validators=[waldur_core.core.validators.validate_name], verbose_name='name')),
                ('uuid', waldur_core.core.fields.UUIDField()),
                ('error_message', models.TextField(blank=True)),
                ('state', django_fsm.FSMIntegerField(choices=[(5, 'Creation Scheduled'), (6, 'Creating'), (1, 'Update Scheduled'), (2, 'Updating'), (7, 'Deletion Scheduled'), (8, 'Deleting'), (3, 'OK'), (4, 'Erred')], default=5)),
                ('backend_id', models.CharField(blank=True, max_length=255, null=True)),
                ('node_command', models.CharField(blank=True, help_text='Rancher generated node installation command base.', max_length=1024)),
            ],
            bases=(waldur_core.core.models.DescendantMixin, waldur_core.core.models.BackendModelMixin, waldur_core.structure.models.StructureLoggableMixin, models.Model),
        ),
        migrations.CreateModel(
            name='Node',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('uuid', waldur_core.core.fields.UUIDField()),
                ('object_id', models.PositiveIntegerField(null=True)),
                ('cluster', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='waldur_rancher.Cluster')),
                ('content_type', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='contenttypes.ContentType')),
            ],
        ),
        migrations.CreateModel(
            name='RancherService',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', waldur_core.core.fields.UUIDField()),
                ('available_for_all', models.BooleanField(default=False, help_text='Service will be automatically added to all customers projects if it is available for all')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='structure.Customer', verbose_name='organization')),
            ],
            options={
                'verbose_name': 'Rancher provider',
                'verbose_name_plural': 'Rancher providers',
            },
            bases=(waldur_core.core.models.DescendantMixin, waldur_core.structure.models.StructureLoggableMixin, models.Model),
        ),
        migrations.CreateModel(
            name='RancherServiceProjectLink',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='structure.Project')),
                ('service', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='waldur_rancher.RancherService')),
            ],
            options={
                'abstract': False,
                'verbose_name': 'Rancher provider project link',
                'verbose_name_plural': 'Rancher provider project links',
            },
            bases=(waldur_core.core.models.DescendantMixin, waldur_core.logging.loggers.LoggableMixin, models.Model),
        ),
        migrations.AddField(
            model_name='rancherservice',
            name='projects',
            field=models.ManyToManyField(related_name='rancher_services', through='waldur_rancher.RancherServiceProjectLink', to='structure.Project'),
        ),
        migrations.AddField(
            model_name='rancherservice',
            name='settings',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='structure.ServiceSettings'),
        ),
        migrations.AddField(
            model_name='cluster',
            name='service_project_link',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='k8s_clusters', to='waldur_rancher.RancherServiceProjectLink'),
        ),
        migrations.AddField(
            model_name='cluster',
            name='tags',
            field=waldur_core.core.shims.TaggableManager(related_name='+', blank=True, help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags'),
        ),
        migrations.AlterUniqueTogether(
            name='rancherserviceprojectlink',
            unique_together=set([('service', 'project')]),
        ),
        migrations.AlterUniqueTogether(
            name='rancherservice',
            unique_together=set([('customer', 'settings')]),
        ),
        migrations.AlterUniqueTogether(
            name='node',
            unique_together=set([('content_type', 'object_id')]),
        ),
        migrations.AlterUniqueTogether(
            name='cluster',
            unique_together=set([('service_project_link', 'name'), ('service_project_link', 'backend_id')]),
        ),
    ]
