from wagtail.core import blocks
from wagtail.images.blocks import ImageChooserBlock

class TextBlock(blocks.StructBlock):
    headline = blocks.CharBlock(max_length=200)
    sticky_headline = blocks.BooleanBlock(required=False)
    left_content = blocks.TextBlock(required=False)
    content = blocks.RichTextBlock(features=['h3', 'bold', 'italic', 'link', 'ol', 'ul', 'embed'])
    large_text = blocks.BooleanBlock(required=False)
    class Meta:
        icon = "doc-full-inverse"
        label = "Text"
        template = "text-columns.html"


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
        template = "benefits.html"


class VacanciesBlock(blocks.StaticBlock):
    class Meta:
        icon = "list-ul"
        label = "Current vacancies"
        template = "vacancies.html"


class TestimonialsBlock(blocks.StructBlock):
    headline = blocks.CharBlock(max_length=200)
    testimonials = blocks.ListBlock(blocks.StructBlock([
        ('quotation', blocks.TextBlock()),
        ('attribution_name', blocks.CharBlock()),
        ('attribution_role', blocks.CharBlock()),
        ('image', ImageChooserBlock())
    ]))
    class Meta:
        icon = "openquote"
        label = "Testimonials"
        template = "testimonials.html"


class PersonCardsBlock(blocks.StructBlock):
    headline = blocks.CharBlock(max_length=200)
    people = blocks.ListBlock(blocks.StructBlock([
        ('image', ImageChooserBlock()),
        ('name', blocks.CharBlock()),
        ('role', blocks.CharBlock()),
        ('biography', blocks.RichTextBlock(features=['bold', 'italic', 'link'])),
    ]))
    class Meta:
        icon = "group"
        label = "Person cards"
        template = "person-cards.html"


class CallToActionBlock(blocks.StructBlock):
    headline = blocks.CharBlock(max_length=200)
    content = blocks.RichTextBlock(features=['bold', 'italic', 'link'])
    large_text = blocks.BooleanBlock(required=False)
    button_destination = blocks.URLBlock()
    button_label = blocks.CharBlock(max_length=30)
    class Meta:
        icon = "tick"
        label = "Call to action bar"
        template = "call-to-action.html"


class KeyStatsBlock(blocks.StructBlock):
    stats = blocks.ListBlock(blocks.StructBlock([
        ('label', blocks.CharBlock()),
        ('value', blocks.CharBlock()),
    ]))
    class Meta:
        icon = "success"
        label = "Key stats"
        template = "key-stats.html"


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
        template = "case-studies.html"