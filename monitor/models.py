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

    # индикатор проблемы
    problem = models.BooleanField(verbose_name="Проблема?", default=False)

    person = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Профиль', default=1)

    def __str__(self):
        return str(self.person) + " " + str(self.bottom_pressure) + " - " + str(self.top_pressure)

    class Meta:
        verbose_name = 'Артериальное давление'
        verbose_name_plural = 'Артериальное давление'


class Blood(models.Model):
    person = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Профиль', default=1)
    # индикатор проблемы
    problem = models.BooleanField(verbose_name="Проблема?", default=False)
    # результат проверки
    fast_check = models.CharField(max_length=1000, default='Общий анализ крови проблем не выявил')
    # дата и время проверки
    date = models.DateTimeField(auto_now=True)

    RBC = models.DecimalField(verbose_name="Эритроциты (× 10х12/л)", default="4.1", max_digits=5, decimal_places=2)
    MCV = models.DecimalField(verbose_name="Средний объем эритроцитов (фл или мкм3)",
                              default="81.0", max_digits=5, decimal_places=2)
    MCH = models.DecimalField(verbose_name="Средний уровень HGB в эритроците (пг)",
                              default="26.0", max_digits=5, decimal_places=2)
    MCHC = models.DecimalField(verbose_name="Средняя концентрация эритроцитов в гемоглобине (%)",
                               default="31.0", max_digits=5, decimal_places=2)
    RFV = models.DecimalField(verbose_name="Анизоцитоз эритроцитов (%)",
                              default="11.4", max_digits=5, decimal_places=2)

    HGB = models.DecimalField(verbose_name="Гемоглобин (г/л)", default="128.0", max_digits=5, decimal_places=2)
    HCT = models.DecimalField(verbose_name="Гематокрит (в % соотношении)",
                              default="40.0", max_digits=5, decimal_places=2)
    CP = models.DecimalField(verbose_name="Цветной показатель", default="0.9", max_digits=5, decimal_places=2)
    PLT = models.DecimalField(verbose_name="Тромбоциты (× 10х9/л)", default="178.0", max_digits=5, decimal_places=2)
    ESR = models.DecimalField(verbose_name="СОЭ (мм/ч)", default="2.0", max_digits=5, decimal_places=2)
    MPV = models.DecimalField(verbose_name="Средний объем тромбоцитов (фл или мкм3)",
                              default="8.0", max_digits=5, decimal_places=2)
    WBC = models.DecimalField(verbose_name="Лейкоциты (× 10х9/л)", default="4.0", max_digits=5, decimal_places=2)

    def __str__(self):
        return str(self.pk) + " " + str(self.person) + " имеет проблемы? " + str(self.problem)

    class Meta:
        verbose_name = 'Общий анализ крови'
        verbose_name_plural = 'Общий анализ крови'
