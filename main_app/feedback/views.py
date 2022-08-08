from django.http import HttpResponse
from django.views.generic import ListView

from market.models import Review, Product


class FeedbackForProductList(ListView):
    template_name = 'feedback/FeedbackForProductList.html'
    context_object_name = 'reviews'

    def get_queryset(self,):
        slug = self.kwargs['product_slug']
        return Review.objects.filter(product_review__slug=slug)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['product'] = Product.objects.get(slug=self.kwargs['product_slug'])
        return context
