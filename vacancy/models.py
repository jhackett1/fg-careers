from django.db import models

from wagtail.core.models import Page
# from wagtail.admin.edit_handlers import FieldPanel

class VacancyPage(Page):
    template = "home/home_page.html"

    parent_page_type = [
        "home.HomePage"
    ]

    

    # page_title = models.CharField(max_length=100, blank=True, null=False)

    # content_panels = Page.content_panels + [
    #     FieldPanel("page_title")
    # ]