from django.urls import path
from . import views

app_name = 'products'
urlpatterns = [
    path('', views.index, name='product_list'),
    path('add/', views.add, name='add_product')
]
