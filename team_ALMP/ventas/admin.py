from django.contrib import admin
from .models import Cliente,Venta,Producto,Proveedor
# Register your models here.
admin.site.register(Cliente)
admin.site.register(Venta)
admin.site.register(Producto)
admin.site.register(Proveedor)
