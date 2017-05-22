# _*_ coding:utf-8 _*_

from django import template

register = template.Library()


@register.filter(name='format_sn')
def format_sn(value):
    n = 5
    l = len(str(value))
    return '0'*(n-l)+"%s"%value

