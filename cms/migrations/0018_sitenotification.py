# Generated by Django 2.1.7 on 2019-05-22 06:15

from django.db import migrations, models
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [("cms", "0017_sections_generalize")]

    operations = [
        migrations.CreateModel(
            name="SiteNotification",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("message", wagtail.core.fields.RichTextField(max_length=255)),
            ],
        )
    ]
