# Generated by Django 3.2.18 on 2023-04-18 01:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('logic', '0009_forecasttable_forecast'),
    ]

    operations = [
        migrations.AlterField(
            model_name='forecast',
            name='date',
            field=models.BigIntegerField(default=1578384000),
        ),
        migrations.AlterField(
            model_name='forecast',
            name='sunrise',
            field=models.BigIntegerField(default=1578384000),
        ),
        migrations.AlterField(
            model_name='forecast',
            name='sunset',
            field=models.BigIntegerField(default=1578384000),
        ),
        migrations.AlterField(
            model_name='forecast',
            name='wind_deg',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='forecast',
            name='wind_speed',
            field=models.IntegerField(default=0),
        ),
    ]