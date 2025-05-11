from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import CartItem

# Create your views here.
"""Fetch cart details."""
#TODO: make @login_required mandatory here
def cart_detail(request):
    return render(request, 'cart/cart_detail.html')

"""Add specific items in cart."""
def add_to_cart(request, product_id):
    return redirect('cart:cart_detail')

"""Remove items from cart."""
def remove_from_cart(request, item_id):
    return redirect({'cart: cart_detail'})


