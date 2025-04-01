# Generated by Django 2.1.1 on 2018-10-22 14:15
from django.db import migrations

from openwisp_users.migrations import create_default_groups


class Migration(migrations.Migration):

    dependencies = [('openwisp_users', '0003_default_organization')]

    operations = [
        migrations.RunPython(
            create_default_groups, reverse_code=migrations.RunPython.noop
        )
    ]
