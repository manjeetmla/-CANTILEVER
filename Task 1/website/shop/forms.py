from django import forms
from .models import Product

class ProductFilterForm(forms.Form):
    discounted_price_min = forms.DecimalField(required=False, label='Min Price')
    discounted_price_max = forms.DecimalField(required=False, label='Max Price')
    processor = forms.CharField(required=False, max_length=100)
    ram = forms.CharField(required=False, max_length=50)
    os = forms.CharField(required=False, max_length=50)
    ssd = forms.CharField(required=False, max_length=50)
    display = forms.CharField(required=False, max_length=50)