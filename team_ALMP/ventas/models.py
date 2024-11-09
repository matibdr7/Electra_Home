from django.db import models

# Venta: fecha, Producto, Cliente, precio, created, updated.
# Create your models here.
class Venta(models.Model):
    fecha: str = models.CharField(max_length=10, verbose_name="Fecha")
    producto: str = models.CharField(max_length=200, verbose_name="Producto")
    cliente: str = models.CharField(max_length=50, verbose_name="Cliente")
    precio: float = models.PositiveIntegerField(verbose_name="Precio")
    create: str = models.DateTimeField(auto_now_add=True, verbose_name="Crear")
    update: str = models.DateTimeField(auto_now=True, verbose_name="Actualizar")

    class Meta:
        verbose_name = "Venta"
        verbose_name_plural = "Ventas"
        ordering = ["-created"]
    
    def __str__(self):
        return self.fecha
    