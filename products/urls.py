from django.urls import path
from . import views

app_name = 'products'
urlpatterns = [
    path('', views.index, name='product_list'),
    path('add/', views.add, name='add_product'),
    path('delete/<int:product_id>/', views.delete, name='delete_product'),
    path('update/<int:product_id>/', views.update, name='update_product'),
]
