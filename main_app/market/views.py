from django.contrib.auth.views import LoginView
from django.shortcuts import render
from django.views.generic import ListView

from market.models import Product


class ProductView(ListView):
    model = Product
    paginate_by = 100
    context_object_name = 'product_list'
    template_name = 'market/base.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['name_page'] = 'market'
        return context
