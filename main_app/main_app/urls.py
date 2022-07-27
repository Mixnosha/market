"""main_app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from market.business_logic import add_basket, buy_product_def
from market.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', ProductView.as_view(), name='main_page'),
    path('category/<slug:slug>', CategoryView.as_view(), name='cats_view'),
    path('product/<slug:slug>', OneProductView.as_view(), name='one_product'),
    path('register', RegisterUser.as_view(), name='register'),
    path('login', LoginUser.as_view(), name='login'),
    path('profile', ProfileView.as_view(), name='profile'),
    path('basket/', BasketView.as_view(), name='basket'),
    path('add_basket', add_basket, name='add_basket'),
    path('buy_product', BuyProductView.as_view(), name='buy_product'),
    path('buy_product_def', buy_product_def, name='buy_product_def'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
