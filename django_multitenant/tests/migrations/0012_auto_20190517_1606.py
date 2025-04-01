# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-05-17 16:06
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django_multitenant.fields


class Migration(migrations.Migration):

    dependencies = [
        ("tests", "0011_distribute_new_table"),
    ]

    operations = [
        migrations.AlterField(
            model_name="projectmanager",
            name="project",
            field=django_multitenant.fields.TenantForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="tests.Project"
            ),
        ),
        migrations.AddField(
            model_name="tempmodel",
            name="project",
            field=django_multitenant.fields.TenantForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="tests.Project",
            ),
        ),
        migrations.AlterField(
            model_name="tempmodel",
            name="account",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="tests.Account",
                db_constraint=False,
            ),
        ),
    ]
