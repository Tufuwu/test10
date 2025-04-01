# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-04-11 15:58
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import markupfield.fields
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='Project title', max_length=255)),
                ('type', models.CharField(choices=[('CATEGORY', 'Category'), ('PROJECT', 'Project')], default='PROJECT', help_text='Type of project ("CATEGORY", "PROJECT")', max_length=64)),
                ('description', models.CharField(help_text='Short project description', max_length=512)),
                ('readme', markupfield.fields.MarkupField(blank=True, help_text='Project README (optional, supports markdown)', null=True, rendered_field=True)),
                ('readme_markup_type', models.CharField(choices=[('', '--'), ('html', 'HTML'), ('plain', 'Plain'), ('markdown', 'Markdown'), ('restructuredtext', 'Restructured Text')], default='markdown', editable=False, max_length=30)),
                ('submit_status', models.CharField(default='OK', help_text='Status of project creation', max_length=64)),
                ('_readme_rendered', models.TextField(editable=False, null=True)),
                ('omics_uuid', models.UUIDField(default=uuid.uuid4, help_text='Project Omics UUID', unique=True)),
            ],
            options={
                'ordering': ['parent__title', 'title'],
            },
        ),
        migrations.CreateModel(
            name='ProjectInvite',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(help_text='Email address of the person to be invited', max_length=254)),
                ('date_created', models.DateTimeField(auto_now_add=True, help_text='DateTime of invite creation')),
                ('date_expire', models.DateTimeField(help_text='Expiration of invite as DateTime')),
                ('message', models.TextField(blank=True, help_text='Message to be included in the invite email (optional)')),
                ('secret', models.CharField(help_text='Secret token provided to user with the invite', max_length=255, unique=True)),
                ('active', models.BooleanField(default=True, help_text='Status of the invite (False if claimed or revoked)')),
                ('omics_uuid', models.UUIDField(default=uuid.uuid4, help_text='ProjectInvite Omics UUID', unique=True)),
            ],
            options={
                'ordering': ['project__title', 'email', 'role__name'],
            },
        ),
        migrations.CreateModel(
            name='ProjectSetting',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Name of the setting', max_length=255)),
                ('type', models.CharField(choices=[('BOOLEAN', 'Boolean'), ('INTEGER', 'Integer'), ('STRING', 'String')], help_text='Type of the setting', max_length=64)),
                ('value', models.CharField(blank=True, help_text='Value of the setting', max_length=255, null=True)),
                ('omics_uuid', models.UUIDField(default=uuid.uuid4, help_text='ProjectSetting Omics UUID', unique=True)),
            ],
            options={
                'ordering': ['project__title', 'app_plugin__name', 'name'],
            },
        ),
        migrations.CreateModel(
            name='ProjectUserTag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='STARRED', help_text='Name of tag to be assigned', max_length=64)),
                ('omics_uuid', models.UUIDField(default=uuid.uuid4, help_text='ProjectUserTag Omics UUID', unique=True)),
            ],
            options={
                'ordering': ['project__title', 'user__username', 'name'],
            },
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Name of role', max_length=64, unique=True)),
                ('description', models.TextField(help_text='Role description')),
            ],
        ),
        migrations.CreateModel(
            name='RoleAssignment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('omics_uuid', models.UUIDField(default=uuid.uuid4, help_text='RoleAssignment Omics UUID', unique=True)),
                ('project', models.ForeignKey(help_text='Project in which role is assigned', on_delete=django.db.models.deletion.CASCADE, related_name='roles', to='projectroles.Project')),
                ('role', models.ForeignKey(help_text='Role to be assigned', on_delete=django.db.models.deletion.CASCADE, related_name='assignments', to='projectroles.Role')),
            ],
            options={
                'ordering': ['project__parent__title', 'project__title', 'role__name', 'user__username'],
            },
        ),
    ]
