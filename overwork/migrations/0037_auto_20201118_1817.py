# Generated by Django 3.0.7 on 2020-11-18 15:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('overwork', '0036_auto_20201118_1803'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='week',
            name='month',
        ),
        migrations.RemoveField(
            model_name='day_off',
            name='week',
        ),
        migrations.RemoveField(
            model_name='overwork',
            name='week',
        ),
        migrations.DeleteModel(
            name='Month',
        ),
        migrations.DeleteModel(
            name='Week',
        ),
        migrations.DeleteModel(
            name='Year',
        ),
    ]
