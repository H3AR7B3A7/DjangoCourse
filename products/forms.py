from django import forms
from django.forms import TextInput, Textarea, NumberInput
from .models import Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = [
            'title',
            'description',
            'price'
        ]
        widgets = {
            'title': TextInput(attrs={'placeholder': 'Title'}),
            'description': Textarea(attrs={'placeholder': 'Description'}),
            'price': NumberInput(attrs={'placeholder': 'Price'})
        }
        labels = {
            'title': '',
            'description': '',
            'price': ''
        }


class CustomProductForm(forms.Form):
    title = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': 'Title'}))
    description = forms.CharField(required=False, label='', widget=forms.Textarea(attrs={'placeholder': 'Description'}))
    price = forms.DecimalField(label='', widget=forms.TextInput(
        attrs={
            'placeholder': 'Price',
            'class': 'my-class my-class2',
            'id': 'my-id',
            'rows': 100,  # overridden by css
            'cols': 100  # overridden by css
        }
    ))
