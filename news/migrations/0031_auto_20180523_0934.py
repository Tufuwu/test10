# Generated by Django 2.0.2 on 2018-05-23 14:34

from django.db import migrations
import news.models
import snippets.models
import wagtail.core.blocks
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0030_auto_20180521_1137'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pressindex',
            name='intro',
        ),
        migrations.AlterField(
            model_name='pressindex',
            name='mentions',
            field=wagtail.core.fields.StreamField((('mention', wagtail.core.blocks.StructBlock((('source', news.models.NewsMentionChooserBlock(snippets.models.NewsSource)), ('url', wagtail.core.blocks.URLBlock()), ('headline', wagtail.core.blocks.CharBlock()), ('date', wagtail.core.blocks.DateBlock())), icon='document')),), null=True),
        ),
    ]
