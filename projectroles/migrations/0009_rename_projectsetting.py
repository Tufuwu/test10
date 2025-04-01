# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-05-09 13:04
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('djangoplugins', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('projectroles', '0008_auto_20190426_0606'),
    ]

    operations = [
        migrations.CreateModel(
            name='AppSetting',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Name of the setting', max_length=255)),
                ('type', models.CharField(choices=[('BOOLEAN', 'Boolean'), ('INTEGER', 'Integer'), ('STRING', 'String')], help_text='Type of the setting', max_length=64)),
                ('value', models.CharField(blank=True, help_text='Value of the setting', max_length=255, null=True)),
                ('sodar_uuid', models.UUIDField(default=uuid.uuid4, help_text='AppSetting SODAR UUID', unique=True)),
                ('app_plugin', models.ForeignKey(help_text='App to which the setting belongs', on_delete=django.db.models.deletion.CASCADE, related_name='settings', to='djangoplugins.Plugin')),
                ('project', models.ForeignKey(blank=True, help_text='Project to which the setting belongs', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='settings', to='projectroles.Project')),
                ('user', models.ForeignKey(blank=True, help_text='User to which the setting belongs', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_settings', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['project__title', 'app_plugin__name', 'name'],
            },
        ),
        migrations.AlterUniqueTogether(
            name='projectsetting',
            unique_together=set([]),
        ),
        migrations.RemoveField(
            model_name='projectsetting',
            name='app_plugin',
        ),
        migrations.RemoveField(
            model_name='projectsetting',
            name='project',
        ),
        migrations.RemoveField(
            model_name='projectsetting',
            name='user',
        ),
        migrations.DeleteModel(
            name='ProjectSetting',
        ),
        migrations.AlterUniqueTogether(
            name='appsetting',
            unique_together=set([('project', 'app_plugin', 'name')]),
        ),
    ]
