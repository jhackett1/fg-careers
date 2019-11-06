from django.db import models

from wagtail.core.models import Page
from wagtail.core.fields import StreamField
from wagtail.admin.edit_handlers import StreamFieldPanel
from wagtail.images.edit_handlers import ImageChooserPanel

from streams import blocks

class HomePage(Page):
    template = "home_page.html"
    max_count = 1

    preview_image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=False,
        on_delete=models.SET_NULL,
        related_name="+",
        help_text="This image appears in social media previews, but not on the page itself"
    )
    content = StreamField(
        [
            ("text", blocks.TextBlock()),
            ("benefits", blocks.BenefitsBlock()),
            ("vacancies", blocks.VacanciesBlock()),
            ("testimonials", blocks.TestimonialsBlock()),
            ("person_cards", blocks.PersonCardsBlock()),
            ("call_to_action", blocks.CallToActionBlock()),
            
            ("key_stats", blocks.KeyStatsBlock()),
            ("case_studies", blocks.CaseStudiesBlock())
        ],
        null=True,
        blank=True
    )

    content_panels = Page.content_panels + [
        StreamFieldPanel("content")
    ]

    promote_panels = Page.promote_panels + [
        ImageChooserPanel("preview_image")
    ]