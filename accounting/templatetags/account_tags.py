from django import template
from django.utils.html import conditional_escape
from django.utils.safestring import mark_safe
from accounting.utils import formatDate, formatDateTime

register = template.Library()

@register.filter(is_safe=True)
def jpdate(value):
    return formatDate(value)

@register.filter(is_safe=True)
def jpdatetime(value):
    return formatDateTime(value)

@register.filter(needs_autoescape=True)
def format_ledger(value, autoescape=True):
    """元帳表記"""
    if autoescape:
        esc = conditional_escape
    else:
        esc = lambda x: x
    ret = "<tr><td><p>{}</p></td>".format(formatDate(value[0]))
    ret = ret + "<td><p>{}</p></td>".format(esc(value[1]))
    if value[2]:
        ret = ret + "<td><p>{}</p></td><td><p>　</p></td>".format(esc(value[3]))
    else:
        ret = ret + "<td><p>　</p></td><td><p>{}</p></td>".format(esc(value[3]))
    ret = ret + "</tr>"
    return mark_safe(ret)
