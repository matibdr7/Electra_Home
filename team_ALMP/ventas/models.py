from django.db import models

# Create your models here.
class Producto (models.Model):
    codigo = models.CharField(max_length=20, unique=True, verbose_name= "Código")
    nombre = models.CharField(max_length=100,verbose_name="Nombre")
    descripcion = models.TextField(verbose_name="Descripción")
    precio = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Precio")
    cantidad=models.PositiveIntegerField(default=0, verbose_name="Cantidad")
    imagen=models.ImageField(verbose_name="Imágen")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name ="producto"
        verbose_name_plural = "productos"
        ordering = ["-created"]
    
    def __str__(self):
        return f'{self.nombre} ({self.codigo})'


class Proveedor(models.Model):
    nombre = models.CharField(max_length=50, verbose_name="Nombre")
    contacto = models.CharField(max_length=100, blank=True, null=True,verbose_name="Contacto")
    telefono = models.CharField(max_length=15, blank=True, null=True, verbose_name="Teléfono")
    email = models.EmailField(blank=True, null=True, verbose_name="Email")
    direccion = models.TextField(blank=True, null=True, verbose_name="Dirección")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name ="proveedor"
        verbose_name_plural = "proveedores"
        ordering = ["-created"]

    def __str__(self):
        return self.nombre

    