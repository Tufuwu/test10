# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-03 15:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('errata', '0012_auto_20170202_1423'),
    ]

    operations = [
        migrations.AddField(
            model_name='errata',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to='errata/user_uploads'),
        ),
    ]
