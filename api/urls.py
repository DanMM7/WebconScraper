from django.urls import path, include
from scraper.views import get_customer

urlpatterns = [
    path('get_customer/', get_customer),
]
