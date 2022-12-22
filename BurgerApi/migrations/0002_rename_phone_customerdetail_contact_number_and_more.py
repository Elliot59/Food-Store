# Generated by Django 4.1.1 on 2022-12-22 07:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('BurgerApi', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customerdetail',
            old_name='phone',
            new_name='contact_number',
        ),
        migrations.RenameField(
            model_name='customerdetail',
            old_name='deliveryAddress',
            new_name='delivery_address',
        ),
        migrations.RenameField(
            model_name='customerdetail',
            old_name='paymentType',
            new_name='payment_type',
        ),
        migrations.RenameField(
            model_name='order',
            old_name='addOns',
            new_name='add_ons',
        ),
        migrations.RenameField(
            model_name='order',
            old_name='orderTime',
            new_name='order_time',
        ),
        migrations.RenameField(
            model_name='order',
            old_name='products',
            new_name='product',
        ),
        migrations.RenameField(
            model_name='orderdetail',
            old_name='addOns',
            new_name='add_ons',
        ),
        migrations.RenameField(
            model_name='orderdetail',
            old_name='orderMasterId',
            new_name='order_master_id',
        ),
        migrations.RenameField(
            model_name='orderdetail',
            old_name='productsId',
            new_name='product_id',
        ),
        migrations.RenameField(
            model_name='ordermaster',
            old_name='customerDetail',
            new_name='customer_detail',
        ),
        migrations.RenameField(
            model_name='ordermaster',
            old_name='orderNo',
            new_name='order_no',
        ),
        migrations.RenameField(
            model_name='ordermaster',
            old_name='orderTime',
            new_name='order_time',
        ),
        migrations.RenameField(
            model_name='ordermaster',
            old_name='userId',
            new_name='user_id',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='addons',
            new_name='add_ons',
        ),
    ]