# Generated by Django 3.0.7 on 2020-06-10 19:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('monitor', '0003_auto_20200610_2249'),
    ]

    operations = [
        migrations.AlterField(
            model_name='arterial',
            name='status',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='monitor.Status', verbose_name='Оценка'),
        ),
    ]
