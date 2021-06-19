import random
import string

from django.shortcuts import render, redirect, get_list_or_404, Http404
from django.core.exceptions import ValidationError
from .models import Product


def index(request):
    try:
        product_list = get_list_or_404(Product)
    except Http404:
        context = {
            'no_product_message': 'No product found, add some.',
        }
    else:
        context = {
            'product_list': product_list,
        }
    return render(request, 'products/index.html', context)


def add(request):
    code = ''.join(random.choices(string.ascii_letters+string.digits, k=6))
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


def delete(request, product_id):
    product = Product.objects.get(pk=product_id)
    product.delete()

    return redirect('products:product_list')


def update(request, product_id):
    product = Product.objects.get(pk=product_id)

    if request.POST:
        product.name = request.POST['name']
        product.category = request.POST['category']
        product.unit_price = request.POST['unit_price']
        product.current_stock = request.POST['current_stock']

        try:
            product.save()
        except ValidationError as e:
            context = {
                'error_message': str(e.messages)
            }
            return redirect('products:product_list', context)
        else:
            return redirect('products:product_list')
    else:
        context = {
            'product': product
        }
        return render(request, 'products/update.html', context)
