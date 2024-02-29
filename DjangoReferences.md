# Django - References, Setup, Guide
-------------
Useful reference: [Django Official Documentation](https://docs.djangoproject.com/en/5.0/)

## Table of Contents:

0. ### Fundamental Components
    - [Virtual Environment](#virtual-environment)
    - [Install Django](#install-django)
    
1. ## Start Django Project
    - [Create Django Project](#create-django-project)
    - [Create Django App](#create-django-app)
    - [Run Local Server](#run-local-server)

2. # Initial Steps
    - [Project Routes Configuration](#project-routes-configuration)
    - [Project URLs Configuration](#project-urls-configuration)
    - [App Views Configuration](#app-views-configuration)
    - [App URLs Configuration](#app-urls-configuration)

3. ### Glossary
    - [APP LEVEL](#app-level)
        - [APP views.py](#app-viewspy)
        - [APP urls.py](#app-urlspy)
    - [PROJECT LEVEL](#project-level)
        - [PROJECT manage.py](#project-managepy)
        - [PROJECT settings.py](#project-settingspy)
        - [PROJECT urls.py](#project-urlspy)
    - [Special Classes](#special-classes)
        - [render()](#render)
        - [HttpResponse()](#httpresponse)
    - [File Structure](#file-structure)
    - [Template Tags](#template-tags)


### Virtual Enviroment
Also reference: PythonReferences.md
**Create the Virtual Environment:** Run:
`python -m venv myenv` 
(Where "myenv" is the enviroment name)
**Activate the Virtual Environment:** 
- macOS/Linux:
`source myenv/bin/activate`
- Windows
`myenv\Scripts\activate`

**Install Dependencies:** Inside the virtual environment, install dependencies using `pip`:
`pip install -r requirements.txt`
or `pip install package_name`
**Deactivate the Virtual Environment:** To exit the virtual environment, use:
`deactivate`

### Install Django
`pip3 install Django`

## Start Django Project 
------
Create a Django Project where you will later on create different applications:
**Run:** 
`django-admin startproject PROJECT_NAME`

### Create a Django App
At PROJECT_NAME dir lvl run:
`python manage.py startapp APP_NAME`

### Runserver
Run a local django server by running:
`python3 manage.py runserver`


# Initial Steps
The following steps will be follow when creating a new app.
------

## PROJECT Routes
**Note:** Each time you create a new app you need to repeat this step and the next one bellow at PROJECT level.

At PROJECT_NAME > `settings.py`
Set the new routes by adding the APP_NAME s to the project's route **Reference Glossary > PROJECT LVL > settings.py**

## PROJECT Urls
at PROJECT_NAME >  `urls.py`
Set the url path of the new app **Reference Glossary > PROJECT LVL > urls.py**

## APP Views
At APP_NAME > `views.py`
Set the initial views also reference **Reference Glossary > APP LVL > views.py**

## APP Urls
Set the URLS paths also reference **Reference Glossary > APP LVL > urls.py**


# Glossary

## APP LEVEL

### APP views.py
APP_NAME > views.py
Something the user will want to see.
** Generic Format: **
```python
def index(request):
    return HttpResponse("Hello this is a new app!")
```

### APP urls.py
Will set the url directioning and also the Url Path / for the application
> APP_NAME > urls.py
**Generic structure:**
```python
from django.urls import path
from . import views

urlpatterns = [
    #path("", )
    path("", views.index, name="index"),
    path()...
]
```
**alternative uses:**
```python
path("<str:name", views.greet, name="greet")
# At views.py:
def greet(request):
    return HttpResponse(f"Hello, {name}!")
```

## PROJECT LEVEL
Aka "Main"

### PROJECT manage.py
Will allow you to execute different commands as "`python3 manage.py runserver`".

### PROJECT settings.py
Important configuration settings as:
When initially creating a new app you must add it to the settings.py at the project lvl
```python
INSTALLED_APPS = [
    'APP_NAME',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]
```

### PROJECT urls.py
Table of contents of all of the urls of the **project** where you will need to include each new app
**Generic Strucure:**
```python
from django.contrib import admin
from django.urls import include, path 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('APP_NAME/', include("APP_NAME.urls"))
]
```


## Special Classes

### render()
It will render an HTML template
First import:

```python
    from django.shortcuts import render` 
    def example(request):
        return render(request, "APP_NAME/")
```

### HttpResponse()
It returns some http response as with the string content as a HTML <h1>

First import:
``
```python
# DONT FORGET TO IMPORT THE MODULE!
from django.http import HttpResponse
def example(request):
    return HttpResponse("Hello this is a new app!")
```

## File Structure

```bash
my_django_project/
├── my_django_project/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── my_app/
│   ├── migrations/
│   │   └── __init__.py
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   └── views.py
├── static/APP_NAME
│              └── (static files like CSS, JavaScript, images, etc.)
├── templates/APP_NAME
│                 └── (HTML templates)
├── manage.py
└── requirements.txt
```
## Template Tags
The template tags are defined by usign `{% %}` syntax inside the HTML code.

**The most common template tags are:**
```HTML
{% extends "APP_NAME/layout.html" %}          <!-- Extend directories from the application -->
{% load static %}                                   <!-- Load an entire folder -->
{% block title %} TITLE! {% endblock %}          <!-- Enter block from the layout -->

{% block main %}           <!-- Enter block from the layout -->

    {% if message %}        <!-- Conditional Statements -->
    <div class="message">
        {{ message }} <!-- "message" variable passed to the template -->
    </div>
    {% endif %}                                     <!-- End of the if statement -->
    
    {% for timer in timers %}                                   <!-- For Loops - Control Flow Statements -->
    <form action="{% url 'APP_NAME:URL Name'%}" method="post">
            {% csrf_token %}           <!-- Validate tokens from post request is MUST!!!  -->
            <input type="submit">
    </form>
        {% empty %}      <!-- In case the there is an empty condition with not values from the loop -->

    {% endfor %}    <!-- End For loop block -->

{% endblock %}  <!-- End the block of <main> -->

{% block scripts %}
<script src="{% static 'APP_NAME/JS_FILE.js' %}"></script>
{% endblock %} <!-- -->