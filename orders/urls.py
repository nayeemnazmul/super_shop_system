from django.urls import path
from . import views

app_name = 'orders'
urlpatterns = [
    path('', views.index, name='order_list'),
    path('cart/', views.view_cart, name='view_cart'),
    path('add/', views.add_order, name='add_order'),
    path('generate-invoice/<int:order_id>/', views.generate_invoice, name='generate_invoice'),
]
