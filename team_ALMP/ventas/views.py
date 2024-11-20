from django.shortcuts import render
from .models import Venta, Cliente, Producto, Proveedor
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.list import ListView
from django.utils import timezone

from django.urls import reverse_lazy

def modelos(request):
    ventas = Venta.objects.all()
    clientes = Cliente.objects.all()
    #clientes = Cliente.objects.filter(nombre__contains='fel')
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
    
class ClienteUpdate(UpdateView):
    model = Cliente
    fields = ['nombre', 'apellido', 'email', 'celular', 'foto']
    template_name_suffix = '_update_cliente'
    
    def get_success_url(self):
        return reverse_lazy('modelos')

def buscar_clientes(request):
    # Si hay un término de búsqueda en la solicitud
    busqueda = request.GET.get('search', '')  # 'search' es el nombre del parámetro de la barra de búsqueda
    clientes = Cliente.objects.filter(nombre__contains=busqueda)
    return render(request, 'ventas/buscar_cliente.html', {'clientes': clientes})