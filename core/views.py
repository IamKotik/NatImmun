from django.shortcuts import render
from django.http import HttpResponse
from django.db.models import Q

# Create your views here.
from rest_framework.response import Response
from rest_framework.views import APIView

from core.models import *
from core.serializers import *


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
    ages = VaccinatedPersonsNat.objects.all()
    return render(request, "main/ages.html", context={
        'ages': ages
    })


def categories(request):
    return render(request, "main/categories.html")


def children(request):
    children = VaccinatedPersonsNat.objects.filter(type='KIDS')
    return render(request, "main/children.html", context={
        'children': children
    })


def adults(request):
    adults = VaccinatedPersonsNat.objects.filter(type='ADULTS')
    return render(request, "main/adults.html", context={
        'adults': adults
    })


def risk(request):
    risks = VaccinatedPersonsNat.objects.filter(at_risk='YES')
    return render(request, "main/risk.html", context={
        'risks': risks
    })


def vaccinations(request):
    vaccinations_nat = VaccinationsNat.objects.all()
    return render(request, "main/vaccinations.html", context={
        'vaccinations_nat': vaccinations_nat,
    })


# def search(request):
#     return render(request, "main/search.html")


def mobile_app(request):
    return render(request, "main/mobile_app.html")


def search(request):
    query = request.GET.get("q").strip()
    vaccins = Vaccinations.objects.filter(Q(name__icontains=query[:-1]))
    return render(request, 'main/search.html', context={
        'vaccins': vaccins,
    })


class VaccinationsView(APIView):
    def get(self, request):
        vaccins = Vaccinations.objects.all()
        serializer = VaccinationsSerializer(vaccins, many="True")
        return Response({"vaccinations": serializer.data})


# убрать
class VaccinationsEpidView(APIView):
    def get(self, request):
        vaccins_epid = VaccinationsEpid.objects.all()
        serializer = VaccinationsEpidSerializer(vaccins_epid, many="True")
        return Response({"vaccins_epid": serializer.data})


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
