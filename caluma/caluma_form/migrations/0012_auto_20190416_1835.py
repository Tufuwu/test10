# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-04-16 18:35
from __future__ import unicode_literals

import localized_fields.fields.field
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [("caluma_form", "0011_auto_20190411_0607")]

    operations = [
        migrations.AddField(
            model_name="question",
            name="info_text",
            field=localized_fields.fields.field.LocalizedField(
                blank=True, null=True, required=[]
            ),
        ),
        migrations.AddField(
            model_name="question",
            name="placeholder",
            field=localized_fields.fields.field.LocalizedField(
                blank=True, null=True, required=[]
            ),
        ),
    ]
