from django.shortcuts import render

from products.models import Category

# Create your views here.
"""Landing page when user enters URL to address bar"""
def homepage(request):
    categories = Category.objects.all() # We pass Category object here to register on home page.
    return render(request, 'core/index.html', {'categories': categories})

def error_404(request, exception):
    return render(request, 'core/404.html', status=404)

def error_500(request):
    return render(request, 'core/500.html', status=500)