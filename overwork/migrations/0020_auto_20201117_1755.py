# Generated by Django 3.0.7 on 2020-11-17 14:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('overwork', '0019_auto_20201117_1628'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='account_week_work_time',
        ),
        migrations.AddField(
            model_name='account_week_work_time',
            name='profile',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='overwork.Profile', verbose_name='Сотрудник'),
        ),
    ]
