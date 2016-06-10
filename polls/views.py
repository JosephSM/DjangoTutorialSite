from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse('This is the Polls index page')


def aboutme(request):
    return HttpResponse('this is the about me page')
