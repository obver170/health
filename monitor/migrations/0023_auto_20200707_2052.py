# Generated by Django 3.0.7 on 2020-07-07 17:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('monitor', '0022_auto_20200707_2038'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blood',
            name='CP',
            field=models.DecimalField(decimal_places=2, default='0.9', max_digits=4, verbose_name='Цветной показатель'),
        ),
    ]
