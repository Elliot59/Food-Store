# Generated by Django 4.1.1 on 2023-01-10 03:33

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BurgerApi', '0005_alter_orderdetail_is_active'),
    ]

    operations = [
        migrations.AddField(
            model_name='ordermaster',
            name='delivery_time',
            field=models.CharField(default=datetime.datetime(2023, 1, 10, 10, 3, 17, 148652), max_length=100),
        ),
    ]
