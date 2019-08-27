from wagtail.core import blocks
from wagtail.images.blocks import ImageChooserBlock

class TextBlock(blocks.StructBlock):
    headline = blocks.CharBlock(max_length=200)
    content = blocks.RichTextBlock(features=['h3', 'bold', 'italic', 'link', 'ol', 'ul', 'embed'])
    large_text = blocks.BooleanBlock()
    class Meta:
        icon = "doc-full-inverse"
        label = "Text"


class BenefitsBlock(blocks.StructBlock):
    headline = blocks.CharBlock(max_length=200)
    image = ImageChooserBlock()
    benefits = blocks.ListBlock(blocks.StructBlock([
        ('crosshead', blocks.CharBlock()),
        ('content', blocks.RichTextBlock(features=['h3', 'bold', 'italic', 'link', 'ol', 'ul', 'embed'])),
    ]))
    class Meta:
        icon = "pick"
        label = "Benefits"


class VacanciesBlock(blocks.StaticBlock):
    class Meta:
        icon = "list-ul"
        label = "Current vacancies"


class TestimonialsBlock(blocks.StructBlock):
    testimonials = blocks.ListBlock(blocks.StructBlock([
        ('quotation', blocks.RichTextBlock(features=['bold', 'italic', 'link'])),
        ('attribution_name', blocks.CharBlock()),
        ('attribution_role', blocks.CharBlock()),
        ('image', ImageChooserBlock())
    ]))
    class Meta:
        icon = "openquote"
        label = "Testimonials"


class PersonCardsBlock(blocks.StructBlock):
    people = blocks.ListBlock(blocks.StructBlock([
        ('image', ImageChooserBlock()),
        ('name', blocks.CharBlock()),
        ('role', blocks.CharBlock()),
        ('biography', blocks.RichTextBlock(features=['bold', 'italic', 'link'])),
    ]))
    class Meta:
        icon = "group"
        label = "Person cards"


class CallToActionBlock(blocks.StructBlock):
    headline = blocks.CharBlock(max_length=200)
    content = blocks.RichTextBlock(features=['bold', 'italic', 'link'])
    large_text = blocks.BooleanBlock()
    button_destination = blocks.URLBlock()
    button_label = blocks.CharBlock(max_length=30)
    class Meta:
        icon = "tick"
        label = "Call to action bar"


class KeyStatsBlock(blocks.StructBlock):
    stats = blocks.ListBlock(blocks.StructBlock([
        ('label', blocks.CharBlock()),
        ('value', blocks.CharBlock()),
    ]))
    class Meta:
        icon = "success"
        label = "Key stats"


class CaseStudiesBlock(blocks.StructBlock):
    headline = blocks.CharBlock(max_length=200)
    case_studies = blocks.ListBlock(blocks.StructBlock([
        ('image', ImageChooserBlock()),
        ('headline', blocks.CharBlock()),
        ('slugline', blocks.CharBlock()),
        ('kicker', blocks.CharBlock()),
        ('destination', blocks.URLBlock()),
    ]))
    class Meta:
        icon = "doc-full"
        label = "Case studies"