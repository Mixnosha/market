from django import template
from django.db.models.functions import Lower

from market.models import Category

register = template.Library()

menu = [
        {'title': "Contacts", 'url_name': "/contacts"},
        {'title': "Basket", 'url_name': "/basket"},
        {'title': 'Company', 'url_name': '/company'},
        ]


@register.simple_tag(name='getcats')
def get_categories():
    return Category.objects.all().order_by(Lower('category_title'))


@register.simple_tag(name='getmenu')
def get_menu():
    return menu



