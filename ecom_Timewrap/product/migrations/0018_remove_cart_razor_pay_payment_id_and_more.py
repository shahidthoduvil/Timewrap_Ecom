# Generated by Django 4.1.7 on 2023-03-21 02:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0017_remove_cart_cart_id_remove_cartitem_user_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='razor_pay_payment_id',
        ),
        migrations.RemoveField(
            model_name='cart',
            name='razor_pay_payment_signature',
        ),
        migrations.AlterField(
            model_name='cart',
            name='razor_pay_order_id',
            field=models.CharField(blank=True, max_length=100, null=True, unique=True),
        ),
    ]
