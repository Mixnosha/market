from django.views.generic import ListView
from market.models import Product, Company


class MainViewCompany(ListView):
    template_name = 'company/main_view_company.html'
    context_object_name = 'products'

    def get_queryset(self, slug):
        company = Company.objects.get(slug=slug)
        return Product.objects.filter(company=company)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(MainViewCompany, self).get_context_data()
        context['title'] = Company.objects.get(slug=kwargs['slug']).name_company
        return context
