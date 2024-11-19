# Generated by Django 5.1.2 on 2024-11-15 03:23

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ventas', '0004_alter_venta_producto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='venta',
            name='producto',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='ventas.producto', verbose_name='Producto'),
        ),
    ]