from django.db import models

from wagtail.core.models import Page
# from wagtail.admin.edit_handlers import FieldPanel

class HomePage(Page):
    template = "home/home_page.html"
    max_count = 1

    # page_title = models.CharField(max_length=100, blank=True, null=False)

    # content_panels = Page.content_panels + [
    #     FieldPanel("page_title")
    # ]