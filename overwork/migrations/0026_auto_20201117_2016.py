# Generated by Django 3.0.7 on 2020-11-17 17:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('overwork', '0025_auto_20201117_2015'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='day_off',
            name='status',
        ),
        migrations.RemoveField(
            model_name='overwork',
            name='status',
        ),
    ]
