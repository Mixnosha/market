from django.contrib.auth.views import LoginView
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import ListView, FormView
from django.views.generic.detail import SingleObjectMixin

from market.forms import SearchForm
from market.models import Product, Category


class ProductView(ListView, View):
    paginate_by = 100
    context_object_name = 'product_list'
    form_class = SearchForm
    template_name = 'market/main_page.html'
    name_url = 'main_page'
    success_url = '/'

    def get_queryset(self):
        if self.request.GET:
            text_search = self.request.GET.get('text_search')
            queryset = Product.objects.filter(product_name__icontains=text_search)
        else:
            queryset = Product.objects.filter(sales__gte=100)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['name_page'] = 'market'
        context['category'] = Category.objects.all()
        return context


class CategoryView(ListView):
    template_name = 'market/category.html'
    paginate_by = 25
    context_object_name = 'category_list'
    name_url = 'cats_view'

    def get_queryset(self):
        slug = self.kwargs["slug"]
        print(slug)
        queryset = Product.objects.filter(category__slug=slug)
        return queryset

    def get_context_data(self, **kwargs):
        context = super(CategoryView, self).get_context_data(**kwargs)
        slug = self.kwargs["slug"]
        cat = Category.objects.get(slug=slug)
        context['name_category'] = cat
        context['form_search_val'] = self.name_url
        return context
