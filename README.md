# Setup 

    - python3 -m venv env
    - source env/bin/activate   
    - env\Scripts\activate //windows

    - pip install django
    - pip install djangorestframework

# Project
   
    - django-admin startproject tutorial
    - python manage.py migrate
    - python manage.py createsuperuser --email admin@example.com --username admin
    
    add module
    
    - python3 manage.py startapp m1
    

# commands

   - python3 manage.py makemigrations
   - python3 manage.py migrate
    
    run server
    
    - python3 manage.py runserver