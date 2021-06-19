import random
import string

from django.shortcuts import render, redirect, get_list_or_404
from django.core.exceptions import ValidationError
from .models import Product


def index(request):
    product_list = get_list_or_404(Product)
    context = {
        'product_list': product_list,
    }
    return render(request, 'products/index.html', context)


def add(request):
    code = random.choice(string.ascii_letters) + str(random.randint(1, 1000)) + random.choice(string.ascii_letters)
    name = request.POST['name']
    category = request.POST['category']
    unit_price = request.POST['unit_price']
    current_stock = request.POST['current_stock']

    try:
        new_product = Product(code=code, name=name, category=category, unit_price=unit_price,
                              current_stock=current_stock)
        new_product.save()
    except ValidationError as e:
        context = {
            'error_message': str(e.messages)
        }
        return redirect('products:product_list', context)
    else:
        return redirect('products:product_list')

