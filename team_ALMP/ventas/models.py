from django.db import models

# Venta: fecha, Producto, Cliente, precio, created, updated.
# Create your models here.
class Venta(models.Model):
    fecha = models.DateTimeField(verbose_name="Fecha")
    producto = models.CharField(max_length=200, verbose_name="Producto")
    cliente = models.CharField(max_length=50, verbose_name="Cliente")
    precio = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Precio")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Crear")
    updated = models.DateTimeField(auto_now=True, verbose_name="Actualizar")

    class Meta:
        verbose_name = "Venta"
        verbose_name_plural = "Ventas"
        ordering = ["-created"]
    
    def __str__(self):
        return f"Venta del {self.fecha.strftime('%d-%m-%Y %H:%M')} - Cliente: {self.cliente}"

#Cliente: nombre, apellido, email, celular, foto, created, updated.
class Cliente(models.Model):
    nombre = models.CharField(max_length=50, verbose_name="Nombre")
    apellido = models.CharField(max_length=50, verbose_name="Apellido")
    email = models.EmailField(verbose_name="Email")
    celular = models.IntegerField(verbose_name="Celular")
    foto = models.ImageField(verbose_name="Foto", upload_to="clientes")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now = True)

    class Meta:
        verbose_name = "cliente"
        verbose_name_plural = "clientes"
        ordering = ["-created"] #Orden descendente
        
    def __str__(self):
        return self.nombre
    
class Producto (models.Model):
    codigo = models.CharField(max_length=20, unique=True, verbose_name= "Código")
    nombre = models.CharField(max_length=100,verbose_name="Nombre")
    descripcion = models.TextField(verbose_name="Descripción")
    precio = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Precio")
    cantidad=models.PositiveIntegerField(default=0, verbose_name="Cantidad")
    imagen=models.ImageField(verbose_name="Imágen", upload_to="productos")
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