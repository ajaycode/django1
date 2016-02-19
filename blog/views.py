from django.shortcuts import render
from django.http import HttpResponse
from django import template
from django.template.loader import get_template
from django.template import Context


# Create your views here.


def post_list (request):
    return render (request, 'blog/post_list.html', {})

def hello (request):
    t = get_template('post_list.html')
    html = t.render({'name': "Joe"})
    return HttpResponse (html)