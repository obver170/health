# Generated by Django 3.0.7 on 2020-07-07 17:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('monitor', '0024_auto_20200707_2053'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blood',
            name='RFV',
            field=models.DecimalField(decimal_places=2, default='11.4', max_digits=5, verbose_name='Анизоцитоз эритроцитов (%)'),
        ),
    ]
