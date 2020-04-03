from django.shortcuts import render

from django.http import HttpResponse


posts = [

    {
        'title': 'post1',
        'content': 'i am from african maldives in south east'
    },
    {
        'title': 'post2',
        'content': 'i am from turkey'
    },
    {
        'title': 'post3',
        'content': 'i am running towards east'
    },
]


def home(request):
    return HttpResponse("<h1>HI google world i am coming !!</h1>")


def index(request):

    context1 = {
        'posts': posts
    }
    return render(request, 'blog/index.html', context1)


def about(request):
    return render(request, 'blog/about.html', {'title': 'about'})
