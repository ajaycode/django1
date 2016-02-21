__author__ = 'Ajay'
from django.conf.urls import url, patterns, include
from . import views
from blog.views import Index, PeopleList
#from django.contrib import admin
#admin.autodiscover()

urlpatterns = [
    #url(r'^$', views.post_list, name='post_list'),
    url(r'^hello$', views.hello, name='post_list'),
    url (r'^$', Index.as_view()),
    url (r'^people$', PeopleList.as_view()),
    url (r'^people_list$', views.people_list)
    #url (r'^admin/', include (admin.site.urls))
]