# Generated by Django 5.0.7 on 2024-07-19 06:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('administracion', '0004_alter_instrumentos_precio'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='instrumentos',
            name='stock',
        ),
    ]
