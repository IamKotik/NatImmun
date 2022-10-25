from django.contrib import admin
from core.models import *


# Register your models here.
@admin.register(Vaccinations)
class VaccinationsAdmin(admin.ModelAdmin):
    list_display = ("code", "name")
