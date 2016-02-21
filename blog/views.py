from django.shortcuts import render
from django.http import HttpResponse
from django import template
from django.template.loader import get_template
from django.views.generic import View
from blog.models import Person


# Create your views here.


def post_list (request):
    return render (request, 'blog/post_list.html', {})

def hello (request):
    t = get_template('base.html')
    html = t.render({'name': "Jane"})
    return HttpResponse (html)

class Index (View):
    def get (self, request):
        return  HttpResponse ("Called from a get Request")
    def post (self, request):
        return  HttpResponse ('Called from a post request')

class PeopleList (View):
    def get(self, request):
        pers = Person.objects.all()
        #pers = people[0]
        return render (request,'profile.html', {'persons': pers})

def people_list (request):
    if request.method == "GET":
        persons = Person.objects.all()
        return render(request,'profile.html' , {'persons': persons})