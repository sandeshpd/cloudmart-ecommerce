"""
Inventory Products Views. This is accessible only to admins/privileged users.
"""
from django.core.paginator import Paginator
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from .forms import ProductCreateForm
from .models import Product

# Create your views here.
"""Display a form to add products in an inventory."""
def add_product_to_inventory(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = ProductCreateForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                messages.success(request, 'Product added to the inventory successfully.')
                return render(request, 'inventory/product_add.html', {'form': form})
            else:
                messages.error(request, 'Something went wrong.')

        else:
            form = ProductCreateForm()

        return render(request, 'inventory/product_add.html', {'form': form})
    else:
        messages.warning(request, 'You must login to proceed')
        return redirect('users:login')

""" Fetch products list from an inventory."""
def inventory_products_list(request):
    if request.user.is_authenticated:
        products = Product.objects.all()
        paginator = Paginator(products, 10)     # Show 10 products per page
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        return render(request, 'inventory/products_list.html', {'products': page_obj})
    else:
        messages.warning(request, 'You must login to proceed.')
        return redirect('users:login')