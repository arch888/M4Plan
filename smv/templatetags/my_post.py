from django import template

register=template.Library()

@register.simple_tag
def fun(value,arg):
   return value[arg]
