# Generated by Django 3.0.7 on 2020-06-21 19:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('monitor', '0008_auto_20200621_2243'),
    ]

    operations = [
        migrations.RenameField(
            model_name='arterial',
            old_name='person_m',
            new_name='person',
        ),
    ]
