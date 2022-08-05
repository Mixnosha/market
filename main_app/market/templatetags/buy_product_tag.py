from django import template

register = template.Library()


@register.simple_tag()
def get_amount(all_amount, obj):
    return all_amount[obj.product_name]


@register.simple_tag()
def multiplication(*args):
    res = 1
    for a in args:
        res *= a
    return res


@register.simple_tag()
def data_format(**kwargs):
    return kwargs['data'].strftime("%d/%m/%Y")
