# Generated by Django 2.0.5 on 2019-03-01 02:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0021_auto_20190301_0740'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='mobile_number',
            field=models.DecimalField(decimal_places=0, max_digits=10, max_length=10),
        ),
    ]
