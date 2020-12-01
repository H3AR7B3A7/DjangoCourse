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

## HttpResponse
For a simple response we can import HttpResponse and add a function to *'views.py'* in the project folder:

    from django.http import HttpResponse
    
    def home_view(*args, **kwargs):
        return "<h1>Hello World</h1>"

Then we need to add to *'urls.py'*:

    from DjangoCourse import views

    urlpatterns = [
        path('', views.index, name='index'),
        path('admin/', admin.site.urls),
    ]

## Templating
To respond with templates we use the *render* import:

    from django.shortcuts import render

    def index(request, *args, **kwargs):
        return render(request, "index.html")

And we can create our templates in the *'templates'* folder. If we aren't using PyCharm we might have to configure 
the templates folder in *settings.py*, like this:

    'DIRS': [BASE_DIR / 'templates']

or with an *'os'* import:

    'DIRS': [os.path.join(BASE_DIR, "templates")]
    
## Template Inheritance
We can create a *'base'-template* to inherit from when creating pages. 
To indicate where our content will go, we use the following tags within this base template:

    {% block content %}{% endblock %}

Likewise we will wrap our content pages with these tags and extend the *'base'-template* at the top of the page:

    {% extends 'base.html' %}
    
## Partials
We can also include partials in other pages with:

    {% include 'navbar.html' %}

## Static resources
At the top of the template where you want to import the static folder:

    {% load static %}

We then reference to the stylesheet like this (presuming the path = static/css/style.css):

    href="{% static 'css/style.css' %}"
    
Configure STATICFILES_DIRS in *'settings.py'* depending on where you want your static folder to be.  
In templates folder:

    STATICFILES_DIRS = [BASE_DIR / 'templates/static']

In project directory:

    STATICFILES_DIRS = [BASE_DIR / 'static']
    
Or similarly with an os import:

    STATICFILES_DIRS = [os.path.join(BASE_DIR, 'templates/static')]

[Official documentation](https://docs.djangoproject.com/en/3.1/howto/static-files/)

## Template Context
We can add context to our template in views.py:

    def index(request, *args, **kwargs):
        my_context = { "my_text": "Some text ...",
                       "my_list": [5, 6, 7, 8]}
        return render(request, "index.html", my_context)

Now we can output this context in *index.html* using the key in between handlebars:

    {{ my_text }}

    {% for item in my_list %}
        <li>{{ item }}</li>
    {% endfor %}
    
To add database entries of an app to our context:

    "list": Product.objects.all()

## Parameters
We can direct users to the details of just one object by fetching a parameter in the url:

    "object": Product.objects.get(id=request.GET['id'])
    
The link to this would be: *'/product/?id=1'*, 
which we could offer the user with something like this on the *'products'-page*:

    {% for item in list %}
    <li><a href="/product/?id={{ item.id }}">{{ item.title }}</a></li>
    {% endfor %}
    
## Filters
We can add simple 'filters' by adding them after a | *'pipe'*:

    {{ item.price|add:10 }}

[Built-in Tags / Filters](https://docs.djangoproject.com/en/3.1/ref/templates/builtins/)  
[Custom Tags / Filters](https://docs.djangoproject.com/en/3.1/howto/custom-template-tags/)

##