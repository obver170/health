# Generated by Django 3.0.7 on 2020-06-08 20:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('monitor', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='arterial',
            options={'verbose_name': 'Артериальное давление', 'verbose_name_plural': 'Артериальное давление'},
        ),
        migrations.AddField(
            model_name='arterial',
            name='name',
            field=models.CharField(default=1, max_length=10, verbose_name='Имя'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='arterial',
            name='age',
            field=models.CharField(choices=[('20', '20'), ('30', '30'), ('40', '40'), ('50', '50'), ('60', '60-65'), ('65', 'старше 65')], max_length=2, verbose_name='Возраст'),
        ),
        migrations.AlterField(
            model_name='arterial',
            name='bottom_pressure',
            field=models.IntegerField(verbose_name='Нижнее давление'),
        ),
        migrations.AlterField(
            model_name='arterial',
            name='sex',
            field=models.CharField(choices=[('M', 'Мужчина'), ('W', 'Женщина')], max_length=1, verbose_name='Пол'),
        ),
        migrations.AlterField(
            model_name='arterial',
            name='top_pressure',
            field=models.IntegerField(verbose_name='Верхнее давление'),
        ),
    ]
