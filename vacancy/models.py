from django.db import models

from wagtail.core.models import Page
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.core.fields import StreamField
from wagtail.admin.edit_handlers import StreamFieldPanel

class VacancyPage(Page):
    template = "vacancy/vacancy_page.html"

    parent_page_type = [
        "home.HomePage"
    ]

    content = StreamField()
    hero_image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=False,
        on_delete=models.SET_NULL,
        related_name="+",
        help_text="test"
    )

    content_panels = Page.content_panels + [
        ImageChooserPanel("hero_image"),
        StreamFieldPanel("content")
    ]