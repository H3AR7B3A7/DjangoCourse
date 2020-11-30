from django.http import HttpResponse
from django.shortcuts import render


def index(request, *args, **kwargs):
    return render(request, "index.html")


def contact(request, *args, **kwargs):
    return HttpResponse("<h1>Contact</h1>")
