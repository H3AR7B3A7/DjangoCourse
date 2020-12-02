from django.urls import path
from products.views import *

app_name = 'products'
urlpatterns = [
    path('', products_all, name='products'),
    path('<int:product_id>', products_detail, name='products-detail'),
    path('create/', products_create, name='products-form'),
    path('customcreate/', products_custom_create, name='products-custom-form'),
    path('<int:product_id>/update/', products_update, name='products-update-form'),
    path('<int:product_id>/delete/', products_delete, name='products-delete'),
]
