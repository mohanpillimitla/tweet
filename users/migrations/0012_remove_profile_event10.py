# Generated by Django 2.0.5 on 2019-02-28 07:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0011_auto_20190226_1121'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='event10',
        ),
    ]
