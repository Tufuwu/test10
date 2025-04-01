# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2018-01-25 17:04
from __future__ import unicode_literals

from django.conf import settings
import django.contrib.postgres.fields.jsonb
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0026_course_should_display_progress'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('grades', '0011_mm_program_certificate'),
    ]

    operations = [
        migrations.CreateModel(
            name='CombinedFinalGrade',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('grade', models.FloatField(validators=[django.core.validators.MinValueValidator(0.0), django.core.validators.MaxValueValidator(1.0)])),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses.Course')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='CombinedFinalGradeAudit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('data_before', django.contrib.postgres.fields.jsonb.JSONField(blank=True, null=True)),
                ('data_after', django.contrib.postgres.fields.jsonb.JSONField(blank=True, null=True)),
                ('acting_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
                ('combined_final_grade', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='grades.CombinedFinalGrade')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AlterUniqueTogether(
            name='combinedfinalgrade',
            unique_together=set([('user', 'course')]),
        ),
    ]
