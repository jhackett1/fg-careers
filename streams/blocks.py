from wagtail.core import blocks

class TextBlock(blocks.StructBlock):

    headline = blocks.CharBlock(required=True, help_text)