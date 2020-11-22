from django.db import models
# Несмотря на подчеркивание красным, этот импорт работает и связывает модель Person из приложения account с текущим
# приложением
from account.models import Person
# from django.conf import settings
# from django.contrib.auth.models import User


# Create your models here.

class Permission(models.Model):
    # Модель для описания прав сотрудника
    PERM_LIST = (
        ('admin', 'Администратор'),
        ('user', 'Пользователь'),
    )
    name_permission = models.CharField(max_length=7, choices=PERM_LIST, verbose_name="Права пользователя")
    descripton_permission = models.CharField(max_length=100, verbose_name="Описание прав", blank=True)

    def __str__(self):
        return str(self.name_permission)

    class Meta:
        verbose_name = 'Права сотрудника'
        verbose_name_plural = 'Права сотрудников'


class Status(models.Model):
    # Описание подчиненности
    STATUS_LIST = (
        ('sub', 'Подчиненный'),
        ('dom', 'Руководитель'),
    )
    name_status = models.CharField(max_length=7, choices=STATUS_LIST, verbose_name="Статус пользователя")
    descripton_status = models.CharField(max_length=100, verbose_name="Описание прав", blank=True)

    def __str__(self):
        return str(self.name_status)

    class Meta:
        verbose_name = 'Статус сотрудника'
        verbose_name_plural = 'Статус сотрудников'


class Departament_name(models.Model):
    # Название подразделения
    name_departament = models.CharField(max_length=30, verbose_name="Название подразделения", unique=True)

    def __str__(self):
        return str(self.name_departament)

    class Meta:
        verbose_name = 'Название подразделения'
        verbose_name_plural = 'Название подразделений'


class Rank(models.Model):
    # Ранг подразделения. Чем выше, тем больше власти у подразделения
    rank = models.SmallIntegerField(verbose_name="Ранг подразделения")

    def __str__(self):
        return str(self.rank)

    class Meta:
        verbose_name = 'Ранг подразделения'
        verbose_name_plural = 'Ранги подразделений'


class Departament(models.Model):
    # Таблица с данными о подразделении
    name_departament = models.OneToOneField(Departament_name, on_delete=models.CASCADE,
                                            verbose_name="Название подразделения", unique=True)
    rank = models.ForeignKey(Rank, on_delete=models.CASCADE, verbose_name="Ранг подразделения")

    def __str__(self):
        return str(self.name_departament)

    class Meta:
        verbose_name = 'Информация о подразделении'
        verbose_name_plural = 'Информация о подразделениях'

class Profile(models.Model):
    # Хранит информацию о сотруднике (дополняет Person из account)
    person = models.OneToOneField(Person, on_delete=models.CASCADE, default=1)

    departament = models.ForeignKey(Departament, on_delete=models.CASCADE, verbose_name="Подразделение")
    status = models.ForeignKey(Status, on_delete=models.CASCADE, verbose_name="Статус сотрудника")
    permission = models.ForeignKey(Permission, on_delete=models.CASCADE, verbose_name="Права сотрудника", default=1)

    def __str__(self):
        return str(self.person)

    class Meta:
        verbose_name = 'Сотрудник'
        verbose_name_plural = 'Сотрудники'


class Amount_hour(models.Model):
    # Таблица хранит количество часов, которое можно добавить к переработке
    hour = models.SmallIntegerField(verbose_name="Количество часов", unique=True)

    def __str__(self):
        return str(self.hour)

    class Meta:
        verbose_name = 'Часы'
        verbose_name_plural = 'Часы'

class Type_overwork(models.Model):
    # Тип переработки
    name_type = models.CharField(max_length=20, unique=True, verbose_name="Тип переработки")
    description_type = models.CharField(max_length=100, blank=True, verbose_name="Описание типа переработки")

    def __str__(self):
        return str(self.name_type)

    class Meta:
        verbose_name = 'Тип переработки'
        verbose_name_plural = 'Тип переработки'


class Overwork(models.Model):
    # Переработка
    profile = models.ForeignKey(Profile, verbose_name="Сотрудник", on_delete=models.CASCADE, default=1)

    is_holiday = models.BooleanField(verbose_name="Во время праздника или выходного дня?", blank=True, default=False)
    type_overwork = models.ForeignKey(Type_overwork, on_delete=models.CASCADE, verbose_name="Тип переработки")
    amount_hour = models.ForeignKey(Amount_hour, on_delete=models.CASCADE, verbose_name="Количество часов")
    date = models.DateField(verbose_name="Дата переработки", default='1999-11-1', blank=True)
    status = models.BooleanField(verbose_name="Проверена?", default=False)
    is_True = models.BooleanField(verbose_name="Заявка верна?", default=False)

    def __str__(self):
        return str(self.profile) + " " + str(self.date) + " " + str(self.type_overwork) + " " + str(self.amount_hour)

    class Meta:
        verbose_name = 'Переработка'
        verbose_name_plural = 'Переработки'


class Type_day_off(models.Model):
    # Тип отгула
    name_type = models.CharField(max_length=20, unique=True, verbose_name="Тип отгула")
    description_type = models.CharField(max_length=100, blank=True, verbose_name="Описание типа отгула")

    def __str__(self):
        return str(self.name_type)

    class Meta:
        verbose_name = 'Тип отгула'
        verbose_name_plural = 'Типы отгулов'


class Day_off(models.Model):
    # Отгулы
    is_vacation = models.BooleanField(verbose_name="Присоединен к отпуску?", blank=True, default=False)
    type_day_off = models.ForeignKey(Type_day_off, on_delete=models.CASCADE, verbose_name="Тип отгула")
    amount_hour = models.ForeignKey(Amount_hour, on_delete=models.CASCADE, verbose_name="Количество часов")
    date = models.DateField(verbose_name="Дата отгула", default='1999-11-1', blank=True)
    status = models.BooleanField(verbose_name="Проверена?", default=False)
    is_True = models.BooleanField(verbose_name="Заявка верна?", default=False)
    profile = models.ForeignKey(Profile, verbose_name="Сотрудник", on_delete=models.CASCADE, default=1)

    def __str__(self):
        return str(self.profile) + " " + str(self.date) + " " + str(self.type_day_off) + " " + str(self.amount_hour)

    class Meta:
        verbose_name = 'Отгул'
        verbose_name_plural = 'Отгулы'