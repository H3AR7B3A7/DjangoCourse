from django.shortcuts import render
from .models import Product
from .forms import ProductForm
from django.shortcuts import redirect


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


def product_form(request):
    form = ProductForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('/products')
    context = {
        "form": form
    }
    return render(request, "product/form.html", context)
