"""Form for adding products in inventory. This is accessible only to admins/privileged users."""
from django import forms
from .models import Product

class ProductCreateForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = [
            'name',
            'description',
            'slug',
            'category',
            'price',
            'stock',
            'image',
        ]

        widgets = {
            'description': forms.Textarea(attrs={'rows': 4}),
            'price': forms.NumberInput(attrs={'step': '0.01'}),
            'stock': forms.NumberInput(),
        }