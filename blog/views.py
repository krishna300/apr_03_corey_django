from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse


def home(request):
    return HttpResponse("<h1>HI google world i am coming !!</h1>")


def index(request):
    return render(request, 'blog/index.html')
