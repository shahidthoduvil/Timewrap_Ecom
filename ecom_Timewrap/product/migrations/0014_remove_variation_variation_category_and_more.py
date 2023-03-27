# Generated by Django 4.1.7 on 2023-03-20 11:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0013_cart_is_paid_cart_razor_pay_order_id_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='variation',
            name='variation_category',
        ),
        migrations.RemoveField(
            model_name='variation',
            name='variation_value',
        ),
        migrations.AddField(
            model_name='variation',
            name='color',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='product.color'),
        ),
        migrations.AddField(
            model_name='variation',
            name='variation',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='variation',
            name='product',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='product.product'),
        ),
    ]