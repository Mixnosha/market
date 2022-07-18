from django.contrib.auth.views import LoginView
from django.shortcuts import render
from django.views.generic import ListView

from market.models import Product, Category


class ProductView(ListView):
    model = Product
    paginate_by = 100
    context_object_name = 'product_list'
    template_name = 'market/base.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['name_page'] = 'market'
        context['category'] = Category.objects.all()
        return context


class CategoryView(ListView):
    template_name = 'market/category.html'
    paginate_by = 25
    context_object_name = 'category_list'

    def get_queryset(self):
        cat_id = self.kwargs["cat_id"]
        print(cat_id)
        queryset = Product.objects.filter(category=cat_id)
        return queryset