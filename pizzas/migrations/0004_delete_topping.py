# Generated by Django 3.0.6 on 2020-05-11 19:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pizzas', '0003_topping'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Topping',
        ),
    ]
