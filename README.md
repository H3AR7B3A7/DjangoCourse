# Django Course
### Setup
Python 3.7.9 | Django 3.1.3

See [here](https://www.youtube.com/watch?v=KcM5ont7jy4) how to start a project using PyCharm.
All we have to do is migrate the database by running 'manage.py migrate' in the console and press 'Run...'  
However, migrating the database isn't that important yet because we are not using it yet.

## Creating a project with CLI 
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

## 