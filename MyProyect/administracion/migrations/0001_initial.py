# Generated by Django 4.1.2 on 2024-06-24 01:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Marca',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('marca', models.CharField(max_length=50)),
                ('descripcion', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Material',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('material', models.CharField(max_length=30)),
                ('descripcion', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Tipo_Instrumento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo_instrumento', models.CharField(max_length=30)),
                ('descripcion', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Instrumentos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('imagen', models.CharField(max_length=200)),
                ('color', models.CharField(max_length=20)),
                ('descripcion', models.CharField(max_length=200)),
                ('marca', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='administracion.marca')),
                ('material', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='administracion.material')),
                ('tipo_instrumento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='administracion.tipo_instrumento')),
            ],
        ),
    ]
