from django.db import models
from django.conf import settings

# Create your models here.

class Person(models.Model):

    SEX_LIST = (
        ('Мужчина', 'Мужчина'),
        ('Женщина', 'Женщина'),
    )

    name = models.CharField(max_length=50, verbose_name="Имя")
    patronymic = models.CharField(max_length=50, verbose_name="Отчество")
    surname = models.CharField(max_length=50, verbose_name="Фамилия")
    number = models.CharField(max_length=12, verbose_name="Номер телефона")
    sex = models.CharField(max_length=7, choices=SEX_LIST, verbose_name="Пол")
    dob = models.DateField(verbose_name="Дата рождения")
    photo = models.ImageField(upload_to='users/%Y/%m/%d', blank=True)

    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'

    def __str__(self):
        return self.surname + " " + self.name[0] + "." + self.patronymic[0] + "."


