from django import template

register = template.Library()


@register.filter
def get(mapping, key):
    return mapping.get(key, "")


@register.filter
def gethttp(mapping, key):
    val = mapping.get(key, "")
    val = val.replace("http://", "https://")
    return val
