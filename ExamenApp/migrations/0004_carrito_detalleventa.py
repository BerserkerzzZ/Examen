# Generated by Django 5.0.6 on 2024-07-11 03:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ExamenApp', '0003_alter_producto_nombre_prod'),
    ]

    operations = [
        migrations.CreateModel(
            name='Carrito',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_carrito', models.PositiveSmallIntegerField()),
                ('total_precio', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='DetalleVenta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_producto', models.PositiveSmallIntegerField()),
                ('id_carrito', models.PositiveSmallIntegerField()),
                ('nombre_prod', models.CharField(max_length=100)),
                ('cantidad_prod', models.PositiveSmallIntegerField()),
                ('precio_prod', models.IntegerField()),
            ],
        ),
    ]
