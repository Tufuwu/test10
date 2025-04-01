# Generated by Django 3.2.7 on 2021-10-01 15:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("resources", "0081_auto_20210928_1820"),
        ("users", "0079_remove_authorization_stream"),
    ]

    operations = [
        migrations.AddField(
            model_name="userprofile",
            name="favorites",
            field=models.ManyToManyField(
                blank=True,
                help_text="The partner(s) that the user has marked as favorite.",
                to="resources.Partner",
            ),
        ),
    ]
