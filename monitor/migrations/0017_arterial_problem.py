# Generated by Django 3.0.7 on 2020-07-01 18:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('monitor', '0016_auto_20200624_1113'),
    ]

    operations = [
        migrations.AddField(
            model_name='arterial',
            name='problem',
            field=models.BooleanField(default=False, verbose_name='Проблема?'),
        ),
    ]