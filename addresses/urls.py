from django.urls import path
from . import views

app_name = 'addresses'

urlpatterns = [
    path('', views.address_list, name='address_list'),
    path('add/', views.add_address, name='add_address'),
]