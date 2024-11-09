from django.db import models

# Create your models here.

#Cliente: nombre, apellido, email, celular, foto, created, updated.
class Cliente(models.Model):
    nombre = models.CharField(max_length=50, verbose_name="Nombre")
    apellido = models.CharField(max_lenght=50, verbose_name="Apellido")
    email = models.EmailField(verbose_name="Email")
    celular = models.IntegerField(verbose_name="Celular")
    foto = models.ImageField(verbose_name="Foto")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now = True)

    class Meta:
        verbose_name = "cliente"
        verbose_name_plural = "clientes"
        ordering = ["-created"] #Orden descendente
        
    def __str__(self):
        return self.nombre
    
    