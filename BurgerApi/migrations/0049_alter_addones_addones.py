# Generated by Django 4.1.1 on 2022-10-11 04:31

from django.db import migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('BurgerApi', '0048_alter_category_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='addones',
            name='addOnes',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('salad', 'Salad'), ('cheese', 'Cheese'), ('meat', 'Meat'), ('spice', 'Spice'), ('mayonnaise', 'Mayonnaise')], max_length=500),
        ),
    ]