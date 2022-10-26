from django.db import models

# Create your models here.

RISK = (
    ('YES', 'Да'),
    ('NO', 'Нет'),
)

TYPES = (
    ('KIDS', 'Дети'),
    ('ADULTS', 'Взрослые'),
)


class Vaccinations(models.Model):
    code = models.CharField(max_length=10, primary_key=True)
    name = models.CharField(max_length=100)

    def __str__(self):
        return "{0}".format(self.name)

    class Meta:
        verbose_name = "Прививка"
        verbose_name_plural = "Прививки"


class VaccinationsEpid(models.Model):
    name = models.ForeignKey(Vaccinations, on_delete=models.CASCADE)
    description = models.TextField(blank=True)

    def __str__(self):
        return "{0}".format(self.name)

    class Meta:
        verbose_name = "Прививка по эпидпоказаниям"
        verbose_name_plural = "Прививки по эпидпоказаниям"


class VaccinationsNat(models.Model):
    name = models.ForeignKey(Vaccinations, on_delete=models.CASCADE)
    first_vac = models.TextField(blank=True)
    second_vac = models.TextField(blank=True)
    third_vac = models.TextField(blank=True)
    third_risk = models.TextField(blank=True)
    fourth_risk = models.TextField(blank=True)
    first_revac = models.TextField(blank=True)
    second_revac = models.TextField(blank=True)
    third_revac = models.TextField(blank=True)
    vaccination = models.TextField(blank=True)
    revaccination = models.TextField(blank=True)

    def __str__(self):
        return "{0}".format(self.name)

    class Meta:
        verbose_name = "Прививка нацкалендарь"
        verbose_name_plural = "Прививки нацкалендарь"