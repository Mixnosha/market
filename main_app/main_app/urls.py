from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

import company
from market.business_logic import add_basket, buy_product_def, buy_all, delete_buy_product
from market.views import *


urlpatterns = [
    path('admin/', admin.site.urls),
    path('feedback/', include('feedback.urls')),
    path('company/', include('company.urls')),
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
    path('buy_all_product', buy_all, name='buy_all_product'),
    path('review/<slug:slug>', ReviewView.as_view(), name='review'),
    path('delete_buy_product', delete_buy_product, name='delete_buy_product')
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
