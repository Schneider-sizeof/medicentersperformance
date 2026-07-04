"""Services views."""
from django.shortcuts import render
from .models import Product, Service
from apps.core.models import Showroom


def services_list(request):
    """Display all active products and services, plus the showroom."""
    products = Product.objects.filter(is_active=True)
    services = Service.objects.filter(is_active=True)
    showrooms = Showroom.objects.filter(is_active=True)
    return render(request, 'services/services_list.html', {
        'products': products,
        'services': services,
        'showrooms': showrooms,
    })
