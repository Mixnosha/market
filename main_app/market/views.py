from django.contrib.auth import login
from django.contrib.auth.views import LoginView
from django.shortcuts import redirect
from django.views import View
from django.views.generic import ListView, CreateView
from market.forms import SearchForm, RegisterUserForms, LoginUserForm, ProfileForm
from market.models import Product, Category, Profile


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
        context['category'] = Category.objects.all()
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
        context['category'] = Category.objects.all()
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
        context['category'] = Category.objects.all()
        return context


class RegisterUser(CreateView):
    form_class = RegisterUserForms
    template_name = 'registration/register.html'
    success_url = 'rock'
    context_object_name = 'form'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Register'

        return context

    def form_valid(self, form):
        user = form.save()
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

    def get_queryset(self):
        if self.request.user.is_authenticated:
            try:
                username = self.request.user.username
                queryset = Profile.objects.get(username=username)
            except Exception:
                queryset = Profile.objects.all()
        else:
            return redirect('/')
        return queryset

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        try:
            username = self.request.user.username
            user = Profile.objects.get(username=username)
            context['prof'] = True
        except Exception:
            context['prof'] = False
        context['title'] = 'profile'
        context['form'] = ProfileForm()
        return context



