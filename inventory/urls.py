from django.urls import path
from . import views

app_name = 'inventory'

urlpatterns = [
    path('', views.add_product_to_inventory, name='add_product'),
    path('products_list/', views.inventory_products_list, name='product_list'),
]