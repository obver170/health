from django.db import models

# Create your models here.

class Arterial(models.Model):

    SEX_LIST = (
        ('Мужчина', 'Мужчина'),
        ('Женщина', 'Женщина'),
    )

    AGE_LIST = (
        ('20', 'до 20'),
        ('30', 'от 21 до 30'),
        ('40', 'от 31 до 40'),
        ('50', 'от 41 до 50'),
        ('60', 'от 51 до 60'),
        ('61', 'старше 60'),
    )
    name = models.CharField(max_length=10, verbose_name="Имя")
    sex = models.CharField(max_length=7, choices=SEX_LIST, verbose_name="Пол")
    age = models.CharField(max_length=2, choices=AGE_LIST, verbose_name="Возраст")
    bottom_pressure = models.IntegerField(verbose_name="Нижнее давление")
    top_pressure = models.IntegerField(verbose_name="Верхнее давление")
    problem = models.BooleanField(verbose_name="Проблема?", default=False)
    fast_check = models.CharField(max_length=100, default='')
    status = models.ForeignKey('Status', null=True, blank=True, on_delete=models.PROTECT, verbose_name='Оценка')

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