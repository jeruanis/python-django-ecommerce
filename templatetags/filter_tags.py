from django import template
from django.template.defaultfilters import stringfilter
import random

register = template.Library()

@register.filter
@stringfilter #this will make the output string
def slashq(value):
    return value.replace("'" ,"\'")

@register.filter()
def int(value):
    return int(value)

@register.filter()
def rand_num(value):
    return random.randint(0,100)
