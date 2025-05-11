from django.contrib import messages
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from .forms import AddressForm

# Create your views here.

"""Fetch address list."""
def address_list(request):
    return render(request, 'addresses/address_list.html')

"""Add Address"""
def add_address(request):
    if request.method == 'POST':
        form = AddressForm(request.POST)
        if form.is_valid():
            return redirect('/home')
        else:
            messages.error(request, "Something went wrong. Check your input and try again.")
    else:
        form = AddressForm()

    return render(request, 'addresses/add_address.html', {'form': form})