# Generated by Django 2.1.7 on 2019-04-30 16:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [("users", "0003_populate_legal_addresses")]

    operations = [
        migrations.AlterField(
            model_name="legaladdress",
            name="user",
            field=models.OneToOneField(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="legal_address",
                to=settings.AUTH_USER_MODEL,
            ),
        )
    ]
