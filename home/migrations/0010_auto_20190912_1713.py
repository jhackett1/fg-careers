# Generated by Django 2.2.4 on 2019-09-12 17:13

from django.db import migrations
import streams.blocks
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_auto_20190912_1649'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homepage',
            name='content',
            field=wagtail.core.fields.StreamField([('text', wagtail.core.blocks.StructBlock([('headline', wagtail.core.blocks.CharBlock(max_length=200)), ('left_content', wagtail.core.blocks.TextBlock(required=False)), ('content', wagtail.core.blocks.RichTextBlock(features=['h3', 'bold', 'italic', 'link', 'ol', 'ul', 'embed'])), ('large_text', wagtail.core.blocks.BooleanBlock(required=False))])), ('benefits', wagtail.core.blocks.StructBlock([('headline', wagtail.core.blocks.CharBlock(max_length=200)), ('image', wagtail.images.blocks.ImageChooserBlock()), ('benefits', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('crosshead', wagtail.core.blocks.CharBlock()), ('content', wagtail.core.blocks.RichTextBlock(features=['h3', 'bold', 'italic', 'link', 'ol', 'ul', 'embed']))])))])), ('vacancies', streams.blocks.VacanciesBlock()), ('testimonials', wagtail.core.blocks.StructBlock([('headline', wagtail.core.blocks.CharBlock(max_length=200)), ('testimonials', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('quotation', wagtail.core.blocks.TextBlock()), ('attribution_name', wagtail.core.blocks.CharBlock()), ('attribution_role', wagtail.core.blocks.CharBlock()), ('image', wagtail.images.blocks.ImageChooserBlock())])))])), ('person_cards', wagtail.core.blocks.StructBlock([('headline', wagtail.core.blocks.CharBlock(max_length=200)), ('people', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock()), ('name', wagtail.core.blocks.CharBlock()), ('role', wagtail.core.blocks.CharBlock()), ('biography', wagtail.core.blocks.RichTextBlock(features=['bold', 'italic', 'link']))])))])), ('call_to_action', wagtail.core.blocks.StructBlock([('headline', wagtail.core.blocks.CharBlock(max_length=200)), ('content', wagtail.core.blocks.RichTextBlock(features=['bold', 'italic', 'link'])), ('large_text', wagtail.core.blocks.BooleanBlock(required=False)), ('button_destination', wagtail.core.blocks.URLBlock()), ('button_label', wagtail.core.blocks.CharBlock(max_length=30))])), ('key_stats', wagtail.core.blocks.StructBlock([('stats', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('label', wagtail.core.blocks.CharBlock()), ('value', wagtail.core.blocks.CharBlock())])))])), ('case_studies', wagtail.core.blocks.StructBlock([('headline', wagtail.core.blocks.CharBlock(max_length=200)), ('case_studies', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock()), ('headline', wagtail.core.blocks.CharBlock()), ('slugline', wagtail.core.blocks.CharBlock()), ('kicker', wagtail.core.blocks.CharBlock()), ('destination', wagtail.core.blocks.URLBlock())])))]))], blank=True, null=True),
        ),
    ]