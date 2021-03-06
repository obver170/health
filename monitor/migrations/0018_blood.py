# Generated by Django 3.0.7 on 2020-07-06 17:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('monitor', '0017_arterial_problem'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blood',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('problem', models.BooleanField(default=False, verbose_name='Проблема?')),
                ('RBC', models.DecimalField(decimal_places=2, default='3.6', max_digits=4, verbose_name='Эритроциты (× 10х12/л)')),
                ('MCV', models.DecimalField(decimal_places=2, default='81', max_digits=5, verbose_name='Средний объем эритроцитов (фл или мкм3)')),
                ('MCH', models.DecimalField(decimal_places=2, default='26', max_digits=5, verbose_name='Средний уровень HGB в эритроците (пг)')),
                ('MCHC', models.DecimalField(decimal_places=2, default='31', max_digits=5, verbose_name='Средняя концентрация эритроцитов в гемоглобине (%)')),
                ('RFV', models.DecimalField(decimal_places=2, default='11.3', max_digits=5, verbose_name='Анизоцитоз эритроцитов (%)')),
                ('HGB', models.DecimalField(decimal_places=2, default='128', max_digits=5, verbose_name='Гемоглобин (г/л)')),
                ('HCT', models.DecimalField(decimal_places=2, default='128', max_digits=5, verbose_name='Гематокрит (в % соотношении)')),
                ('CP', models.DecimalField(decimal_places=2, default='0.8', max_digits=4, verbose_name='Гемоглобин (г/л)')),
                ('PLT', models.DecimalField(decimal_places=2, default='178', max_digits=5, verbose_name='Тромбоциты (× 10х9/л)')),
                ('ESR', models.DecimalField(decimal_places=2, default='2', max_digits=4, verbose_name='СОЭ (мм/ч)')),
                ('MPV', models.DecimalField(decimal_places=2, default='8', max_digits=4, verbose_name='Средний объем тромбоцитов (фл или мкм3)')),
                ('WBC', models.DecimalField(decimal_places=2, default='4', max_digits=4, verbose_name='Лейкоциты (× 10х9/л)')),
                ('person', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Профиль')),
            ],
        ),
    ]
