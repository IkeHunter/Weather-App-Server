# Generated by Django 3.2.18 on 2023-04-18 00:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('logic', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Condition',
        ),
        migrations.DeleteModel(
            name='ConditionGroup',
        ),
        migrations.DeleteModel(
            name='Conditionset',
        ),
        migrations.DeleteModel(
            name='DayConditions',
        ),
        migrations.DeleteModel(
            name='DayConditions2',
        ),
        migrations.AddField(
            model_name='conditionslist',
            name='date',
            field=models.BigIntegerField(default=1578384000),
            preserve_default=False,
        ),
    ]
