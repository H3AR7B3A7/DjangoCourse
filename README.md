# Django Course
### Setup
[Python](https://docs.python.org/3.7/) 3.7.9 | [Django](https://docs.djangoproject.com/en/3.1/) 3.1.3

See [here](https://www.youtube.com/watch?v=KcM5ont7jy4) how to start a project using PyCharm.
All we have to do is migrate the database by running 'manage.py migrate' in the console and press 'Run...'  
However, migrating the database isn't that important yet because we are not using it yet.

## Creating a Project with CLI 
- **python -m venv "C:\...\projectname"**
- **.\Scripts\activate**
- **pip install django**
- **mkdir src**
- **cd src**
- **django-admin startproject projectname .**
- **python manage.py migrate**
- **python manage.py runserver**

(Specify python and django versions if not using system defaults!)
- **Ctrl + C**, to shut down server
- **deactivate**, to leave virtual environment

## Creating Super User
**manage.py createsuperuser**
Username: admin
Password: pass

To delete using the shell:
> python manage.py shell
> from django.contrib.auth.models import User
> User.objects.get(username="joebloggs", is_superuser=True).delete()

In our development db this password isn't important, but when we add a db for production we will use a stronger password.

## Creating a Basic App
**manage.py startapp name**

- Create model in models.py
- **manage.py makemigrations**
- **manage.py migrate**
- Add *'products'* to installed apps in *settings.py*

In *'admin.py'*:

    from .models import Product
    admin.site.register(Product)

We can now add products on: http://127.0.0.1:8000/admin/products/product/

### In the shell
> python manage.py shell
> from products.models import Product
> Products.objects.create(title="Product Name",price="10")
> Product.objects.all()

## Creating Views
For a partial we can import HttpResponse and add a function to *'views.py'* in the project folder:

    from django.http import HttpResponse
    from django.shortcuts import render
    
    def home_view(*args, **kwargs):
        return "<h1>Hello World</h1>"

Then we need to add to *'urls.py'*:

    from DjangoCourse import views

    urlpatterns = [
        path('', views.index, name='index'),
        path('admin/', admin.site.urls),
    ]

