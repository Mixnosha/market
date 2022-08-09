from django.urls import path

from company.views import *

app_name = 'company'
urlpatterns = [
    path('', MainViewCompany.as_view(), name='all_company'),
    path('<slug:slug>', ViewCompany.as_view(), name='main_company_view')
]