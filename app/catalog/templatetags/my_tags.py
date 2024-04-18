from django import template
from django.conf import settings

register = template.Library()

@register.filter(name='my_path')
def my_path(value):
    return f"{settings.MEDIA_URL}{value}"


@register.simple_tag
def mediapath(value):
    return f"{settings.MEDIA_URL}{value}"