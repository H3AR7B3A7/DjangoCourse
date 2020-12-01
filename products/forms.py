from django import forms
from .models import Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = [
            'title',
            'description',
            'price'
        ]


class CustomProductForm(forms.Form):
    title = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': 'Title'}))
    description = forms.CharField(required=False, label='', widget=forms.TextInput(attrs={'placeholder': 'Description'}))
    price = forms.DecimalField(label='', widget=forms.TextInput(attrs={'placeholder': 'Price'}))
