# Generated by Django 3.0.7 on 2020-11-16 16:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('overwork', '0009_auto_20201116_1952'),
    ]

    operations = [
        migrations.CreateModel(
            name='Account_week_work_time',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day_off', models.ManyToManyField(to='overwork.Day_off', verbose_name='Отгулы')),
                ('overwork', models.ManyToManyField(to='overwork.Overwork', verbose_name='Переработка')),
            ],
        ),
    ]
