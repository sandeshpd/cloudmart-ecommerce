"""
Inventory Products Model. This is accessible only to admins/privileged users.
"""
from django.db import models
from products.models import Category

# Create your models here.
# class Category(models.Model):
#     name = models.CharField(max_length=200)
#     slug = models.SlugField(unique=True)

#     def __str__(self):
#         return self.name
    
#     class Meta:
#         ordering = ['name']
    
class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField(default=0)
    slug = models.SlugField(unique=True)
    image = models.ImageField(upload_to='product_images/',blank=True,null=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
