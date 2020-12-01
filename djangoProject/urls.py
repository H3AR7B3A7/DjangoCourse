"""djangoProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from DjangoCourse.views import *
from products.views import *

urlpatterns = [
    path('', index, name='index'),
    path('contact/', contact, name='contact'),

    path('products/', products_all, name='products'),
    path('products/<int:product_id>', products_detail, name='products-detail'),
    path('products/create/', products_create, name='products-create'),
    path('products/customcreate/', products_custom_create, name='custom-product-form'),
    path('products/<int:product_id>/update/', products_update, name='update-product-form'),
    path('products/<int:product_id>/delete/', products_delete, name='delete-product'),

    path('admin/', admin.site.urls),
]
