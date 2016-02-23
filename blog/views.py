from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django import template
from django.template.loader import get_template
from django.views.generic import View
from blog.models.models import Person
from blog.forms import PersonForm


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

def person_new (request):
    if request.method == 'POST':
        form = PersonForm(request.POST)
        if form.is_valid ():
            person = form.save (commit=False)
            person.save ()
            return redirect ('person_detail', pk=person.pk)
    else:
        form = PersonForm ()
    return render(request, 'blog/person_edit.html', {'form': form})

def person_edit (request, pk):
    person = get_object_or_404(Person, pk=pk)
    if request.method == 'POST':
        form = PersonForm (request.POST, instance=person)
        if form.is_valid ():
            person = form.save(commit=False)
            print (person)
            person.first_name = request.POST['first_name']
            person.last_name  = request.POST['last_name']
            person.gender = 'M'
            person.save()
            return redirect('person_detail', pk=person.pk)
    else:
        form = PersonForm (instance=person)
    return render (request, 'blog/person_edit.html', {'form': form})

def person_detail (request, pk):
    person = get_object_or_404(Person, pk=pk)
    return render(request, 'blog/person_detail.html', {'person':person})