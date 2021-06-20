from django.shortcuts import render, get_list_or_404, Http404
from .models import Order


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

