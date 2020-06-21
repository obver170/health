# Generated by Django 3.0.7 on 2020-06-18 09:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Имя')),
                ('patronymic', models.CharField(max_length=50, verbose_name='Отчество')),
                ('surname', models.CharField(max_length=50, verbose_name='Фамилия')),
                ('number', models.CharField(max_length=12, verbose_name='Номер телефона')),
                ('sex', models.CharField(choices=[('Мужчина', 'Мужчина'), ('Женщина', 'Женщина')], max_length=7, verbose_name='Пол')),
                ('dob', models.DateField(verbose_name='Дата рождения')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Профиль',
                'verbose_name_plural': 'Профили',
            },
        ),
    ]