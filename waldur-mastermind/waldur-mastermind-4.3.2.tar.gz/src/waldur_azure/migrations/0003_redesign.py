# -*- coding: utf-8 -*-
# Generated by Django 1.11.18 on 2019-01-28 14:05
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import django_fsm
import model_utils.fields
import re
import waldur_core.core.shims
import waldur_azure.validators
import waldur_core.core.fields
import waldur_core.core.models
import waldur_core.core.validators
import waldur_core.logging.loggers


class Migration(migrations.Migration):

    dependencies = [
        ('structure', '0005_customer_domain'),
        ('core', '0003_enlarge_username'),
        ('taggit', '0002_auto_20150616_2121'),
        ('waldur_azure', '0002_immutable_default_json'),
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, validators=[waldur_core.core.validators.validate_name], verbose_name='name')),
                ('uuid', waldur_core.core.fields.UUIDField()),
                ('latitude', models.FloatField(blank=True, null=True)),
                ('longitude', models.FloatField(blank=True, null=True)),
                ('backend_id', models.CharField(db_index=True, max_length=255)),
                ('settings', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='structure.ServiceSettings')),
            ],
            options={
                'abstract': False,
            },
            bases=(waldur_core.core.models.BackendModelMixin, models.Model),
        ),
        migrations.CreateModel(
            name='Network',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('description', models.CharField(blank=True, max_length=500, verbose_name='description')),
                ('uuid', waldur_core.core.fields.UUIDField()),
                ('error_message', models.TextField(blank=True)),
                ('runtime_state', models.CharField(blank=True, max_length=150, verbose_name='runtime state')),
                ('state', django_fsm.FSMIntegerField(choices=[(5, 'Creation Scheduled'), (6, 'Creating'), (1, 'Update Scheduled'), (2, 'Updating'), (7, 'Deletion Scheduled'), (8, 'Deleting'), (3, 'OK'), (4, 'Erred')], default=5)),
                ('backend_id', models.CharField(blank=True, max_length=255)),
                ('name', models.CharField(max_length=64, validators=[django.core.validators.RegexValidator(message='The name can contain only letters, numbers, underscore, period and hyphens.', regex=re.compile('[a-zA-Z][a-zA-Z0-9._-]+$'))])),
                ('cidr', models.CharField(max_length=32)),
            ],
            options={
                'abstract': False,
            },
            bases=(waldur_core.core.models.DescendantMixin, waldur_core.core.models.BackendModelMixin, waldur_core.logging.loggers.LoggableMixin, models.Model),
        ),
        migrations.CreateModel(
            name='NetworkInterface',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('description', models.CharField(blank=True, max_length=500, verbose_name='description')),
                ('uuid', waldur_core.core.fields.UUIDField()),
                ('error_message', models.TextField(blank=True)),
                ('runtime_state', models.CharField(blank=True, max_length=150, verbose_name='runtime state')),
                ('state', django_fsm.FSMIntegerField(choices=[(5, 'Creation Scheduled'), (6, 'Creating'), (1, 'Update Scheduled'), (2, 'Updating'), (7, 'Deletion Scheduled'), (8, 'Deleting'), (3, 'OK'), (4, 'Erred')], default=5)),
                ('backend_id', models.CharField(blank=True, max_length=255)),
                ('name', models.CharField(max_length=80, validators=[django.core.validators.RegexValidator(message='The name can contain only letters, numbers, underscore, period and hyphens.', regex=re.compile('[a-zA-Z][a-zA-Z0-9._-]+$'))])),
                ('config_name', models.CharField(max_length=255)),
            ],
            options={
                'abstract': False,
            },
            bases=(waldur_core.core.models.DescendantMixin, waldur_core.core.models.BackendModelMixin, waldur_core.logging.loggers.LoggableMixin, models.Model),
        ),
        migrations.CreateModel(
            name='ResourceGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('description', models.CharField(blank=True, max_length=500, verbose_name='description')),
                ('uuid', waldur_core.core.fields.UUIDField()),
                ('error_message', models.TextField(blank=True)),
                ('runtime_state', models.CharField(blank=True, max_length=150, verbose_name='runtime state')),
                ('state', django_fsm.FSMIntegerField(choices=[(5, 'Creation Scheduled'), (6, 'Creating'), (1, 'Update Scheduled'), (2, 'Updating'), (7, 'Deletion Scheduled'), (8, 'Deleting'), (3, 'OK'), (4, 'Erred')], default=5)),
                ('backend_id', models.CharField(blank=True, max_length=255)),
                ('name', models.CharField(max_length=90, validators=[django.core.validators.RegexValidator(message='The name can include alphanumeric, underscore, parentheses, hyphen, period (except at end), and Unicode characters that match the allowed characters.', regex=re.compile('^[-\\w._()]+$'))])),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='waldur_azure.Location')),
            ],
            options={
                'abstract': False,
            },
            bases=(waldur_core.core.models.DescendantMixin, waldur_core.core.models.BackendModelMixin, waldur_core.logging.loggers.LoggableMixin, models.Model),
        ),
        migrations.CreateModel(
            name='Size',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, validators=[waldur_core.core.validators.validate_name], verbose_name='name')),
                ('uuid', waldur_core.core.fields.UUIDField()),
                ('backend_id', models.CharField(db_index=True, max_length=255)),
                ('max_data_disk_count', models.PositiveIntegerField()),
                ('memory_in_mb', models.PositiveIntegerField()),
                ('number_of_cores', models.PositiveIntegerField()),
                ('os_disk_size_in_mb', models.PositiveIntegerField()),
                ('resource_disk_size_in_mb', models.PositiveIntegerField()),
                ('settings', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='structure.ServiceSettings')),
            ],
            options={
                'abstract': False,
            },
            bases=(waldur_core.core.models.BackendModelMixin, models.Model),
        ),
        migrations.CreateModel(
            name='SQLDatabase',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('description', models.CharField(blank=True, max_length=500, verbose_name='description')),
                ('name', models.CharField(max_length=150, validators=[waldur_core.core.validators.validate_name], verbose_name='name')),
                ('uuid', waldur_core.core.fields.UUIDField()),
                ('error_message', models.TextField(blank=True)),
                ('runtime_state', models.CharField(blank=True, max_length=150, verbose_name='runtime state')),
                ('state', django_fsm.FSMIntegerField(choices=[(5, 'Creation Scheduled'), (6, 'Creating'), (1, 'Update Scheduled'), (2, 'Updating'), (7, 'Deletion Scheduled'), (8, 'Deleting'), (3, 'OK'), (4, 'Erred')], default=5)),
                ('backend_id', models.CharField(blank=True, max_length=255)),
                ('charset', models.CharField(blank=True, max_length=255)),
                ('collation', models.CharField(blank=True, max_length=255)),
                ('resource_group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='waldur_azure.ResourceGroup')),
            ],
            options={
                'abstract': False,
            },
            bases=(waldur_core.core.models.DescendantMixin, waldur_core.core.models.BackendModelMixin, waldur_core.logging.loggers.LoggableMixin, models.Model),
        ),
        migrations.CreateModel(
            name='SQLServer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('description', models.CharField(blank=True, max_length=500, verbose_name='description')),
                ('name', models.CharField(max_length=150, validators=[django.core.validators.RegexValidator(message='The name can only be made up of lowercase letters "a"-"z", the numbers 0-9 and the hyphen. The hyphen may not lead or trail in the name.', regex=re.compile('[a-z0-9][a-z0-9-]+[a-z0-9]$'))], verbose_name='name')),
                ('uuid', waldur_core.core.fields.UUIDField()),
                ('error_message', models.TextField(blank=True)),
                ('runtime_state', models.CharField(blank=True, max_length=150, verbose_name='runtime state')),
                ('state', django_fsm.FSMIntegerField(choices=[(5, 'Creation Scheduled'), (6, 'Creating'), (1, 'Update Scheduled'), (2, 'Updating'), (7, 'Deletion Scheduled'), (8, 'Deleting'), (3, 'OK'), (4, 'Erred')], default=5)),
                ('backend_id', models.CharField(blank=True, max_length=255)),
                ('username', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=50)),
                ('storage_mb', models.PositiveIntegerField(null=True)),
                ('resource_group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='waldur_azure.ResourceGroup')),
            ],
            options={
                'abstract': False,
            },
            bases=(waldur_core.core.models.DescendantMixin, waldur_core.core.models.BackendModelMixin, waldur_core.logging.loggers.LoggableMixin, models.Model),
        ),
        migrations.CreateModel(
            name='SubNet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('description', models.CharField(blank=True, max_length=500, verbose_name='description')),
                ('uuid', waldur_core.core.fields.UUIDField()),
                ('error_message', models.TextField(blank=True)),
                ('runtime_state', models.CharField(blank=True, max_length=150, verbose_name='runtime state')),
                ('state', django_fsm.FSMIntegerField(choices=[(5, 'Creation Scheduled'), (6, 'Creating'), (1, 'Update Scheduled'), (2, 'Updating'), (7, 'Deletion Scheduled'), (8, 'Deleting'), (3, 'OK'), (4, 'Erred')], default=5)),
                ('backend_id', models.CharField(blank=True, max_length=255)),
                ('name', models.CharField(max_length=80, validators=[django.core.validators.RegexValidator(message='The name can contain only letters, numbers, underscore, period and hyphens.', regex=re.compile('[a-zA-Z][a-zA-Z0-9._-]+$'))])),
                ('cidr', models.CharField(max_length=32)),
                ('network', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='waldur_azure.Network')),
                ('resource_group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='waldur_azure.ResourceGroup')),
            ],
            options={
                'abstract': False,
            },
            bases=(waldur_core.core.models.DescendantMixin, waldur_core.core.models.BackendModelMixin, waldur_core.logging.loggers.LoggableMixin, models.Model),
        ),
        migrations.RemoveField(
            model_name='instanceendpoint',
            name='instance',
        ),
        migrations.RemoveField(
            model_name='azureserviceprojectlink',
            name='cloud_service_name',
        ),
        migrations.RemoveField(
            model_name='virtualmachine',
            name='private_ips',
        ),
        migrations.RemoveField(
            model_name='virtualmachine',
            name='public_ips',
        ),
        migrations.RemoveField(
            model_name='virtualmachine',
            name='user_password',
        ),
        migrations.RemoveField(
            model_name='virtualmachine',
            name='user_username',
        ),
        migrations.AddField(
            model_name='image',
            name='offer',
            field=models.CharField(default=None, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='image',
            name='publisher',
            field=models.CharField(default=None, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='image',
            name='settings',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='structure.ServiceSettings'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='image',
            name='sku',
            field=models.CharField(default=None, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='image',
            name='version',
            field=models.CharField(default=None, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='virtualmachine',
            name='image',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='waldur_azure.Image'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='virtualmachine',
            name='password',
            field=models.CharField(default=None, max_length=72, validators=[django.core.validators.MinLengthValidator(6), django.core.validators.MaxLengthValidator(72), waldur_azure.validators.validate_password]),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='virtualmachine',
            name='ssh_key',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.SshPublicKey'),
        ),
        migrations.AddField(
            model_name='virtualmachine',
            name='username',
            field=models.CharField(default=None, max_length=32, validators=[waldur_azure.validators.VirtualMachineUsernameValidator]),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='image',
            name='backend_id',
            field=models.CharField(db_index=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='virtualmachine',
            name='name',
            field=models.CharField(max_length=15, validators=[django.core.validators.RegexValidator(message='The name can contain only letters, numbers, and hyphens. The name must be shorter than 15 characters and start with a letter and must end with a letter or a number.', regex=re.compile('[a-zA-Z][a-zA-Z0-9-]{0,13}[a-zA-Z0-9]$'))]),
        ),
        migrations.AlterUniqueTogether(
            name='image',
            unique_together=set([('settings', 'backend_id')]),
        ),
        migrations.DeleteModel(
            name='InstanceEndpoint',
        ),
        migrations.AddField(
            model_name='subnet',
            name='service_project_link',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='waldur_azure.AzureServiceProjectLink'),
        ),
        migrations.AddField(
            model_name='subnet',
            name='tags',
            field=waldur_core.core.shims.TaggableManager(related_name='+', blank=True, help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags'),
        ),
        migrations.AddField(
            model_name='sqlserver',
            name='service_project_link',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='waldur_azure.AzureServiceProjectLink'),
        ),
        migrations.AddField(
            model_name='sqlserver',
            name='tags',
            field=waldur_core.core.shims.TaggableManager(related_name='+', blank=True, help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags'),
        ),
        migrations.AddField(
            model_name='sqldatabase',
            name='server',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='waldur_azure.SQLServer'),
        ),
        migrations.AddField(
            model_name='sqldatabase',
            name='service_project_link',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='waldur_azure.AzureServiceProjectLink'),
        ),
        migrations.AddField(
            model_name='sqldatabase',
            name='tags',
            field=waldur_core.core.shims.TaggableManager(related_name='+', blank=True, help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags'),
        ),
        migrations.AddField(
            model_name='resourcegroup',
            name='service_project_link',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='waldur_azure.AzureServiceProjectLink'),
        ),
        migrations.AddField(
            model_name='resourcegroup',
            name='tags',
            field=waldur_core.core.shims.TaggableManager(related_name='+', blank=True, help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags'),
        ),
        migrations.AddField(
            model_name='networkinterface',
            name='resource_group',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='waldur_azure.ResourceGroup'),
        ),
        migrations.AddField(
            model_name='networkinterface',
            name='service_project_link',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='waldur_azure.AzureServiceProjectLink'),
        ),
        migrations.AddField(
            model_name='networkinterface',
            name='subnet',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='waldur_azure.SubNet'),
        ),
        migrations.AddField(
            model_name='networkinterface',
            name='tags',
            field=waldur_core.core.shims.TaggableManager(related_name='+', blank=True, help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags'),
        ),
        migrations.AddField(
            model_name='network',
            name='resource_group',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='waldur_azure.ResourceGroup'),
        ),
        migrations.AddField(
            model_name='network',
            name='service_project_link',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='waldur_azure.AzureServiceProjectLink'),
        ),
        migrations.AddField(
            model_name='network',
            name='tags',
            field=waldur_core.core.shims.TaggableManager(related_name='+', blank=True, help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags'),
        ),
        migrations.AddField(
            model_name='virtualmachine',
            name='network_interface',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='waldur_azure.NetworkInterface'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='virtualmachine',
            name='resource_group',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='waldur_azure.ResourceGroup'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='virtualmachine',
            name='size',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='waldur_azure.Size'),
            preserve_default=False,
        ),
        migrations.AlterUniqueTogether(
            name='size',
            unique_together=set([('settings', 'backend_id')]),
        ),
    ]
