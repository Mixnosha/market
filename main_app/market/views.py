from django.contrib.auth import login
from django.contrib.auth.views import LoginView
from django.db.models import Q
from django.shortcuts import redirect
from django.views import View
from django.views.generic import ListView, CreateView, FormView
from market.business_logic import get_sum_product_price_basket,  get_all_amount, \
    get_delivered_product
from market.forms import RegisterUserForms, LoginUserForm, ProfileForm, ReviewForm
from market.models import Product, Category, Profile, Basket, BuyProduct


class ProductView(ListView, View):
    paginate_by = 100
    context_object_name = 'product_list'
    template_name = 'market/main_page.html'
    success_url = '/'

    def get_queryset(self):
        if self.request.GET:
            text_search = self.request.GET.get('text_search')
            queryset = Product.objects.filter(product_name__icontains=text_search)
        else:
            try:
                queryset = Product.objects.filter(sales__gte=100)
            except Exception:
                queryset = Product.objects.all()
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.GET:
            context['search'] = True
        context['name_page'] = 'market'
        return context


class CategoryView(ListView):
    template_name = 'market/category.html'
    paginate_by = 25
    context_object_name = 'category_list'

    def get_queryset(self):
        slug = self.kwargs["slug"]
        queryset = Product.objects.filter(category__slug=slug)
        return queryset

    def get_context_data(self, **kwargs):
        context = super(CategoryView, self).get_context_data(**kwargs)
        slug = self.kwargs["slug"]
        cat = Category.objects.get(slug=slug)
        context['name_category'] = cat
        return context


class OneProductView(ListView):
    template_name = 'market/one_product_view.html'
    context_object_name = 'one_product'

    def get_queryset(self):
        slug = self.kwargs['slug']
        try:
            queryset = Product.objects.get(slug=slug)
        except Exception:
            return redirect('/')
        return queryset

    def get_context_data(self, **kwargs):
        context = super(OneProductView, self).get_context_data(**kwargs)
        return context


class RegisterUser(CreateView):
    form_class = RegisterUserForms
    template_name = 'registration/register.html'
    success_url = '/'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Register'
        return context

    def form_valid(self, form):
        user = form.save()
        Profile.objects.create(user=user)
        login(self.request, user)
        return redirect('/')


class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = 'registration/login.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Login'
        return context


class ProfileView(ListView):
    template_name = 'market/profile.html'
    context_object_name = 'profile'

    def post(self, request):
        form = ProfileForm(instance=request.user.profile, data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            return redirect('profile')
        else:
            return redirect('/')

    def get_queryset(self):
        if self.request.user.is_authenticated:
            queryset = Profile.objects.get(user=self.request.user)
        else:
            return redirect('/')
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = Profile.objects.get(user=self.request.user)
        context['title'] = 'profile'
        context['delivered_product'] = get_delivered_product(self.request)
        context['basket_product'] = BuyProduct.objects.filter(Q(user=user), ~Q(delivery__delivery='Delivered'))
        context['form'] = ProfileForm(instance=self.request.user.profile)
        if bool(self.request.GET.get('change_profile')):
            context['change'] = True
        return context


class BasketView(ListView):
    template_name = 'market/basket.html'
    context_object_name = 'product_basket'

    def get_queryset(self):
        if self.request.user.is_authenticated:
            try:
                if self.request.GET.get('delete_product_id'):
                    id = self.request.GET.get('delete_product_id')
                    del_prod = Basket.objects.get(id=id)
                    del_prod.delete()
                user = Profile.objects.get(user=self.request.user)
                queryset = Basket.objects.filter(user=user)
            except Exception:
                queryset = Basket.objects.all()
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['all_price'] = get_sum_product_price_basket(self.request)
        try:
            bas = Basket.objects.filter(user=Profile.objects.get(user=self.request.user))
            if bas:
                context['buy_all'] = True
        except Exception:
            context['buy_all'] = False
        context['title'] = 'basket'
        return context


class BuyProductView(ListView):
    template_name = 'market/buy_product.html'
    context_object_name = 'profile'

    def get_queryset(self):
        queryset = Profile.objects.get(user=self.request.user)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Buy_product'
        pr_id = self.request.GET.get('buy_product_id')
        context['all_product'] = all_product = Product.objects.filter(id=pr_id)
        context['all_amount'] =all_amount = get_all_amount(self.request, all_product)
        all_price = 0
        for p in all_product:
            all_price += p.product_price * all_amount[p.product_name]
        context['all_price'] = all_price
        return context


class Review(FormView):
    template_name = 'market/review.html'
    form_class = ReviewForm
    success_url = '/'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["product"] = Product.objects.get(id=self.request.GET.get('product_id'))
        return context


