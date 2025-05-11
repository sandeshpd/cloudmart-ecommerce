from django.contrib import admin
from inventory.models import Product

# Register your models here.
admin.site.register(Product)

# @admin.register(Category)
# class CategoryAdmin(admin.ModelAdmin):
#     list_display = ['name', 'slug']
#     prepopulated_fields = {'slug':('name',)}

# @admin.register(Product)
# class ProductAdmin(admin.ModelAdmin):
#     list_display = ['name', 'category', 'price', 'stock', 'is_active', 'created_at']
#     list_filter = ['category', 'is_active', 'created_at']
#     search_fields = ['name', 'description']
#     prepopulated_fields = {'slug': ('name',)}
