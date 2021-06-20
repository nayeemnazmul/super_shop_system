import random
import string

from django.shortcuts import render, redirect, get_list_or_404, Http404
from django.http import JsonResponse
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


def json_detail(request, product_id):
    if request.is_ajax():
        try:
            product = Product.objects.get(id=product_id)
            quantity = int(request.GET['quantity'])

            if quantity > product.current_stock:
                response = {
                    'error_message': 'Order quantity is larger than current stock: ' + str(product.current_stock)
                }
                return JsonResponse(response)
            else:
                response = {
                    'id': product.id,
                    'code': product.code,
                    'name': product.name,
                    'unit_price': product.unit_price,
                    'current_stock': product.current_stock,
                }
                return JsonResponse(response)
        except (KeyError, Product.DoesNotExist) as e:
            response = {
                'error_message': 'Product not found.',
            }
            return JsonResponse(response, status=404)
    else:
        return redirect('orders:view_cart')
