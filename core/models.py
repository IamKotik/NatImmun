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
