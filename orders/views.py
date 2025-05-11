from django.shortcuts import render

# Create your views here.
"""Checking out items to order."""
def checkout(request):
    return render(request, 'orders/checkout.html')

"""To Access Order history associated to the user."""
def order_history(request):
    return render(request, 'orders/order_history.html')


