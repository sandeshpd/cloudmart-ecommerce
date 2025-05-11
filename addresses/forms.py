"""Form to add a new address"""
from django import forms
from .models import Address

class AddressForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = [
            'full_name',
            'phone',
            'street_address',
            'city',
            'state',
            'postal_code',
            'country'
        ]