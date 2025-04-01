# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-09-09 06:29
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('lan', '0021_lan_allow_manual_payment'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Poll',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_open', models.BooleanField(default=False, verbose_name='open')),
                ('enforce_payment', models.BooleanField(default=False, help_text='Require users to have paid for the LAN in order to vote.', verbose_name='enforce payment')),
                ('lan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lan.LAN', verbose_name='LAN')),
            ],
            options={
                'verbose_name': 'poll',
                'verbose_name_plural': 'polls',
                'permissions': (('open_close', 'Can open and close polls'),),
            },
        ),
        migrations.CreateModel(
            name='PollOption',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.CharField(max_length=50, verbose_name='value')),
                ('poll', models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, to='poll.Poll', verbose_name='poll')),
            ],
            options={
                'verbose_name': 'poll option',
                'verbose_name_plural': 'poll options',
            },
        ),
        migrations.CreateModel(
            name='PollParticipant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('option', models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, to='poll.PollOption', verbose_name='option')),
                ('poll', models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, to='poll.Poll', verbose_name='poll')),
                ('user', models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='user')),
            ],
            options={
                'verbose_name': 'poll participant',
                'verbose_name_plural': 'poll participants',
            },
        ),
        migrations.CreateModel(
            name='PollTranslation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language', models.CharField(choices=[(b'nb', 'Norsk'), (b'en', 'English')], max_length=15, verbose_name='language')),
                ('title', models.CharField(max_length=50, verbose_name='title')),
                ('description', models.TextField(verbose_name='description')),
                ('model', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='translations', to='poll.Poll', verbose_name=b'poll')),
            ],
            options={
                'verbose_name': 'poll translation',
                'verbose_name_plural': 'poll translations',
            },
        ),
    ]
