# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-05-14 15:33
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('djangoplugins', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('projectroles', '0014_update_appsetting_value_json'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='appsetting',
            unique_together=set([('project', 'user', 'app_plugin', 'name')]),
        ),
    ]
