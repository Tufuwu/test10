# Generated by Django 2.0.13 on 2019-10-25 17:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('odonto', '0021_auto_20190718_1647'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orthodonticassessment',
            name='assessment_and_review',
            field=models.BooleanField(default=False, verbose_name='Assess & review'),
        ),
    ]
