# Generated by Django 3.0.7 on 2020-07-07 08:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('monitor', '0019_auto_20200706_2038'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blood',
            name='fast_check',
            field=models.CharField(default='Общий анализ крови проблем не выявил', max_length=1000),
        ),
    ]
