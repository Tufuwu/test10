# Generated by Django 2.2.15 on 2020-09-01 14:35

import caluma.caluma_core.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [("caluma_workflow", "0025_auto_20200901_1415")]

    operations = [
        migrations.AlterField(
            model_name="case",
            name="status",
            field=caluma.caluma_core.models.ChoicesCharField(
                choices=[
                    ("running", "Case is running and work items need to be completed."),
                    ("completed", "Case is done."),
                    ("canceled", "Case is canceled."),
                    ("suspended", "Case is suspended."),
                ],
                db_index=True,
                max_length=50,
            ),
        ),
        migrations.AlterField(
            model_name="historicalcase",
            name="status",
            field=caluma.caluma_core.models.ChoicesCharField(
                choices=[
                    ("running", "Case is running and work items need to be completed."),
                    ("completed", "Case is done."),
                    ("canceled", "Case is canceled."),
                    ("suspended", "Case is suspended."),
                ],
                db_index=True,
                max_length=50,
            ),
        ),
    ]
