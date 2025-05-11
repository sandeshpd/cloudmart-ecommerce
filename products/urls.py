from django.urls import path
from . import views

app_name = 'products'

urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('<int:pk>/', views.product_detail, name='detail'),
    path('category/<int:category_id>', views.product_list_by_category, name='products_by_category'),
]