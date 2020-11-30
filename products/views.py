from django.http import HttpResponse
from django.shortcuts import render


def products(request, *args, **kwargs):
    return render(request, "products.html")
