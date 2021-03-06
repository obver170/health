# Generated by Django 3.0.7 on 2020-06-14 14:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('monitor', '0005_arterial_problem'),
    ]

    operations = [
        migrations.AddField(
            model_name='arterial',
            name='fast_check',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='arterial',
            name='age',
            field=models.CharField(choices=[('20', 'до 20'), ('30', 'от 21 до 30'), ('40', 'от 31 до 40'), ('50', 'от 41 до 50'), ('60', 'от 51 до 60'), ('61', 'старше 60')], max_length=2, verbose_name='Возраст'),
        ),
        migrations.AlterField(
            model_name='arterial',
            name='sex',
            field=models.CharField(choices=[('Мужчина', 'Мужчина'), ('Женщина', 'Женщина')], max_length=7, verbose_name='Пол'),
        ),
    ]
