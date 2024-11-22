from django.shortcuts import render
from .models import Venta, Cliente, Producto, Proveedor
from django.views.generic.edit import CreateView, UpdateView
from django.db.models import Q
from datetime import datetime
from django import forms

from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required

@login_required
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
    busqueda = request.GET.get('search', '')
    clientes = Cliente.objects.filter(nombre__contains=busqueda)
    return render(request, 'ventas/buscar_cliente.html', {'clientes': clientes})

def buscar_proveedor(request):
    busqueda_proveedor = request.GET.get('busqueda_proveedor', '')
    if busqueda_proveedor:
        proveedores = Proveedor.objects.filter(nombre__contains=busqueda_proveedor)
    else:
        proveedores = Proveedor.objects.all()
    return render(request, 'ventas/buscar_proveedor.html', {'proveedores': proveedores})

class ProveedorCreate(CreateView):
    model = Proveedor
    fields = ['nombre', 'contacto', 'telefono', 'email', 'direccion']
    success_url = reverse_lazy('modelos')

class ProductoCreate(CreateView):
    model = Producto
    fields = ['codigo', 'nombre', 'descripcion', 'precio', 'cantidad', 'imagen', 'imagenExtra1', 'imagenExtra2', 'proveedor']
    success_url = reverse_lazy('modelos')
    
def buscar_productos(request):
    busqueda_productos = request.GET.get('busqueda_productos', '')
    if busqueda_productos:
        productos = Producto.objects.filter(nombre__contains=busqueda_productos)
    else:
        productos = Producto.objects.all()
    return render(request, 'ventas/buscar_producto.html', {'productos' : productos})

class ProductoUpdate(UpdateView):
    model = Producto
    fields = ['imagen', 'imagenExtra1', 'imagenExtra2']
    template_name_suffix = '_update_producto'
    
    def get_success_url(self):
        return reverse_lazy('modelos')

def buscar_ventas(request):
    busqueda_venta = request.GET.get('q', '')
    if busqueda_venta:
        try:
            fecha_busqueda = datetime.strptime(busqueda_venta, '%Y-%m-%d').date()
            ventas = Venta.objects.filter(
                Q(producto__nombre__icontains=busqueda_venta)
            )
        except ValueError:
            ventas = Venta.objects.filter(
                Q(producto__nombre__icontains=busqueda_venta)
            )
    else:
        ventas = Venta.objects.all()

    return render(request, 'ventas/venta_list.html', {'ventas': ventas})

meses_abreviados = {
    'jan': 1, 'feb': 2, 'mar': 3, 'apr': 4, 'may': 5, 'jun': 6,
    'jul': 7, 'aug': 8, 'sep': 9, 'oct': 10, 'nov': 11, 'dec': 12
}

meses_completos = {
    'enero': 1, 'febrero': 2, 'marzo': 3, 'abril': 4, 'mayo': 5, 'junio': 6,
    'julio': 7, 'agosto': 8, 'septiembre': 9, 'octubre': 10, 'noviembre': 11, 'diciembre': 12
}

meses_espanol_a_ingles = {
    'enero': 'jan', 'febrero': 'feb', 'marzo': 'mar', 'abril': 'apr',
    'mayo': 'may', 'junio': 'jun', 'julio': 'jul', 'agosto': 'aug', 
    'septiembre': 'sep', 'octubre': 'oct', 'noviembre': 'nov', 'diciembre': 'dec'
}

from datetime import datetime

def formatear_fecha_busqueda(fecha_str):
    fecha_str = fecha_str.replace('.', '').replace(',', '').strip().lower()

    palabras = fecha_str.split()
    for i, palabra in enumerate(palabras):
        if palabra in meses_espanol_a_ingles:
            palabras[i] = meses_espanol_a_ingles[palabra]
    fecha_str = ' '.join(palabras)

    try:
        partes = fecha_str.split()
        if len(partes) == 3:
            dia, mes, año = partes
            dia = int(dia)
            año = int(año)
            
            mes = meses_abreviados.get(mes[:3].lower(), meses_completos.get(mes))
            if mes:
                return datetime(año, mes, dia)

        if fecha_str in meses_completos.keys() or fecha_str in meses_abreviados.keys():
            mes = meses_completos.get(fecha_str, meses_abreviados.get(fecha_str[:3]))
            return datetime(datetime.now().year, mes, 1)
        
        if fecha_str.isdigit() and len(fecha_str) == 4:
            return datetime(int(fecha_str), 1, 1)

        if fecha_str.isdigit() and len(fecha_str) <= 2:
            dia = int(fecha_str)
            return datetime(datetime.now().year, 1, dia)

    except Exception as e:
        print(f"Error al procesar la fecha: {e}")
        return None

    return None

def buscar_ventas_por_fecha(request):
    fechas = []
    busqueda_fecha = request.GET.get('q', '').strip()

    if busqueda_fecha:
        fecha_formateada = formatear_fecha_busqueda(busqueda_fecha)

        if fecha_formateada:
            if len(busqueda_fecha.split()) == 3:
                fechas = Venta.objects.filter(fecha__date=fecha_formateada)
            elif busqueda_fecha.isdigit() and len(busqueda_fecha) == 4:
                fechas = Venta.objects.filter(fecha__year=fecha_formateada.year)
            elif busqueda_fecha.lower() in meses_completos.keys():
                fechas = Venta.objects.filter(fecha__month=fecha_formateada.month)
            elif busqueda_fecha.lower()[:3] in meses_abreviados.keys():
                fechas = Venta.objects.filter(fecha__month=fecha_formateada.month)
            elif busqueda_fecha.isdigit() and len(busqueda_fecha) <= 2:
                fechas = Venta.objects.filter(fecha__day=fecha_formateada.day)
        else:
            fechas = []
    else:
        fechas = Venta.objects.all()

    return render(request, 'ventas/venta_list_fecha.html', {'fechas': fechas})

class CreateVenta(CreateView):
    model = Venta
    fields = ['fecha', 'precio', 'cliente', 'producto']
    template_name = "ventas/crear_venta.html"
    success_url = reverse_lazy('modelos')

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields['fecha'].widget = forms.DateTimeInput(attrs={
            'type': 'datetime-local',
            'class': 'form-control fecha-input',
        })
        form.fields['precio'].widget = forms.NumberInput(attrs={
            'class': 'form-control',
            'min': '0',
            'step': '0.01'
        })
        return form