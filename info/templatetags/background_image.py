from django import template
import random

register = template.Library()


class BackgroundImageChooser(template.Node):
    def __init__(self):
        pass

    def render(self, context):
        return random.choice(['bg_1', 'bg_2', 'bg_3', 'bg_4', 'bg_5', 'bg_6', 'bg_7', 'bg_8', 'bg_9', 'bg_10', 'bg_11', 'bg_12', 'bg_13', 'bg_14', 'bg_15'])


@register.tag(name="background_image_value")
def background_image(parser, token):
    return BackgroundImageChooser()
