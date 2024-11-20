from django.shortcuts import render
from .models import Venta, Cliente, Producto, Proveedor
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy

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
class ClienteCreate(CreateView):
    model = Cliente
    fields = ['nombre', 'apellido', 'email', 'celular', 'foto']
    success_url = reverse_lazy('modelos')
    
