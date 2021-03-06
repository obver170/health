# Generated by Django 3.0.7 on 2020-07-06 17:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('monitor', '0018_blood'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='blood',
            options={'verbose_name': 'Общий анализ крови', 'verbose_name_plural': 'Общий анализ крови'},
        ),
        migrations.AddField(
            model_name='blood',
            name='date',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='blood',
            name='fast_check',
            field=models.CharField(default='', max_length=1000),
        ),
    ]
