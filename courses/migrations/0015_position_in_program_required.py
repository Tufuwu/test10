# -*- coding: utf-8 -*-
# Generated by Django 1.9.10 on 2016-10-19 16:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0014_program_ga_tracking_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='position_in_program',
            field=models.PositiveSmallIntegerField(),
        ),
    ]
