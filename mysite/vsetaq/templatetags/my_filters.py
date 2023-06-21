from django import template

register = template.Library()


@register.filter(name='multiply')
def multiplied_by(income, multiplier):
    return income.income * multiplier