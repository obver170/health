# Generated by Django 3.0.7 on 2020-06-24 07:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('monitor', '0012_remove_arterial_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='arterial',
            name='person',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Профиль'),
        ),
    ]
