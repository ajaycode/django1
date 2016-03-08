__author__ = 'Ajay'
from django.conf.urls import url, patterns, include
from . import views
from blog.views import Index, PeopleList
from django.contrib import admin
admin.autodiscover()

urlpatterns = [
    #url(r'^$', views.post_list, name='post_list'),
    url(r'^hello$', views.hello, name='post_list'),
    url (r'^$', Index.as_view()),
    url (r'^people$', PeopleList.as_view()),
    url (r'^people_list$', views.people_list),
    url (r'^admin/', include (admin.site.urls)),
    url(r'^person/new/$', views.person_new, name='person_new'),
    url (r'^person/edit/(?P<pk>[0-9]+)/$', views.person_edit, name='person_edit'),
    url (r'^person/(?P<pk>[0-9]+)/$', views.person_detail, name='person_detail'),
    url (r'^person/(?P<pk>[0-9]+)/spouse/', views.spouse_view, name='spouse_view')

]

#To Do from here
"""
url (r'^person/parents/add/(?P<pk>[0-9]+)/$', views.person_add_parents, name='person_add_parents'),
url (r'^person/parents/edit/(?P<pk>[0-9]+)/$', views.person_edit_parents, name='person_edit_parents'),
url (r'^person/parents/remove/(?P<pk>[0-9]+)/$', views.person_remove_parents, name='person_remove_parents'),
url (r'^person/parents/view/(?P<pk>[0-9]+)/$', views.person_view_parents, name='person_view_parents'),
url (r'^person/(?P<pk>[0-9]+)/children/', views.person_view_children, name='person_view_children'),
"""