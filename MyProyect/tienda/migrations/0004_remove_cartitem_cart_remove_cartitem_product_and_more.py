# Generated by Django 5.0.7 on 2024-07-19 07:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tienda', '0003_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cartitem',
            name='cart',
        ),
        migrations.RemoveField(
            model_name='cartitem',
            name='product',
        ),
        migrations.DeleteModel(
            name='Cart',
        ),
        migrations.DeleteModel(
            name='CartItem',
        ),
    ]
