from django import template

register = template.Library()

menu = [{'title': "About", 'url_name': "about"},
        {'title': "Contacts", 'url_name': "contacts"},
        {'title': "Category", 'url_name': "category"},
        {'title': "Basket", 'url_name': "basket"},

        ]


@register.simple_tag(name='getmenu')
def get_menu():
    return menu
