__author__ = 'Ajay'
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
    url(r'^hello$', views.hello, name='post_list'),
]