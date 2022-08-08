from django.urls import path

from company.views import MainViewCompany

app_name = 'company'
urlpatterns = [
    path('<slug:slug>', MainViewCompany.as_view(), name='main_company_view')
]