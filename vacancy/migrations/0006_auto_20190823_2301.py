# Generated by Django 2.2.4 on 2019-08-23 23:01

from django.db import migrations
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('vacancy', '0005_auto_20190823_2250'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vacancypage',
            name='content',
            field=wagtail.core.fields.StreamField([('text_block', wagtail.core.blocks.StructBlock([('headline', wagtail.core.blocks.CharBlock(max_length=200)), ('content', wagtail.core.blocks.RichTextBlock(features=['h3', 'bold', 'italic', 'link', 'ol', 'ul', 'embed']))])), ('benefits_block', wagtail.core.blocks.StructBlock([('headline', wagtail.core.blocks.CharBlock(max_length=200)), ('image', wagtail.images.blocks.ImageChooserBlock()), ('benefits', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('crosshead', wagtail.core.blocks.CharBlock()), ('content', wagtail.core.blocks.RichTextBlock())])))]))], blank=True, null=True),
        ),
    ]
