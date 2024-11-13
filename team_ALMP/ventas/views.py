from django.shortcuts import render
from .models import Venta, Cliente, Producto, Proveedor

def modelos(request):
    ventas = Venta.objects.all()
    clientes = Cliente.objects.all()
    productos = Producto.objects.all()
    proveedores = Proveedor.objects.all()

    contexto = {
        'ventas': ventas,
        'clientes': clientes,
        'productos': productos,
        'proveedores': proveedores,
    }
    
    return render(request, "ventas/modelos.html", contexto)
# Create your views here.
