from django import template
from accounting.utils import formatDate, formatDateTime

register = template.Library()

@register.filter
def jpdate(value):
    return formatDate(value)

@register.filter
def jpdatetime(value):
    return formatDateTime(value)
