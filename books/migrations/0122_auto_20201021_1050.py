# Generated by Django 3.0.4 on 2020-10-21 15:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0121_auto_20201020_1707'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='savings',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
