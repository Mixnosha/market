from django.views.generic import ListView
from market.models import Product, Company


class ViewCompany(ListView):
    template_name = 'company/main_view_company.html'
    context_object_name = 'products'

    def get_queryset(self):
        company = Company.objects.get(slug=self.kwargs['slug'])
        return Product.objects.filter(company=company)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ViewCompany, self).get_context_data()
        context['title'] = Company.objects.get(slug=self.kwargs['slug']).name_company
        context['company'] = Company.objects.get(slug=self.kwargs['slug'])
        return context


class MainViewCompany(ListView):
    template_name = 'company/view_all_company.html'
    context_object_name = 'all_company'
    queryset = Company.objects.all()

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(MainViewCompany, self).get_context_data()
        context['title'] = 'Company'
        return context

