from django.urls import path

from feedback.views import FeedbackForProductList

urlpatterns = [
    path('<slug:product_slug>', FeedbackForProductList.as_view(), name='feedback_for_product')
]