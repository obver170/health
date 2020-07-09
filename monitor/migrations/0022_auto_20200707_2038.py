# Generated by Django 3.0.7 on 2020-07-07 17:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('monitor', '0021_auto_20200707_2036'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blood',
            name='ESR',
            field=models.DecimalField(decimal_places=2, default='2.0', max_digits=4, verbose_name='СОЭ (мм/ч)'),
        ),
        migrations.AlterField(
            model_name='blood',
            name='HCT',
            field=models.DecimalField(decimal_places=2, default='40.0', max_digits=5, verbose_name='Гематокрит (в % соотношении)'),
        ),
        migrations.AlterField(
            model_name='blood',
            name='HGB',
            field=models.DecimalField(decimal_places=2, default='128.0', max_digits=5, verbose_name='Гемоглобин (г/л)'),
        ),
        migrations.AlterField(
            model_name='blood',
            name='MCH',
            field=models.DecimalField(decimal_places=2, default='26.0', max_digits=5, verbose_name='Средний уровень HGB в эритроците (пг)'),
        ),
        migrations.AlterField(
            model_name='blood',
            name='MCHC',
            field=models.DecimalField(decimal_places=2, default='31.0', max_digits=5, verbose_name='Средняя концентрация эритроцитов в гемоглобине (%)'),
        ),
        migrations.AlterField(
            model_name='blood',
            name='MCV',
            field=models.DecimalField(decimal_places=2, default='81.0', max_digits=5, verbose_name='Средний объем эритроцитов (фл или мкм3)'),
        ),
        migrations.AlterField(
            model_name='blood',
            name='MPV',
            field=models.DecimalField(decimal_places=2, default='8.0', max_digits=4, verbose_name='Средний объем тромбоцитов (фл или мкм3)'),
        ),
        migrations.AlterField(
            model_name='blood',
            name='PLT',
            field=models.DecimalField(decimal_places=2, default='178.0', max_digits=5, verbose_name='Тромбоциты (× 10х9/л)'),
        ),
        migrations.AlterField(
            model_name='blood',
            name='WBC',
            field=models.DecimalField(decimal_places=2, default='4.0', max_digits=4, verbose_name='Лейкоциты (× 10х9/л)'),
        ),
    ]