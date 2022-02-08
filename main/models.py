from django.db import models


class City(models.Model):
    name = models.CharField(verbose_name='Название', max_length=255, unique=True)

    def __str__(self):
        return f"{self.name}"


    class Meta:
        verbose_name = "Город"
        verbose_name_plural = "Города"


class Resident(models.Model):
    last_name = models.CharField(verbose_name='Фамилия', max_length=255, blank=False, null=False)
    first_name = models.CharField(verbose_name='Имя', max_length=255, blank=False, null=False)
    patronymic = models.CharField(verbose_name='Отчество', max_length=255, blank=False, null=False)
    city = models.ForeignKey(City, verbose_name='Город', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.first_name} {self.last_name} {self.patronymic}"


    class Meta:
        verbose_name = "Житель"
        verbose_name_plural = "Жители"
