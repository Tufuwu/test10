# Generated by Django 3.0.4 on 2021-01-26 16:56

from django.db import migrations, models
import django.db.models.deletion
import pages.custom_blocks
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0059_apply_collection_ordering'),
        ('wagtailforms', '0004_add_verbose_name_plural'),
        ('wagtailredirects', '0006_redirect_increase_max_length'),
        ('pages', '0018_auto_20210126_0947'),
    ]

    operations = [
        migrations.CreateModel(
            name='Impact',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('improving_access', wagtail.core.fields.StreamField([('image', wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(required=False)), ('alt_text', wagtail.core.blocks.CharBlock(required=False)), ('link', wagtail.core.blocks.URLBlock(required=False)), ('alignment', pages.custom_blocks.ImageFormatChoiceBlock()), ('identifier', wagtail.core.blocks.CharBlock(help_text='Used by the frontend for Google Analytics.', required=False))])), ('heading', wagtail.core.blocks.CharBlock()), ('description', wagtail.core.blocks.RichTextBlock()), ('button_text', wagtail.core.blocks.CharBlock()), ('button_href', wagtail.core.blocks.URLBlock())], blank=True)),
                ('reach', wagtail.core.fields.StreamField([('heading', wagtail.core.blocks.CharBlock()), ('description', wagtail.core.blocks.RichTextBlock()), ('cards', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('icon', pages.custom_blocks.APIImageChooserBlock(required=False)), ('title', wagtail.core.blocks.CharBlock(required=True)), ('description', wagtail.core.blocks.RichTextBlock(required=True))])))], blank=True)),
                ('quote', wagtail.core.fields.StreamField([('image', wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(required=False)), ('alt_text', wagtail.core.blocks.CharBlock(required=False)), ('link', wagtail.core.blocks.URLBlock(required=False)), ('alignment', pages.custom_blocks.ImageFormatChoiceBlock()), ('identifier', wagtail.core.blocks.CharBlock(help_text='Used by the frontend for Google Analytics.', required=False))])), ('quote', wagtail.core.blocks.RichTextBlock())], blank=True)),
                ('making_a_difference', wagtail.core.fields.StreamField([('heading', wagtail.core.blocks.CharBlock()), ('description', wagtail.core.blocks.RichTextBlock()), ('stories', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('image', pages.custom_blocks.APIImageChooserBlock(required=False)), ('story_text', wagtail.core.blocks.TextBlock(required=False)), ('embeded_video', wagtail.core.blocks.RawHTMLBlock(required=False))])))], blank=True)),
                ('disruption', wagtail.core.fields.StreamField([('heading', wagtail.core.blocks.CharBlock()), ('description', wagtail.core.blocks.TextBlock()), ('graph', wagtail.core.blocks.StructBlock([('top_caption', wagtail.core.blocks.CharBlock()), ('bottom_caption', wagtail.core.blocks.RichTextBlock()), ('image', wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(required=False)), ('alt_text', wagtail.core.blocks.CharBlock(required=False)), ('link', wagtail.core.blocks.URLBlock(required=False)), ('alignment', pages.custom_blocks.ImageFormatChoiceBlock()), ('identifier', wagtail.core.blocks.CharBlock(help_text='Used by the frontend for Google Analytics.', required=False))], required=False)), ('image_alt_text', wagtail.core.blocks.CharBlock(required=False))]))], blank=True)),
                ('supporter_community', wagtail.core.fields.StreamField([('heading', wagtail.core.blocks.CharBlock()), ('image', wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(required=False)), ('alt_text', wagtail.core.blocks.CharBlock(required=False)), ('link', wagtail.core.blocks.URLBlock(required=False)), ('alignment', pages.custom_blocks.ImageFormatChoiceBlock()), ('identifier', wagtail.core.blocks.CharBlock(help_text='Used by the frontend for Google Analytics.', required=False))])), ('quote', wagtail.core.blocks.RichTextBlock()), ('link_text', wagtail.core.blocks.CharBlock()), ('link_href', wagtail.core.blocks.URLBlock())], blank=True)),
                ('giving', wagtail.core.fields.StreamField([('heading', wagtail.core.blocks.CharBlock()), ('description', wagtail.core.blocks.TextBlock()), ('link', wagtail.core.blocks.CharBlock()), ('link_text', wagtail.core.blocks.CharBlock())], blank=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
        migrations.DeleteModel(
            name='AnnualReportPage',
        ),
    ]
