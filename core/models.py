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

VACS = (
    ('ALL', 'Общ'),
    ('NAT', 'Нац'),
    ('EPID', 'Эпид'),
)


class Vaccinations(models.Model):
    code = models.CharField(max_length=10, primary_key=True)
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=5, choices=VACS, default='Общ')

    def __str__(self):
        return "{0}".format(self.name)

    class Meta:
        verbose_name = "Прививка"
        verbose_name_plural = "Прививки"


class VaccinationsEpid(models.Model):
    name = models.ForeignKey(Vaccinations, on_delete=models.CASCADE, related_name="vaccinations_epid")
    description = models.TextField(blank=True)

    def __str__(self):
        return "{0}".format(self.name)

    class Meta:
        verbose_name = "Прививка по эпидпоказаниям"
        verbose_name_plural = "Прививки по эпидпоказаниям"


class VaccinationsNat(models.Model):
    name = models.ForeignKey(Vaccinations, on_delete=models.CASCADE, related_name="vaccinations_nat")
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


class VaccinatedPersonsNat(models.Model):
    code = models.CharField(max_length=10, primary_key=True)
    type = models.CharField(max_length=10, choices=TYPES)
    age = models.TextField()
    age_description = models.TextField(blank=True)
    at_risk = models.CharField(max_length=3, choices=RISK)
    risk_description = models.TextField(blank=True)
    first_vaccin_one = models.ForeignKey(Vaccinations, on_delete=models.CASCADE, blank=True, null=True,
                                         related_name='vac_first_vaccin_one')
    first_vaccin_two = models.ForeignKey(Vaccinations, on_delete=models.CASCADE, blank=True, null=True,
                                         related_name='vac_first_vaccin_two')
    first_vaccin_three = models.ForeignKey(Vaccinations, on_delete=models.CASCADE, blank=True, null=True,
                                           related_name='vac_first_vaccin_three')
    second_vaccin_one = models.ForeignKey(Vaccinations, on_delete=models.CASCADE, blank=True, null=True,
                                          related_name='vac_second_vaccin_one')
    second_vaccin_two = models.ForeignKey(Vaccinations, on_delete=models.CASCADE, blank=True, null=True,
                                          related_name='vac_second_vaccin_two')
    second_vaccin_three = models.ForeignKey(Vaccinations, on_delete=models.CASCADE, blank=True, null=True,
                                            related_name='vac_second_vaccin_three')
    second_vaccin_four = models.ForeignKey(Vaccinations, on_delete=models.CASCADE, blank=True, null=True,
                                           related_name='vac_second_vaccin_four')
    third_vaccin_one = models.ForeignKey(Vaccinations, on_delete=models.CASCADE, blank=True, null=True,
                                         related_name='vac_third_vaccin_one')
    third_vaccin_two = models.ForeignKey(Vaccinations, on_delete=models.CASCADE, blank=True, null=True,
                                         related_name='vac_third_vaccin_two')
    third_vaccin_three = models.ForeignKey(Vaccinations, on_delete=models.CASCADE, blank=True, null=True,
                                           related_name='vac_third_vaccin_three')
    third_vaccin_four = models.ForeignKey(Vaccinations, on_delete=models.CASCADE, blank=True, null=True,
                                          related_name='vac_third_vaccin_four')
    third_vaccin_risk = models.ForeignKey(Vaccinations, on_delete=models.CASCADE, blank=True, null=True,
                                          related_name='vac_third_vaccin_risk')
    fourth_vaccin_risk = models.ForeignKey(Vaccinations, on_delete=models.CASCADE, blank=True, null=True,
                                           related_name='vac_fourth_vaccin_risk')
    first_revac_one = models.ForeignKey(Vaccinations, on_delete=models.CASCADE, blank=True, null=True,
                                        related_name='vac_first_revac_one')
    first_revac_two = models.ForeignKey(Vaccinations, on_delete=models.CASCADE, blank=True, null=True,
                                        related_name='vac_first_revac_two')
    second_revac = models.ForeignKey(Vaccinations, on_delete=models.CASCADE, blank=True, null=True,
                                     related_name='vac_second_revac')
    third_revac = models.ForeignKey(Vaccinations, on_delete=models.CASCADE, blank=True, null=True,
                                    related_name='vac_third_revac')
    vaccintaion_one = models.ForeignKey(Vaccinations, on_delete=models.CASCADE, blank=True, null=True,
                                        related_name='vac_vaccintaion_one')
    vaccintaion_one_descript = models.TextField(blank=True)
    vaccintaion_two = models.ForeignKey(Vaccinations, on_delete=models.CASCADE, blank=True, null=True,
                                        related_name='vac_vaccintaion_two')
    vaccintaion_three = models.ForeignKey(Vaccinations, on_delete=models.CASCADE, blank=True, null=True,
                                          related_name='vac_vaccintaion_three')
    revaccintaion_one = models.ForeignKey(Vaccinations, on_delete=models.CASCADE, blank=True, null=True,
                                          related_name='vac_revaccintaion_one')
    revaccintaion_one_descript = models.TextField(blank=True)
    revaccintaion_two = models.ForeignKey(Vaccinations, on_delete=models.CASCADE, blank=True, null=True,
                                          related_name='vac_revaccintaion_two')

    def __str__(self):
        return "{0}".format(self.age)

    class Meta:
        verbose_name = "Человек по нацкалендарю"
        verbose_name_plural = "Люди по нацкалендарю"
