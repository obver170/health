# Generated by Django 3.0.7 on 2020-11-17 17:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('overwork', '0028_auto_20201117_2022'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='overwork',
            name='status',
        ),
    ]
