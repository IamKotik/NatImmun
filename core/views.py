from django.shortcuts import render
from django.http import HttpResponse
from core.models import *


# Create your views here.

def index(request):
    return render(request, "main/index.html")


def calendar_list(request):
    return render(request, "main/calendar_list.html")


def nat_calendar(request):
    return render(request, "main/nat_calendar.html")


def epid_calendar(request):
    vaccinations_epid = VaccinationsEpid.objects.all()
    return render(request, "main/epid_calendar.html", context={
        'vaccinations_epid': vaccinations_epid
    })


def ages(request):
    return render(request, "main/ages.html")


def categories(request):
    return render(request, "main/categories.html")


def vaccinations(request):
    vaccinations_nat = VaccinationsNat.objects.all()
    return render(request, "main/vaccinations.html", context={
        'vaccinations_nat': vaccinations_nat,
    })


def search(request):
    return render(request, "main/search.html")


def mobile_app(request):
    return render(request, "main/mobile_app.html")


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
