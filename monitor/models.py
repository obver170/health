from django.db import models
# from account.models import Person
from django.contrib.auth.models import User


# Create your models here.

class Arterial(models.Model):

    name = models.CharField(max_length=10, verbose_name="Имя", default="Владимир")
    sex = models.CharField(max_length=7, verbose_name="Пол", default="Мужчина")
    age = models.CharField(max_length=3, verbose_name="Возраст", default="45")
    bottom_pressure = models.IntegerField(verbose_name="Нижнее давление", default="80")
    top_pressure = models.IntegerField(verbose_name="Верхнее давление", default="120")
    fast_check = models.CharField(max_length=100, default='')

    person = models.ForeignKey(User, null=True, blank=True, on_delete=models.PROTECT, verbose_name='Профиль')

    # status = models.ForeignKey('Status', null=True, blank=True, on_delete=models.PROTECT, verbose_name='Оценка')

    def __str__(self):
        return self.name + " " + str(self.bottom_pressure) + " - " + str(self.top_pressure)

    class Meta:
        verbose_name = 'Артериальное давление'
        verbose_name_plural = 'Артериальное давление'


class Status(models.Model):
    STATUS_LIST = (
        ('problem', 'проблема'),
        ('normally', 'в пределах нормы'),
    )

    str_status = models.CharField(max_length=10, choices=STATUS_LIST, verbose_name='Оценка показателя')

    def __str__(self):
        return self.str_status

    class Meta:
        verbose_name = 'Статус'
        verbose_name_plural = 'Статусы'
