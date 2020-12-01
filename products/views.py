from django.shortcuts import render, get_object_or_404
from .models import Product
from .forms import ProductForm
from django.shortcuts import redirect
from .forms import CustomProductForm


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


def custom_product_form(request):
    my_form = CustomProductForm()
    if request.method == "POST":
        my_form = CustomProductForm(request.POST)
        if my_form.is_valid():
            print(my_form.cleaned_data)
            Product.objects.create(**my_form.cleaned_data)
        else:
            print(my_form.errors)
        return redirect('/products')
    context = {
        "form": my_form
    }
    return render(request, "product/custom_form.html", context)


def update_form(request, product_id):
    obj = get_object_or_404(Product, id=product_id)
    initial_data = {
        'title': obj.title,
        'description': obj.description,
        'price': obj.price
    }
    form = ProductForm(request.POST or None, initial=initial_data, instance=obj)
    if form.is_valid():
        form.save()
        return redirect('/products')
    context = {
        "form": form
    }
    return render(request, "product/form.html", context)


def delete_product(request, product_id):
    obj = get_object_or_404(Product, id=product_id)
    if request.method == "POST":
        obj.delete()
    return redirect('/products')