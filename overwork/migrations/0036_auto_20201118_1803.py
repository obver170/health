# Generated by Django 3.0.7 on 2020-11-18 15:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('overwork', '0035_auto_20201118_1801'),
    ]

    operations = [
        migrations.AlterField(
            model_name='amount_hour',
            name='hour',
            field=models.SmallIntegerField(unique=True, verbose_name='Количество часов'),
        ),
    ]