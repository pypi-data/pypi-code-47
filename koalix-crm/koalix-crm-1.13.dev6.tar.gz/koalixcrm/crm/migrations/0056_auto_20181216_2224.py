# Generated by Django 2.1.4 on 2018-12-16 22:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0055_auto_20181022_1937'),
    ]

    operations = [
        migrations.AlterField(
            model_name='call',
            name='last_modified_by',
            field=models.ForeignKey(blank=True, limit_choices_to={'is_staff': True}, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='db_calllstmodified', to=settings.AUTH_USER_MODEL, verbose_name='Last modified by'),
        ),
        migrations.AlterField(
            model_name='call',
            name='staff',
            field=models.ForeignKey(blank=True, limit_choices_to={'is_staff': True}, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='db_relcallstaff', to=settings.AUTH_USER_MODEL, verbose_name='Staff'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='last_modified_by',
            field=models.ForeignKey(blank=True, limit_choices_to={'is_staff': True}, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Last modified by'),
        ),
        migrations.AlterField(
            model_name='contract',
            name='last_modified_by',
            field=models.ForeignKey(limit_choices_to={'is_staff': True}, on_delete=django.db.models.deletion.CASCADE, related_name='db_contractlstmodified', to=settings.AUTH_USER_MODEL, verbose_name='Last modified by'),
        ),
        migrations.AlterField(
            model_name='contract',
            name='staff',
            field=models.ForeignKey(blank=True, limit_choices_to={'is_staff': True}, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='db_relcontractstaff', to=settings.AUTH_USER_MODEL, verbose_name='Staff'),
        ),
        migrations.AlterField(
            model_name='genericprojectlink',
            name='last_modified_by',
            field=models.ForeignKey(limit_choices_to={'is_staff': True}, on_delete=django.db.models.deletion.CASCADE, related_name='db_project_link_last_modified', to=settings.AUTH_USER_MODEL, verbose_name='Last modified by'),
        ),
        migrations.AlterField(
            model_name='generictasklink',
            name='last_modified_by',
            field=models.ForeignKey(limit_choices_to={'is_staff': True}, on_delete=django.db.models.deletion.CASCADE, related_name='db_task_link_last_modified', to=settings.AUTH_USER_MODEL, verbose_name='Last modified by'),
        ),
        migrations.AlterField(
            model_name='position',
            name='product_type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='crm.ProductType', verbose_name='Product'),
        ),
        migrations.AlterField(
            model_name='producttype',
            name='last_modified_by',
            field=models.ForeignKey(blank=True, limit_choices_to={'is_staff': True}, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Last modified by'),
        ),
        migrations.AlterField(
            model_name='project',
            name='last_modified_by',
            field=models.ForeignKey(limit_choices_to={'is_staff': True}, on_delete=django.db.models.deletion.CASCADE, related_name='db_project_last_modified', to=settings.AUTH_USER_MODEL, verbose_name='Last modified by'),
        ),
        migrations.AlterField(
            model_name='project',
            name='project_manager',
            field=models.ForeignKey(blank=True, limit_choices_to={'is_staff': True}, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='db_rel_project_staff', to=settings.AUTH_USER_MODEL, verbose_name='Staff'),
        ),
        migrations.AlterField(
            model_name='salesdocument',
            name='last_modified_by',
            field=models.ForeignKey(blank='True', limit_choices_to={'is_staff': True}, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='db_lstscmodified', to=settings.AUTH_USER_MODEL, verbose_name='Last modified by'),
        ),
        migrations.AlterField(
            model_name='salesdocument',
            name='staff',
            field=models.ForeignKey(blank=True, limit_choices_to={'is_staff': True}, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='db_relscstaff', to=settings.AUTH_USER_MODEL, verbose_name='Staff'),
        ),
    ]
