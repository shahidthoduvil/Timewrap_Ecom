# Generated by Django 4.1.7 on 2023-03-28 15:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0004_orderitem_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='payment',
            name='discount',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
