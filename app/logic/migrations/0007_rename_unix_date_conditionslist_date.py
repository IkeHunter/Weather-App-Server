# Generated by Django 3.2.18 on 2023-04-18 00:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('logic', '0006_remove_conditionslist_date'),
    ]

    operations = [
        migrations.RenameField(
            model_name='conditionslist',
            old_name='unix_date',
            new_name='date',
        ),
    ]
