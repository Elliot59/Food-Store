# Generated by Django 4.1.1 on 2023-01-10 05:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BurgerApi', '0015_alter_ordermaster_delivery_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ordermaster',
            name='delivery_time',
            field=models.TimeField(default='11:30:41'),
        ),
    ]