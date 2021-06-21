import random
import string

from django.shortcuts import render, get_list_or_404, Http404, redirect

from .models import Order, OrderProduct
from products.models import Product


def index(request):
    try:
        order_list = get_list_or_404(Order)
    except Http404:
        context = {
            'no_order_message': 'No order found, add some.',
        }
    else:
        context = {
            'order_list': order_list,
        }
    return render(request, 'orders/index.html', context)


def view_cart(request):
    try:
        product_list = get_list_or_404(Product)
    except Http404:
        context = {
            'no_product_message': 'No product found to order, add some.',
        }
    else:
        context = {
            'product_list': product_list,
        }
    return render(request, 'orders/cart.html', context)


def add_order(request):
    code = ''.join(random.choices(string.ascii_letters + string.digits, k=6))
    customer_name = request.POST['customer_name']
    customer_phone = request.POST['customer_phone']
    customer_email = request.POST['customer_email']

    order = Order(code=code, customer_name=customer_name, customer_phone=customer_phone, customer_email=customer_email)
    order.save()

    product_id_list = request.POST.getlist('product_id')
    product_id_list = [int(product_id) for product_id in product_id_list]
    quantity_list = request.POST.getlist('quantity')
    quantity_list = [int(qty_item) for qty_item in quantity_list]

    order_total_price = 0
    for product_id, quantity in zip(product_id_list, quantity_list):
        product = Product.objects.get(id=product_id)

        order_product_total_price = product.unit_price * quantity
        order_total_price += order_product_total_price

        product.current_stock = (product.current_stock - quantity) if (product.current_stock - quantity) >= 0 else 0
        product.save()
        order_product = OrderProduct(order=order, product=product, quantity=quantity, total_price=order_product_total_price)
        order_product.save()

    order.total_price = order_total_price
    order.save()

    return redirect('orders:order_list')


def generate_invoice(request, order_id):
    order = Order.objects.get(id=order_id)

    context = {
        'order': order,
    }

    return render(request, 'orders/invoice.html', context)
