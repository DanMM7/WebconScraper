from django.shortcuts import render
from django.http import JsonResponse
from .helpers import get_all_customer_urls


# Create your views here.
def get_customer(request):
    return JsonResponse({'status': 200})
