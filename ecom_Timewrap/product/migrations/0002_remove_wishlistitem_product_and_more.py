# Generated by Django 4.1.7 on 2023-03-17 05:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='wishlistitem',
            name='product',
        ),
        migrations.RemoveField(
            model_name='wishlistitem',
            name='wishlist',
        ),
        migrations.DeleteModel(
            name='Wishlist',
        ),
        migrations.DeleteModel(
            name='WishlistItem',
        ),
    ]
