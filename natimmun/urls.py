"""natimmun URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from core import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('calendar_list', views.calendar_list, name='calendar_list'),
    path('nat_calendar', views.nat_calendar, name='nat_calendar'),
    path('epid_calendar', views.epid_calendar, name='epid_calendar'),
    path('ages', views.ages, name='ages'),
    path('categories', views.categories, name='categories'),
    path('children', views.children, name='children'),
    path('adults', views.adults, name='adults'),
    path('risk', views.risk, name='risk'),
    path('vaccinations', views.vaccinations, name='vaccinations'),
    path('search', views.search, name='search'),
    path('mobile_app', views.mobile_app, name='mobile_app'),
    path('simple/', views.simple, name='simple'),
    path('map/', views.map, name='map'),
    path('api/vaccinations_epid', views.VaccinationsView.as_view(), name="vaccinations_api"),
]
