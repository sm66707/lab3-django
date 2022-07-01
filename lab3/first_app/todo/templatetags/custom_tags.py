from django import template

register=template.Library()


@register.simple_tag
def my_custom_tag():
    return "hello custom tag"

@register.filter
def my_filter(data):
    return data[:5]