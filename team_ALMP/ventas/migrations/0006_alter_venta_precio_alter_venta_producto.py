# Generated by Django 5.1.2 on 2024-11-22 16:48

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ventas', '0005_alter_venta_producto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='venta',
            name='precio',
            field=models.DecimalField(decimal_places=2, max_digits=10, validators=[django.core.validators.MinValueValidator(0.0)], verbose_name='Precio'),
        ),
        migrations.AlterField(
            model_name='venta',
            name='producto',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='ventas.producto', verbose_name='Producto'),
        ),
    ]
