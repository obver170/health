from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Permission(models.Model):
    # Модель для описания прав сотрудника
    PERM_LIST = (
        ('admin', 'Администратор'),
        ('user', 'Пользователь'),
    )
    name_permission = models.CharField(max_length=7, choices=PERM_LIST, verbose_name="Права пользователя")

    def __str__(self):
        return str(self.pk) + " " + str(self.name_permission)

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
    permission = models.ForeignKey(Permission, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.pk) + " " + str(self.name_status)

    class Meta:
        verbose_name = 'Статус сотрудника'
        verbose_name_plural = 'Статус сотрудников'


class Departament_name(models.Model):
    # Название подразделения
    name_departament = models.CharField(max_length=30, verbose_name="Название подразделения", unique=True)

    def __str__(self):
        return str(self.pk) + " " + str(self.name_departament)

    class Meta:
        verbose_name = 'Название подразделения'
        verbose_name_plural = 'Название подразделений'


class List_dom(models.Model):
    # Список вышестоящих подразделений
    name_list = models.CharField(max_length=30, verbose_name="Название списка")
    name_departament = models.ForeignKey(Departament_name, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.pk) + " " + str(self.name_list)

    class Meta:
        verbose_name = 'Список вышестоящих подразделений'
        verbose_name_plural = 'Список вышестоящих подразделениях'


class Departament_info(models.Model):
    # Таблица с данными о подразделении
    name_departament = models.OneToOneField(Departament_name,
                                            on_delete=models.CASCADE, verbose_name="Название подразделения")
    list_dom = models.OneToOneField(List_dom, on_delete=models.CASCADE,
                                    verbose_name="Список начальствующих подразделений")

    def __str__(self):
        return str(self.pk) + " " + str(self.name_departament) + " подчиняется " + str(self.list_dom)

    class Meta:
        verbose_name = 'Информация о подразделении'
        verbose_name_plural = 'Информация о подразделениях'


class Year(models.Model):
    # Таблица с годами
    year = models.SmallIntegerField(verbose_name="Год")

    def __str__(self):
        return str(self.year)

    class Meta:
        verbose_name = 'Год'
        verbose_name_plural = 'Года'


class Month(models.Model):
    # Таблица с месяцами

    MONTH_LIST = (
        ('1', 'Январь'),
        ('2', 'Февраль'),
        ('3', 'Март'),
        ('4', 'Апрель'),
        ('5', 'Май'),
        ('6', 'Июнь'),
        ('7', 'Июль'),
        ('8', 'Август'),
        ('9', 'Сентябрь'),
        ('10', 'Октябрь'),
        ('11', 'Ноябрь'),
        ('12', 'Декабрь'),
    )

    month = models.CharField(max_length=11, choices=MONTH_LIST, verbose_name="Месяц")
    year = models.ForeignKey(Year, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.month) + " " + str(self.year)

    class Meta:
        verbose_name = 'Месяц'
        verbose_name_plural = 'Месяца'


class Week(models.Model):
    # Таблица с неделями в месяце

    WEEK_LIST = (
        ('1', 'Первая'),
        ('2', 'Вторая'),
        ('3', 'Третья'),
        ('4', 'Четвертая'),
        ('5', 'Пятая'),
    )

    week = models.CharField(max_length=11, choices=WEEK_LIST, verbose_name="Неделя")
    month = models.ForeignKey(Month, verbose_name="Неделя", on_delete=models.CASCADE)
    date_start = models.SmallIntegerField(verbose_name="Дата начала недели")
    date_end = models.SmallIntegerField(verbose_name="Дата конца недели")

    def __str__(self):
        return str(self.week) + str(self.month)

    class Meta:
        verbose_name = 'Неделя'
        verbose_name_plural = 'Недели'


class Amount_hour(models.Model):
    # Таблица хранит количество часов, которое можно добавить к переработке
    hour = models.SmallIntegerField(verbose_name="Количество часов")

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
    is_holiday = models.BooleanField(verbose_name="Во время праздника или выходного дня?", blank=False, default=False)
    week = models.ForeignKey(Week, on_delete=models.CASCADE, verbose_name="К какой неделе относится?")
    type_overwork = models.ForeignKey(Type_overwork, on_delete=models.CASCADE, verbose_name="Тип переработки")
    amount_hour = models.ForeignKey(Amount_hour, on_delete=models.CASCADE, verbose_name="Количество часов")
    date = models.DateField(verbose_name="Дата переработки", default='1999-11-1', blank=False)

    def __str__(self):
        return "Переработка: " + str(self.week) + " " + str(self.type_overwork) + str(self.amount_hour)

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
    is_vacation = models.BooleanField(verbose_name="Присоединен к отпуску?", blank=False, default=False)
    week = models.ForeignKey(Week, on_delete=models.CASCADE, verbose_name="К какой неделе относится?")
    type_overwork = models.ForeignKey(Type_day_off, on_delete=models.CASCADE, verbose_name="Тип отгула")
    amount_hour = models.ForeignKey(Amount_hour, on_delete=models.CASCADE, verbose_name="Количество часов")
    date = models.DateField(verbose_name="Дата отгула", default='1999-11-1', blank=False)

    def __str__(self):
        return "Отгулы: " + str(self.week) + " " + str(self.type_overwork) + str(self.amount_hour)

    class Meta:
        verbose_name = 'Отгул'
        verbose_name_plural = 'Отгулы'


class Account_week_work_time(models.Model):
    # Сумма переработки и отгулов за неделю
    overwork = models.ManyToManyField(Overwork, verbose_name="Переработка")
    day_off = models.ManyToManyField(Day_off, verbose_name="Отгулы")

    def __str__(self):
        return "Отгулы: " + str(self.day_off) + " Переработка: " + str(self.overwork)

    class Meta:
        verbose_name = 'Сумма переработки и отгулов за неделю'
        verbose_name_plural = 'Сумма переработки и отгулов за неделю'


class Profile(models.Model):
    # Хранит информацию о сотруднике
    name = models.CharField(max_length=20, verbose_name="Имя")
    surname = models.CharField(max_length=20, verbose_name="Фамилия")
    departament = models.ForeignKey(Departament_name, on_delete=models.CASCADE, verbose_name="Название подразделения")
    status = models.ForeignKey(Status, on_delete=models.CASCADE, verbose_name="Статус сотрудника")
    account_week_work_time = models.ManyToManyField(Account_week_work_time, verbose_name="Учет времени за неделю")

    profile = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Профиль', default=1)

    def __str__(self):
        return str(self.name) + " " + str(self.surname) + " " + str(self.departament)

    class Meta:
        verbose_name = 'Сотрудник'
        verbose_name_plural = 'Сотрудники'
