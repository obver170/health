# Generated by Django 3.0.7 on 2020-11-16 16:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('overwork', '0005_auto_20201116_1943'),
    ]

    operations = [
        migrations.AlterField(
            model_name='day_off',
            name='date',
            field=models.DateField(default='1999-11-1', verbose_name='Дата отгула'),
        ),
        migrations.AlterField(
            model_name='overwork',
            name='date',
            field=models.DateField(default='1999-11-1', verbose_name='Дата переработки'),
        ),
    ]