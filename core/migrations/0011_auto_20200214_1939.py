# Generated by Django 3.0.3 on 2020-02-15 03:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_timer_child'),
    ]

    operations = [
        migrations.AddField(
            model_name='diaperchange',
            name='notes',
            field=models.TextField(blank=True, null=True, verbose_name='Notes'),
        ),
        migrations.AddField(
            model_name='feeding',
            name='notes',
            field=models.TextField(blank=True, null=True, verbose_name='Notes'),
        ),
        migrations.AddField(
            model_name='sleep',
            name='notes',
            field=models.TextField(blank=True, null=True, verbose_name='Notes'),
        ),
        migrations.AddField(
            model_name='temperature',
            name='notes',
            field=models.TextField(blank=True, null=True, verbose_name='Notes'),
        ),
        migrations.AddField(
            model_name='weight',
            name='notes',
            field=models.TextField(blank=True, null=True, verbose_name='Notes'),
        ),
    ]
