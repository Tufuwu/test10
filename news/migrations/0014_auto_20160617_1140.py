# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-17 16:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0013_auto_20160616_1033'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newsarticle',
            name='subheading',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
    ]
