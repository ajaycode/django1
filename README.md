

Admin Site:
````
Username: admin
Password: supervisor
````

####Install Django####

    pip install django==1.9.2

####Run HTTP Server####

    python manage.py runserver
    python manage.py runserver 0.0.0.0:80000 #site accessible on LAN

####Relevant Links####
* [Split views into multiple files](http://stackoverflow.com/questions/1921771/django-split-views-py-in-several-files)
* Login, Logout, Register [1](http://stackoverflow.com/questions/20856800/is-there-a-example-in-django-1-6-and-python-3-to-build-a-accounts-app-includer?rq=1), [2](https://github.com/ubernostrum/django-registration), [3](http://stackoverflow.com/questions/6014834/django-login-logout?rq=1), [4](https://docs.djangoproject.com/en/1.9/topics/auth/default/)

####Queries to run####
* Get education records Person.his_education.objects.all()
````
     from blog.models import Person, Education
     pers = Person.objects.all()[0]
     pers.his_education.all()
````

* Usage of Django Shell
````
     from blog.models.models import Person
     p = Person.objects.all()
     print (p[0].spouse)
````
* Get spouse(s)
* Get children
* Get parents
* Get siblings
* Get marital status