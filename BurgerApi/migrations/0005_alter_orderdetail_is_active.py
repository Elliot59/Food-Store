# Generated by Django 4.1.1 on 2023-01-02 07:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BurgerApi', '0004_customerdetail_user_id_orderdetail_is_active_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderdetail',
            name='is_active',
            field=models.BooleanField(auto_created=True, default=True, editable=False),
        ),
    ]
