from django.shortcuts import render, HttpResponse
from .models import Product


def index(request):
    product_list = Product.objects.all()
    context = {
        'product_list': product_list,
    }
    return render(request, 'products/index.html', context)
