from django.shortcuts import render
from .models import Product


def product_all(request, *args, **kwargs):
    context = {
        "list": Product.objects.all()
    }
    return render(request, "product/products.html", context)


def product_detail(request, *args, **kwargs):
    context = {
        "object": Product.objects.get(id=request.GET['id'])
    }
    return render(request, "product/detail.html", context)
