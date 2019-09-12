# Generated by Django 2.2.4 on 2019-09-12 16:46

from django.db import migrations
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('vacancy', '0008_auto_20190827_1704'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vacancypage',
            name='content',
            field=wagtail.core.fields.StreamField([('text', wagtail.core.blocks.StructBlock([('headline', wagtail.core.blocks.CharBlock(max_length=200)), ('content', wagtail.core.blocks.RichTextBlock(features=['h3', 'bold', 'italic', 'link', 'ol', 'ul', 'embed'])), ('large_text', wagtail.core.blocks.BooleanBlock(blank=True))])), ('key_stats', wagtail.core.blocks.StructBlock([('stats', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('label', wagtail.core.blocks.CharBlock()), ('value', wagtail.core.blocks.CharBlock())])))])), ('case_studies', wagtail.core.blocks.StructBlock([('headline', wagtail.core.blocks.CharBlock(max_length=200)), ('case_studies', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock()), ('headline', wagtail.core.blocks.CharBlock()), ('slugline', wagtail.core.blocks.CharBlock()), ('kicker', wagtail.core.blocks.CharBlock()), ('destination', wagtail.core.blocks.URLBlock())])))])), ('call_to_action', wagtail.core.blocks.StructBlock([('headline', wagtail.core.blocks.CharBlock(max_length=200)), ('content', wagtail.core.blocks.RichTextBlock(features=['bold', 'italic', 'link'])), ('large_text', wagtail.core.blocks.BooleanBlock()), ('button_destination', wagtail.core.blocks.URLBlock()), ('button_label', wagtail.core.blocks.CharBlock(max_length=30))]))], blank=True, null=True),
        ),
    ]