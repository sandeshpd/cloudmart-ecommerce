from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404

from inventory.models import Product
from products.models import Category

# Create your views here.

"""List out Products view."""
def product_list(request):
    products = Product.objects.all()
    paginator = Paginator(products, 10)     # Show 10 products per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'products/product_list.html', {'products': page_obj})

""" List products by category. """
def product_list_by_category(request, category_id):
    category = get_object_or_404(Category, pk=category_id)
    products = Product.objects.filter(category=category)
    return render(request, 'products/product_list.html', {'products': products, 'category': category})

"""Get specific product details."""
def product_detail(request, pk):
    product = Product.objects.get(pk = pk)
    return render(request, "products/product_detail.html", {'product': product})