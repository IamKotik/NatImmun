from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def index(request):
    return render(request, "main/index.html")


def simple(request):
    return render(
        request,
        'main/simple.html',
        {
            'title': 'МЕЧТЫ СБЫВАЮТСЯ в СмолГУ',
            'message': 'Я мечтаю получить ОГРОМНЫЙ ПРИЗ!!!!',
        }
    )


def map(request):
    return render(request, 'main/map.html')

