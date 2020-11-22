# Generated by Django 3.0.7 on 2020-11-17 14:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('overwork', '0020_auto_20201117_1755'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='day_off',
            name='week',
        ),
        migrations.RemoveField(
            model_name='overwork',
            name='week',
        ),
        migrations.AddField(
            model_name='account_week_work_time',
            name='week',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='overwork.Week', verbose_name='К какой неделе относится?'),
        ),
    ]