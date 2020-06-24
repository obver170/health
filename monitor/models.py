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
    date = models.DateTimeField(auto_now=True)

    person = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Профиль', default=1)



    def __str__(self):
        return str(self.person) + " " + str(self.bottom_pressure) + " - " + str(self.top_pressure)

    class Meta:
        verbose_name = 'Артериальное давление'
        verbose_name_plural = 'Артериальное давление'


