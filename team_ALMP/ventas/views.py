from django.shortcuts import render
from .models import Venta, Cliente, Producto, Proveedor

def modelos(request):
    ventas = Venta.objects.all()
    clientes = Cliente.objects.all()
    productos = Producto.objects.all()
    proveedores = Proveedor.objects.all()
    return render(request, "ventas/modelos.html", {'ventas':ventas}, {'clientes':clientes}, {'productos':productos}, {'proveedores':proveedores})

# Create your views here.
