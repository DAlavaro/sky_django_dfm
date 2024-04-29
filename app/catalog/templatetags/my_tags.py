from django import template
from django.conf import settings

register = template.Library()

@register.filter(name='my_path')
def my_path(value):
    if not value:
        return 'Ничего нет'
    return f"{settings.MEDIA_URL}{value}"


@register.simple_tag
def mediapath(value):
    if not value:
        return 'Ничего нет'  # Возможно стоит предусмотреть дефолтное изображение
    return f'{settings.MEDIA_URL}{value}'