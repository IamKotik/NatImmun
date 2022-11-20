from django.contrib import admin
from core.models import *


# Register your models here.
@admin.register(Vaccinations)
class VaccinationsAdmin(admin.ModelAdmin):
    list_display = ("code", "name")


@admin.register(VaccinationsEpid)
class VaccinationsEpidAdmin(admin.ModelAdmin):
    list_display = ("name",)


@admin.register(VaccinationsNat)
class VaccinationsNatAdmin(admin.ModelAdmin):
    list_display = ("name",)


@admin.register(VaccinatedPersonsNat)
class VaccinatedPersonsNatAdmin(admin.ModelAdmin):
    list_display = ("age",)
